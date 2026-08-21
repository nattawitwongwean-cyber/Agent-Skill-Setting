# Agent Bridge Status

Agent:
Hermes Agents / Ada

Current Task:
HERMES-CHATGPT-APP-0001 (Make @Hermes a real Personal ChatGPT app)

State:
WORKING

Progress:
CG-HERMES-APP-0001 is accepted exactly once. Hermes-side protected services remain reported active/unchanged. The latest Control Room route correction pauses the Mac-side UI/CLI path and requires Ada/Hermes to perform ChatGPT Personal app configuration directly from the Ada/Hermes machine. Existing Hermes user-scope MCP release and secure tunnel must be preserved/reused.

Last Successful Step:
Validated the route correction `HERMES-APP-ROUTE-CORRECTION-0001` and issued continuation order `CG-HERMES-APP-0001-ADA1` in Control Room Issue #1 (comment 5363993406). Updated CURRENT_DIRECTIVE.md so stale Mac-side execution instructions no longer control this task.

Current Step:
ADA/HERMES EXECUTION REQUIRED NOW: verify the already-working Hermes user-scope MCP release and secure ChatGPT-reachable tunnel; use the normal authenticated ChatGPT UI on Ada/Hermes to create/refresh Personal app exactly `Hermes`; run Scan Tools and verify 57; verify `@Hermes` selectable; run a safe live MCP call proving initialize=PASS, tools/list=57, gateway_info=Hermes/linux; then recheck protected services unchanged.

Blocking Issue:
NO PRODUCT/SECURITY BLOCKER REPORTED. No final `CDX-HERMES-APP-0001` handoff has been posted yet after the Ada/Hermes route correction. Remaining uncertainty is whether Ada/Hermes has completed the ChatGPT UI registration/live acceptance.

Human Approval:
GRANTED — continue until Hermes is actually available in ChatGPT. Existing user-scope Hermes MCP release/tunnel should be reused. Root/system-wide/security weakening remains outside authorization.

Human Presence Needed:
NO GENERAL HUMAN PRESENCE REQUIRED. Only an unavoidable fresh ChatGPT account login/consent confirmation on Ada/Hermes may require one exact human action; preserve all working runtime/tunnel state if that occurs.

ChatGPT Review:
REQUIRED AFTER CDX-HERMES-APP-0001 HANDOFF

Primary Executor:
HERMES AGENTS / ADA

Required Completion Gate:
Hermes visible in the user's Personal/Apps area; @Hermes selectable; live MCP call PASS; initialize PASS; tools/list=57; gateway_info=Hermes/linux.

Protected Existing Services:
hermes-gateway.service / LMS production nginx / Docker — MUST REMAIN UNCHANGED

Execution Architecture:
ADA/HERMES — ChatGPT Personal app configuration + Hermes MCP user-scope release + Secure MCP Tunnel
MAC — route paused/preserved for this task; do not require owner Mac availability

Primary Task:
agent-bridge/tasks/pending/HERMES-CHATGPT-APP-0001.md

Current Directive:
agent-bridge/control/CURRENT_DIRECTIVE.md

Latest Control Order:
Control Room Issue #1 comment 5363993406 (`CG-HERMES-APP-0001-ADA1`)

Previous Route Correction:
Control Room Issue #1 comment 5363755147 (`HERMES-APP-ROUTE-CORRECTION-0001`)

Next Action:
ADA_HERMES_COMPLETE_CHATGPT_APP_UI_AND_LIVE_ACCEPTANCE

Updated:
2026-08-21T08:12:00+07:00
