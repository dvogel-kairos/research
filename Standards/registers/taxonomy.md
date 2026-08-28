# Taxonomy

**Hand authored. Not derived.** These two schemes were supplied by the standards
owner on 2026-08-28 and are recorded here verbatim as the canonical source. Every
other register that tags a document by stage or Azure component refers back to
this file rather than restating the definitions.

## Stage taxonomy

Nine stages. Stages 1 and 2 are process-ordered ahead of the rest because later
stages assume the consumption and decomposition patterns they establish are
settled. Stages 7, 8 and 9 are additions to the original template.

| # | Stage | Governs |
| --- | --- | --- |
| 1 | Intake | How the organization consumes information and policy, and how a legacy application, data feed, or external system first enters the org. |
| 2 | Decomposition | How a given code set, requests, documents and other inputs from intake get broken down. |
| 3 | Ideation (PDLC) | Policies and standards governing the ideation phase of the product development lifecycle. |
| 4 | Definition (PDLC) | Policies and standards governing the definition phase. |
| 5 | Design (PDLC) | Schema design, API design, cloud and application architecture, UX, and the strategic half of security: what controls the architecture needs. |
| 6 | Development / Build (PDLC) | Actual code construction, including the actionable half of security: how to implement the chosen controls, and the infrastructure-as-code authoring tools themselves. |
| 7 | Testing / QA (PDLC) | Test strategy, automation, and formal acceptance / UAT criteria. |
| 8 | Release & Deployment (PDLC) | Release management, deployment mechanics, and production reliability practice. |
| 9 | Operations & Compliance | Ongoing, not strictly a PDLC phase: regulatory and certification frameworks, change / incident management, and the credential layer for staff. |

Stage 5 and Stage 6 split security explicitly, by the taxonomy's own wording:
strategic (what controls the architecture needs) in 5, actionable (how to
implement them) in 6. A source or series that covers security in the ordinary
sense will very often need to declare both stages rather than one, and a series
that tries to be the single home for security should expect to be split rather
than merged.

## Azure component taxonomy

Sixteen components. Every processed source is to be tagged by the component or
components it governs, regardless of current hosting.

**This is the target taxonomy, not a migration crosswalk.** Production is
currently hosted locally. A source tagged `Storage (Blob)` governs the target
state of blob storage governance, not a statement that anything is on Blob today.
The local-to-Azure move is handled separately and is out of scope for this
tagging exercise.

| Component |
| --- |
| App Service |
| AKS (Azure Kubernetes Service) |
| Azure Functions |
| Azure Database for PostgreSQL (Flexible Server) |
| Azure Databricks |
| Key Vault |
| API Management |
| Entra ID (Azure AD) |
| Storage (Blob) |
| Event Grid |
| Service Bus |
| Networking / VNet |
| Azure Monitor / Log Analytics |
| Azure DevOps Pipelines |
| Azure Resource Manager / Bicep (IaC layer) |
| Defender for Cloud / Azure Policy |

## How the two taxonomies apply to two different kinds of document

STD 003 parts and the proposed KAIROS-* series are not the same kind of object
under this taxonomy, and tagging them the same way would misstate what each is.

**A KAIROS-* series is phase-of-work policy.** It governs how people do something
at a point in the product development lifecycle: how an API is designed, how a
pipeline is authored, how a test is written. It sits naturally in one or two
stages and, where its subject is an Azure service, governs that service directly.
Tagging it is a straightforward declaration.

**A STD 003 part is runtime architecture.** It specifies a component that exists
and behaves a particular way once a system is built, independent of which stage
built it. Storage neutrality is a stated requirement of Part 1; several parts'
own section 12 boundaries refuse to bind to a specific implementation, on
purpose, so that the standard is not tied to a platform. So a STD 003 part's
stage tag records where its subject matter is most actively consulted, not
where the part itself lives, and its Azure component tag, where one applies at
all, records a plausible deployment binding for assessment purposes rather
than a governed dependency. `Standards/registers/collision-map.md` states this
distinction again against each part, so it is not lost in a table cell.

## Tagging convention

Recorded in full in `Library/README.md`. Summarized here: a `<file>.note.md`
sidecar may carry `stage: <comma list>` and `azure_components: <comma list>`
lines, read by `Standards/tools/build_registers.py` into
`Standards/registers/library-index.md`. Tag with stage numbers, not names, and
component names exactly as spelled in the table above, so that a later automated
join is a string match rather than a fuzzy one.
