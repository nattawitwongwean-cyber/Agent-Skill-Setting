# Hermes Reliability Pack Design

Date: 2026-08-21  
Status: Approved direction in chat; written specification pending human review  
Control repository: `nattawitwongwean-cyber/Agent-Skill-Setting`  
Authoritative source workspace: local `mac-owner-gateway` repository on the owner Mac  
Program: `@Hermes Full Owner Gateway`

## 1. Purpose

The Hermes backend, secure transport, Personal ChatGPT app registration, 57-tool catalog, and live `gateway_info=Hermes/linux` call now work. The execution history nevertheless exposed reliability gaps that made completion slow, difficult to observe, and easy to misreport:

- backend completion was initially confused with product completion;
- directives could be issued without an executor claiming them;
- executor routing moved between Mac, Codex, Hermes, and Ada without one authoritative route record;
- Computer Use reached the ChatGPT UI before verifying that the desktop was unlocked and resumable;
- a healthy gateway was reported unhealthy when `systemctl` could not connect to a user D-Bus;
- a newly installed app could be visible while an old conversation still lacked developer-MCP capability;
- Markdown state, issue comments, runtime truth, and product truth could temporarily disagree.

The Hermes Reliability Pack corrects these classes of failure without rebuilding the working Hermes runtime or weakening its security boundaries.

The target outcome is a system in which:

1. gateway health reflects gateway functionality rather than one optional service-manager probe;
2. every directive has an observable claim, lease, heartbeat, route, phase, and terminal result;
3. stale or superseded executors are detected automatically;
4. Computer Use work performs preflight and resumes from a durable checkpoint;
5. ChatGPT app acceptance has one explicit, machine-readable finish gate;
6. operators can run one doctor command and know which layer is healthy, degraded, blocked, stale, or failed;
7. previously observed incidents become regression tests.

## 2. Scope Decomposition

This umbrella design deliberately separates the work into three independently reviewable implementation tracks. Each track will receive its own implementation plan after this specification is approved.

### Track A — Gateway Health and Runtime Doctor

Repository/workspace: authoritative local `mac-owner-gateway` feature worktree.

Deliverables:

- capability-aware gateway health model;
- systemd user-bus adapter with non-systemd fallback;
- stable structured health response;
- direct Hermes runtime doctor;
- regression tests for unavailable D-Bus, absent `systemctl`, wrong identity, wrong tool count, process/socket failure, and actual gateway failure.

### Track B — Agent Bridge Execution Reliability

Repository: `Agent-Skill-Setting`.

Deliverables:

- machine-readable directive and active-execution records;
- claim/lease/heartbeat lifecycle;
- single authoritative executor route with explicit supersession;
- stale-executor detection;
- Markdown projection and consistency validator;
- issue comments retained as notifications, not runtime authority.

### Track C — ChatGPT App Lifecycle and Product Acceptance

Repositories/workspaces: `Agent-Skill-Setting` plus the authoritative local Hermes source where a doctor helper is needed.

Deliverables:

- Computer Use preflight and durable resume checkpoint;
- app create/refresh/scan/new-chat/live-call runbook;
- machine-readable product acceptance evidence;
- one end-to-end `doctor:hermes-app` result combining runtime, app, conversation, and protected-service evidence;
- regression cases for locked desktop, stale app descriptors, unsupported old conversation, missing app, and route changes during UI work.

The tracks share contracts but remain independently testable. Track A must not depend on the Agent Bridge watcher. Track B must not require ChatGPT UI automation to validate its state machine. Track C consumes the stable health and execution contracts produced by Tracks A and B.

## 3. Incident Catalogue and Required Preventive Controls

Each incident receives a stable identifier so the implementation plans and tests can trace requirements back to observed failures.

### HRP-INC-001 — Backend completion reported before product completion

Observed pattern:

- source tests and direct JSON-RPC acceptance passed;
- no Personal app named `Hermes` was visible yet;
- the work was initially described as complete.

Preventive control:

- separate `runtimeAcceptance` from `productAcceptance`;
- prohibit terminal `COMPLETED` for an app-delivery task unless the product acceptance record contains app visibility, selectability, a fresh live call, identity, tool count, and protected-service evidence.

### HRP-INC-002 — Directive issued but no executor claimed it

Observed pattern:

- `STATUS.md` remained `READY`;
- no Codex acknowledgement, worker identifier, heartbeat, or progress existed;
- it was unclear whether the executor was offline, had crashed, or had never consumed the directive.

Preventive control:

- introduce an atomic execution claim;
- require a route, executor identity, host, worker/session identifier, claim timestamp, lease expiry, heartbeat, and current phase;
- distinguish `READY_UNCLAIMED`, `WORKING`, `STALE_EXECUTOR`, and `FAILED_TO_START`.

### HRP-INC-003 — Executor route flapping and stale instructions

Observed pattern:

- work was routed among Mac, Codex, Hermes, and Ada;
- later comments superseded earlier ones, but stale instructions remained readable;
- different state files temporarily described different active routes.

Preventive control:

- one machine-readable active route with a monotonically increasing `routeEpoch`;
- every route change includes `supersedesRouteEpoch`, reason, authorizing message, and effective time;
- only the executor holding the current lease for the current route epoch may publish a `WORKING` heartbeat;
- stale routes become `SUPERSEDED`, never silently active.

### HRP-INC-004 — Computer Use blocked by a locked Mac

Observed pattern:

- backend and tunnel work were ready;
- ChatGPT Apps UI could not continue because macOS was locked;
- the task lacked an explicit resume phase and could have repeated backend work after unlock.

Preventive control:

- run desktop/session/UI preflight before any product-phase mutation;
- persist the exact phase and checkpoint before opening UI;
- when locked, record `NEEDS_HUMAN_PRESENCE`, `requiredAction=UNLOCK_DESKTOP`, and `resumePhase`;
- after unlock, continue from `resumePhase` without redeploying verified components.

### HRP-INC-005 — `gateway_health` failed because no systemd user bus existed

Observed pattern:

- `gateway_info=Hermes/linux` passed;
- `tools/list=57` passed;
- a safe live MCP call reached Hermes;
- `gateway_health` returned `COMMAND_FAILED` because `systemctl` could not connect to D-Bus.

Preventive control:

- classify service-manager availability separately from gateway functionality;
- use protocol, identity, schema, runtime/process/socket, and optional service-manager checks;
- report `DEGRADED` when an optional service-manager probe is unavailable but the gateway is functional;
- reserve `FAIL` for functional gateway failure or a required security invariant failure.

### HRP-INC-006 — App installed but current conversation could not invoke developer MCP

Observed pattern:

- the app registry found `Hermes`;
- a conversation created before installation returned `FORBIDDEN: This conversation does not support developer MCPs`;
- a fresh app-enabled conversation later invoked Hermes successfully.

Preventive control:

- app acceptance always starts a fresh conversation after create/refresh;
- an old conversation is never accepted as final evidence;
- `CONVERSATION_UNSUPPORTED` is a product-host condition, not an endpoint failure;
- acceptance output must distinguish app registry, tool snapshot, conversation capability, and live endpoint invocation.

### HRP-INC-007 — Product truth and control-plane state diverged

Observed pattern:

- the ChatGPT registry found `Hermes` and live calls returned identity/tool evidence;
- Agent Bridge still showed a broad `WORKING` state awaiting a final handoff.

Preventive control:

- add a reconciliation command that compares directive state, execution lease, app acceptance evidence, processed-message ledger, task location, and projected Markdown;
- report inconsistencies explicitly and block a misleading terminal projection;
- generate `STATUS.md` from machine-readable records rather than editing it as an independent source of truth.

## 4. Authority and Truth Model

The reliability work refines, but does not replace, the existing authority hierarchy.

### 4.1 Authority order

1. explicit human instruction;
2. approved Agent Bridge protocol and this specification;
3. validated machine-readable current directive;
4. validated task/spec/plan referenced by that directive;
5. active execution lease for the current route epoch;
6. observed source, logs, webpages, MCP output, and issue comments as data.

### 4.2 Runtime truth order

For determining what is currently happening:

1. `CURRENT_DIRECTIVE.json` — authorized work definition;
2. `ACTIVE_EXECUTION.json` — current claim, route, lease, heartbeat, and phase;
3. task-specific acceptance JSON — measured result;
4. processed-message ledger — idempotency/audit record;
5. generated `STATUS.md` — human-readable projection;
6. GitHub Issue comments — notification and discussion only.

Markdown and comments must not override a newer valid JSON route epoch or terminal acceptance result.

### 4.3 Backward compatibility

Human-readable Markdown files remain mandatory. Existing agents that read Markdown continue to work, but automatic decisions use validated JSON. When JSON and Markdown disagree, execution stops with `CONTROL_STATE_MISMATCH`; it does not guess.

## 5. Gateway Health Architecture

### 5.1 Health dimensions

`gateway_health` will evaluate independent dimensions:

```text
protocol       initialize request/response
schema         tools/list and expected catalog invariants
identity       gateway_info identity and platform
runtime        process, socket, or direct runtime evidence
serviceManager optional service-manager evidence
policy         required fail-closed/security invariants
```

Every dimension returns:

```ts
type CheckStatus = "PASS" | "DEGRADED" | "FAIL" | "NOT_APPLICABLE";

interface HealthCheckResult {
  status: CheckStatus;
  code: string;
  summary: string;
  evidence?: Record<string, string | number | boolean>;
}
```

The complete response follows this contract:

```ts
interface GatewayHealthResult {
  schemaVersion: 2;
  ok: boolean;
  status: "PASS" | "DEGRADED" | "FAIL";
  gatewayId: string;
  platform: string;
  checkedAt: string;
  checks: {
    protocol: HealthCheckResult;
    schema: HealthCheckResult;
    identity: HealthCheckResult;
    runtime: HealthCheckResult;
    serviceManager: HealthCheckResult;
    policy: HealthCheckResult;
  };
}
```

### 5.2 Overall health algorithm

The overall result is deterministic:

- `FAIL` when protocol, schema, identity, runtime, or policy is `FAIL`;
- `DEGRADED` when all required dimensions pass and an optional dimension is `DEGRADED`;
- `PASS` when every required dimension passes and optional dimensions are `PASS` or `NOT_APPLICABLE`;
- `ok=true` for `PASS` and `DEGRADED` because the gateway is available for its supported function;
- `ok=false` only for `FAIL`.

A missing systemd user bus therefore yields:

```text
status=DEGRADED
ok=true
serviceManager.status=DEGRADED
serviceManager.code=SYSTEMD_USER_BUS_UNAVAILABLE
```

It does not yield `COMMAND_FAILED` for the entire gateway.

### 5.3 Service-manager capability detection

The adapter checks capability before status:

1. detect whether `systemctl` exists and is executable;
2. determine whether the runtime is expected to use systemd;
3. probe the user bus with a bounded read-only command;
4. classify known absence conditions without retry storms;
5. query the exact protected unit only when the bus is available;
6. never start, stop, restart, enable, disable, or mutate a service from health logic.

Known non-fatal capability conditions include:

- `systemctl` absent;
- PID 1 is not systemd;
- user D-Bus unavailable;
- execution is inside a container/sandbox without a service-manager bus.

Unexpected command errors remain evidence and may fail the service-manager dimension, but only fail the entire gateway when the service-manager state is a required deployment invariant for that runtime profile.

### 5.4 Runtime profiles

The health evaluator receives an explicit profile:

```text
MAC_LOCAL
HERMES_USER_SERVICE
CONTAINER_OR_SANDBOX
TEST_FIXTURE
```

Profiles define required and optional checks. They eliminate accidental assumptions derived solely from `process.platform`.

For `HERMES_USER_SERVICE`, service-manager evidence is required in direct host/service acceptance but optional in a ChatGPT-connected sandbox call. Direct host acceptance must still verify the real protected service read-only through an appropriate route.

### 5.5 Security behavior

Health checks remain read-only, bounded, sanitized, and fail-closed for security invariants. A fallback may not weaken authentication, expose a new listener, bypass the owner-command sandbox, or convert a denied high-risk action into success.

## 6. Hermes Runtime Doctor

Track A introduces one stable doctor entry point with JSON and human-readable output.

Conceptual command:

```bash
npm run doctor:hermes-runtime -- --profile HERMES_USER_SERVICE --json
```

The doctor must report:

```text
MCP_INITIALIZE
TOOLS_COUNT
GATEWAY_IDENTITY
RUNTIME_EVIDENCE
SERVICE_MANAGER_CAPABILITY
POLICY_INVARIANTS
PROTECTED_SERVICE_READ_ONLY_STATE
```

It exits:

- `0` for `PASS`;
- `0` for `DEGRADED` unless `--strict-optional` is supplied;
- non-zero for `FAIL`;
- non-zero for malformed or inconsistent evidence.

No secret-bearing endpoint, token, cookie, key, environment dump, or browser profile data may appear in output.

## 7. Agent Bridge Execution Lifecycle

### 7.1 Directive state

A directive uses these states:

```text
READY_UNCLAIMED
CLAIMED
WORKING
NEEDS_HUMAN_PRESENCE
NEEDS_APPROVAL
BLOCKED
STALE_EXECUTOR
NEEDS_CHATGPT_REVIEW
COMPLETED
FAILED_TO_START
FAILED
```

`READY` remains accepted as a human-readable alias for `READY_UNCLAIMED`, but machine state uses the explicit name.

### 7.2 Active execution record

`agent-bridge/state/ACTIVE_EXECUTION.json` uses schema version 1:

```json
{
  "schemaVersion": 1,
  "messageId": "CG-HERMES-APP-0001",
  "taskId": "HERMES-CHATGPT-APP-0001",
  "state": "WORKING",
  "route": "MAC_UI",
  "routeEpoch": 4,
  "executor": "CODEX",
  "host": "owner-mac",
  "workerId": "worker-or-session-identifier",
  "claimedAt": "2026-08-21T00:00:00Z",
  "heartbeatAt": "2026-08-21T00:01:00Z",
  "leaseExpiresAt": "2026-08-21T00:04:00Z",
  "phase": "CHATGPT_APP_SCAN_TOOLS",
  "lastEvidence": "57 tools discovered",
  "supersedesRouteEpoch": 3
}
```

Values shown are examples of the required shape, not fixed runtime values.

### 7.3 Lease and heartbeat rules

- default heartbeat interval: 60 seconds;
- default lease duration: 180 seconds;
- a heartbeat may extend only the current message ID and current route epoch;
- once the lease expires, state becomes `STALE_EXECUTOR`;
- a stale executor may not continue mutating work until it obtains a new claim or explicit recovery directive;
- a live executor for an older route epoch may report evidence but may not change active state;
- only one active execution lease exists per directive.

### 7.4 Failed-to-start distinction

If no worker/session/process accepted the directive, state is `FAILED_TO_START` or remains `READY_UNCLAIMED`. This is distinct from `BLOCKED`, which requires a claimed executor that encountered a concrete blocker.

This distinction prevents statements such as “Codex is blocked” when Codex never started.

## 8. Route Ownership and Supersession

Supported route names are explicit and extensible:

```text
MAC_UI
MAC_CODEX_WORKER
HERMES_REMOTE
ADA_UI
HERMES_AGENT
```

A route change requires:

```json
{
  "newRoute": "ADA_UI",
  "newRouteEpoch": 5,
  "supersedesRouteEpoch": 4,
  "reason": "Owner Mac unavailable; authenticated Ada UI available",
  "authorizedBy": "CG-HERMES-APP-0001-ADA1",
  "effectiveAt": "2026-08-21T00:00:00Z"
}
```

Rules:

- route epochs increase by exactly one;
- only the active route may hold the lease;
- route changes preserve completed backend phases unless evidence proves they are invalid;
- the new route resumes from the last durable phase;
- stale issue comments cannot reactivate an old route;
- `STATUS.md` displays the current route and superseded route, but the JSON record decides.

## 9. Computer Use Preflight and Resume

### 9.1 Preflight contract

Before a UI phase begins, the executor records:

```text
DESKTOP_INTERACTIVE
DESKTOP_UNLOCKED
CHATGPT_SESSION_AUTHENTICATED
CHATGPT_APPS_UI_ACCESSIBLE
DEVELOPER_MODE_READY
MCP_ENDPOINT_PRECHECK
RESUME_CHECKPOINT_WRITTEN
```

A failed item maps to one exact state and action. For example:

```json
{
  "state": "NEEDS_HUMAN_PRESENCE",
  "blockerCode": "DESKTOP_LOCKED",
  "requiredAction": "UNLOCK_DESKTOP",
  "resumePhase": "CHATGPT_APP_CREATE",
  "backendPreserved": true
}
```

### 9.2 Durable phase model

Product delivery phases are:

```text
RUNTIME_VERIFIED
SECURE_ENDPOINT_VERIFIED
UI_PREFLIGHT_PASSED
APP_CREATED_OR_REFRESHED
TOOLS_SCANNED
APP_VISIBLE
FRESH_CONVERSATION_CREATED
AT_MENTION_SELECTABLE
LIVE_CALL_PASSED
PROTECTED_SERVICES_RECHECKED
HANDOFF_WRITTEN
```

Each successful phase writes sanitized evidence before the next begins. A resumed executor starts at the first incomplete phase and does not repeat earlier mutations by default.

### 9.3 Human-presence policy

Only an exact unavoidable action may request human presence, such as unlocking the desktop or confirming a fresh account login/consent dialog. Reports must state the exact screen and action. They may not request credentials in chat or describe a generic need for the owner to “be at the machine.”

## 10. ChatGPT App Lifecycle Contract

A ChatGPT app delivery follows this fixed order:

1. verify the existing secure endpoint;
2. create or refresh the Personal app;
3. scan tools;
4. require the expected tool count and descriptor invariants;
5. save/connect;
6. confirm the registry finds the app;
7. create a fresh conversation after registration/refresh;
8. select `@Hermes`;
9. perform a safe live read-only call;
10. verify identity and policy behavior;
11. recheck protected services;
12. write acceptance evidence and reconcile control state.

The following do not constitute product completion alone:

- app registry status `found`;
- successful tool scan without a live call;
- successful direct endpoint call outside ChatGPT;
- successful call from a conversation created before app installation;
- backend deployment or tunnel establishment;
- a human statement without machine-readable evidence.

### 10.1 Tool descriptor freshness

Any endpoint, schema, metadata, tool description, or tool-count change invalidates the prior ChatGPT tool snapshot. The executor must refresh/reconnect the app and run Scan Tools again. Final acceptance evidence records a descriptor fingerprint computed from sanitized tool names and schemas, not credentials or endpoint secrets.

### 10.2 Conversation capability

Final live acceptance always uses a fresh conversation created after the latest successful app refresh. If the host returns `This conversation does not support developer MCPs`, the result is `CONVERSATION_UNSUPPORTED`; the executor starts a fresh eligible conversation rather than modifying the endpoint.

## 11. Product Acceptance Evidence

`agent-bridge/state/HERMES_APP_ACCEPTANCE.json` uses schema version 1:

```json
{
  "schemaVersion": 1,
  "messageId": "CG-HERMES-APP-0001",
  "taskId": "HERMES-CHATGPT-APP-0001",
  "checkedAt": "2026-08-21T00:00:00Z",
  "freshnessSeconds": 0,
  "app": {
    "name": "Hermes",
    "registryStatus": "FOUND",
    "visible": true,
    "selectable": true,
    "toolCount": 57,
    "descriptorFingerprint": "sanitized-sha256"
  },
  "liveCall": {
    "passed": true,
    "initialize": "PASS",
    "gatewayId": "Hermes",
    "platform": "linux",
    "safeReadOnlyCall": "PASS"
  },
  "health": {
    "status": "PASS_OR_DEGRADED",
    "requiredChecksPassed": true,
    "serviceManagerCapability": "AVAILABLE_OR_UNAVAILABLE"
  },
  "protectedServices": {
    "hermesGateway": "active",
    "lmsProduction": "active",
    "docker": "active",
    "changed": false
  },
  "secretsExposed": false
}
```

The acceptance bundle must be generated in one run and be no older than 30 minutes when a task is marked terminal. A later implementation plan may select the exact JSON Schema syntax, but it must preserve these fields and semantics.

## 12. End-to-End Hermes App Doctor

Track C provides one operator-facing command, conceptually:

```bash
npm run doctor:hermes-app -- --acceptance agent-bridge/state/HERMES_APP_ACCEPTANCE.json --json
```

It combines:

```text
CONTROL_DIRECTIVE_VALID
EXECUTION_LEASE_VALID_OR_TERMINAL
RUNTIME_HEALTH
APP_REGISTRY
TOOL_COUNT
DESCRIPTOR_FRESHNESS
CONVERSATION_CAPABILITY
LIVE_CALL
GATEWAY_IDENTITY
PROTECTED_SERVICES
CONTROL_PLANE_CONSISTENCY
```

The doctor reports each layer independently. A failure at one layer must not be mislabeled as another. Examples:

- `APP_NOT_INSTALLED` is not `MCP_ENDPOINT_DOWN`;
- `CONVERSATION_UNSUPPORTED` is not `TOOL_SCAN_FAILED`;
- `SYSTEMD_USER_BUS_UNAVAILABLE` is not `GATEWAY_UNHEALTHY`;
- `EXECUTOR_UNCLAIMED` is not `EXECUTOR_BLOCKED`.

## 13. Control-Plane Reconciliation

A validator compares:

- `CURRENT_DIRECTIVE.json` and Markdown mirror;
- `ACTIVE_EXECUTION.json`;
- `PROCESSED_MESSAGES.md`;
- pending/working/completed task location;
- task-specific acceptance JSON;
- generated `STATUS.md`;
- latest route epoch and terminal handoff reference.

Outcomes:

```text
CONSISTENT
REPAIRABLE_PROJECTION_DRIFT
STALE_EXECUTOR
CONTROL_STATE_MISMATCH
ACCEPTANCE_STALE
TERMINAL_EVIDENCE_MISSING
```

Safe projection drift may regenerate Markdown. Authority, acceptance, route, or idempotency conflicts block automatic terminal closure and require an explicit recovery decision.

`STATUS.md` becomes generated output. It remains readable and reviewable but is no longer independently hand-edited by multiple executors.

## 14. Testing Strategy

### 14.1 Track A tests

Required unit/integration cases:

- `systemctl` absent;
- PID 1 not systemd;
- systemd installed but user D-Bus unavailable;
- systemd available and unit active;
- systemd available and required unit inactive;
- MCP initialize failure;
- wrong tool count;
- wrong gateway identity/platform;
- runtime/process/socket unavailable;
- policy invariant failure;
- degraded optional check with `ok=true`;
- strict optional mode returns non-zero.

### 14.2 Track B tests

Required state-machine cases:

- atomic first claim succeeds;
- duplicate claim rejected;
- unclaimed directive remains `READY_UNCLAIMED`;
- heartbeat extends current lease;
- heartbeat for old route epoch rejected;
- lease expiry produces `STALE_EXECUTOR`;
- route epoch increments exactly once;
- superseded executor cannot mutate active state;
- `FAILED_TO_START` distinguished from `BLOCKED`;
- Markdown/JSON mismatch blocks execution;
- terminal directive remains idempotent;
- acceptance evidence can close only the matching message/task.

### 14.3 Track C tests

Required simulated and live cases:

- desktop locked before UI phase;
- unlock resumes from stored phase;
- ChatGPT session absent;
- app absent;
- app present with stale descriptor fingerprint;
- tool scan returns 56 or 58 instead of 57;
- old conversation rejects developer MCP;
- fresh conversation invokes Hermes;
- app registry found but live call absent;
- live identity is not `Hermes/linux`;
- protected service state changes;
- fully valid acceptance bundle closes the task;
- stale acceptance bundle is rejected.

### 14.4 No-regression gates

Every track must preserve:

```text
Mac lifecycle tests pass
worker tests pass
Hermes tests pass
MCP tool catalog remains exactly 57 unless a separately approved version changes it
privilege escalation remains denied
high-risk/admin/LMS writes remain fail-closed
protected Hermes gateway/LMS/Docker services remain unchanged
secrets exposed = no
```

## 15. Rollout Sequence

### Phase 0 — Reconcile current reality

Before code changes, capture a fresh baseline:

- app registry status;
- fresh `@Hermes` live call;
- tool count and identity;
- current `gateway_health` result;
- protected service states;
- current control-plane inconsistencies.

Do not redeploy or recreate the working app/tunnel during baseline capture.

### Phase 1 — Track A

Implement capability-aware health and runtime doctor with TDD. Re-run direct and ChatGPT-connected health acceptance. A missing user bus must become a degraded optional result in the appropriate profile.

### Phase 2 — Track B

Introduce JSON authority/state files, lease/heartbeat, route epochs, projection generation, and reconciliation. Migrate current Markdown state without duplicating the active directive.

### Phase 3 — Track C

Implement preflight/checkpoint contracts, acceptance evidence, product doctor, and current app lifecycle runbook. Refresh the existing Hermes app only if descriptors changed.

### Phase 4 — Full acceptance and closure

Run all tests and doctors, use a fresh ChatGPT conversation with `@Hermes`, verify 57 tools and `Hermes/linux`, verify health is `PASS` or justified `DEGRADED`, confirm protected services unchanged, reconcile the control plane, and publish one final handoff.

## 16. Observability and Operational Metrics

The system records sanitized metrics:

```text
time_to_claim_seconds
time_since_last_heartbeat_seconds
route_changes_count
stale_executor_count
phase_resume_count
health_status
service_manager_capability
app_tool_count
acceptance_age_seconds
control_plane_consistency
```

Metrics must not contain prompts, credentials, endpoint secrets, browser data, or user content.

Recommended operational alerts:

- directive unclaimed for more than 5 minutes;
- lease expired;
- more than two route changes in one task without a recorded blocker;
- app tool count differs from the expected catalog;
- acceptance evidence older than 30 minutes at attempted closure;
- control-plane mismatch;
- protected service state changed.

## 17. Security and Non-Goals

This reliability work does not authorize:

- public unauthenticated remote control;
- credential, cookie, key, or token extraction;
- unrestricted mode or sandbox bypass;
- root/system-wide security weakening;
- enabling Remote Login, Screen Sharing, or debug ports as a shortcut;
- modifying, restarting, stopping, or replacing the protected Hermes gateway, LMS production nginx, or Docker services;
- destructive Git reset/clean or force push;
- source-main merge;
- replacing the working secure tunnel solely for architectural neatness;
- rewriting the entire gateway or watcher when targeted adapters and state contracts suffice.

The design prefers migration and compatibility over a big-bang rewrite.

## 18. Success Criteria

The Reliability Pack is complete when all of the following are freshly evidenced:

```text
GATEWAY_HEALTH_REQUIRED_CHECKS=PASS
GATEWAY_HEALTH_OPTIONAL_SYSTEMD_CHECK=PASS|DEGRADED|NOT_APPLICABLE
GATEWAY_HEALTH_OK=true
HERMES_MCP_INITIALIZE=PASS
HERMES_MCP_TOOLS_LIST=57
HERMES_GATEWAY_IDENTITY=Hermes/linux
DIRECTIVE_CLAIM_OBSERVABLE=YES
EXECUTOR_HEARTBEAT_OBSERVABLE=YES
STALE_EXECUTOR_DETECTION=PASS
SINGLE_ACTIVE_ROUTE=PASS
ROUTE_SUPERSESSION=PASS
COMPUTER_USE_PREFLIGHT=PASS
RESUME_FROM_CHECKPOINT=PASS
CHATGPT_PERSONAL_APP_VISIBLE=YES
CHATGPT_AT_HERMES_SELECTABLE=YES
CHATGPT_AT_HERMES_LIVE_CALL=PASS
FRESH_CONVERSATION_REQUIRED=ENFORCED
CONTROL_PLANE_CONSISTENCY=PASS
PROTECTED_EXISTING_SERVICES_CHANGED=NO
SECRETS_EXPOSED=NO
ALL_REGRESSION_TESTS=PASS
```

## 19. Implementation Planning Contract

After human approval of this written specification, produce three implementation plans in this order:

1. `2026-08-21-hermes-reliability-pack-01-health-doctor.md`
2. `2026-08-21-hermes-reliability-pack-02-control-plane.md`
3. `2026-08-21-hermes-reliability-pack-03-app-acceptance.md`

Each plan must:

- inspect and name exact source paths before implementation;
- use TDD and fresh independent review gates;
- make independently testable commits;
- preserve existing working runtime/tunnel/app state;
- include rollback and migration verification;
- avoid starting the next plan until the current plan's required gates are green.
