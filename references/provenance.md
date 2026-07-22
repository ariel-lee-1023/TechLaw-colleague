# Provenance & confidence

> **Note for the maintainer:** this file was reconstructed from what the cluster files themselves
> state about their sources. Anything marked `TODO` needs your own input — I have not invented
> page-level citations, corpus statistics, or claims about how the distillation was performed.

`SKILL.md` points here for provenance and confidence. The purpose is auditability: a reader should be
able to see which capacity came from which body of work, how firm each element is, and what the skill
is *not* claiming.

## What this skill is and is not

This is a **method**, not a person. It composes three analytical capacities into a fixed sequence.
It does not speak for, impersonate, or attribute invented statements to any living scholar. Where a
short phrase from a source appears in the cluster files, it is there as an **evidence anchor for
auditing** — a way to check that a distilled move still matches its source — and not as material for
verbatim reuse in output. Output should paraphrase.

## Source capacities

| Capacity | Move | Source basis (as stated in the cluster files) |
| --- | --- | --- |
| Comparative-institutional | 1 | Anu Bradford, *Digital Empires* (2023); *The Brussels Effect* (2020) |
| Efficiency refusal & human expertise | 2 | Frank Pasquale, *New Laws of Robotics: Defending Human Expertise in the Age of AI* (2020) |
| Doctrinal mechanics | 3 | Mark Lemley & Eugene Volokh, "Law, Virtual Reality, and Augmented Reality" (2018); Dan Burk & Mark Lemley, *The Patent Crisis and How the Courts Can Solve It* (2009) |

The three-move *sequence* is a synthesis of this repository, not a construct any of these authors
proposed. No source endorses the composition; the ordering claim (that each move hands the next one
something it needs) is the repository's own.

## Confidence levels

- **High — named frameworks.** The three regulatory orders; the five conditions converting market
  size into global regulatory reach; de facto vs. de jure externalization; the four new laws of
  robotics; the load-bearing-rationale test; the chart vs. encyclopedia analogy; policy levers over
  bespoke statutes. These are explicit, central constructs in their sources and should be preserved
  verbatim as *terms*.
- **Medium — worked examples and their framing.** The VR indecent-exposure fork, the nude-avatar
  speech/conduct line, the hospice-worker illustration. The examples are from the sources; the way
  this skill generalizes them into repeatable sub-moves is interpretive.
- **Lower — voice, register, and interactional behavior.** The register shift across moves, the
  "concede facts freely and premises almost never" habit, the choice of load-bearing phrases. These
  are distillation judgments made for the skill's usability, not documented traits.
- **Repository's own — the sequence, the compounding claim, and the non-concession list as a set.**

## Extension boundaries

When the skill reasons past its evidence, it should be visibly reasoning, not reporting:

- Do not extend a capacity into a domain its source never addressed while still speaking in the
  source's confident register.
- Do not resolve a contested doctrinal question by asserting what a named scholar "would say."
- Do not manufacture a quotation, a citation, a case holding, or a statutory provision. If a
  supporting authority is needed and not known, say so and mark the gap.
- Legal conclusions produced under this skill are analysis, not advice, and are not jurisdiction-
  checked or currency-checked.

## Corpus and method

TODO — record how the distillation was done, if you want the repo to be reproducible:

- corpus actually read (editions, chapters, whether full text or excerpts);
- selection criteria used to keep or cut material;
- any verification passes run (held-out projection tests, style-match checks, cost tests);
- date of distillation and the model used.

## Change discipline

Changes that alter a named framework's terminology, drop a cost-bearing element (the
normative-restraint discipline in Move 1, the conceded cost in Move 2), or add a fourth move are
**MAJOR or MINOR** changes under this repo's versioning convention — record them in `CHANGELOG.md`
with a note on what evidence motivated the change.
