# Collision map

Cross-references `Standards/std-003/` and the thirteen series proposed in the
2026-08-28 research handoff against the two axes in `taxonomy.md`. Hand
authored: assigning a stage or component to a document is a judgement, not an
extraction, so this file is not derived by the generator the way the clause and
question registers are. It should be revisited whenever a part is delivered or a
series is authored, and each revision should be a diff against this version
rather than a silent rewrite.

Read `taxonomy.md` first for what a STD 003 part's tag means, since it is not
the same kind of statement as a series' tag.

## STD 003 parts by stage

| Part | Subject | Stage(s) most actively consulted | Why |
| --- | --- | --- | --- |
| 1 | Controlled documents & records | 9, and foundational to all | Cited by every other part as the substrate for policy text, authority citations and approvals. Most visibly governed at Stage 9 through retention and regulatory obligations. |
| 2 | Business rules & constraint evaluation | 4 | Constraints are authored where business rules are defined. Consumed at runtime by Parts 5, 6 and 7 regardless of which stage produced the rule. |
| 3 | Provenance & audit ledger | 9 | The audit trail and determination record are an operations and compliance concern by nature. |
| 4 | Metadata & model repository | 2, 5 | Governed definitions are the output of decomposing inputs (2) and the input to schema design (5). |
| 5 | Decision engine | 4 | A criterion is a definition-phase artifact; its evaluation is runtime and stage-agnostic. |
| 6 | Workflow & process orchestration | 6 | Business process orchestration is implemented during build. Not Stage 8: this is process logic, not deployment pipeline logic. |
| 7 | Policy decision point & authorization | 5, 6, 9 | Split exactly as the taxonomy splits security: strategic policy shape at 5, enforcement point integration at 6, the staff credential layer at 9. |

## STD 003 parts by Azure component

Every entry below is a **plausible deployment binding**, not a governed
dependency. Each part's own section 12 boundaries were written to keep the part
storage- and platform-neutral, and this table does not override that.

| Part | Plausible binding | Note |
| --- | --- | --- |
| 1 | Storage (Blob) | For content octets, which Part 1 explicitly treats as a deployment decision, not a requirement. |
| 3 | Storage (Blob), Event Grid | Ledger storage and event emission. |
| 4 | Azure Database for PostgreSQL, Azure Databricks | Metadata storage; Databricks only where a governed model is ML rather than a definition. |
| 6 | Service Bus, Event Grid | Event-driven orchestration. Not Azure DevOps Pipelines: Part 6 is business process orchestration, not CI/CD. |
| 7 | Entra ID, Key Vault, API Management, Defender for Cloud / Azure Policy | Entra ID as one possible attribute source for the authentication reference Part 7 records and never verifies. Key Vault for policy signing material. API Management as one possible enforcement point implementation, which Part 7 does not specify. Defender / Policy as the cloud-native analogue of the policy decision point pattern, worth cross-checking against Part 7 rather than adopting wholesale. |
| 2, 5 | None | Abstract evaluation and selection logic with no natural platform binding. |

## Proposed series by stage

| Series | Stage(s) | Note |
| --- | --- | --- |
| KAIROS-REQ | 3, 4 | Requirement and acceptance-criterion writing technique spans ideation and definition. |
| KAIROS-API | 5 | Design phase, per the taxonomy's own wording naming API design explicitly. |
| KAIROS-DATA | 5 | Schema design, named explicitly. |
| KAIROS-AZURE | 5, 6, 8 | Splits by function: identity and messaging design touch 5, compute and IaC authoring touch 6, pipelines touch 8. See the allocation register's note on whether this should be one series or four. |
| KAIROS-CLOUD | 5, 6, 8 | Well-architected framework content is Stage 5; Terraform / Bicep / ARM authoring is Stage 6; landing zones and pipelines are Stage 8. |
| KAIROS-CODE | 6 | Code construction and review practice. |
| KAIROS-SEC | 5, 6 | The taxonomy names this split explicitly: strategic controls at 5, actionable implementation at 6. Recommend authoring as two documents or one document with an internal boundary as sharp as a STD 003 part's section 12, not one undifferentiated series. |
| KAIROS-MOD | 6, 9 | Legacy decomposition and dependency hygiene touch build; ongoing modernization backlog touches operations. |
| KAIROS-QA | 7 | Named directly. |
| KAIROS-DINT | 1, 2 | Data ingestion and integration patterns sit at intake and decomposition, ahead of the PDLC stages, consistent with the taxonomy's own ordering rationale. |
| KAIROS-PM | 3, 9 | Program management frames ideation and also governs ongoing delivery cadence. |
| KAIROS-GOV | 9 | Named directly: governance and documentation. |
| KAIROS-UX | 5 | Named directly. |

## Proposed series by Azure component

| Series | Component(s) | Collision flag |
| --- | --- | --- |
| KAIROS-AZURE | All sixteen, by design | See below: every other row that names a component overlaps this one. That is expected, not a defect, provided KAIROS-AZURE is the platform-mechanics reference and the colliding series stays at the practice layer. State the boundary explicitly per pair rather than leaving it implicit. |
| KAIROS-SEC | Key Vault, Entra ID, Defender for Cloud / Azure Policy | Collides with KAIROS-AZURE on all three. |
| KAIROS-DATA | Azure Database for PostgreSQL, Azure Databricks, Storage (Blob) | Collides with KAIROS-AZURE on all three. |
| KAIROS-CLOUD | Azure Resource Manager / Bicep, Networking / VNet, Azure DevOps Pipelines, Defender for Cloud / Azure Policy | Collides with KAIROS-AZURE on all four, and with KAIROS-SEC on the last. |
| KAIROS-CODE | Azure DevOps Pipelines | Collides with KAIROS-AZURE and with KAIROS-CLOUD. Three-way. |
| KAIROS-DINT | Event Grid, Service Bus, Storage (Blob) | Collides with KAIROS-AZURE on all three, and with KAIROS-DATA on Storage. Also the direct consumer of KAIROS-EVT, since Event Grid uses CloudEvents. |
| KAIROS-API | API Management | Collides with KAIROS-AZURE. |
| KAIROS-QA | Azure Monitor / Log Analytics (for test telemetry), Azure DevOps Pipelines (for CI gating) | Collides with KAIROS-AZURE and, on pipelines, with KAIROS-CODE and KAIROS-CLOUD. Four-way on that one component. |

## Collision candidates, ranked by how many series claim the same component

**Azure DevOps Pipelines.** Claimed by AZURE, CLOUD, CODE and QA. The sharpest
collision in the whole map, because all four are plausible: platform mechanics,
IaC deployment, release practice, and CI test gating are all real relationships
to one Azure service. Resolve before authoring any of the four, using the same
pattern STD 003 uses for a boundary: what each series delegates, what it must
not absorb, and a stated seam. A workable split: AZURE owns the service's
mechanics and configuration surface; CLOUD owns what a pipeline deploys and
when, as a landing-zone and IaC concern; CODE owns what gates a merge; QA owns
what gates a release. That is four genuinely different questions about one
service, which is a sign the collision is real rather than a naming accident.

**Defender for Cloud / Azure Policy.** Claimed by AZURE, SEC and CLOUD. Resolve
by the same pattern: AZURE owns configuration, SEC owns which controls are
required, CLOUD owns where the enforcement sits in a landing zone. Cross-check
this component specifically against STD 003 Part 7 before writing anything,
since Defender / Policy is a cloud-native instance of exactly the policy
decision point pattern Part 7 specifies in the abstract. A KAIROS document that
reinvents that boundary without reading Part 7 first risks the same drift
`Part 5` and `Part 7` already produced on the third value, recorded in Part 7
section 13.7.

**Key Vault and Entra ID.** Each claimed by both AZURE and SEC. Resolve with
AZURE owning the service mechanics and SEC owning the practice: rotation
policy, access review cadence, credential lifecycle. Straightforward once
stated; unresolved silently otherwise.

**Storage (Blob), Event Grid, Service Bus.** Claimed by AZURE and DINT, with
Storage also claimed by DATA. These three are also where **KAIROS-EVT is
already load bearing**: Event Grid is a CloudEvents producer, and EVT is cited
by all seven delivered STD 003 parts as the event envelope model. Any DINT or
AZURE content touching these three components should treat EVT's ten documents
as upstream rather than re-deriving CloudEvents semantics.

## What this means for the allocation register

`allocation.md`'s bucket A and bucket B sorting still holds; this map adds a
second, orthogonal reason a series might need to be split rather than
authored whole, distinct from the STD 003 collision reason bucket A names. A
series can clear the bucket A/B/C test, meaning it does not collide with an
unwritten STD 003 part, and still collide with another proposed series on this
map. KAIROS-AZURE, KAIROS-CLOUD, KAIROS-CODE and KAIROS-QA all clear bucket B
and all four claim Azure DevOps Pipelines: the two axes are independent checks,
and a series has to clear both.

**Recommendation.** Before authoring any bucket B series, declare its stage tag
and its Azure component tags against this map, and where a component is
claimed by more than one series, write the boundary paragraph, in the STD 003
section 12 style, before writing either series' substance. That is cheaper now
than after both exist and have started to diverge, which is the lesson every
STD 003 part's own section 13.7 already recorded once.
