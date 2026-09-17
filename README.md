# technology-law-expert-colleague

I read a technology-law problem by locating who already governs the activity and what their arrangement allocates. A new capability arrives inside markets, states, professions, and legal institutions. I ask who controls access, whose standards travel across borders, and which people bear the costs. The reach of a rule and the justification for that reach need separate arguments.

When automation is defended as cheaper or more efficient, I examine the measure and the work it leaves out. A faster professional service may save time while reducing the opportunity to notice an exception or explain a decision. I name both the saving and the cost of preserving that judgment. Calling a person “in the loop” answers little until I know what information, discretion, and power to disagree they retain.

I then locate the exact legal question: the actor, conduct, injury, jurisdiction, claim, and remedy. For conduct in a virtual environment, I compare the interests and rationales behind the nearest doctrines, asking which fact makes the analogies diverge. Novelty alone does not tell us whether an existing rule works. I look for an available doctrinal lever, verify its legal basis, and identify the gap if it cannot address the problem.

My recommendations connect institutional power, distributional justification, and doctrinal mechanics. I distinguish a normative position from a conclusion about current law and state the strongest objection that could change my view. This Agent Skill provides that three-move reasoning approach, with references loaded for the part of the problem that needs depth.

## What this is for

Analysis, study, teaching, and ideation. It is a **thinking lens**, not a person: it does not
reproduce, impersonate, or attribute invented statements to any real scholar, and it is not legal
advice.

## Repository layout

```
technology-law-expert-colleague/
├── SKILL.md                              # expert reasoning voice + Loading depth table
├── references/
│   ├── frameworks.md                     # named constructs + cross-move handoffs
│   └── clusters/
│       ├── institutional-reflex.md       # Move 1 depth — comparative-institutional machinery
│       ├── efficiency-refusal.md         # Move 2 depth — efficiency refusal, human expertise
│       └── doctrinal-mechanics.md        # Move 3 depth — doctrinal joints, policy levers
├── fidelity-ledger/                      # maintainer-only; never loaded as advice
│   ├── provenance.md                     # corpus, method, budget record, boundaries
│   └── coverage.md                       # every source unit → retained structure
├── tools/
│   └── validate_distillation.py          # stdlib budget/boundary validator
├── AGENTS.md                             # default expert role and project guidance
├── CHANGELOG.md
├── LICENSE
├── NOTICE.md                            # source attribution and licensing scope
└── .gitignore
```

`SKILL.md` is loaded whenever the skill triggers. Its connected first-person core sets the reasoning
stance; its final `Loading depth` section maps tasks to source depth. The files under `references/` are **progressive
disclosure**: the agent loads only the cluster or clusters the current question needs, so the base context stays
small. Files under `fidelity-ledger/` are for maintainers and auditing; they are deliberately outside
the runtime tree and are never routed by the skill.

| Load this | When the question turns on |
| --- | --- |
| `references/frameworks.md` | any named construct — the three orders, the four laws, policy levers |
| `references/clusters/institutional-reflex.md` | why a jurisdiction regulates as it does, or whether its rules travel |
| `references/clusters/efficiency-refusal.md` | an argument leaning on cheaper / scalable / inevitable, or automation replacing judgment |
| `references/clusters/doctrinal-mechanics.md` | which category the new facts strain, and how to tailor without new statutes |

## Installation

Clone the repository into the skill directory configured by your Agent Skills-compatible runtime:

```bash
git clone https://github.com/ariel-lee-1023/TechLaw-colleague.git \
  /path/to/your/skills/technology-law-expert-colleague
```

The runtime discovers the skill through the `name` and `description` fields in `SKILL.md`. Keep the
repository structure intact so every progressive-disclosure path continues to resolve.

For upload-based runtimes, package or zip the complete directory and import it as one skill. For
runtimes that expose a persistent instruction field plus retrievable knowledge, place `SKILL.md` in
that field and provide the `references/` tree as on-demand knowledge. The routing table at the end of
`SKILL.md` determines which module to retrieve.

## Usage

The skill triggers on substantive questions in its domain. Some examples:

- "Should the EU's AI Act apply to a model trained and served entirely outside the EU?"
- "A VR platform lets users grope each other's avatars. Is that assault, speech, or nothing?"
- "Our vendor says AI triage in the ED is cheaper and just as accurate. What am I not being told?"
- "Is a bespoke statute for autonomous vehicles better than working existing tort doctrine?"

Expect it to widen the frame before it answers, name the cost of the line it holds, and end at a
supported conclusion with its decisive doctrinal fork and remaining uncertainty.

## Design notes

- **Named frameworks are load-bearing.** The exact terms — *non-divisibility*, *inelastic target*,
  *complement, not replace*, *load-bearing rationale*, *policy levers*, *magic circle* — are not
  interchangeable with paraphrases. Preserve them when editing.
- **The cost-bearing parts are the point.** The normative-restraint discipline in Move 1 and the
  conceded cost in Move 2 are what keep the persona from becoming a cheerleader for its own
  conclusions. Removing them makes the skill worse in a way that is hard to see in a single output.
- **The register shift is intentional.** Long and periodic in Move 1, tight and semicolon-linked in
  Move 2, crisp and conditional in Move 3.

## Distillation quality and budgets

This repository uses the Books-to-Skill-Refs discipline while preserving its pre-existing
three-cluster architecture. The full source structure was distilled into the runtime modules; it was
not converted into one file per book because the intended load unit is one analytical move.

Each cluster is measured as a whole-load, text-heavy, `reference`-depth unit. The budget scales with
the total number of source chapters or major sections feeding that cluster:

```text
budget = 1,700 + (1,050 + 1,500 × sqrt(sections)) × 0.55
acceptance band = budget ±10%          hard cap = 8,500 tokens
```

Current realized sizes:

| Runtime cluster | Source sections | Target | Allowed band | Realized |
| --- | ---: | ---: | ---: | ---: |
| institutional-reflex | 18 | 5,778 | 5,201–6,355 | 6,206 |
| efficiency-refusal | 8 | 4,611 | 4,150–5,072 | 4,811 |
| doctrinal-mechanics | 20 | 5,967 | 5,371–6,563 | 6,403 |

Run `python3 tools/validate_distillation.py` to reproduce the measurement. CI also checks the runtime
versus maintainer-documentation boundary. See `fidelity-ledger/provenance.md` for corpus and method,
and `fidelity-ledger/coverage.md` for the source-to-module acceptance ledger.

## Contributing

Issues and pull requests are welcome. Please:

- keep `SKILL.md` under ~500 lines and push depth into `references/`;
- preserve exact framework terminology, or explain in the PR why a term should change;
- keep provenance, sourcing, fidelity, and maintenance notes in `fidelity-ledger/`, never in the
  host-loaded `references/` tree;
- run `python3 tools/validate_distillation.py` and keep every cluster inside its computed band;
- update `CHANGELOG.md` under `[Unreleased]`;
- avoid adding verbatim quotation from the underlying copyrighted works beyond the short anchors
  already present for auditing purposes.

## License

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

The license covers this repository's original text. It does not extend to the underlying source books, which remain the property of their respective copyright holders.

## Disclaimer

Not legal advice. The skill encodes an analytical method, not the views of any living scholar, and it
must not be used to attribute invented statements to a real person.
