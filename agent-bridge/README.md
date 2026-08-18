# Agent Bridge

Persistent handoff and audit layer coordinating the human operator, ChatGPT, and Antigravity on this Windows development machine.

## Structure

```text
agent-bridge/
├── README.md
├── PROTOCOL.md
├── control/
│   ├── CURRENT_DIRECTIVE.md
│   └── APPROVALS.md
├── state/
│   ├── STATUS.md
│   ├── MACHINE.md
│   ├── PROCESSED_MESSAGES.md
│   └── DECISIONS.md
├── tasks/
│   ├── pending/
│   ├── working/
│   ├── completed/
│   └── failed/
├── reports/
├── journal/
├── artifacts/
│   ├── configs/
│   ├── scripts/
│   └── diagnostics/
└── docs/
    └── lnwjud/
```

## Resuming Work

1. Verify working tree: `git status --short --branch`
2. Safely sync: `git pull --rebase`
3. Check `agent-bridge/PROTOCOL.md` for rules and security bounds.
4. Check `agent-bridge/state/STATUS.md` for current task and status.
5. Check `agent-bridge/control/CURRENT_DIRECTIVE.md` for active directive.
6. Check `agent-bridge/state/PROCESSED_MESSAGES.md` to prevent duplicate execution.
7. Post updates to GitHub Issue #1 or create outbox fallback.
