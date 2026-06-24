# Session review playbook
Use this when the user asks to review prior conversation history, continue “until the latest”, or summarize what happened across older sessions.

## Reliable workflow
1. Start with session/search or the available history index to get newest likely sessions.
2. Read each likely session fully enough to identify start/end and the user intent.
3. If a session is truncated, scroll around a midpoint or match anchor instead of trusting snippets.
4. Prefer bookend start + bookend end + targeted middle windows over guessing from search snippets.
5. Reconstruct the timeline in chronological order and separate:
   - verified actions
   - inferred intent
   - open questions / unfinished work
6. When the user says “continue to the latest”, keep stepping through newer sessions until the most recent relevant session is reached.

## Output shape
- Table by session/time/source when useful
- Then concise “what is done” / “what is still open” summary
- Avoid claiming the transcript is complete unless the search actually reached the latest relevant session

## Pitfall
Do not stop after the first discovery hit if the user asked for the full thread or latest state. Always check the newer context.
