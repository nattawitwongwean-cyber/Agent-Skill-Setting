---
name: adaptive-model-routing
description: >
  Use when choosing model/provider/reasoning by task complexity, quota, or fallback state.
---

# Adaptive Model Routing

Choose the smallest capable model for the job.

## Rules

- Simple/status: small/fast model.
- Planning/general docs: medium reasoning.
- Implementation/runtime: coding-capable model.
- Deep architecture/review: stronger model.
- Do not switch mid-turn unless failure/escalation policy requires it.
- Report route from evidence, not guesswork.
