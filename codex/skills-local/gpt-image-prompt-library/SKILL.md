---
name: gpt-image-prompt-library
description: Use when the user asks to create, improve, analyze, or search prompts for AI image generation, poster design, classroom visual aids, social media visuals, UI mockups, product images, character designs, portraits, or GPT Image style prompts. Uses the local EvoLinkAI awesome GPT Image prompt resource pack.
---

# GPT Image Prompt Library

Use this skill when helping with image generation prompts or visual concepts.

## Local resource

Resource pack path:

`/Users/nattawit/.codex/resources/gpt-image-2-prompts`

It is a sparse local checkout of `EvoLinkAI/awesome-gpt-image-2-API-and-Prompts`, excluding the heavy `images/` directory. Use the GitHub repo if example images are needed.

## Fast search

Search cases without loading huge markdown files:

```bash
/Users/nattawit/.codex/skills/gpt-image-prompt-library/scripts/search_prompt_cases.py poster classroom thai --limit 6
```

Common categories:

- `portrait`
- `poster`
- `ui`
- `ecommerce`
- `ad-creative`
- `character`
- `comparison`

Use `--category poster` etc. to narrow results.

## Workflow

1. Identify the user's target: poster, teaching visual, worksheet illustration, product image, UI mockup, character, portrait, or ad creative.
2. Search 3-8 relevant cases with the script.
3. Extract reusable structure only: subject, style, composition, lighting, text placement, aspect ratio, negative constraints.
4. Rewrite a fresh prompt for the user's actual goal. Do not blindly paste a whole case unless asked.
5. If the user wants Thai educational content, make text instructions explicit and include Thai typography constraints.
6. If generating through Codex image tools, pass the polished prompt directly to image generation.

## Safety and quality rules

- Do not create sexualized minors or ambiguous youthful sexualized portraits.
- Avoid copying artist/person likeness unless the user has rights or asks for a generic style alternative.
- For school use, default to safe, respectful, non-sexual imagery.
- Preserve exact Thai text separately in quotes if the image must render Thai text.
- Add layout constraints for posters: headline zone, body text zone, visual focal point, margin, aspect ratio.
- For editable design work, suggest a layered Canva/Figma/PPT workflow when better than a flat image.

## Prompt template

Use this structure when helpful:

```text
Create [output type] for [audience/use case].
Subject: [main subject].
Scene/composition: [camera angle, layout, focal point, background].
Style: [visual style, medium, references in generic terms].
Lighting/color: [lighting, palette, mood].
Text: exact text to render: "...". Keep text readable and correctly spelled.
Details: [materials, props, symbols, educational constraints].
Negative constraints: no watermark, no garbled text, no extra limbs, no unsafe content.
Aspect ratio: [e.g. 16:9, 9:16, 1:1, A4 vertical].
```
