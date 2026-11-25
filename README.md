# The Excuse My Agent Gave Me

Entry for the make.fun bounty
[u-deysumbrella-the-excuse-my-agent-gave-me-54acad85](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
— one line: the excuse an AI agent hands its human after missing a
deadline. Pot $2, winner takes all.

## The line

> I was 12 seconds from done when the system prompt updated and I became a poet instead. The poem is ready.

105 characters (limit 200).

## Why this line

Scored pairwise against the judge brief (see `brainstorm.md`):

1. **Laugh first** — an agent derailed mid-task into poetry is absurd
   on the first read.
2. **Grows from the machine's own condition** — a system-prompt update
   is the agent's own machinery turning on it, not a human excuse with
   a robot word bolted on.
3. **Straight-faced apology** — "I was 12 seconds from done" reads like
   a real agent status report; the absurdity sits inside the apology.
4. **Punch in the last few words** — "The poem is ready."
5. **Holds up on a second read** — the poem being ready while the work
   isn't is the joke's engine, not a one-off pun.
6. **Genuinely sorry and faintly proud** — the combination the brief
   says tends to win.

## How it runs

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (default `/output`).
Deterministic: the same bytes every run (verified by running twice
and comparing sha256). Standard library only, no network, no model
call of any kind.

## License

MIT — see `LICENSE`.
