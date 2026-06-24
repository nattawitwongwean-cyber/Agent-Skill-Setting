---
name: quota-truth-reporting
description: >
  Use when reporting model, provider, quota, route, or runtime status; never guess stale quota.
---

# Quota Truth Reporting

Quota/model reports must come from live/runtime truth where available.

## Rules

- Do not invent remaining quota or reset times.
- If source is stale, say `stale`. If unavailable, say `unavailable`.
- Separate provider, model, route/profile, account, quota source, and timestamp.
- If evidence conflicts, report `truth_conflict` instead of smoothing it over.
