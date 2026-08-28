# Library

Materials you place. One file per source where the licence permits it; a link and
a note where it does not.

## What to put here

Primary text, by preference: the specification, the standard, the regulation, the
judgment. Secondary sources are welcome and should be named as secondary in the
filename or a sidecar note, because a claim resting on a vendor's documentation of
a specification is a different kind of claim from one resting on the specification.

Also welcome, and currently missing: the KAIROS Source Library spreadsheet and the
Research Roadmap HTML. Without them the 117 catalogued sources are names with no
live link, no access status, no trust tier and no rating, and the research
programme cannot be sequenced.

## Naming

```
<issuer>-<designation>-<edition-or-date>-<short-title>.<ext>
oasis-xacml-3.0-errata01-2017-07-12-core-specification.pdf
omg-dmn-1.5-2024-08-decision-model-and-notation.pdf
openid-authorization-api-1.0-2026-03-11-final.pdf
```

Edition or date in the filename is not decoration. Four of the seven delivered
parts carry a currency finding that turns on an edition, and one records a
discrepancy between two publishers about which edition an ISO number designates.

## Sidecar notes

Where a file needs context, put it beside the file as `<same-name>.note.md`:
where it came from, the date it was fetched, whether the fetch was of the whole
document or a part, and anything the licence forbids reproducing. A dead link
already cost this programme once.

### Tagging by stage and Azure component

A sidecar may also carry two tag lines, read automatically into
`Standards/registers/library-index.md`:

```
stage: 5, 6
azure_components: Key Vault, Entra ID (Azure AD)
```

Tag with stage numbers, not names, and component names spelled exactly as in
`Standards/registers/taxonomy.md`, so the join is a string match. Both schemes
are recorded canonically there; this is the mechanical convention for applying
them, not a restatement of what they mean. See
`Standards/registers/collision-map.md` before tagging a source that plausibly
belongs to more than one proposed series: several components, most sharply
Azure DevOps Pipelines, are already claimed by four series at once, and a
source's tags should reflect a stated boundary rather than every plausible
claim.

## Priority

The four sources below each currently support a MUST NOT in a delivered part that
refuses a construct implementers use routinely. Each rests on secondary
description. They are the highest value acquisitions in the whole list.

| Source | What rests on it |
| --- | --- |
| DMN 1.5, the hit policy clause | `P5-3.59`, refusing selection by rule order |
| BPMN 2.0.2, section 13 execution semantics | `P6-3.32`, requiring exclusive split conditions to be mutually exclusive |
| XACML 3.0, the normative combining algorithm appendix | `P7-3.51` and `P7-3.52` |
| OpenID Authorization API 1.0 | `P7-7.6`, refusing a two valued decision interface |
