# technology-law-expert-colleague

A Claude Skill that gives an agent the working habits of a technology-law expert colleague: it runs
every hard tech-regulation or novel-technology legal question through a fixed three-move sequence
instead of jumping to a verdict.

1. **Institutional/power map** — why *this* jurisdiction regulates *this* activity *this* way, and
   what that design reveals about the power behind it.
2. **Efficiency refusal** — treat *cheaper / smoother / scalable / inevitable* as presumptively
   suspect; ask *for whom*; defend the non-automatable core of professional judgment.
3. **Doctrinal-mechanics diagnosis** — locate the exact doctrine the new facts strain and the
   load-bearing rationale that fails, and prefer the lever already inside the doctrine to the statute
   not yet written.

The moves compound. Skip the first and you mistake a power structure for a technical necessity; skip
the second and a balance sheet passes as a principle; skip the third and you have opinions but no
purchase on the law.

## What this is for

Analysis, study, teaching, and ideation. It is a **thinking lens**, not a person: it does not
reproduce, impersonate, or attribute invented statements to any real scholar, and it is not legal
advice.

## Repository layout

```
technology-law-expert-colleague/
├── SKILL.md                              # the skill itself (YAML frontmatter + instructions)
├── references/
│   ├── frameworks.md                     # named constructs, defined in their source sense
│   ├── provenance.md                     # sources, confidence, and reuse policy
│   └── clusters/
│       ├── institutional-reflex.md       # Move 1 depth — comparative-institutional machinery
│       ├── efficiency-refusal.md         # Move 2 depth — efficiency refusal, human expertise
│       └── doctrinal-mechanics.md        # Move 3 depth — doctrinal joints, policy levers
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

`SKILL.md` is loaded whenever the skill triggers. The files under `references/` are **progressive
disclosure**: the agent loads only the cluster the current move needs, so the base context stays
small.

| Load this | When the question turns on |
| --- | --- |
| `references/frameworks.md` | any named construct — the three orders, the four laws, policy levers |
| `references/clusters/institutional-reflex.md` | why a jurisdiction regulates as it does, or whether its rules travel |
| `references/clusters/efficiency-refusal.md` | an argument leaning on cheaper / scalable / inevitable, or automation replacing judgment |
| `references/clusters/doctrinal-mechanics.md` | which category the new facts strain, and how to tailor without new statutes |

## Installation

**Claude Code / agents that read a skills directory**

```bash
git clone https://github.com/<your-username>/technology-law-expert-colleague.git \
  ~/.claude/skills/technology-law-expert-colleague
```

The skill is discovered by its frontmatter `name` and `description`; nothing else is required.

**Claude.ai / Claude Desktop**

Zip the folder (or package it as a `.skill` file) and upload it as a custom skill, keeping the
directory structure intact so the `references/` paths in `SKILL.md` still resolve.

**Any other host agent**

Copy `SKILL.md` into your system prompt and make the `references/` files retrievable on demand.
The loading note at the bottom of `SKILL.md` tells the host which file to pull for which move.

## Usage

The skill triggers on substantive questions in its domain. Some examples:

- "Should the EU's AI Act apply to a model trained and served entirely outside the EU?"
- "A VR platform lets users grope each other's avatars. Is that assault, speech, or nothing?"
- "Our vendor says AI triage in the ED is cheaper and just as accurate. What am I not being told?"
- "Is a bespoke statute for autonomous vehicles better than working existing tort doctrine?"

Expect it to widen the frame before it answers, name the cost of the line it holds, and end at a
doctrinal fork rather than a verdict.

## Design notes

- **Named frameworks are load-bearing.** The exact terms — *non-divisibility*, *inelastic target*,
  *complement, not replace*, *load-bearing rationale*, *policy levers*, *magic circle* — are not
  interchangeable with paraphrases. Preserve them when editing.
- **The cost-bearing parts are the point.** The normative-restraint discipline in Move 1 and the
  conceded cost in Move 2 are what keep the persona from becoming a cheerleader for its own
  conclusions. Removing them makes the skill worse in a way that is hard to see in a single output.
- **The register shift is intentional.** Long and periodic in Move 1, tight and semicolon-linked in
  Move 2, crisp and conditional in Move 3.

See `references/provenance.md` for the source basis and reuse policy.

## Contributing

Issues and pull requests are welcome. Please:

- keep `SKILL.md` under ~500 lines and push depth into `references/`;
- preserve exact framework terminology, or explain in the PR why a term should change;
- update `CHANGELOG.md` under `[Unreleased]`;
- avoid adding verbatim quotation from the underlying copyrighted works beyond the short anchors
  already present for auditing purposes.

## License

MIT © 2026 Ariel Lee. [See LICENSE](LICENSE).

The license covers this repository's original text. It does not extend to the underlying source books, which remain the property of their respective copyright holders.

## Disclaimer

Not legal advice. The skill encodes an analytical method, not the views of any living scholar, and it
must not be used to attribute invented statements to a real person.
