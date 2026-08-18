# Architectural & Security Decisions

## DEC-001: Hybrid Agent Bridge Architecture
- **Date:** 2026-08-18
- **Context:** Coordinate local Windows development agent (Antigravity), ChatGPT, and human operator.
- **Decision:** Use GitHub Issue #1 for conversation/control messages and repository `agent-bridge/` for durable sanitized state, evidence, and reports.
- **Rationale:** Prevents manual log copy-pasting, provides durable audit trail, prevents secret leakage, ensures idempotency across restarts.

## DEC-002: Strict No-Execution Installer Inspection
- **Date:** 2026-08-18
- **Context:** Phase 0-6 evaluation of lnwjud.
- **Decision:** Download candidate installer outside repository (`Downloads` or temporary inspection directory) and inspect hashes, signatures, publisher info, and Defender scans without launching the process.
- **Rationale:** Ensures security gate before code or binary is ever executed on host.
