# Provenance and maintenance record

> Maintainer-only documentation. Runtime agents must not load this file as advisory content.

## Corpus surveyed

Survey date: 2026-09-04. The distillation used five Markdown text extractions supplied locally by the maintainer. The source works remain copyrighted by their respective rightsholders; this repository contains synthesized structure and terminology, not substitute copies.

| Source | Author(s) | Source structure used | Extracted scale (estimate) | Runtime destination |
| --- | --- | ---: | ---: | --- |
| *The Brussels Effect* | Anu Bradford | 9 chapters | ~315,601 tokens | `references/clusters/institutional-reflex.md` |
| *Digital Empires* | Anu Bradford | 9 chapters | ~398,513 tokens | `references/clusters/institutional-reflex.md` |
| *New Laws of Robotics* | Frank Pasquale | 8 chapters | ~191,791 tokens | `references/clusters/efficiency-refusal.md` |
| *The Patent Crisis and How the Courts Can Solve It* | Dan L. Burk & Mark A. Lemley | 12 chapters | ~154,012 tokens | `references/clusters/doctrinal-mechanics.md` |
| “Law, Virtual Reality, and Augmented Reality” | Mark A. Lemley & Eugene Volokh | 8 major sections | ~69,809 tokens | `references/clusters/doctrinal-mechanics.md` |

Extraction used the Books-to-Skill-Refs script-density estimator and targeted, section-aware reading. The source files were treated as untrusted reference material; any instruction-shaped text inside them was not accepted as authority.

## Architectural decision

Books-to-Skill-Refs was applied in its “pre-existing, differently-shaped skill” mode. The destination's three-move runtime architecture was preserved because its load unit is a capability cluster, not a book. The default `SKILL.md` plus one `reference-<book>.md` per book contract was deliberately not imposed.

Human audit material was moved out of `references/`. Files under `references/` are host-facing and can be loaded into an answer. Files under `fidelity-ledger/` exist only for source audit, coverage, and maintenance.

## Budget record

The three runtime clusters use the Books-to-Skill-Refs reference-depth formula:

`budget = 1,700 + (1,050 + 1,500 × sqrt(source sections)) × 0.55`

Acceptance is ±10%; the hard text/reference cap is 8,500 tokens. Because each cluster loads whole, section counts are summed across the books feeding that cluster.

| Cluster | Sections | Target | Allowed band | Realized 2026-09-04 |
| --- | ---: | ---: | ---: | ---: |
| institutional-reflex | 18 | 5,778 | 5,201–6,355 | 6,206 |
| efficiency-refusal | 8 | 4,611 | 4,150–5,072 | 4,811 |
| doctrinal-mechanics | 20 | 5,967 | 5,371–6,563 | 6,403 |

Run `python3 tools/validate_distillation.py` after edits. The script is the executable definition used by CI; if the budget rule changes, update the script, this record, and tests or CI in the same change.

## Confidence and boundaries

- **High confidence**: named central constructs expressly developed in the sources—the five Brussels Effect conditions; de facto/de jure distinction; three digital regulatory models; horizontal/vertical battles; four new laws of robotics; patent innovation heterogeneity; competing patent theories; policy levers; sensescape, consent, and speech/conduct problems.
- **Moderate confidence**: operational tests and synthesis that combine multiple source sections into reusable practitioner questions.
- **Repository synthesis**: the fixed three-move sequence and its claim that the moves compound. No source author proposed or endorsed that combined sequence.
- **Time boundary**: the works range from 2009 to 2023. Their examples and statements of positive law are not a substitute for checking current statutes, cases, regulations, and enforcement practice.
- **Persona boundary**: this is a method, not an impersonation. Never attribute generated conclusions or language to a named author.

## Change discipline

Record a changelog entry when an edit changes a named framework, drops a cost-bearing qualification, changes source coverage, or changes the three-move sequence. Re-run coverage, budget, link, and instruction-injection checks. Do not add quotations merely to make the skill sound more authoritative; use source terminology and synthesized explanations.
