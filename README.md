# Kill Team — podręcznik po polsku

Polish handbook for **Warhammer 40,000: Kill Team (3rd edition)**, written for an 11-year-old player.
This repo is the source of truth; content gets published to a self-hosted Wiki.js.

**Start reading:** [`podrecznik/README.md`](podrecznik/README.md)
**Working on it (agents & humans):** [`AGENTS.md`](AGENTS.md)

## Contents

| Part | File | Topic |
|---|---|---|
| 1 | [Zasady podstawowe](podrecznik/01_zasady_podstawowe.md) | Core rules: actions, movement, shooting, melee, cover, orders, weapon rules, terrain |
| 2 | [Misje](podrecznik/02_misje.md) | Approved Ops 2025: setup, initiative cards, primary op, Crit/Tac/Kill Ops |
| 3 | [Sprzęt](podrecznik/03_sprzet.md) | Universal equipment |
| 4 | [Strefy walki](podrecznik/04_strefy_walki.md) | Killzones and Close Quarters rules |
| 5 | [Inne tryby gry](podrecznik/05_inne_tryby_gry.md) | Preliminary, Joint (co-op/solo), Multiplayer Ops; campaigns |
| 6 | [Słowniczek](podrecznik/06_slowniczek.md) | EN→PL glossary |
| 7 | [Oddziały](podrecznik/07_oddzialy/README.md) | Team rules: Kommandos, Deathwatch, Legionaries (more coming) |
| — | [Prompty do obrazków](podrecznik/prompty_obrazki.md) | Image-model prompts for illustrations and diagrams |

## Status

- Rules current to the **October 2026** official update; last content pass 23 Nov 2026.
- 3 of 17 planned teams written. See the backlog in [`AGENTS.md`](AGENTS.md#backlog).
- Illustrations not generated yet; rule diagrams are simple matplotlib renders.

## Repo layout

- `podrecznik/` — the handbook (Polish markdown + images)
- `research/` — English fact notes the handbook is based on
- `scripts/` — diagram generators and PDF preview build (`./scripts/build_pdf.sh`)
- `build/` — generated PDF (git-ignored)

---

Unofficial fan resource. Warhammer 40,000, Kill Team and related names are trademarks of Games Workshop.
Not a substitute for the official rules.
