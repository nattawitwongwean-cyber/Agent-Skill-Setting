# Codex Skill Snapshot

Generated: 2026-06-24T09:24:45.648057+00:00

## Counts

- Local skill dirs: 53
- Symlink skills: 61
- Symlink skills copied as real files: 61
- Missing SKILL.md dirs: 1
- Enabled plugins: 19

## Local Skills

- `adaptive-model-routing` - >
- `adaptive-task-reporting` - >
- `antigravity-proxy-matrix` - >
- `banner-design` - "Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with AI-generated visuals. Actions: design, create, generate banner. Platforms: Facebook, Twitter/X, LinkedIn, YouTube, Instagram, Google Display, website hero, print. Styles: minimalist, gradient, bold typography, photo-based, illustrated, geometric, retro, glassmorphism, 3D, neon, duotone, editorial, collage. Uses ui-ux-pro-max, frontend-design, ai-artist, ai-multimodal skills."
- `brand` - Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand compliance, style guides.
- `caveman` - >
- `chronicle` - |
- `cloudflare-deploy` - Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or set up a project on Cloudflare.
- `context-bootstrap` - Use when starting work in an unfamiliar repository, preparing Codex for a project, refreshing AGENTS.md or repo context, reducing repeated exploration, or creating compact context maps, handoff notes, command references, architecture notes, or AI onboarding files.
- `context-compression-checkpoint` - >
- `design` - "Comprehensive design skill: brand identity, design tokens, UI styling, logo generation (55 styles, Gemini AI), corporate identity program (50 deliverables, CIP mockups), HTML presentations (Chart.js), banner design (22 styles, social/ads/web/print), icon design (15 styles, SVG, Gemini 3.1 Pro), social photos (HTML→screenshot, multi-platform). Actions: design logo, create CIP, generate mockups, build slides, design banner, generate icon, create social photos, social media images, brand identity, design system. Platforms: Facebook, Twitter, LinkedIn, YouTube, Instagram, Pinterest, TikTok, Threads, Google Ads."
- `design-system` - Token architecture, component specifications, and slide generation. Three-layer tokens (primitive→semantic→component), CSS variables, spacing/typography scales, component specs, strategic slide creation. Use for design tokens, systematic design, brand-compliant presentations.
- `diagnose` - Disciplined diagnosis loop for hard bugs and performance regressions. Reproduce → minimise → hypothesise → instrument → fix → regression-test. Use when user says "diagnose this" / "debug this", reports a bug, says something is broken/throwing/failing, or describes a performance regression.
- `git-guardrails-claude-code` - Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute. Use when user wants to prevent destructive git operations, add git safety hooks, or block git push/reset in Claude Code.
- `github-workflows` - >
- `google-workspace-intake` - >
- `gpt-image-prompt-library` - Use when the user asks to create, improve, analyze, or search prompts for AI image generation, poster design, classroom visual aids, social media visuals, UI mockups, product images, character designs, portraits, or GPT Image style prompts. Uses the local EvoLinkAI awesome GPT Image prompt resource pack.
- `grill-me` - Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
- `grill-with-docs` - Grilling session that challenges your plan against the existing domain model, sharpens terminology, and updates documentation (CONTEXT.md, ADRs) inline as decisions crystallise. Use when user wants to stress-test a plan against their project's language and documented decisions.
- `handoff` - Compact the current conversation into a handoff document for another agent to pick up.
- `headroom-context-compression` - Use when compressing, checkpointing, summarizing, or reducing token usage for long logs, audit reports, runtime state, conversation context, tool outputs, or Hermes/Codex reports using Headroom from chopratejas/headroom.
- `impeccable` - "Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend interface. Covers websites, landing pages, dashboards, product UI, app shells, components, forms, settings, onboarding, and empty states. Handles UX review, visual hierarchy, information architecture, cognitive load, accessibility, performance, responsive behavior, theming, anti-patterns, typography, fonts, spacing, layout, alignment, color, motion, micro-interactions, UX copy, error states, edge cases, i18n, and reusable design systems or tokens. Also use for bland designs that need to become bolder or more delightful, loud designs that should become quieter, live browser iteration on UI elements, or ambitious visual effects that should feel technically extraordinary. Not for backend-only or non-UI tasks."
- `improve-codebase-architecture` - Find deepening opportunities in a codebase, informed by the domain language in CONTEXT.md and the decisions in docs/adr/. Use when the user wants to improve architecture, find refactoring opportunities, consolidate tightly-coupled modules, or make a codebase more testable and AI-navigable.
- `migrate-to-shoehorn` - Migrate test files from `as` type assertions to @total-typescript/shoehorn. Use when user mentions shoehorn, wants to replace `as` in tests, or needs partial test data.
- `news-new-ai-digest` - >
- `pdf` - "Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction."
- `personal-knowledge-intake` - >
- `playwright` - "Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script."
- `ponytail` - >
- `ponytail-audit` - >
- `ponytail-debt` - >
- `ponytail-help` - >
- `ponytail-review` - >
- `prototype` - Build a throwaway prototype to flesh out a design before committing to it. Routes between two branches — a runnable terminal app for state/business-logic questions, or several radically different UI variations toggleable from one route. Use when the user wants to prototype, sanity-check a data model or state machine, mock up a UI, explore design options, or says "prototype this", "let me play with it", "try a few designs".
- `quota-truth-reporting` - >
- `rtk-shell-guard` - >
- `scaffold-exercises` - Create exercise directory structures with sections, problems, solutions, and explainers that pass linting. Use when user wants to scaffold exercises, create exercise stubs, or set up a new course section.
- `setup-matt-pocock-skills` - Sets up an `## Agent skills` block in AGENTS.md/CLAUDE.md and `docs/agents/` so the engineering skills know this repo's issue tracker (GitHub or local markdown), triage label vocabulary, and domain doc layout. Run before first use of `to-issues`, `to-prd`, `triage`, `diagnose`, `tdd`, `improve-codebase-architecture`, or `zoom-out` — or if those skills appear to be missing context about the issue tracker, triage labels, or domain docs.
- `setup-pre-commit` - Set up Husky pre-commit hooks with lint-staged (Prettier), type checking, and tests in the current repo. Use when user wants to add pre-commit hooks, set up Husky, configure lint-staged, or add commit-time formatting/typechecking/testing.
- `superpowers-bootstrap` - Use when an Antigravity-style Superpowers bootstrap is requested in Codex - maps the bootstrap behavior to Codex's using-superpowers skill
- `tdd` - Test-driven development with red-green-refactor loop. Use when user wants to build features or fix bugs using TDD, mentions "red-green-refactor", wants integration tests, or asks for test-first development.
- `teacher-thai-workflow` - >
- `teamwork-preview` - Use when an Antigravity-style teamwork-preview workflow is requested in Codex - maps to the Codex-native subagent-driven-development workflow.
- `teamwork-preview-goal` - >
- `thai-token-optimizer` - >
- `to-issues` - Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. Use when user wants to convert a plan into issues, create implementation tickets, or break down work into issues.
- `to-prd` - Turn the current conversation context into a PRD and publish it to the project issue tracker. Use when user wants to create a PRD from the current context.
- `triage` - Triage issues through a state machine driven by triage roles. Use when user wants to create an issue, triage issues, review incoming bugs or feature requests, prepare issues for an AFK agent, or manage issue workflow.
- `ui-styling` - Create beautiful, accessible user interfaces with shadcn/ui components (built on Radix UI + Tailwind), Tailwind CSS utility-first styling, and canvas-based visual designs. Use when building user interfaces, implementing design systems, creating responsive layouts, adding accessible components (dialogs, dropdowns, forms, tables), customizing themes and colors, implementing dark mode, generating visual designs and posters, or establishing consistent styling patterns across applications.
- `ui-ux-pro-max` - "UI/UX design intelligence for web and mobile. Includes 50+ styles, 161 color palettes, 57 font pairings, 161 product types, 99 UX guidelines, and 25 chart types across 10 stacks (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui, and HTML/CSS). Actions: plan, build, create, design, implement, review, fix, improve, optimize, enhance, refactor, and check UI/UX code. Projects: website, landing page, dashboard, admin panel, e-commerce, SaaS, portfolio, blog, and mobile app. Elements: button, modal, navbar, sidebar, card, table, form, and chart. Styles: glassmorphism, claymorphism, minimalism, brutalism, neumorphism, bento grid, dark mode, responsive, skeuomorphism, and flat design. Topics: color systems, accessibility, animation, layout, typography, font pairing, spacing, interaction states, shadow, and gradient. Integrations: shadcn/ui MCP for component search and examples."
- `write-a-skill` - Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, or build a new skill.
- `writing-workflows` - Use when an Antigravity-style workflow or skill authoring task is requested in Codex - maps to Superpowers writing-skills
- `zoom-out` - Tell the agent to zoom out and give broader context or a higher-level perspective. Use when you're unfamiliar with a section of code or need to understand how it fits into the bigger picture.

## Symlink Skills

- `a11y-debugging` -> `/Users/nattawit/.codex/vendor/google-skills/chrome-devtools-mcp/skills/a11y-debugging` (copied)
- `adaptive` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/jetpack-compose/adaptive` (copied)
- `agent-platform-deploy` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-deploy` (copied)
- `agent-platform-endpoint-management` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-endpoint-management` (copied)
- `agent-platform-eval-flywheel` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-eval-flywheel` (copied)
- `agent-platform-inference` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-inference` (copied)
- `agent-platform-migrate-from-ai-studio` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-migrate-from-ai-studio` (copied)
- `agent-platform-model-registry` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-model-registry` (copied)
- `agent-platform-prompt-management` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-prompt-management` (copied)
- `agent-platform-rag-engine-management` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-rag-engine-management` (copied)
- `agent-platform-skill-registry` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-skill-registry` (copied)
- `agent-platform-tuning` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-tuning` (copied)
- `agent-platform-tuning-management` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/agent-platform-tuning-management` (copied)
- `agp-9-upgrade` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/build/agp/agp-9-upgrade` (copied)
- `alloydb-basics` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/alloydb-basics` (copied)
- `android-cli` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/devtools/android-cli` (copied)
- `bigquery-basics` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/bigquery-basics` (copied)
- `brainstorming` -> `/Users/nattawit/.codex/superpowers/skills/brainstorming` (copied)
- `chrome-devtools` -> `/Users/nattawit/.codex/vendor/google-skills/chrome-devtools-mcp/skills/chrome-devtools` (copied)
- `chrome-devtools-cli` -> `/Users/nattawit/.codex/vendor/google-skills/chrome-devtools-mcp/skills/chrome-devtools-cli` (copied)
- `chrome-extensions` -> `/Users/nattawit/.codex/vendor/google-skills/modern-web-guidance/skills/chrome-extensions` (copied)
- `cloud-run-basics` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/cloud-run-basics` (copied)
- `cloud-sql-basics` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/cloud-sql-basics` (copied)
- `debug-optimize-lcp` -> `/Users/nattawit/.codex/vendor/google-skills/chrome-devtools-mcp/skills/debug-optimize-lcp` (copied)
- `dispatching-parallel-agents` -> `/Users/nattawit/.codex/superpowers/skills/dispatching-parallel-agents` (copied)
- `edge-to-edge` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/system/edge-to-edge` (copied)
- `executing-plans` -> `/Users/nattawit/.codex/superpowers/skills/executing-plans` (copied)
- `finishing-a-development-branch` -> `/Users/nattawit/.codex/superpowers/skills/finishing-a-development-branch` (copied)
- `firebase-basics` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/firebase-basics` (copied)
- `gcloud` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/gcloud` (copied)
- `gemini-agents-api` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/gemini-agents-api` (copied)
- `gemini-api` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/gemini-api` (copied)
- `gemini-interactions-api` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/gemini-interactions-api` (copied)
- `gke-basics` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/gke-basics` (copied)
- `google-cloud-networking-observability` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/google-cloud-networking-observability` (copied)
- `google-cloud-recipe-auth` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/google-cloud-recipe-auth` (copied)
- `google-cloud-recipe-onboarding` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/google-cloud-recipe-onboarding` (copied)
- `google-cloud-waf-cost-optimization` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/google-cloud-waf-cost-optimization` (copied)
- `google-cloud-waf-operational-excellence` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/google-cloud-waf-operational-excellence` (copied)
- `google-cloud-waf-performance-optimization` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/google-cloud-waf-performance-optimization` (copied)
- `google-cloud-waf-reliability` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/google-cloud-waf-reliability` (copied)
- `google-cloud-waf-security` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/google-cloud-waf-security` (copied)
- `google-cloud-waf-sustainability` -> `/Users/nattawit/.codex/vendor/google-skills/google-skills/skills/cloud/google-cloud-waf-sustainability` (copied)
- `memory-leak-debugging` -> `/Users/nattawit/.codex/vendor/google-skills/chrome-devtools-mcp/skills/memory-leak-debugging` (copied)
- `migrate-xml-views-to-jetpack-compose` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/jetpack-compose/migration/migrate-xml-views-to-jetpack-compose` (copied)
- `modern-web-guidance` -> `/Users/nattawit/.codex/vendor/google-skills/modern-web-guidance/skills/modern-web-guidance` (copied)
- `navigation-3` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/navigation/navigation-3` (copied)
- `perfetto-sql` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/profilers/perfetto-sql` (copied)
- `perfetto-trace-analysis` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/profilers/perfetto-trace-analysis` (copied)
- `r8-analyzer` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/performance/r8-analyzer` (copied)
- `receiving-code-review` -> `/Users/nattawit/.codex/superpowers/skills/receiving-code-review` (copied)
- `requesting-code-review` -> `/Users/nattawit/.codex/superpowers/skills/requesting-code-review` (copied)
- `subagent-driven-development` -> `/Users/nattawit/.codex/superpowers/skills/subagent-driven-development` (copied)
- `systematic-debugging` -> `/Users/nattawit/.codex/superpowers/skills/systematic-debugging` (copied)
- `test-driven-development` -> `/Users/nattawit/.codex/superpowers/skills/test-driven-development` (copied)
- `testing-setup` -> `/Users/nattawit/.codex/vendor/google-skills/android-skills/testing/testing-setup` (copied)
- `using-git-worktrees` -> `/Users/nattawit/.codex/superpowers/skills/using-git-worktrees` (copied)
- `using-superpowers` -> `/Users/nattawit/.codex/superpowers/skills/using-superpowers` (copied)
- `verification-before-completion` -> `/Users/nattawit/.codex/superpowers/skills/verification-before-completion` (copied)
- `writing-plans` -> `/Users/nattawit/.codex/superpowers/skills/writing-plans` (copied)
- `writing-skills` -> `/Users/nattawit/.codex/superpowers/skills/writing-skills` (copied)

## Missing SKILL.md Directories

- `subagent-development`

## Enabled Plugins

- `documents@openai-primary-runtime`
- `spreadsheets@openai-primary-runtime`
- `presentations@openai-primary-runtime`
- `codex-security@openai-curated`
- `google-calendar@openai-curated`
- `google-drive@openai-curated`
- `openai-developers@openai-curated`
- `github@openai-curated`
- `gmail@openai-curated`
- `vercel@openai-curated`
- `build-web-apps@openai-curated`
- `jam@openai-curated`
- `superpowers@openai-curated`
- `cloudflare@openai-curated`
- `computer-use@openai-bundled`
- `pdf@openai-primary-runtime`
- `browser@openai-bundled`
- `chrome@openai-bundled`
- `template-creator@openai-primary-runtime`
