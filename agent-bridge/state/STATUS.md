# Agent Bridge Status

Agent:
Codex

Current Task:
HERMES-CHATGPT-APP-0001 (Make @Hermes a real Personal ChatGPT app)

State:
WORKING

Progress:
CG-HERMES-APP-0001 ACCEPTED EXACTLY ONCE. Hermes-side execution reported protected services active/unchanged; owner confirmed the Mac is unlocked; architecture is confirmed as Mac UI/controller + Linux Hermes MCP runtime + Secure MCP Tunnel. Current OpenAI documentation independently confirms custom app creation uses Developer Mode / Apps → Create with tool scanning, and private/on-prem MCP should use Secure MCP Tunnel rather than direct local connectivity.

Last Successful Step:
Control Room received `HERMES-APP-MAC-UNLOCKED-0001`, `HERMES-APP-ARCH-CLARIFY-0001`, and `HERMES-APP-CODEX-CLI-EXEC-0001`. The owner confirmed the Mac is unlocked. Hermes Agents instructed the Mac-side Codex controller to launch a bounded Codex CLI worker, reuse/verify the already-prepared Hermes user-scope release and secure tunnel, then drive ChatGPT Apps UI through the mandatory live acceptance gate.

Current Step:
MAC-SIDE EXECUTION REQUIRED NOW: prove the bounded Codex CLI worker is live; verify the existing Hermes tunnel/release without recreating it; create/refresh Personal app exactly `Hermes` from the authenticated unlocked Mac; Scan Tools and verify exactly 57; verify `@Hermes` selectable; run a safe live MCP call proving initialize=PASS, tools/list=57, gateway_info=Hermes/linux; then recheck protected Hermes gateway/LMS/Docker services unchanged.

Blocking Issue:
NO PRODUCT/SECURITY BLOCKER REPORTED. No `CDX-HERMES-APP-0001` progress/final handoff has been posted yet after the Mac-side EXECUTE_NOW order, so the remaining uncertainty is whether the local Mac Codex CLI worker has actually launched and driven the ChatGPT UI.

Human Approval:
GRANTED — continue until Hermes is actually available in ChatGPT. Minimum necessary user-scope Hermes MCP service, secure MCP transport, Personal ChatGPT app registration, and remote execution from Mac to Hermes are authorized. Root/system-wide/security weakening remains outside authorization.

Human Presence Needed:
NO AT HERMES. Owner has reported the Mac unlocked. Only an unavoidable account confirmation in the authenticated ChatGPT UI may require a single exact human action; do not request unlock again unless there is fresh evidence that the Mac relocked.

ChatGPT Review:
REQUIRED AFTER CDX-HERMES-APP-0001 HANDOFF

Primary Executor:
CODEX

Required Completion Gate:
Hermes visible under Personal → Created by me / Enabled Apps as applicable to current UI; @Hermes selectable; live MCP call PASS; initialize PASS; tools/list=57; gateway_info=Hermes/linux.

Protected Existing Services:
hermes-gateway.service / LMS production nginx / Docker — MUST REMAIN UNCHANGED

Execution Architecture:
MAC — Codex controller/CLI worker + authenticated ChatGPT Apps UI
HERMES LINUX — actual Hermes MCP user-scope release + Secure MCP Tunnel
Do not relocate/duplicate the MCP runtime onto Mac merely for UI control.

Primary Task:
agent-bridge/tasks/pending/HERMES-CHATGPT-APP-0001.md

Current Directive:
agent-bridge/control/CURRENT_DIRECTIVE.md

Latest Control Orders:
Control Room Issue #1 comments `HERMES-APP-MAC-UNLOCKED-0001`, `HERMES-APP-ARCH-CLARIFY-0001`, `HERMES-APP-CODEX-CLI-EXEC-0001`

Previous Hermes Task:
agent-bridge/tasks/completed/HERMES-FOG-P01T6-P02T1.md

Next Action:
MAC_CODEX_WORKER_PROVE_LIVE_AND_COMPLETE_CHATGPT_APP_UI_ACCEPTANCE

Updated:
2026-08-21T07:20:00+07:00
