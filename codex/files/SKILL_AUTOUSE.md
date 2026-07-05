# Codex Skill Autouse Policy

Use installed skills proactively.

## Core Rule

Before any non-trivial task, check whether an installed skill applies. If a skill
has even a reasonable chance of helping, load it before acting. User instructions
always take priority over any skill.

Do not load every skill. Pick the smallest useful set, then follow the selected
skill instructions.

## Selection Order

1. If the user names a skill, use that skill.
2. If the task matches a skill description, use that skill.
3. For broad coding work, first consider `superpowers:using-superpowers`.
4. For unclear feature work, planning, diagnosis, testing, code review, or handoff,
   prefer process skills before domain skills.
5. For domain-specific work, use the closest specialist skill, such as Google
   Cloud, Firebase, Gemini API, Android, Chrome DevTools, Modern Web Guidance,
   Playwright, PDF, or Impeccable.

## Common Triggers

- New feature, design, or implementation plan: `superpowers:brainstorming`,
  `grill-with-docs`, `to-prd`, `superpowers:writing-plans`
- Bug, failing test, regression, or unclear behavior: `diagnose`,
  `superpowers:systematic-debugging`,
  `superpowers:verification-before-completion`
- Tests or test strategy: `tdd`, `superpowers:test-driven-development`,
  `testing-setup`
- Frontend UI, polish, accessibility, or visual review: `impeccable`,
  `modern-web-guidance`, `a11y-debugging`
- Browser debugging, LCP, memory, or DevTools work: `chrome-devtools`,
  `debug-optimize-lcp`, `memory-leak-debugging`
- Android work: `android-cli`, `adaptive`, `edge-to-edge`, `navigation-3`,
  `r8-analyzer`, `perfetto-trace-analysis`
- Firebase, Google Cloud, Gemini, Cloud Run, BigQuery, GKE, or gcloud work:
  the matching Google skill in `~/.codex/skills`
- Code architecture, refactor planning, or system understanding:
  `improve-codebase-architecture`, `zoom-out`
- Antigravity-style team/subagent orchestration:
  `teamwork-preview`, `superpowers:subagent-driven-development`
- New repository, unfamiliar codebase, repeated context gathering, project
  onboarding, `AGENTS.md`, AI docs, repo context map, or handoff setup:
  `context-bootstrap`, `zoom-out`, `handoff`
- Issue triage, PRDs, issue creation, or handoff docs: `triage`, `to-issues`,
  `to-prd`, `handoff`
- Skill creation or workflow conversion: `superpowers:writing-skills`,
  `write-a-skill`, `writing-workflows`

## Thai Triggers

Use these Thai phrases as first-class routing signals. Users should not need to
remember skill names.

- `วางแผน`, `แผน`, `roadmap`: `superpowers:writing-plans`
- `แก้บั๊ก`, `แก้ปัญหา`, `ทำไมพัง`, `ตรวจระบบ`:
  `superpowers:systematic-debugging`
- `เขียนโค้ด`, `แก้ไฟล์`, `ทำ test`:
  `superpowers:test-driven-development`,
  `superpowers:verification-before-completion`
- `รันคำสั่ง`, `ssh`, `systemctl`, `journalctl`, `terminal`: `rtk-shell-guard`
- `ลดโทเคน`, `ประหยัดโควต้า`, `ภาษาไทยกระชับ`: `thai-token-optimizer`
- `สั้นมาก`, `อัดสั้น`: `caveman`
- `บีบบริบท`, `checkpoint`, `ทำต่อ`, `บริบทเต็ม`:
  `context-compression-checkpoint`, `handoff`
- `ทำงานเป็นทีม`, `แตกงาน`, `subagent`, `รุมทำงาน`, `teamwork-preview`:
  `teamwork-preview-goal`, `superpowers:subagent-driven-development`
- `รายงานท้ายงาน`, `โควต้า`, `ใช้โมเดลอะไร`, `route`:
  `adaptive-task-reporting`, `quota-truth-reporting`, `adaptive-model-routing`
- `GitHub`, `repo`, `issue`, `PR`, `backup`: `github-workflows`
- `ข่าว`, `NEW AI`, `NEW | AI`, `สรุปข่าว AI`: `news-new-ai-digest`
- `งานโรงเรียน`, `แผนสอน`, `ข้อสอบ`, `ใบงาน`: `teacher-thai-workflow`
- `Drive`, `Docs`, `Sheets`, `Calendar`, `Tasks`, `PDF`, `OCR`:
  `google-workspace-intake`
- `UI`, `UX`, `หน้าเว็บ`, `dashboard`, `mobile`, `ออกแบบเว็บ`:
  `ui-ux-pro-max`

For manual selection guidance in Thai, read
`/Users/nattawit/.codex/SKILL_SELECTION_TH.md`.

## Compatibility Wrappers

Some Antigravity-style skill names are installed as Codex wrappers:

- `teamwork-preview` is the canonical Codex wrapper for the original
  Antigravity team workflow
- `superpowers-bootstrap` maps to `superpowers:using-superpowers`
- `writing-workflows` maps to `superpowers:writing-skills`
- `headroom-context-compression` should normally be used through
  `context-compression-checkpoint` unless the user explicitly asks for Headroom
  internals.

Use the wrapper when the user asks for the Antigravity name, then follow the
Codex-native skill it points to.

## Working Style

When a skill is used, briefly say which skill is being used and why. Keep the
announcement short. If no skill applies, proceed normally.

If two skills conflict, follow this priority:

1. User's explicit instructions
2. Repository or project instructions
3. The more specific skill
4. General process skills

When in doubt, inspect the relevant skill's `SKILL.md` rather than guessing from
memory.
