# KAIROS STD 003 Part 10: Reference and Master Data Management

**Standard.** KAIROS STD 003, the enterprise architecture standard.
**Part.** Part 10 of 14 (Part 0 and Parts 1 through 13). Cited as `KAIROS STD 003 Part 10`.
**Title.** Reference and master data management.
**Version.** 1.0.0.
**Status.** Proposed. This part has not been approved and is not effective. It is issued for review against the authoring brief of 2026-08-17.
**Date of issue.** 2026-08-18.
**Supersedes.** Nothing. This is the first version.

## Binding of requirement language

The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in this part are to be interpreted as described in RFC 2119 and RFC 8174, and only in the upper case forms. This part does not use SHALL, SHALL NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED or OPTIONAL as requirement keywords.

Every requirement in this part is a numbered clause. A clause identifier has the form `P10-S.N`, where `S` is the section number and `N` is the ordinal of the clause within that section. Clause identifiers are permanent. A clause that is later removed has its identifier retired and never reissued. A clause that is later added to a section takes the next unused ordinal in that section, so ordinals are stable but not contiguous over the life of the part.

Text that is not a numbered clause is not binding. Narrative, tables, algorithms, examples and the discussion of standards are provided to make the clauses intelligible and testable, and where a table carries normative content a clause says so explicitly and names the table.

Where a clause carries a **Source.** note, the note states the specification or practice on which the clause's subject rests and whether this part adopts that treatment or departs from it. The note is narrative and not binding; the clause governs.

## Conformance

An implementation conforms to this part if it satisfies every MUST and MUST NOT clause and records, for each SHOULD and SHOULD NOT clause it does not satisfy, the reason. This part does not define conformance levels, profiles or a certification scheme, and it does not define the method of assessment. Assessment method is the subject of `KAIROS STD 003 Part 12` and is out of scope here.

Where a clause states that a value is an implementation decision, conformance requires that the implementation declare the value, not that it adopt a particular one. An undeclared implementation decision is a nonconformity.

## Clause index

The index below is generated from the clause text of this document. It lists every clause identifier, its modality and its subject label. The counts that follow the index are derived by the same extraction and are stated with the grain at which they were counted.

| Clause | Modality | Subject |
| --- | --- | --- |
| P10-1.1 | MUST | Code systems owned |
| P10-1.2 | MUST | Concepts owned |
| P10-1.3 | MUST | Value sets owned |
| P10-1.4 | MUST | Expansions owned |
| P10-1.5 | MUST | Membership determination owned |
| P10-1.6 | MUST | Relations owned |
| P10-1.7 | MUST | Maps owned |
| P10-1.8 | MUST | Master entities owned |
| P10-1.9 | MUST | Contributions owned |
| P10-1.10 | MUST | Match and merge assertions owned |
| P10-1.11 | MUST | Survivorship outcomes owned |
| P10-1.12 | MUST | Distribution record owned |
| P10-1.13 | MUST | Consumption reports owned |
| P10-1.14 | MUST | Stewardship owned |
| P10-1.15 | MUST NOT | Not the meaning of a governed term |
| P10-1.16 | MUST NOT | Not a rules engine |
| P10-1.17 | MUST NOT | Not a schema authority |
| P10-1.18 | MUST NOT | Not a decision point for access |
| P10-1.19 | MUST NOT | Not a decision engine |
| P10-1.20 | MUST NOT | Not the document authority |
| P10-1.21 | MUST NOT | Not the audit ledger |
| P10-1.22 | MUST NOT | Not the artifact store |
| P10-1.23 | MUST NOT | Not a work manager |
| P10-1.24 | MUST NOT | Not the enforcer of its own currency |
| P10-1.25 | MUST NOT | Not an assessor of itself |
| P10-1.26 | MUST | The two subjects distinguished |
| P10-1.27 | MUST NOT | No matching over concepts |
| P10-1.28 | MUST NOT | No release gate on a factual correction |
| P10-1.29 | MUST | Kind declared per operation |
| P10-1.30 | MUST NOT | No conformance assessment anticipated |
| P10-2.1 | MUST NOT | No redefinition of another part's terms |
| P10-2.2 | MUST NOT | Concept not equated with designation |
| P10-2.3 | MUST NOT | Value set not equated with code system |
| P10-2.4 | MUST NOT | Expansion not equated with definition |
| P10-2.5 | MUST NOT | Master identifier not equated with source identifier |
| P10-2.6 | MUST NOT | Golden view not equated with record |
| P10-2.7 | MUST | Kinds registered before use |
| P10-2.8 | MUST NOT | No private meanings |
| P10-3.1 | MUST | Types declared |
| P10-3.2 | MUST | Instants carry offset and resolution |
| P10-3.3 | MUST NOT | No representation dependent identity |
| P10-3.4 | MUST | Two records kept apart |
| P10-3.5 | MUST NOT | No inference of consumption from distribution |
| P10-3.6 | MUST | Absence of a report is ordinary |
| P10-3.7 | MUST | Unreported population countable |
| P10-3.8 | MUST NOT | No currency claim without reports |
| P10-3.9 | MUST | Currency figure declares its base |
| P10-3.10 | MUST | Inventory normative |
| P10-3.11 | MUST | Immutability observed |
| P10-3.12 | MUST | Kind attached to every entity |
| P10-3.13 | MUST | Version is the unit of reference |
| P10-3.14 | MUST NOT | No ordering from a designation |
| P10-3.15 | MUST | Completeness of content declared |
| P10-3.16 | MUST NOT | No determination of non membership against a fragment |
| P10-3.17 | MUST | External authorship recorded |
| P10-3.18 | MUST NOT | No local edit of external content |
| P10-3.19 | MUST | Key scheme registered |
| P10-3.20 | MUST | Case sensitivity declared |
| P10-3.21 | MUST NOT | Keys never reused |
| P10-3.22 | MUST NOT | No deletion of a concept |
| P10-3.23 | MUST | Definition present and textual |
| P10-3.24 | MUST | One preferred designation per language |
| P10-3.25 | MUST NOT | No meaning change under a stable key |
| P10-3.26 | MUST | Designation change distinguished from meaning change |
| P10-3.27 | MUST | Inactivation reason recorded |
| P10-3.28 | MUST | Successor stated or its absence stated |
| P10-3.29 | MUST | Successor association kind declared |
| P10-3.30 | MUST NOT | No automatic substitution of a successor |
| P10-3.31 | MUST | Definition mode declared |
| P10-3.32 | MUST NOT | No membership attributed to an intensional definition alone |
| P10-3.33 | MUST | Code system version binding declared |
| P10-3.34 | MUST | Unpinned binding surfaces as a hazard |
| P10-3.35 | MUST NOT | No enumeration in place of a reference |
| P10-3.36 | MUST | Rule kinds registered |
| P10-3.37 | MUST | Rule kinds carry a closure declaration |
| P10-3.38 | MUST | Expansion is an artifact |
| P10-3.39 | MUST | Expansion records its inputs |
| P10-3.40 | MUST NOT | No expansion reuse across inputs |
| P10-3.41 | MUST | Truncation declared |
| P10-3.42 | MUST NOT | No membership determination from a truncated expansion |
| P10-3.43 | MUST | Inclusion of inactive members declared |
| P10-3.44 | MUST | Withheld marked, never omitted |
| P10-3.45 | MUST | Withheld count returned |
| P10-3.46 | MUST NOT | No non membership from a set with withheld members |
| P10-3.47 | MUST | Marking vocabulary named |
| P10-3.48 | MUST | Distribution constraint recorded |
| P10-3.49 | MUST NOT | No distribution beyond a recorded constraint |
| P10-3.50 | MUST | Licence dependent membership exposed |
| P10-3.51 | MUST | Relation kinds registered with transitivity |
| P10-3.52 | MUST NOT | No inferred relation published as asserted |
| P10-3.53 | MUST | Equivalence class on every entry |
| P10-3.54 | MUST | Unmatched recorded as an entry |
| P10-3.55 | MUST NOT | No silent unmapped default |
| P10-3.56 | MUST NOT | No automatic inversion |
| P10-3.57 | MUST NOT | No composition of maps |
| P10-3.58 | MUST | Map completeness declared |
| P10-3.59 | MUST | Conditional entries carry their condition |
| P10-3.60 | MUST | Master identifier assigned here |
| P10-3.61 | MUST NOT | Master identifiers never reused |
| P10-3.62 | MUST | Source identifiers retained as cross references |
| P10-3.63 | MUST | Existence basis recorded |
| P10-3.64 | MUST | Domain declared before records |
| P10-3.65 | MUST | Contributions retained whole |
| P10-3.66 | MUST NOT | No overwrite of a contribution |
| P10-3.67 | MUST | Two instants distinguished |
| P10-3.68 | MUST NOT | No inference of currency from receipt order |
| P10-3.69 | MUST | Bound values carry their value set version |
| P10-3.70 | MUST | Match is an assertion |
| P10-3.71 | MUST | Basis recorded, with its parameters |
| P10-3.72 | MUST NOT | No merge without a match assertion |
| P10-3.73 | MUST NOT | No deletion on merge |
| P10-3.74 | MUST | Absorbed identifier resolves |
| P10-3.75 | MUST | Unmerge supported |
| P10-3.76 | MUST | Unmerge recorded, not erased |
| P10-3.77 | MUST NOT | No survivorship by source order |
| P10-3.78 | MUST | Survivorship rule declared per attribute |
| P10-3.79 | MUST | Survivorship determination recorded |
| P10-3.80 | MUST | Survivorship conflict reported |
| P10-3.81 | MUST | Unresolved conflict has an owner |
| P10-3.82 | MUST NOT | No probabilistic match executed as final without a threshold declaration |
| P10-3.83 | MUST | Match band declared |
| P10-3.84 | MUST | Adjudication obtained, not performed |
| P10-3.85 | MUST | Consumers registered |
| P10-3.86 | MUST | Distribution recorded per consumer |
| P10-3.87 | MUST | Report basis recorded |
| P10-3.88 | MUST | Reporting capability declared |
| P10-3.89 | MUST NOT | No exclusion of the incapable from the count |
| P10-3.90 | MUST | Expansion digest reported where computed |
| P10-3.91 | MUST | Staleness measured against the declared interval |
| P10-3.92 | MUST | Steward assigned to every subject |
| P10-3.93 | MUST | Stewardship is accountability, not access |
| P10-3.94 | MUST | Steward absence blocks progression |
| P10-3.95 | MUST | Steward changes recorded |
| P10-3.96 | MUST | Retention floor recorded per version |
| P10-3.97 | MUST | Retention floor raised on citation |
| P10-3.98 | MUST NOT | No disposition below the floor |
| P10-3.99 | MUST | Unknown citation exposed |
| P10-3.100 | MUST | Tombstone on disposition |
| P10-3.101 | MUST | Digests survive disposition |
| P10-3.102 | MUST | Projections marked as such |
| P10-3.103 | MUST | Golden view is a projection |
| P10-3.104 | MUST | Contributions retrievable from the projection |
| P10-3.105 | MUST | Flattened expansion marked |
| P10-3.106 | MUST NOT | No boolean membership projection as a record |
| P10-4.1 | MUST | Operations defined over the entities of section 3 |
| P10-4.2 | MUST | Idempotency key accepted |
| P10-4.3 | MUST | Idempotency conflict refused |
| P10-4.4 | MUST | Authorisation obtained per operation |
| P10-4.5 | MUST | One outcome per operation |
| P10-4.6 | MUST | Refusals recorded |
| P10-4.7 | MUST NOT | No mutation of published content |
| P10-4.8 | MUST | Publication refused without a steward |
| P10-4.9 | MUST | Publication refused without a document identity |
| P10-4.10 | MUST | Inactivation refused without a reason |
| P10-4.11 | MUST | Inactivation refused without a successor statement |
| P10-4.12 | MUST | Key reuse refused |
| P10-4.13 | MUST | Map entry refused without an equivalence class |
| P10-4.14 | MUST | Map publication refused without a completeness declaration |
| P10-4.15 | MUST | Withdrawal refused while cited within the floor |
| P10-4.16 | MUST | Distribution refused to an unregistered consumer |
| P10-4.17 | MUST | Membership determination requires a pinned version |
| P10-4.18 | MUST | Membership determination requires code system versions |
| P10-4.19 | MUST | Membership determination returns an outcome, not a boolean |
| P10-4.20 | MUST | Expansion requires pinned inputs |
| P10-4.21 | MUST | Closure mode declared on request |
| P10-4.22 | MUST | Translate returns the equivalence class |
| P10-4.23 | MUST | Translate returns unmatched as a result |
| P10-4.24 | MUST | Absorbed identifier resolution returns the assertion |
| P10-4.25 | MUST NOT | No merge without adjudication in the referral band |
| P10-4.26 | MUST | Affected determinations answerable |
| P10-4.27 | MUST | Point in time read supported |
| P10-4.28 | MUST NOT | No state change from a read |
| P10-4.29 | MUST | Read carries the version that answered it |
| P10-4.30 | MUST | Withheld count on every delivered set |
| P10-4.31 | MUST NOT | No read of unpublished content by a consumer |
| P10-4.32 | MUST | Published versions immutable |
| P10-4.33 | MUST NOT | No assumption of expansion stability |
| P10-4.34 | MUST NOT | No assumption that absence of a finding means membership |
| P10-4.35 | MUST NOT | No assumption of successor substitutability |
| P10-4.36 | MUST NOT | No assumption that a master identifier denotes a verified entity |
| P10-4.37 | MUST NOT | No assumption of consumer currency |
| P10-4.38 | MUST | Reads treated as fallible |
| P10-4.39 | MUST NOT | No proceeding on an authorisation failure |
| P10-4.40 | MUST NOT | No caching beyond a pinning scope |
| P10-4.41 | MUST | Event per transition |
| P10-4.42 | MUST | Event carries prior state and cause |
| P10-4.43 | MUST | Events delivered to the ledger |
| P10-4.44 | MUST | Membership change event names affected sets |
| P10-4.45 | MUST | Concept inactivation event carries successors |
| P10-4.46 | MUST | Unpinned expansion drift event |
| P10-4.47 | MUST | Withholding event distinct |
| P10-4.48 | SHOULD | Unreported consumer signal |
| P10-5.1 | MUST | States held as transitions |
| P10-5.2 | MUST | One state per axis per instant |
| P10-5.3 | MUST NOT | No derivation of one axis from another |
| P10-5.4 | MUST | Transitions carry authorisation |
| P10-5.5 | MUST | Illegal transitions recorded |
| P10-5.6 | MUST NOT | No unlisted transition |
| P10-5.7 | MUST | Recorded requires complete metadata |
| P10-5.8 | MUST | Qualified requires steward and authority |
| P10-5.9 | MUST NOT | Recorded is not a quality claim |
| P10-5.10 | MUST | Superseded names its successor |
| P10-5.11 | MUST | Retired subjects still resolve |
| P10-5.12 | MUST | Draft content not distributable |
| P10-5.13 | MUST | Published content immutable |
| P10-5.14 | MUST | Deprecated content still determinable |
| P10-5.15 | MUST | Sunset requires the holder population |
| P10-5.16 | MUST NOT | No withdrawal while consumers report holding |
| P10-5.17 | MUST | Withdrawal reason recorded |
| P10-5.18 | MUST | No terminal state that removes resolvability |
| P10-5.19 | MUST | Inactive concepts remain in historical expansions |
| P10-5.20 | MUST | Reactivation reasoned |
| P10-5.21 | MUST NOT | No key release from retired_key |
| P10-5.22 | MUST | Expansion states terminal |
| P10-5.23 | MUST | Partial expansions retained |
| P10-5.24 | MUST | Provisional distinguished from confirmed |
| P10-5.25 | MUST | Absorbed records resolve |
| P10-5.26 | MUST | Unmerge restores the prior state |
| P10-5.27 | MUST | Void is terminal and resolvable |
| P10-5.28 | MUST | Disputed exposed |
| P10-5.29 | MUST | Merge state separate from record state |
| P10-5.30 | MUST | Withdrawn merges retained |
| P10-5.31 | MUST | Five states distinguished |
| P10-5.32 | MUST | Four states counted as unreported |
| P10-5.33 | MUST NOT | No terminal consumption state |
| P10-6.1 | MUST | Determination reproducible from its record |
| P10-6.2 | MUST | Expansion reproducible from its inputs |
| P10-6.3 | MUST | Reproducibility set recorded |
| P10-6.4 | MUST | Non reproducibility reported |
| P10-6.5 | MUST NOT | No clock in a determination |
| P10-6.6 | MUST NOT | No ordering dependence in an expansion |
| P10-6.7 | MUST | Non confluent definition refused |
| P10-6.8 | MUST | One snapshot per expansion |
| P10-6.9 | MUST | Unresolvable key refused |
| P10-6.10 | MUST | Exclusions applied after inclusions |
| P10-6.11 | MUST | Withholding applied last and counted |
| P10-6.12 | MUST | Size bound declared |
| P10-6.13 | MUST | Bound finite |
| P10-6.14 | MUST | Determination against an expansion or a definition, declared |
| P10-6.15 | MUST NOT | No determination from a stale expansion |
| P10-6.16 | MUST | Inactive membership distinguished |
| P10-6.17 | MUST NOT | Unknown code never non membership |
| P10-6.18 | MUST NOT | No non membership on an unresolvable input |
| P10-6.19 | MUST | Case handling declared and applied |
| P10-6.20 | MUST NOT | No normalisation of a submitted value |
| P10-6.21 | MUST | Determination cites the expansion |
| P10-6.22 | MUST | Closure requested, never assumed |
| P10-6.23 | MUST | Closure over a declared kind only |
| P10-6.24 | MUST | Closure result marked as inferred |
| P10-6.25 | MUST | Cycles detected and reported |
| P10-6.26 | MUST | Depth bound declared |
| P10-6.27 | MUST NOT | No closure across code systems |
| P10-6.28 | MUST NOT | No associative relation in a closure |
| P10-6.29 | MUST | Map applied under a pinned version |
| P10-6.30 | MUST | Every applicable entry returned |
| P10-6.31 | MUST NOT | No selection among map entries |
| P10-6.32 | MUST | Ambiguity reported |
| P10-6.33 | MUST NOT | No inversion at application time |
| P10-6.34 | MUST NOT | No chaining at application time |
| P10-6.35 | MUST | Unmapped policy applied and recorded |
| P10-6.36 | MUST | Conditional entry verdict obtained |
| P10-6.37 | MUST NOT | No non verdict treated as inapplicable |
| P10-6.38 | MUST | Matching deterministic given its inputs |
| P10-6.39 | MUST | Algorithm version pinned |
| P10-6.40 | MUST NOT | No re-run overwriting an assertion |
| P10-6.41 | MUST | Threshold change surfaces the affected population |
| P10-6.42 | MUST | Transitive merge closure declared |
| P10-6.43 | MUST | Inferred merge recorded as inferred |
| P10-6.44 | MUST | Unmerge recomputes the survivorship |
| P10-6.45 | MUST NOT | No survivorship from a merged away record without record |
| P10-6.46 | MUST | Rule evaluated per attribute |
| P10-6.47 | MUST | Rule kinds registered |
| P10-6.48 | MUST | Recency rules use the asserted instant |
| P10-6.49 | MUST | Source trust expressed as a declared weight |
| P10-6.50 | MUST | Tie reported, never broken arbitrarily |
| P10-6.51 | MUST | Conflict does not suppress the attribute |
| P10-6.52 | MUST | Determination idempotent under a key |
| P10-6.53 | MUST | Publication serialised |
| P10-6.54 | MUST | Contribution ingestion concurrent and ordered per source |
| P10-6.55 | MUST | Merge serialised per record |
| P10-6.56 | MUST | Bounds recorded |
| P10-6.57 | MUST NOT | No revaluation of a recorded determination |
| P10-6.58 | MUST | Affected determinations exposed |
| P10-6.59 | MUST NOT | No decision on the consequence |
| P10-6.60 | MUST | Change class stated with the exposure |
| P10-6.61 | MUST NOT | No retrospective application of a successor |
| P10-6.62 | MUST | Member coverage against consumers answerable |
| P10-6.63 | MUST | Full membership exposed for a consumer's own checks |
| P10-6.64 | MUST | Unused member reporting supported |
| P10-6.65 | MUST NOT | No coverage claim over an unenumerated population |
| P10-7.1 | MUST | One enumeration per value |
| P10-7.2 | MUST NOT | No value outside the enumerations |
| P10-7.3 | MUST | Properties of an outcome exposed |
| P10-7.4 | MUST | Not a member only on a complete determination |
| P10-7.5 | MUST NOT | No collapse to non membership |
| P10-7.6 | MUST NOT | No collapse to membership |
| P10-7.7 | MUST | Three incompleteness causes distinguished |
| P10-7.8 | MUST | System not referenced distinguished from unknown code |
| P10-7.9 | MUST | Complete only when nothing was withheld or truncated |
| P10-7.10 | MUST NOT | No refusal reported as an empty expansion |
| P10-7.11 | MUST | Refusal distinguished from failure |
| P10-7.12 | MUST | Unmatched distinguished from not covered |
| P10-7.13 | MUST NOT | No empty result for an uncovered source |
| P10-7.14 | MUST | Direction unavailable, never inverted |
| P10-7.15 | MUST NOT | No undetermined match treated as different |
| P10-7.16 | MUST | Referral is an outcome, not a delay |
| P10-7.17 | MUST | Insufficient attributes reported with the deficit |
| P10-7.18 | MUST | Authorisation denial distinguished from unavailability |
| P10-7.19 | MUST | Malformed distinguished from a determination |
| P10-7.20 | MUST | Three properties exposed |
| P10-7.21 | MUST NOT | No fault reported as a determination |
| P10-7.22 | MUST | Invariant violation halts the subject |
| P10-7.23 | MUST | Outcome carried whole |
| P10-7.24 | MUST NOT | No aggregation losing incompleteness |
| P10-7.25 | MUST | Non result retained where unconsumed |
| P10-7.26 | MUST | Counts report non results as categories |
| P10-8.1 | MUST | Completeness of each record declared |
| P10-8.2 | MUST NOT | No estate figure without its unknown |
| P10-8.3 | MUST | Grain stated with every count |
| P10-8.4 | MUST | Concept counts state their state filter |
| P10-8.5 | MUST | Membership counts state their expansion |
| P10-8.6 | MUST | Master counts state their record states |
| P10-8.7 | MUST NOT | No count of entities that mixes kinds |
| P10-8.8 | MUST | Every authoring act recorded |
| P10-8.9 | MUST | Every version transition recorded |
| P10-8.10 | MUST | Every determination recorded |
| P10-8.11 | MUST | Every expansion recorded |
| P10-8.12 | MUST | Every translation recorded |
| P10-8.13 | MUST | Every contribution recorded |
| P10-8.14 | MUST | Every match and merge recorded |
| P10-8.15 | MUST | Every survivorship determination recorded |
| P10-8.16 | MUST | Every withholding recorded |
| P10-8.17 | MUST | Every distribution and report recorded |
| P10-8.18 | MUST | Every refusal recorded |
| P10-8.19 | MUST | Content of a version at an instant |
| P10-8.20 | MUST | Membership of a value set at an instant |
| P10-8.21 | MUST | Inputs of a determination |
| P10-8.22 | MUST | Reason a concept ceased to be usable |
| P10-8.23 | MUST | Provenance of a presented master value |
| P10-8.24 | MUST | Basis of a merge |
| P10-8.25 | MUST | Withheld extent of a delivery |
| P10-8.26 | MUST | Holding of a consumer at an instant |
| P10-8.27 | MUST NOT | No reconstruction dependent on this component running |
| P10-8.28 | MUST | Unreported consumer population |
| P10-8.29 | MUST | Stale holding population |
| P10-8.30 | MUST | Unpinned value set population |
| P10-8.31 | MUST | Withheld dependent set population |
| P10-8.32 | MUST | Incomplete content population |
| P10-8.33 | MUST | Uncited version population |
| P10-8.34 | MUST | Unresolved survivorship conflict population |
| P10-8.35 | MUST | Disputed record population |
| P10-8.36 | MUST | Referral backlog population |
| P10-8.37 | MUST | Provisional record population |
| P10-8.38 | MUST | Inactive member population |
| P10-8.39 | MUST | Successorless inactive population |
| P10-8.40 | MUST | Affected determination population |
| P10-8.41 | SHOULD | Divergent expansion signal |
| P10-8.42 | MUST | Package assemblable for a determination |
| P10-8.43 | MUST | Package assemblable for a master value |
| P10-8.44 | MUST | Package states what it omits |
| P10-8.45 | MUST | Package integrity protected |
| P10-8.46 | MUST | Retention governed elsewhere, floors owned here |
| P10-8.47 | MUST NOT | No disposition of a determination record with its version retained |
| P10-8.48 | MUST | Legal hold refuses disposition |
| P10-8.49 | MUST NOT | No alteration of a published version's content |
| P10-8.50 | MUST NOT | No alteration of a determination, expansion, contribution or assertion |
| P10-8.51 | MUST NOT | No removal of a key from the register |
| P10-9.1 | MUST | Closed sets not extended |
| P10-9.2 | MUST | Open sets extended only through a registry |
| P10-9.3 | MUST | Content enumerations open by construction |
| P10-9.4 | MUST | Registration before use |
| P10-9.5 | MUST | Definition mandatory at registration |
| P10-9.6 | MUST | Registration attributable |
| P10-9.7 | MUST NOT | No meaning change under a registered identifier |
| P10-9.8 | MUST | Retirement of a kind recorded, content retained |
| P10-9.9 | MUST | Transitivity declared per kind |
| P10-9.10 | MUST | Hierarchical or associative declared |
| P10-9.11 | MUST | Symmetry declared |
| P10-9.12 | MUST | Inverse named where one exists |
| P10-9.13 | MUST | Rule kind semantics registered |
| P10-9.14 | MUST | Rule kind confluence declared |
| P10-9.15 | MUST | Rule kind bound declared |
| P10-9.16 | MUST | Rule kind inputs registered |
| P10-9.17 | MUST | Tie behaviour registered |
| P10-9.18 | MUST NOT | No source order rule kind |
| P10-9.19 | MUST | Source systems registered |
| P10-9.20 | MUST | Consumer capability registered |
| P10-9.21 | MUST | Constraint kinds registered |
| P10-9.22 | MUST | Marking vocabulary registered |
| P10-9.23 | MUST | Supplements composed, not merged |
| P10-9.24 | MUST | Composed value set records its constituents |
| P10-9.25 | MUST NOT | No composed map without authorship |
| P10-9.26 | MUST | Composition depth bounded |
| P10-10.1 | MUST | Cited edition recorded |
| P10-10.2 | MUST | Basis marked |
| P10-10.3 | MUST | External code system edition pinned |
| P10-10.4 | MUST | Requirements of this part alone identified |
| P10-11.1 | MUST NOT | No reuse |
| P10-11.2 | MUST NOT | No unknown as non membership |
| P10-11.3 | MUST | Withheld marked and counted |
| P10-11.4 | MUST NOT | No expansion reuse across code system versions |
| P10-11.5 | MUST | Unpinned bindings exposed |
| P10-11.6 | MUST NOT | No automatic substitution |
| P10-11.7 | MUST | Closure declared on both sides |
| P10-11.8 | MUST NOT | No inversion |
| P10-11.9 | MUST NOT | No composition at application time |
| P10-11.10 | MUST | Golden view a projection only |
| P10-11.11 | MUST NOT | No deletion on merge |
| P10-11.12 | MUST NOT | No source order survivorship |
| P10-11.13 | MUST NOT | No currency claim without reports |
| P10-11.14 | MUST NOT | No exclusion of the incapable |
| P10-11.15 | MUST NOT | No revaluation |
| P10-11.16 | MUST NOT | No edit of external content |
| P10-11.17 | MUST NOT | No concept definition in a value set |
| P10-11.18 | MUST NOT | No identity in a designation |
| P10-11.19 | MUST | Completeness declared and honoured |
| P10-11.20 | MUST NOT | No entitlement from stewardship |
| P10-11.21 | MUST NOT | No source identifier as master |
| P10-11.22 | MUST | Threshold change surfaces the affected population |
| P10-11.23 | MUST | Existence basis presented |
| P10-11.24 | MUST | Transitivity declared or refused |
| P10-12.1 | MUST | Document identity obtained |
| P10-12.2 | MUST NOT | No local effective dating |
| P10-12.3 | MUST | Determinations are records |
| P10-12.4 | MUST NOT | No conditional membership |
| P10-12.5 | MUST | Conditional map verdicts obtained |
| P10-12.6 | MUST NOT | No non verdict absorbed |
| P10-12.7 | MUST | Events emitted to the ledger |
| P10-12.8 | MUST NOT | No self assertion as the chain |
| P10-12.9 | MUST | Retention floor notified |
| P10-12.10 | MUST | Concept cites its governed definition |
| P10-12.11 | MUST NOT | No governed meaning authored here |
| P10-12.12 | MUST | Reverse index exposed |
| P10-12.13 | MUST | Definition change surfaces as a concept review |
| P10-12.14 | MUST | Survivorship distinguished from decision |
| P10-12.15 | MUST NOT | No business selection performed |
| P10-12.16 | MUST | Domain supplied by pin |
| P10-12.17 | MUST | Status is a fact, not a position |
| P10-12.18 | MUST NOT | No process definition held |
| P10-12.19 | MUST | Authorisation obtained per act |
| P10-12.20 | MUST NOT | No authorisation decision rendered |
| P10-12.21 | MUST | Withholding marked, per the obligation |
| P10-12.22 | MUST | Membership supplied by pin, never enumerated in a policy |
| P10-12.23 | MUST | Member change reported |
| P10-12.24 | MUST NOT | No stewardship as entitlement |
| P10-12.25 | MUST | Adjudication obtained, not managed |
| P10-12.26 | MUST NOT | No assertion from task closure |
| P10-12.27 | MUST | Organisational reference supplied by pin |
| P10-12.28 | MUST | Case scoped bindings not absorbed |
| P10-12.29 | MUST | Membership determination available to validation |
| P10-12.30 | MUST NOT | No schema authority |
| P10-12.31 | MUST | Divergence detectable |
| P10-12.32 | MUST | Binding strength honoured in the outcome |
| P10-12.33 | MUST NOT | No artifact bytes held |
| P10-12.34 | MUST | Content address held per version |
| P10-12.35 | MUST | Unresolvable artifact reported |
| P10-12.36 | MUST | State exposed for verification |
| P10-12.37 | MUST NOT | No self assurance |
| P10-12.38 | MUST | Attested reports accepted |
| P10-12.39 | MUST | Model output recorded as a proposal |
| P10-12.40 | MUST | Invocation reference recorded |
| P10-12.41 | MUST NOT | No model authored concept |
| P10-12.42 | MUST | Accepting party recorded |
| P10-12.43 | MUST | Authority declared, not assumed |
| P10-12.44 | MUST | Non results returned unmodified |
| P10-12.45 | MUST | Consumption gap exposed to composition |
| P10-13.1 | MUST | Unverified reciprocals declared |
| P10-13.2 | SHOULD | Register maintained |
| P10-13.3 | MUST | Gaps declared, not filled |
| P10-13.4 | SHOULD | Open questions carried forward |

### Derived counts

Every figure below is derived by extraction from the clause text of this document and not asserted independently. The grain of counting is stated for each figure. A clause is one line of the document matching the clause heading form given under Binding of requirement language, that is, an identifier of the form `P10-S.N`, a modality in parentheses, and a subject label. Narrative sentences containing a requirement keyword are not clauses and are not counted; per that same section they are not binding. No clause of this part states a requirement keyword in its prose, so the modality of a clause is unambiguous.

**Total clauses.** 470. Grain: one clause heading.

**By modality.** Grain: one clause heading, counted once against its single declared modality.

| Modality | Clauses | Share |
| --- | --- | --- |
| MUST | 332 | 70.6% |
| MUST NOT | 134 | 28.5% |
| SHOULD | 4 | 0.9% |
| SHOULD NOT | 0 | 0.0% |
| MAY | 0 | 0.0% |
| **All** | **470** | **100.0%** |

**Absolute requirements.** 466 clauses carry MUST or MUST NOT and are therefore conditions of conformance. 4 carry SHOULD or SHOULD NOT and require a recorded reason where not satisfied. 0 carry MAY and constrain nothing. Grain: one clause heading. These three figures sum to the total.

**By section.** Grain: one clause heading, attributed to the numbered section in which its heading appears.

| Section | Title | Clauses | MUST | MUST NOT | SHOULD | SHOULD NOT | MAY |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Scope and responsibilities | 30 | 16 | 14 | 0 | 0 | 0 |
| 2 | Terminology | 8 | 1 | 7 | 0 | 0 | 0 |
| 3 | Data model | 106 | 76 | 30 | 0 | 0 | 0 |
| 4 | Interfaces | 48 | 36 | 11 | 1 | 0 | 0 |
| 5 | State model | 33 | 27 | 6 | 0 | 0 | 0 |
| 6 | Execution semantics | 65 | 47 | 18 | 0 | 0 | 0 |
| 7 | Outcome and failure taxonomy | 26 | 18 | 8 | 0 | 0 | 0 |
| 8 | Observability and the audit record | 51 | 43 | 7 | 1 | 0 | 0 |
| 9 | Extension model | 26 | 23 | 3 | 0 | 0 | 0 |
| 10 | Standards and specifications | 4 | 4 | 0 | 0 | 0 | 0 |
| 11 | Anti patterns | 24 | 8 | 16 | 0 | 0 | 0 |
| 12 | Boundaries with other parts | 45 | 31 | 14 | 0 | 0 | 0 |
| 13 | What could not be established | 4 | 2 | 0 | 2 | 0 | 0 |
| **All** | | **470** | **332** | **134** | **4** | **0** | **0** |

**Ordinal integrity.** In this version, the highest ordinal in each section equals the number of clauses in that section, so no identifier has yet been retired. This will cease to be true at the first clause removal, and the count rather than the highest ordinal is then the figure to rely on.

**Cross part citations.** This part cites ten clauses of other parts: P2-12.18, P3-12.18, P7-12.26, P7-12.28, P7-12.29, P8-12-17, P8-12-18, P8-12-19, P9-12-10 and P9-12-13. Every citation to `Part 7`, `Part 8` and `Part 9` was verified against the delivered text of those parts. The two citations to `Part 2` and `Part 3` were verified only as quoted within `Part 7`, since those parts were not available; section 13.1 records this. Grain: one distinct clause identifier cited.

**Sourced clauses.** 23 clauses carry a **Source.** note naming the specification or practice their subject rests on. Grain: one clause heading carrying at least one Source note. Section 10.1 states how the notes are to be read and section 13.1 lists the sources not obtained in full text.

## 1. Scope and responsibilities

### 1.1 What this component is

This component is the authority for the values other components are permitted to use and for the entities other components are permitted to refer to. It holds two kinds of thing that are commonly held in one system and are not one subject: sets of permitted values with governed meanings, and identified records of the real world entities an enterprise transacts about. Section 1.3 separates them and the separation governs the rest of the part.

The component's difficulty is not storage. It is that everything it publishes is consumed by parties it cannot compel, that every value it publishes may be cited by a determination that outlives the value's currency, and that the question it is most often asked, whether a given value is permitted, has no answer that is not relative to a version, a version of the system that version draws on, and an instant.

**P10-1.1 (MUST) Code systems owned.** An implementation must own the identity, versioning, membership and retention of every code system it publishes.

**P10-1.2 (MUST) Concepts owned.** An implementation must own the concept, being the identified unit of meaning within a code system, and its designations, definitions and state.

**P10-1.3 (MUST) Value sets owned.** An implementation must own the value set, being a named selection of concepts drawn from one or more code systems, and its versions.

**P10-1.4 (MUST) Expansions owned.** An implementation must own the expansion, being the enumerated membership a value set version resolves to against stated code system versions at a stated instant.

**P10-1.5 (MUST) Membership determination owned.** An implementation must own the determination of whether a stated value is a member of a stated value set version, and the record of that determination.

**P10-1.6 (MUST) Relations owned.** An implementation must own every asserted relation between concepts within a code system, including hierarchical and associative relations.

**P10-1.7 (MUST) Maps owned.** An implementation must own every map between concepts of different code systems, and the equivalence class asserted for each mapped pair.

**P10-1.8 (MUST) Master entities owned.** An implementation must own the master record, being the identified representation of one real world entity, and the identifier by which other components refer to it.

**P10-1.9 (MUST) Contributions owned.** An implementation must own the contribution, being an assertion about a master entity originating from a named source at a named instant.

**P10-1.10 (MUST) Match and merge assertions owned.** An implementation must own the assertion that two contributions or two master records concern the same entity, and the basis of that assertion.

**P10-1.11 (MUST) Survivorship outcomes owned.** An implementation must own the determination of which contributed value is presented as the current value of a master attribute, and the record of why.

**P10-1.12 (MUST) Distribution record owned.** An implementation must own the record of what it published, to whom it was made available, and under what constraint.

**P10-1.13 (MUST) Consumption reports owned.** An implementation must own the report of what a consumer holds, where a consumer reports it, and must own the population of consumers that have not reported.

**P10-1.14 (MUST) Stewardship owned.** An implementation must own the assignment of stewardship over every code system, value set, map and master entity domain it holds.

### 1.2 What this component is not

**P10-1.15 (MUST NOT) Not the meaning of a governed term.** An implementation must not define the meaning of a data element, a conceptual domain or a governed business term, and must obtain those from `Part 4`.

**P10-1.16 (MUST NOT) Not a rules engine.** An implementation must not evaluate a constraint that is not a membership, relation or map determination over its own content, and must obtain such evaluations from `Part 2`.

**P10-1.17 (MUST NOT) Not a schema authority.** An implementation must not assign version identity to a schema and must not validate a payload, and must obtain both from `Part 9`.

**P10-1.18 (MUST NOT) Not a decision point for access.** An implementation must not decide whether a party may read a code system, a value set or a master record, and must obtain that decision from `Part 7`.

**P10-1.19 (MUST NOT) Not a decision engine.** An implementation must not select among candidate values by governed algorithm where the selection is a business outcome, and must obtain such a selection from `Part 5`.

**P10-1.20 (MUST NOT) Not the document authority.** An implementation must not govern the approval, effective date or retention schedule of a published version as a document, and must obtain those from `Part 1`.

**P10-1.21 (MUST NOT) Not the audit ledger.** An implementation must not represent its own records as the evidentiary chain of a determination, and must emit its events to `Part 3`.

**P10-1.22 (MUST NOT) Not the artifact store.** An implementation must not store the bytes of a distributed release artifact, and must hold the content address held by `Part 11`.

**P10-1.23 (MUST NOT) Not a work manager.** An implementation must not assign, offer or escalate the work by which a steward adjudicates a match or resolves a duplicate, and must obtain the work item from `Part 8`.

**P10-1.24 (MUST NOT) Not the enforcer of its own currency.** An implementation must not represent a consumer as holding a current version in the absence of a consumption report, per section 3.13.

**P10-1.25 (MUST NOT) Not an assessor of itself.** An implementation must not report its own conformance to this part as assurance, and must expose the state `Part 12` requires.

### 1.3 Reference data and master data are two subjects under one component

They are placed in one component because they share a governance apparatus: a steward, a registration lifecycle, a versioned release, a distribution record and a retention obligation coupled to the determinations that cited them. They are separated within it because their identity models are incompatible.

A concept's identity is assigned by an authority and its referent is a meaning. Its correctness is a matter of definition, so a concept is right or wrong by fiat and by agreement, never by observation. It changes rarely, it is consumed by every component, and its principal risk is that a consumer holds a stale version and computes a wrong answer without any error occurring.

A master record's identity is assigned by this component and its referent is a thing in the world that exists independently of any record of it. Its correctness is a matter of fact, so it is right or wrong by observation and it is routinely wrong. It changes constantly, it is contributed to by many sources that disagree, and its principal risk is that two records denote one entity or one record denotes two, which is a mistake about the world rather than about a definition.

Conflating them produces two specific failures. Applying reference data governance to master data yields a change control process for facts, so a correction to a customer's address requires a release. Applying master data governance to reference data yields probabilistic matching over concepts, so two codes that mean different things are merged because their labels are similar.

**P10-1.26 (MUST) The two subjects distinguished.** An implementation must record, for every set it holds, whether it is reference content or master content, and must apply the requirements this part attaches to that kind.

**P10-1.27 (MUST NOT) No matching over concepts.** An implementation must not assert an identity between two concepts on the basis of a similarity computation, and must require every concept equivalence to be an authored map entry per section 3.9.

**P10-1.28 (MUST NOT) No release gate on a factual correction.** An implementation must not require a version release of a master domain in order to correct a contributed value, and must record the correction as a contribution.

**P10-1.29 (MUST) Kind declared per operation.** An implementation must declare, for every operation of section 4, whether it applies to reference content, to master content or to both, and must refuse an operation applied to the kind it does not serve.

### 1.4 What this part is written for

A reviewer should read section 3.2 first, then section 7. Section 3.2 states the position on which the part turns and section 7 is where the part is testable. Section 12 discharges the reciprocal statements the prior parts require of this component, and section 13.7 records the structural repetitions across the standard, which are now the most likely thing to require a coordinated amendment across parts.

**P10-1.30 (MUST NOT) No conformance assessment anticipated.** An implementation must not read this part as assessing any system, and must treat assessment as the subject of `Part 12`.

## 2. Terminology

### 2.1 Terms owned by this part

**Code system.** A governed set of concepts, each identified by a key that is unique within the system, published as versions by a named authority. Corresponds to what ISO/IEC 11179 treats as a value domain's set of permissible values, to a SKOS concept scheme, and to what HL7 FHIR calls a CodeSystem.

**Concept.** One identified unit of meaning within a code system, having a key, at least one designation, a definition and a state. The concept and not the designation is the unit of identity, so a relabelling is not a new concept and a change of referent is not a relabelling.

**Key.** The identifier of a concept within its code system. This part forbids reuse of a key for a different referent under any circumstance, and section 11.1 gives the evidence.

**Designation.** A human readable label for a concept, in a stated language, of a stated kind, being preferred, alternative or hidden. SKOS distinguishes `skos:prefLabel`, `skos:altLabel` and `skos:hiddenLabel`; this part adopts the three kinds and requires the language to be stated.

**Code system version.** One immutable published state of a code system.

**Value set.** A named selection of concepts, drawn from one or more code systems, published as versions. Corresponds to what FHIR calls a ValueSet.

**Extensional definition.** A value set definition that enumerates its members as concept keys.

**Intensional definition.** A value set definition that states a rule by which members are selected from a code system, such as all descendants of a stated concept. An intensional definition has no membership of its own; it has a membership only against stated code system versions at a stated instant.

**Expansion.** The enumerated membership that a value set version resolves to against stated code system versions at a stated instant, recorded as an artifact with its own identity.

**Membership determination.** The recorded determination of whether one stated value is a member of one stated value set version, with the outcome drawn from section 7.2.

**Relation.** An asserted link between two concepts of one code system, of a registered relation kind, being hierarchical or associative.

**Direct relation.** A relation asserted between two concepts without an intervening concept.

**Transitive closure.** The set of concepts reachable from a stated concept by repeated traversal of a stated hierarchical relation kind. This part requires the closure to be requested explicitly and never assumed, and section 6.5 gives the reason.

**Map.** A named, versioned set of entries, each asserting a relation between a concept of a source code system version and a concept of a target code system version, with a declared equivalence class.

**Equivalence class.** The declared strength and direction of a map entry, drawn from the closed enumeration in section 3.9.

**Withheld member.** A member of a published set that a consumer is not permitted to receive, marked as withheld rather than omitted. The construction is required of this component by `Part 2` and `Part 3` through `Part 7`, and section 3.10 specifies it.

**Distribution constraint.** A recorded restriction on the redistribution of content this component publishes but does not own the rights to.

**Release.** One published, addressable artifact conveying one or more versions to consumers.

**Distribution record.** The record of a release having been made available, to which consumers, under which constraint.

**Consumption report.** A report from a consumer stating which versions it holds and from which instant. It is the analogue of the enforcement report of `Part 7` and it is incomplete by construction.

**Unreported consumer.** A registered consumer with no current consumption report. The count of them is the measure of how much of an estate is running on reference content of unknown vintage.

**Master domain.** A governed class of real world entities, such as parties, products or locations, for which this component is the authority.

**Master record.** The identified representation of one entity within a master domain.

**Master identifier.** The identifier this component assigns to a master record, which other components use to refer to the entity.

**Source identifier.** An identifier assigned to the same entity by a contributing system, retained as a cross reference and never used as the master identifier.

**Contribution.** One assertion about a master entity from one named source at one instant, retained whether or not it was selected.

**Match assertion.** The recorded assertion that two contributions, or two master records, concern the same entity, with a basis and a confidence.

**Merge.** The act of representing two master records as one, effected as an assertion and never as a deletion.

**Unmerge.** The act of withdrawing a merge assertion and restoring the separate identity of the records it joined.

**Survivorship.** The determination of which contributed value is presented as the current value of a master attribute.

**Golden view.** A projection presenting one current value per master attribute. It is a projection and never a record, and section 3.16 requires the contributions behind it to remain retrievable.

**Steward.** The party accountable for the fitness of a code system, value set, map or master domain, whose sponsorship is required for progression of registration status.

### 2.2 Clauses governing terminology

**P10-2.1 (MUST NOT) No redefinition of another part's terms.** An implementation must not redefine a term this standard allocates to another part, and must use it with the meaning that part gives it.

**P10-2.2 (MUST NOT) Concept not equated with designation.** An implementation must not treat a designation as the identity of a concept and must not treat a change of designation as a change of concept.

**P10-2.3 (MUST NOT) Value set not equated with code system.** An implementation must not treat a value set as a code system and must not permit a value set to define a concept.

**P10-2.4 (MUST NOT) Expansion not equated with definition.** An implementation must not treat an expansion as the definition of a value set version and must not permit an expansion to be edited.

**P10-2.5 (MUST NOT) Master identifier not equated with source identifier.** An implementation must not use a source identifier as a master identifier and must not present a source identifier as this component's assignment.

**P10-2.6 (MUST NOT) Golden view not equated with record.** An implementation must not treat a golden view as the record of a master entity and must retain every contribution behind it.

**P10-2.7 (MUST) Kinds registered before use.** An implementation must register every relation kind, equivalence class, designation kind, match basis and distribution constraint kind before content uses it, per section 9.

**P10-2.8 (MUST NOT) No private meanings.** An implementation must not publish a concept, relation kind or equivalence class whose meaning rests on an understanding between two parties rather than on a registered definition. **Source.** `Part 7` section 9.3 refuses the same construction for obligation kinds, on the ground that a control whose meaning is private is one no third party can audit. This part refuses it for the same reason and extends it to relation kinds and equivalence classes, where the practice is widespread.

## 3. Data model

### 3.1 Type vocabulary

Types in this section are abstract and impose no representation. `identifier` is an opaque immutable string unique within its declared scope. `key` is a concept identifier unique within a code system. `instant` is a point in time with an offset from UTC and at least millisecond resolution. `interval` is a pair of instants, either bound of which may be open. `digest` is a cryptographic hash together with the identifier of the algorithm that produced it. `pin` is a reference that resolves to a stated version of a stated object as it stood at a stated instant. `content-address` is an address held by `Part 11`. `enum(...)` is a closed set unless the field description states otherwise.

**P10-3.1 (MUST) Types declared.** An implementation must declare the concrete representation it adopts for every abstract type in section 3.1 and must not vary it between records of one class.

**P10-3.2 (MUST) Instants carry offset and resolution.** An implementation must record every instant with an offset from UTC and must declare its resolution.

**P10-3.3 (MUST NOT) No representation dependent identity.** An implementation must not derive the identity of any record from its representation, and must not change an identifier when a representation changes.

### 3.2 Publication is not consumption

This is the position on which the part turns, and it is the same structure `Part 7` section 3.2 establishes for decision and enforcement. That part can prove what it decided and cannot prove what happened. This component can prove what it published and cannot prove what anyone is using.

The consequence is that a reference data authority which reports its content as current is reporting on itself. The estate's actual state is the set of versions its consumers hold, and this component learns that only where a consumer tells it. A consumer that reads a value set once at deployment and caches it for three years is, from this component's view, indistinguishable from one that refreshes hourly. Both appear in the distribution record and neither appears in a consumption report unless it sends one.

Two records therefore exist and are never merged. The distribution record is complete, because this component writes it. The consumption report set is incomplete by construction, because consumers write it. Treating the first as evidence of the second is the characteristic error of this component, and it is the reason a reference data programme can report full compliance while a quarter of the estate validates against a set that was superseded two years ago.

**P10-3.4 (MUST) Two records kept apart.** An implementation must record a distribution and a consumption report as two records and must not merge them into one.

**P10-3.5 (MUST NOT) No inference of consumption from distribution.** An implementation must not treat the availability of a version to a consumer as evidence that the consumer holds it.

**P10-3.6 (MUST) Absence of a report is ordinary.** An implementation must treat the absence of a consumption report as the ordinary case and must not record it as an error condition of the consumer.

**P10-3.7 (MUST) Unreported population countable.** An implementation must expose the count of registered consumers with no current consumption report, at the grain of one consumer per registered subscription.

**P10-3.8 (MUST NOT) No currency claim without reports.** An implementation must not report an estate wide currency figure that treats unreported consumers as current.

**P10-3.9 (MUST) Currency figure declares its base.** An implementation must state, with every currency figure it publishes, the number of consumers reporting and the number registered.

### 3.3 Entity inventory

The table is normative as to which entities exist and which component owns each. Every entity in it is specified in a subsection of section 3.

| Entity | Kind | Immutable once written | Owned here |
|---|---|---|---|
| Code system | reference | no, versions are | yes |
| Code system version | reference | yes | yes |
| Concept | reference | no, its state changes | yes |
| Designation | reference | no | yes |
| Value set | reference | no, versions are | yes |
| Value set version | reference | yes | yes |
| Expansion | reference | yes | yes |
| Relation assertion | reference | yes | yes |
| Map | reference | no, versions are | yes |
| Map version | reference | yes | yes |
| Map entry | reference | yes | yes |
| Release | both | yes | yes |
| Distribution record | both | yes | yes |
| Consumption report | both | yes | yes |
| Consumer registration | both | no | yes |
| Withholding record | both | yes | yes |
| Distribution constraint | both | no | yes |
| Master domain | master | no | yes |
| Master record | master | no, its assertions are | yes |
| Contribution | master | yes | yes |
| Match assertion | master | yes | yes |
| Merge assertion | master | yes | yes |
| Survivorship determination | master | yes | yes |
| Stewardship assignment | both | no | yes |
| Governed definition | — | — | no, `Part 4` |
| Authorisation decision | — | — | no, `Part 7` |
| Schema version | — | — | no, `Part 9` |
| Release artifact bytes | — | — | no, `Part 11` |

**P10-3.10 (MUST) Inventory normative.** An implementation must hold every entity the table in section 3.3 marks as owned here and must not hold as its own any entity the table allocates to another part.

**P10-3.11 (MUST) Immutability observed.** An implementation must not modify any record the table in section 3.3 marks immutable once written, and must express a correction as a new record superseding it.

**P10-3.12 (MUST) Kind attached to every entity.** An implementation must attach the kind reference, master or both to every entity instance it holds.

### 3.4 Code systems and their versions

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `code_system_id` | identifier | yes | 1 | Not possible |
| `canonical_uri` | uri | yes | 1 | Not possible |
| `authority` | pin to party | yes | 1 | Not possible; where this component is the authority it names itself |
| `externally_authored` | boolean | yes | 1 | Not possible |
| `steward` | pin to party | yes | 1 | Not possible |
| `distribution_constraint_id` | identifier | no | 0..n | No restriction on redistribution is recorded, not that none applies; see P10-3.44 |
| `key_scheme` | identifier | yes | 1 | Not possible; the registered scheme governing key syntax |
| `case_sensitive_keys` | boolean | yes | 1 | Not possible |
| `content_completeness` | enum(`complete`,`fragment`,`supplement`,`example`,`not_present`) | yes | 1 | Not possible; see P10-3.15 |
| `hierarchy_meaning` | identifier | no | 0..1 | The system asserts no hierarchical relation kind |
| `versions` | identifier | yes | 1..n | Not possible |

| Field, version | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `code_system_version_id` | identifier | yes | 1 | Not possible |
| `version_designation` | string | yes | 1 | Not possible; ordering is never inferred from it |
| `predecessor_id` | identifier | no | 0..1 | First version, not unknown predecessor |
| `concept_count` | integer | yes | 1 | Not possible; the count at the grain of one concept |
| `content_digest` | digest | yes | 1 | Not possible |
| `artifact_address` | content-address | yes | 1 | Not possible |
| `registration_status` | enum, §5.2 | yes | 1 | Not possible |
| `version_state` | enum, §5.3 | yes | 1 | Not possible |
| `document_ref` | pin to `Part 1` | yes | 1 | Not possible |
| `published_at` | instant | no | 0..1 | Not yet published |
| `retention_floor` | instant | no | 0..1 | No determination is yet known to have cited this version; see §3.15 |

**P10-3.13 (MUST) Version is the unit of reference.** An implementation must require every external reference to code system content to name a version, and must refuse a reference that names a code system without one.

**P10-3.14 (MUST NOT) No ordering from a designation.** An implementation must not derive a predecessor or successor relation from a version designation and must derive it from recorded transitions.

**P10-3.15 (MUST) Completeness of content declared.** An implementation must declare, for every code system version, whether the content it holds is the complete set of concepts, a fragment, a supplement to another version, an example, or absent. **Source.** FHIR carries this distinction on a CodeSystem resource, and its purpose is that a membership determination against a fragment is not a determination against the system. This part adopts it and section 7.2 attaches a distinct outcome to a determination made against incomplete content.

**P10-3.16 (MUST NOT) No determination of non membership against a fragment.** An implementation must not return a non membership outcome from a determination made against a code system version whose content completeness is other than complete, and must return the outcome of section 7.2 that names the incompleteness.

**P10-3.17 (MUST) External authorship recorded.** An implementation must record whether a code system is authored externally and must not represent an externally authored system as one over which it has editorial authority.

**P10-3.18 (MUST NOT) No local edit of external content.** An implementation must not add, remove or alter a concept of an externally authored code system version, and must express any local addition as a supplement with its own identity.

**P10-3.19 (MUST) Key scheme registered.** An implementation must register the key scheme of every code system and must reject a concept whose key does not satisfy it.

**P10-3.20 (MUST) Case sensitivity declared.** An implementation must declare whether keys of a code system are case sensitive and must apply the declaration uniformly in every determination.

### 3.5 Concepts, keys and the prohibition on reuse

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `concept_id` | identifier | yes | 1 | Not possible |
| `code_system_id` | identifier | yes | 1 | Not possible |
| `key` | key | yes | 1 | Not possible |
| `first_version_id` | identifier | yes | 1 | Not possible; the version in which the key first appeared |
| `state` | enum, §5.4 | yes | 1 | Not possible |
| `definition` | text | yes | 1 | Not possible; see P10-3.23 |
| `definition_ref` | pin to `Part 4` | no | 0..1 | The concept carries no governed definition; a defect for any concept a schema position binds, per §12.4 |
| `designations` | structure below | yes | 1..n | Not possible |
| `inactivated_at` | instant | no | 0..1 | The concept is not inactive |
| `inactivation_reason` | enum, §5.4 | no | 0..1 | The concept is not inactive; required whenever `inactivated_at` is present |
| `successor_relations` | structure: successor key, association kind, version | no | 0..n | No successor is designated; for an inactive concept this is itself recorded, per P10-3.28 |

Each designation carries: a `designation_id`, a `language` tag, a `kind` of `preferred`, `alternative` or `hidden`, the `text`, a `valid_interval`, and the `code_system_version_id` in which it applies.

**P10-3.21 (MUST NOT) Keys never reused.** An implementation must not assign a key that has previously denoted a different referent within the same code system, at any interval and under any reservation period. **Source.** ISO 3166-1 reassigned the alpha-2 code element CS, which denoted Czechoslovakia until 1993, to Serbia and Montenegro from 2003, and ISO's own register records the reuse. The successor code register then assigned CSHH to Serbia and Montenegro although CSHH already denoted Czechoslovakia, and the collision was corrected by newsletter to CSXX. The current reservation period is fifty years and a five year period was in force when the reuse occurred. This part refuses reuse absolutely, because a reservation period bounds the risk and does not remove it, and because no reservation period helps a determination made over data spanning both intervals.

**P10-3.22 (MUST NOT) No deletion of a concept.** An implementation must not remove a concept from a code system and must express withdrawal as an inactivation with a recorded reason. **Source.** The permanence of concepts and their inactivation rather than deletion is the practice of the major clinical terminologies and is the only practice under which a historical record citing a concept remains resolvable.

**P10-3.23 (MUST) Definition present and textual.** An implementation must require a definition for every concept, and must not accept a designation in place of a definition.

**P10-3.24 (MUST) One preferred designation per language.** An implementation must permit at most one preferred designation per concept per language per code system version, and must record any further designation as alternative or hidden.

**P10-3.25 (MUST NOT) No meaning change under a stable key.** An implementation must not alter the referent of a concept, and must express a change of referent as the inactivation of the concept and the creation of a new concept with a new key.

**P10-3.26 (MUST) Designation change distinguished from meaning change.** An implementation must record a change of designation as a designation event and must not record it as a change to the concept.

**P10-3.27 (MUST) Inactivation reason recorded.** An implementation must record an inactivation reason from the enumeration of section 5.4 for every inactivated concept.

**P10-3.28 (MUST) Successor stated or its absence stated.** An implementation must record, for every inactivated concept, either at least one successor relation or the explicit fact that no successor exists.

**P10-3.29 (MUST) Successor association kind declared.** An implementation must declare the association kind of every successor relation from the closed enumeration `same_as`, `replaced_by`, `possibly_equivalent_to`, `moved_to` and `alternative`, and must not record a successor without one.

**P10-3.30 (MUST NOT) No automatic substitution of a successor.** An implementation must not substitute a successor concept for an inactive concept in any determination, and must return the inactive concept with its successor relations so that the caller decides.

Clause P10-3.30 exists because the association kinds are not interchangeable. A `same_as` successor may be substituted without changing meaning. A `replaced_by` successor may not, because the replacement was chosen for going forward and not for reinterpreting the past. A `possibly_equivalent_to` successor asserts uncertainty, and substituting it silently converts a recorded uncertainty into a recorded fact.

### 3.6 Value sets and their versions

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `value_set_id` | identifier | yes | 1 | Not possible |
| `canonical_uri` | uri | yes | 1 | Not possible |
| `steward` | pin to party | yes | 1 | Not possible |
| `versions` | identifier | yes | 1..n | Not possible |

| Field, version | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `value_set_version_id` | identifier | yes | 1 | Not possible |
| `version_designation` | string | yes | 1 | Not possible |
| `definition_mode` | enum(`extensional`,`intensional`,`mixed`) | yes | 1 | Not possible |
| `extensional_members` | key with code system version | no | 0..n | The definition contains no enumerated member; required to be non empty where mode is extensional |
| `intensional_rules` | structure: code system id, rule kind, parameters | no | 0..n | The definition contains no rule; required to be non empty where mode is intensional |
| `referenced_code_systems` | identifier | yes | 1..n | Not possible |
| `code_system_version_binding` | enum(`pinned`,`unpinned`) | yes | 1 | Not possible; see P10-3.33 |
| `pinned_code_system_versions` | identifier | no | 0..n | The binding is unpinned; required to be non empty where the binding is pinned |
| `definition_digest` | digest | yes | 1 | Not possible |
| `registration_status` | enum, §5.2 | yes | 1 | Not possible |
| `version_state` | enum, §5.3 | yes | 1 | Not possible |
| `document_ref` | pin to `Part 1` | yes | 1 | Not possible |
| `retention_floor` | instant | no | 0..1 | No determination is yet known to have cited this version |

**P10-3.31 (MUST) Definition mode declared.** An implementation must declare whether a value set version is defined extensionally, intensionally or by a combination, and must not accept a version without the declaration.

**P10-3.32 (MUST NOT) No membership attributed to an intensional definition alone.** An implementation must not represent an intensional value set version as having a membership, and must represent its membership only as an expansion against stated code system versions at a stated instant.

**P10-3.33 (MUST) Code system version binding declared.** An implementation must declare, for every value set version, whether it pins the versions of the code systems it draws on, and must record the pinned versions where it does.

**P10-3.34 (MUST) Unpinned binding surfaces as a hazard.** An implementation must expose every published value set version whose code system version binding is unpinned, since its membership can change without any change to it.

Clause P10-3.34 names the mechanism by which a value set changes without being changed. An intensional definition selecting the descendants of a concept, bound to no particular code system version, has a different membership on the day the code system publishes a new descendant. Nothing in the value set changed, its digest is identical, its version designation is unchanged, and every consumer computing membership from it now gets a different answer.

**P10-3.35 (MUST NOT) No enumeration in place of a reference.** An implementation must not accept an extensional member that names a key without naming the code system version the key is drawn from.

**P10-3.36 (MUST) Rule kinds registered.** An implementation must register every intensional rule kind before a definition uses it, and must not accept a rule whose kind is unregistered.

**P10-3.37 (MUST) Rule kinds carry a closure declaration.** An implementation must require every intensional rule kind that traverses a hierarchical relation to declare whether it uses direct relations or the transitive closure, per section 6.5.

### 3.7 Expansions

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `expansion_id` | identifier | yes | 1 | Not possible |
| `value_set_version_id` | identifier | yes | 1 | Not possible |
| `computed_at` | instant | yes | 1 | Not possible |
| `code_system_versions_used` | identifier | yes | 1..n | Not possible |
| `members` | key with code system version id | no | 0..n | The expansion is empty as a computed fact, distinguished from an expansion that could not be computed by its outcome |
| `outcome` | enum, §7.3 | yes | 1 | Not possible |
| `total_count` | integer | no | 0..1 | The count is unknown, which is permitted only where the outcome records incompleteness |
| `truncated` | boolean | yes | 1 | Not possible |
| `withheld_count` | integer | yes | 1 | Not possible; zero means nothing was withheld |
| `withholding_record_ids` | identifier | no | 0..n | Nothing was withheld |
| `inactive_included` | boolean | yes | 1 | Not possible |
| `closure_used` | enum(`direct`,`transitive`,`mixed`,`not_applicable`) | yes | 1 | Not possible |
| `expansion_digest` | digest | yes | 1 | Not possible |
| `requested_by` | pin to party or component | yes | 1 | Not possible |

**P10-3.38 (MUST) Expansion is an artifact.** An implementation must record every expansion it computes as an artifact with its own identity, and must not treat an expansion as a transient result.

**P10-3.39 (MUST) Expansion records its inputs.** An implementation must record, with every expansion, the value set version, every code system version used, the instant of computation and the closure mode applied.

**P10-3.40 (MUST NOT) No expansion reuse across inputs.** An implementation must not return an expansion computed against code system versions other than those a caller pinned, and must recompute or refuse.

**P10-3.41 (MUST) Truncation declared.** An implementation must declare whether an expansion is truncated and must not return a truncated expansion without the declaration.

**P10-3.42 (MUST NOT) No membership determination from a truncated expansion.** An implementation must not determine non membership from a truncated expansion and must return the outcome of section 7.2 that names the truncation.

**P10-3.43 (MUST) Inclusion of inactive members declared.** An implementation must declare whether an expansion includes inactive concepts, and must default to excluding them where no caller declaration is supplied.

### 3.8 Withheld members and distribution constraints

Three of the prior parts require this component to mark what it restricted rather than remove it. Section 3.10 of `Part 7` specifies the withholding obligation and clauses P2-12.18 and P3-12.18 both require the restricting component to identify what it restricted as withheld. This component is the one that most often has something to withhold, for two independent reasons: a consumer may not be authorised to see every member of a set, and this component may not hold the right to redistribute content it publishes.

Both reasons produce the same hazard. A consumer receiving a filtered set with no marking treats it as complete, computes non membership from it, and is wrong in a direction that admits nothing and refuses everything.

| Field, withholding record | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `withholding_record_id` | identifier | yes | 1 | Not possible |
| `subject_kind` | enum(`expansion`,`release`,`master_record`,`attribute`) | yes | 1 | Not possible |
| `subject_id` | identifier | yes | 1 | Not possible |
| `withheld_count` | integer | yes | 1 | Not possible |
| `basis` | enum(`authorisation`,`distribution_constraint`,`legal_hold`,`stewardship_embargo`) | yes | 1 | Not possible |
| `authorisation_ref` | pin to `Part 7` | no | 0..1 | The basis is not authorisation; required where it is |
| `constraint_id` | identifier | no | 0..1 | The basis is not a distribution constraint; required where it is |
| `marking_vocabulary_id` | identifier | yes | 1 | Not possible; see P10-3.47 |
| `withheld_at` | instant | yes | 1 | Not possible |

**P10-3.44 (MUST) Withheld marked, never omitted.** An implementation must mark every member it withholds from a delivered set as withheld and must not omit it silently. **Source.** Required of this component by `Part 7` section 3.11 and by clauses P2-12.18 and P3-12.18, each of which requires a restricting component to identify what it restricted rather than remove it.

**P10-3.45 (MUST) Withheld count returned.** An implementation must return the count of withheld members with every delivered set, and must return zero where nothing was withheld rather than omitting the count.

**P10-3.46 (MUST NOT) No non membership from a set with withheld members.** An implementation must not return a non membership outcome from a determination against a set with a non zero withheld count, and must return the outcome of section 7.2 that names the withholding.

**P10-3.47 (MUST) Marking vocabulary named.** An implementation must name the marking vocabulary it uses to express withholding and must not vary it between deliveries of one set. **Source.** `Part 7` section 12.14 hands `Part 0` the question of whether the marking vocabulary should be specified once for the estate, recording that four parts consume the distinction and each names it differently. This part is the fifth and names the same question in section 13.9.

**P10-3.48 (MUST) Distribution constraint recorded.** An implementation must record, for every code system version it publishes but does not author, whether a constraint restricts its redistribution and to whom.

**P10-3.49 (MUST NOT) No distribution beyond a recorded constraint.** An implementation must not deliver content to a consumer beyond what a recorded distribution constraint permits, and must express the shortfall as a withholding record.

**P10-3.50 (MUST) Licence dependent membership exposed.** An implementation must expose every value set version whose expansion is subject to withholding for a distribution constraint, since consumers of it can never receive a complete membership.

### 3.9 Relations and maps

| Field, relation assertion | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `relation_id` | identifier | yes | 1 | Not possible |
| `code_system_version_id` | identifier | yes | 1 | Not possible |
| `source_key` | key | yes | 1 | Not possible |
| `target_key` | key | yes | 1 | Not possible |
| `relation_kind` | identifier | yes | 1 | Not possible; a registered kind |
| `transitivity` | enum(`transitive`,`non_transitive`,`undeclared`) | yes | 1 | Not possible; `undeclared` is permitted only for a kind registered as such |
| `asserted` | boolean | yes | 1 | Not possible; false denotes an inferred relation, which must not be published as asserted |

| Field, map version | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `map_version_id` | identifier | yes | 1 | Not possible |
| `source_code_system_version_id` | identifier | yes | 1 | Not possible |
| `target_code_system_version_id` | identifier | yes | 1 | Not possible |
| `direction` | enum(`source_to_target`,`bidirectional_asserted`) | yes | 1 | Not possible; see P10-3.56 |
| `entries` | structure below | yes | 1..n | Not possible |
| `unmapped_policy` | enum(`no_default`,`fixed_concept`,`use_source_code`,`refuse`) | yes | 1 | Not possible |
| `completeness` | enum(`complete_over_source`,`partial`,`undeclared`) | yes | 1 | Not possible; `undeclared` is a defect under P10-3.58 |
| `registration_status` | enum, §5.2 | yes | 1 | Not possible |
| `version_state` | enum, §5.3 | yes | 1 | Not possible |

Each map entry carries a `source_key`, a `target_key` or the explicit absence of one, an `equivalence_class`, an optional `condition_ref` to a `Part 2` rule where the entry applies conditionally, and a `provenance` naming the authoring party.

Equivalence classes, closed enumeration:

| Class | Meaning | Invertible |
|---|---|---|
| `equivalent` | The two concepts may be used interchangeably in every context the map declares | yes |
| `source_narrower_than_target` | The source denotes a subset of the target | no |
| `source_broader_than_target` | The source denotes a superset of the target | no |
| `inexact` | The two overlap and neither contains the other | no |
| `related` | An associative relation with no containment claim | yes |
| `unmatched` | No target concept exists for the source | not applicable |
| `disjoint` | The source is asserted to have no relation to the target | yes |

**P10-3.51 (MUST) Relation kinds registered with transitivity.** An implementation must register every relation kind with a declared transitivity and must not accept a relation whose kind has none. **Source.** SKOS declares `skos:broader` and `skos:narrower` as non transitive by convention, so that they assert only an immediate hierarchical link, and provides `skos:broaderTransitive` and `skos:narrowerTransitive` as transitive super properties intended for inference rather than assertion. This part adopts the separation and makes the declaration mandatory rather than conventional.

**P10-3.52 (MUST NOT) No inferred relation published as asserted.** An implementation must not publish an inferred relation with `asserted` true, and must distinguish the transitive closure from the asserted relations at every interface. **Source.** SKOS states that by convention the transitive properties are not used to make assertions and are used to draw inferences about the transitive closure.

**P10-3.53 (MUST) Equivalence class on every entry.** An implementation must require an equivalence class from the enumeration in section 3.9 on every map entry and must not accept an entry without one.

**P10-3.54 (MUST) Unmatched recorded as an entry.** An implementation must record an unmatched source concept as a map entry with the class `unmatched` and must not express it by the absence of an entry.

**P10-3.55 (MUST NOT) No silent unmapped default.** An implementation must not substitute a default target for an unmapped source concept unless the map version declares an unmapped policy permitting it, and must record every substitution.

**P10-3.56 (MUST NOT) No automatic inversion.** An implementation must not derive a target to source map by inverting a source to target map, and must require the reverse direction to be authored.

Clause P10-3.56 follows from the enumeration. Inverting `source_narrower_than_target` yields a broader relation, which is a different assertion about what may safely be substituted, and inverting `inexact` yields an assertion no one authored. Only `equivalent`, `related` and `disjoint` invert without loss, and a map is rarely composed only of those.

**P10-3.57 (MUST NOT) No composition of maps.** An implementation must not derive a map from the composition of two maps and must require a composed map to be authored and registered in its own right. **Source.** SKOS declares `skos:exactMatch` transitive and a sub property of `skos:closeMatch`, and declares `skos:closeMatch` non transitive, so that chaining close matches is not valid; published analysis of SKOS mapping quality records that asserting a transitive hierarchical relation through mapping properties produces inconsistency and unintended claims about another scheme's content.

**P10-3.58 (MUST) Map completeness declared.** An implementation must declare whether a map version is complete over its source code system version, and must treat an undeclared completeness as a defect blocking publication.

**P10-3.59 (MUST) Conditional entries carry their condition.** An implementation must record the `Part 2` rule reference of every map entry that applies conditionally and must not apply such an entry without obtaining the verdict.

### 3.10 Master domains, records and identifiers

| Field, master record | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `master_identifier` | identifier | yes | 1 | Not possible |
| `master_domain_id` | identifier | yes | 1 | Not possible |
| `record_state` | enum, §5.6 | yes | 1 | Not possible |
| `created_at` | instant | yes | 1 | Not possible |
| `created_from` | identifier | yes | 1..n | Not possible; the contributions that caused the record to exist |
| `source_identifiers` | structure: source system id, source identifier, first seen, last seen | no | 0..n | No source identifier is cross referenced, which for a record created from a contribution is not possible |
| `merged_into` | identifier | no | 0..1 | The record is not merged into another |
| `merge_assertion_ids` | identifier | no | 0..n | No merge assertion concerns this record |
| `steward` | pin to party | yes | 1 | Not possible |
| `existence_basis` | enum(`asserted_by_source`,`verified_externally`,`steward_asserted`) | yes | 1 | Not possible; see P10-3.63 |
| `retention_floor` | instant | no | 0..1 | No determination is yet known to have cited this record |

**P10-3.60 (MUST) Master identifier assigned here.** An implementation must assign the master identifier of every master record and must not adopt a source identifier as one.

**P10-3.61 (MUST NOT) Master identifiers never reused.** An implementation must not assign a master identifier that has previously denoted a different entity, under any circumstance.

**P10-3.62 (MUST) Source identifiers retained as cross references.** An implementation must retain every source identifier by which a contributing system denoted an entity, and must not discard one on merge.

**P10-3.63 (MUST) Existence basis recorded.** An implementation must record the basis on which it holds that the entity a master record denotes exists, and must not present an entity asserted by one source as verified.

Clause P10-3.63 exists because the failure it prevents is invisible. A master record created from a single contribution asserts that an entity exists on the authority of the system that asserted it. Where that system's input was a free text form, the record may denote nothing. Every downstream use treats the master identifier as denoting a real entity, and nothing in the record says which of the three bases applies.

**P10-3.64 (MUST) Domain declared before records.** An implementation must register a master domain, its steward, its identifier scheme and its attribute set before it creates a record in that domain.

### 3.11 Contributions

| Field | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `contribution_id` | identifier | yes | 1 | Not possible |
| `master_identifier` | identifier | no | 0..1 | The contribution is not yet resolved to a master record; distinguished from one that could not be resolved by its outcome |
| `source_system_id` | identifier | yes | 1 | Not possible |
| `source_identifier` | string | no | 0..1 | The source supplied no identifier of its own |
| `asserted_at` | instant | yes | 1 | Not possible; the instant the source asserts the values were true |
| `received_at` | instant | yes | 1 | Not possible; the instant this component received them |
| `attribute_values` | structure: attribute id, value, value set version where bound | yes | 1..n | Not possible |
| `superseded_by` | identifier | no | 0..1 | The contribution is the latest from its source for its attributes |
| `provenance_ref` | pin to `Part 3` | yes | 1 | Not possible |

**P10-3.65 (MUST) Contributions retained whole.** An implementation must retain every contribution it receives, whether or not any of its values were selected by survivorship.

**P10-3.66 (MUST NOT) No overwrite of a contribution.** An implementation must not modify a contribution and must express a corrected assertion from the same source as a new contribution superseding it.

**P10-3.67 (MUST) Two instants distinguished.** An implementation must record both the instant a source asserts a value was true and the instant it received the assertion, and must not conflate them.

**P10-3.68 (MUST NOT) No inference of currency from receipt order.** An implementation must not treat the most recently received contribution as the most recently true, and must use the asserted instant where survivorship rests on recency.

**P10-3.69 (MUST) Bound values carry their value set version.** An implementation must record, for every contributed value drawn from a value set, the value set version against which it was accepted.

### 3.12 Match, merge and survivorship

| Field, match assertion | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `match_assertion_id` | identifier | yes | 1 | Not possible |
| `left_ref` | identifier | yes | 1 | Not possible |
| `right_ref` | identifier | yes | 1 | Not possible |
| `verdict` | enum(`same_entity`,`different_entity`,`undetermined`) | yes | 1 | Not possible |
| `basis` | enum(`deterministic_rule`,`probabilistic_score`,`external_authority`,`steward_adjudication`) | yes | 1 | Not possible |
| `rule_ref` | pin | no | 0..1 | The basis is not a deterministic rule |
| `score` | number | no | 0..1 | The basis is not a probabilistic score |
| `threshold` | number | no | 0..1 | The basis is not a probabilistic score |
| `algorithm_ref` | pin | no | 0..1 | No algorithm was used |
| `adjudicated_by` | pin to party | no | 0..1 | No person adjudicated; required where the basis is steward adjudication |
| `work_item_ref` | pin to `Part 8` | no | 0..1 | No work item carried the adjudication; required where a person adjudicated |
| `asserted_at` | instant | yes | 1 | Not possible |
| `superseded_by` | identifier | no | 0..1 | The assertion is current |

| Field, merge assertion | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `merge_assertion_id` | identifier | yes | 1 | Not possible |
| `surviving_identifier` | identifier | yes | 1 | Not possible |
| `absorbed_identifier` | identifier | yes | 1 | Not possible |
| `match_assertion_id` | identifier | yes | 1 | Not possible |
| `state` | enum, §5.7 | yes | 1 | Not possible |
| `unmerged_at` | instant | no | 0..1 | The merge is in force |
| `unmerge_reason` | enum, declared by the domain steward | no | 0..1 | The merge is in force |

**P10-3.70 (MUST) Match is an assertion.** An implementation must record every determination that two records concern the same entity as an assertion with a basis, and must not effect it as an unrecorded consequence of a computation.

**P10-3.71 (MUST) Basis recorded, with its parameters.** An implementation must record the algorithm reference, score and threshold of every match assertion whose basis is a probabilistic score, and must not record a score without the threshold it was compared against.

**P10-3.72 (MUST NOT) No merge without a match assertion.** An implementation must not record a merge assertion that does not reference a match assertion with the verdict `same_entity`.

**P10-3.73 (MUST NOT) No deletion on merge.** An implementation must not delete the absorbed master record, its identifier, its contributions or its source cross references on merge.

**P10-3.74 (MUST) Absorbed identifier resolves.** An implementation must resolve a reference to an absorbed master identifier and must return the surviving record together with the merge assertion, and must not return the surviving record alone.

**P10-3.75 (MUST) Unmerge supported.** An implementation must support the withdrawal of a merge assertion and the restoration of the separate identity of the records it joined.

**P10-3.76 (MUST) Unmerge recorded, not erased.** An implementation must retain the withdrawn merge assertion with its unmerge instant and reason, and must not delete it.

**P10-3.77 (MUST NOT) No survivorship by source order.** An implementation must not determine which contributed value survives by the position of its source in a configured list. **Source.** This is the fifth part of this standard to refuse resolution by declaration order, after `Part 2`'s salience, `Part 5`'s first match, `Part 6`'s branch order and `Part 7`'s first applicable. Section 13.7 records the repetition.

**P10-3.78 (MUST) Survivorship rule declared per attribute.** An implementation must declare a survivorship rule for every master attribute and must not apply a domain wide default to an attribute with no declared rule.

**P10-3.79 (MUST) Survivorship determination recorded.** An implementation must record, for every presented master attribute value, the contribution it came from and the rule under which it was selected.

**P10-3.80 (MUST) Survivorship conflict reported.** An implementation must report a conflict where two contributions supply different values for one attribute and the declared rule does not resolve between them, and must not select arbitrarily.

**P10-3.81 (MUST) Unresolved conflict has an owner.** An implementation must assign every unresolved survivorship conflict to the domain steward and must expose the population of unresolved conflicts.

**P10-3.82 (MUST NOT) No probabilistic match executed as final without a threshold declaration.** An implementation must not act on a probabilistic match whose threshold is undeclared, and must record the threshold as an implementation decision of the domain.

**P10-3.83 (MUST) Match band declared.** An implementation must declare, for every domain using probabilistic matching, the score band within which a match is referred for adjudication rather than asserted, and must refer every match falling in it.

**P10-3.84 (MUST) Adjudication obtained, not performed.** An implementation must obtain the work by which a steward adjudicates a referred match from `Part 8` and must record the work item reference on the resulting assertion.

### 3.13 Consumers, releases, distribution and consumption

| Field, consumer registration | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `consumer_registration_id` | identifier | yes | 1 | Not possible |
| `party_ref` | pin to party | yes | 1 | Not possible |
| `subscribed_subjects` | identifier | yes | 1..n | Not possible; the code systems, value sets, maps or domains subscribed |
| `declared_refresh_interval` | interval | no | 0..1 | The consumer declares no refresh cadence, which prevents any staleness expectation being set |
| `reporting_capability` | enum(`reports`,`cannot_report`,`undeclared`) | yes | 1 | Not possible; see P10-3.88 |
| `registered_at` | instant | yes | 1 | Not possible |
| `withdrawn_at` | instant | no | 0..1 | The registration is current |

| Field, distribution record | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `distribution_record_id` | identifier | yes | 1 | Not possible |
| `release_id` | identifier | yes | 1 | Not possible |
| `consumer_registration_id` | identifier | yes | 1 | Not possible |
| `made_available_at` | instant | yes | 1 | Not possible |
| `withholding_record_ids` | identifier | no | 0..n | Nothing was withheld from this delivery |
| `constraint_ids_applied` | identifier | no | 0..n | No distribution constraint applied |

| Field, consumption report | Type | Required | Cardinality | Absence means |
|---|---|---|---|---|
| `consumption_report_id` | identifier | yes | 1 | Not possible |
| `consumer_registration_id` | identifier | yes | 1 | Not possible |
| `reported_at` | instant | yes | 1 | Not possible |
| `versions_held` | structure: subject id, version id, held since | yes | 1..n | Not possible |
| `basis` | enum(`self_reported`,`observed`,`attested`) | yes | 1 | Not possible |
| `expansion_digests_held` | digest | no | 0..n | The consumer reports versions without reporting the expansions it computed |

**P10-3.85 (MUST) Consumers registered.** An implementation must maintain a consumer registration for every party or component to which it distributes, and must not distribute to an unregistered consumer.

**P10-3.86 (MUST) Distribution recorded per consumer.** An implementation must record a distribution for each consumer a release was made available to, at the grain of one record per consumer per release.

**P10-3.87 (MUST) Report basis recorded.** An implementation must record whether a consumption report is self reported, observed by this component or attested by an accountable party.

**P10-3.88 (MUST) Reporting capability declared.** An implementation must record whether each registered consumer can report at all, and must count a consumer that cannot report in the unreported population rather than excluding it.

**P10-3.89 (MUST NOT) No exclusion of the incapable from the count.** An implementation must not remove a consumer declared unable to report from the unreported population, since the purpose of the population is to measure what is unknown.

**P10-3.90 (MUST) Expansion digest reported where computed.** An implementation must accept and record the digest of every expansion a consumer reports computing, so that a consumer computing a different membership from the same version is detectable.

**P10-3.91 (MUST) Staleness measured against the declared interval.** An implementation must measure a consumer's staleness against that consumer's declared refresh interval and must report a consumer with no declared interval as unmeasurable rather than as current.

### 3.14 Stewardship

**P10-3.92 (MUST) Steward assigned to every subject.** An implementation must assign a steward to every code system, value set, map and master domain, and must not publish a subject with none.

**P10-3.93 (MUST) Stewardship is accountability, not access.** An implementation must not treat a stewardship assignment as conferring any permission, and must obtain every permission from `Part 7`. **Source.** `Part 7` section 11.19 names stewardship treated as entitlement as an anti pattern; this part states the reciprocal prohibition.

**P10-3.94 (MUST) Steward absence blocks progression.** An implementation must not progress the registration status of a subject above the recorded level where no steward is assigned.

**P10-3.95 (MUST) Steward changes recorded.** An implementation must record every change of steward with its instant, the prior steward and the authorising decision.

### 3.15 Retention coupled to the determinations that cited a version

`Part 7` section 12.10 requires this component to retain every superseded version for at least as long as the longest retained decision that read it. The requirement generalises: every part that pins a version of this component's content creates a retention obligation here that this component cannot discover by itself.

**P10-3.96 (MUST) Retention floor recorded per version.** An implementation must record, for every code system version, value set version, map version, expansion and master record, the latest instant to which a citing determination is retained, as its retention floor.

**P10-3.97 (MUST) Retention floor raised on citation.** An implementation must raise the retention floor of a version when it is notified that a determination citing it is retained beyond the current floor.

**P10-3.98 (MUST NOT) No disposition below the floor.** An implementation must not dispose of a version, expansion or master record before its retention floor, and must refuse a disposition act that would.

**P10-3.99 (MUST) Unknown citation exposed.** An implementation must expose every version with no recorded retention floor, since a version believed uncited may be cited by a determination in a component that does not notify.

**P10-3.100 (MUST) Tombstone on disposition.** An implementation must retain, for every disposed version or record, a tombstone carrying its identifier, its class, the disposing act and the instant, so that a citation to it resolves to an explanation rather than to nothing.

**P10-3.101 (MUST) Digests survive disposition.** An implementation must retain the content digest and the identity of every disposed version, so that a later presentation of content can be tested against the record of what was published.

### 3.16 Projections

**P10-3.102 (MUST) Projections marked as such.** An implementation must mark every projection it exposes as a projection and must not permit a projection to be cited as a record.

**P10-3.103 (MUST) Golden view is a projection.** An implementation must expose the current value of a master attribute as a projection over contributions and survivorship determinations, and must not hold it as an independent record.

**P10-3.104 (MUST) Contributions retrievable from the projection.** An implementation must make every contribution behind a presented attribute value retrievable from the projection.

**P10-3.105 (MUST) Flattened expansion marked.** An implementation must mark every delivered expansion with its withheld count, its truncation flag and its closure mode, and must not deliver a bare list of members.

**P10-3.106 (MUST NOT) No boolean membership projection as a record.** An implementation must not record a membership determination as a boolean, and may expose a boolean only as a projection over a recorded outcome from section 7.2. **Source.** `Part 7` section 3.16 takes the same position on a two valued projection over a recorded fuller decision, and its section 13 records the question of whether the refusal stands against a newer standard specifying a boolean interface. This part inherits the position and the open question.

### 3.17 Worked demonstration

The demonstration is narrative and binds nothing. It exists because the difference between this model and a conventional one is not visible in a field list.

A value set version `VS-7`, defined intensionally as all descendants of concept `C-100` in code system `CS-A` with an unpinned code system binding, is expanded on 2026-03-01 against `CS-A` version 12. The expansion `EXP-9001` enumerates 340 members, closure mode transitive, withheld count zero, truncated false, inactive excluded. A consumer receives release `REL-55` conveying `VS-7` and `EXP-9001` and reports holding both.

On 2026-06-01 `CS-A` version 13 inactivates `C-217`, a descendant of `C-100`, with reason `erroneous` and a successor relation of kind `replaced_by` to `C-980`, and adds `C-981` as a new descendant of `C-100`. Nothing about `VS-7` changes: its definition digest is identical and its version designation is unchanged. Under clause P10-3.34 the registry already exposes `VS-7` as having an unpinned binding, so the hazard was declared before it materialised.

A membership determination for `C-981` against `VS-7` on 2026-06-02 must not be answered from `EXP-9001`. Under clause P10-3.40 the expansion may not be reused against a different code system version, so a new expansion `EXP-9107` is computed against version 13, enumerating 340 members again, being 339 carried forward plus `C-981`, with `C-217` excluded as inactive. The determination returns member, citing `EXP-9107`.

A determination for `C-217` returns `member_inactive` and not `not_a_member`, with the successor relation attached and no substitution performed, per clauses P10-3.30 and section 7.2. A caller that wants `C-980` must decide to take it, because the association kind is `replaced_by` and this component will not decide that the past should be reinterpreted.

A determination made on 2026-04-01, before the change, is not revalued. Under section 6.9 the earlier determination stands with its citation to `EXP-9001`, and the affected determination query exposes it as one whose inputs have since changed. The estate's exposure is the set of consumers still holding `EXP-9001`, which is knowable only from consumption reports, and the consumers that never report are counted under clause P10-3.7 rather than assumed current.

## 4. Interfaces

### 4.1 Interface principles

**P10-4.1 (MUST) Operations defined over the entities of section 3.** An implementation must define every operation it exposes in terms of the entities of section 3 and must state which records each creates and which events it emits.

**P10-4.2 (MUST) Idempotency key accepted.** An implementation must accept a caller supplied idempotency key on every state changing operation and must return the original result when invoked again with the same key and arguments.

**P10-4.3 (MUST) Idempotency conflict refused.** An implementation must refuse an operation invoked with a previously seen idempotency key and different arguments, and must not apply it.

**P10-4.4 (MUST) Authorisation obtained per operation.** An implementation must obtain an authorisation decision from `Part 7` before applying any operation that publishes, progresses, withdraws, merges, unmerges or adjudicates, and must record the decision reference.

**P10-4.5 (MUST) One outcome per operation.** An implementation must return exactly one outcome from section 7 for every operation and must not return a success outcome where any part of the requested change was not applied.

**P10-4.6 (MUST) Refusals recorded.** An implementation must record every refused operation with the requesting party, the instant, the argument digest and the refusal code.

**P10-4.7 (MUST NOT) No mutation of published content.** An implementation must not expose an operation that alters a published code system version, value set version, map version or expansion.

### 4.2 Authoring and publication operations

| Operation | Effect | Kind |
|---|---|---|
| `register_code_system` | Creates a code system with its authority, steward and key scheme | reference |
| `draft_code_system_version` | Creates a version in draft | reference |
| `add_concept` | Adds a concept to a draft version | reference |
| `inactivate_concept` | Records an inactivation with reason and successors in a draft version | reference |
| `add_designation` | Adds a designation to a concept in a draft version | reference |
| `assert_relation` | Adds a relation assertion to a draft version | reference |
| `register_value_set` | Creates a value set with its steward | reference |
| `draft_value_set_version` | Creates a value set version with its definition mode and binding | reference |
| `register_map` | Creates a map with its steward | reference |
| `draft_map_version` | Creates a map version with its direction and completeness declaration | reference |
| `add_map_entry` | Adds an entry with its equivalence class | reference |
| `progress_status` | Appends a registration status transition | both |
| `publish_version` | Sets version state to published | both |
| `deprecate_version` | Sets version state to deprecated | both |
| `sunset_version` | Sets version state to sunset | both |
| `withdraw_version` | Sets version state to withdrawn with a reason | both |
| `register_master_domain` | Creates a domain with its steward, identifier scheme and attributes | master |
| `register_consumer` | Creates a consumer registration | both |
| `record_release` | Creates a release conveying stated versions | both |
| `record_distribution` | Creates a distribution record per consumer | both |
| `record_consumption` | Records a consumption report | both |
| `record_distribution_constraint` | Records a redistribution restriction | reference |
| `assign_steward` | Assigns or changes a steward | both |

**P10-4.8 (MUST) Publication refused without a steward.** An implementation must refuse `publish_version` where the subject has no assigned steward.

**P10-4.9 (MUST) Publication refused without a document identity.** An implementation must refuse `publish_version` where the version carries no `Part 1` document identity.

**P10-4.10 (MUST) Inactivation refused without a reason.** An implementation must refuse `inactivate_concept` where no inactivation reason is supplied.

**P10-4.11 (MUST) Inactivation refused without a successor statement.** An implementation must refuse `inactivate_concept` where neither a successor nor the explicit absence of one is supplied.

**P10-4.12 (MUST) Key reuse refused.** An implementation must refuse `add_concept` where the key has previously denoted a different referent in the same code system.

**P10-4.13 (MUST) Map entry refused without an equivalence class.** An implementation must refuse `add_map_entry` where no equivalence class from section 3.9 is supplied.

**P10-4.14 (MUST) Map publication refused without a completeness declaration.** An implementation must refuse `publish_version` for a map version whose completeness is undeclared.

**P10-4.15 (MUST) Withdrawal refused while cited within the floor.** An implementation must refuse `withdraw_version` where the version's retention floor has not passed, and must record the refusal.

**P10-4.16 (MUST) Distribution refused to an unregistered consumer.** An implementation must refuse `record_distribution` naming a consumer with no registration.

### 4.3 Determination operations

| Operation | Effect | Kind |
|---|---|---|
| `determine_membership` | Creates a membership determination for one value against one value set version | reference |
| `expand_value_set` | Creates an expansion against stated code system versions | reference |
| `lookup_concept` | Returns a concept with its state, designations and successor relations | reference |
| `resolve_relations` | Returns direct relations or a declared transitive closure | reference |
| `translate` | Returns map entries for a source concept under a map version | reference |
| `resolve_master_identifier` | Returns a master record, or the surviving record with the merge assertion | master |
| `assert_match` | Creates a match assertion | master |
| `assert_merge` | Creates a merge assertion | master |
| `withdraw_merge` | Withdraws a merge assertion | master |
| `determine_survivorship` | Creates a survivorship determination for an attribute | master |
| `affected_determinations` | Returns determinations whose cited inputs have since changed | both |
| `coverage_report` | Returns the members of a version no consumer is known to hold, and the converse | both |

**P10-4.17 (MUST) Membership determination requires a pinned version.** An implementation must require `determine_membership` to name a value set version and must refuse a request naming a value set alone.

**P10-4.18 (MUST) Membership determination requires code system versions.** An implementation must require `determine_membership` against an unpinned value set version to name the code system versions to use, and must refuse the request where they are not supplied.

**P10-4.19 (MUST) Membership determination returns an outcome, not a boolean.** An implementation must return an outcome from section 7.2 from `determine_membership` and must not return a two valued result as the operation's result.

**P10-4.20 (MUST) Expansion requires pinned inputs.** An implementation must require `expand_value_set` to resolve every code system version it will use before computing, and must record them on the expansion.

**P10-4.21 (MUST) Closure mode declared on request.** An implementation must require `resolve_relations` to declare whether direct relations or a transitive closure is requested, and must refuse a request that declares neither.

**P10-4.22 (MUST) Translate returns the equivalence class.** An implementation must return the equivalence class with every entry `translate` returns and must not return a bare target concept.

**P10-4.23 (MUST) Translate returns unmatched as a result.** An implementation must return an `unmatched` entry where one exists rather than an empty result, and must distinguish both from a map that does not cover the source.

**P10-4.24 (MUST) Absorbed identifier resolution returns the assertion.** An implementation must return the merge assertion with the surviving record when `resolve_master_identifier` is called with an absorbed identifier.

**P10-4.25 (MUST NOT) No merge without adjudication in the referral band.** An implementation must not accept `assert_merge` resting on a match whose score falls within the declared referral band and which carries no adjudication.

**P10-4.26 (MUST) Affected determinations answerable.** An implementation must answer `affected_determinations` for a stated version or record, and must report the determinations it cannot enumerate separately from those it can.

### 4.4 Reading operations

**P10-4.27 (MUST) Point in time read supported.** An implementation must answer, for any stated past instant, the state and content of a code system version, value set version, map version, concept and master record as at that instant.

**P10-4.28 (MUST NOT) No state change from a read.** An implementation must not change any state other than a read record in response to a reading operation.

**P10-4.29 (MUST) Read carries the version that answered it.** An implementation must return, with every read, the identity of every version from which the answer was composed.

**P10-4.30 (MUST) Withheld count on every delivered set.** An implementation must return the withheld count with every set a reading operation delivers.

**P10-4.31 (MUST NOT) No read of unpublished content by a consumer.** An implementation must not return draft content to a consumer registration and must restrict draft reads to the authoring and stewardship path.

### 4.5 What a caller may and may not assume

**P10-4.32 (MUST) Published versions immutable.** A caller may assume that a published version's content will never change under the same identity.

**P10-4.33 (MUST NOT) No assumption of expansion stability.** A caller must not assume that expanding one value set version twice yields the same membership, unless the version pins its code system versions.

**P10-4.34 (MUST NOT) No assumption that absence of a finding means membership.** A caller must not assume that a value not reported as withheld, truncated or inactive is therefore a member, and must read the outcome.

**P10-4.35 (MUST NOT) No assumption of successor substitutability.** A caller must not assume that a successor concept may be substituted for an inactive one, and must read the association kind.

**P10-4.36 (MUST NOT) No assumption that a master identifier denotes a verified entity.** A caller must not assume an entity exists in the world because a master record denotes it, and must read the existence basis.

**P10-4.37 (MUST NOT) No assumption of consumer currency.** A caller must not assume that a consumer holds the current version of any subject in the absence of a consumption report.

### 4.6 Reads from other components

| Read | Component | Pinning | On failure |
|---|---|---|---|
| Governed definition for a concept | `Part 4` | pinned per concept | refuse publication; do not publish a concept citing an unresolvable definition |
| Authorisation decision | `Part 7` | policy version pinned per decision | deny the operation; never permit on failure |
| Rule verdict for a conditional map entry | `Part 2` | rule version pinned per evaluation | record the non verdict; do not apply the entry |
| Document identity, approval, effective date | `Part 1` | pinned per version | refuse publication |
| Release artifact bytes | `Part 11` | content address | refuse distribution; report the release as unresolvable |
| Work item for adjudication | `Part 8` | work item reference | leave the match undetermined; do not assert |
| Party identity for steward, source and consumer | this component | own content | refuse the operation |
| Schema of a distributed release payload | `Part 9` | schema version pinned | refuse the release |

**P10-4.38 (MUST) Reads treated as fallible.** An implementation must treat every read in the table in section 4.6 as fallible and must apply the stated failure behaviour rather than a default.

**P10-4.39 (MUST NOT) No proceeding on an authorisation failure.** An implementation must not proceed with an operation when the authorisation read fails, and must deny.

**P10-4.40 (MUST NOT) No caching beyond a pinning scope.** An implementation must not use a cached read from another component beyond the pinning scope in section 4.6 without recording the cache instant and treating the value as pinned at it.

### 4.7 Events emitted

**P10-4.41 (MUST) Event per transition.** An implementation must emit an event for every registration status transition, version state transition, concept state transition, merge, unmerge and stewardship change.

**P10-4.42 (MUST) Event carries prior state and cause.** An implementation must carry on every event the record identifier, the prior state where one changed, the instant, the acting party and the event's own identifier.

**P10-4.43 (MUST) Events delivered to the ledger.** An implementation must deliver every event to `Part 3` at least once and must retain the event until delivery is acknowledged.

**P10-4.44 (MUST) Membership change event names affected sets.** An implementation must emit an event on the addition or removal of a member from a published set, naming every value set version whose expansion is affected. **Source.** Required of this component by `Part 7` clause P7-12.29, which records a change to a pinned value set version as requiring a new policy version where target completeness is affected. The event is what makes that check possible.

**P10-4.45 (MUST) Concept inactivation event carries successors.** An implementation must carry the inactivation reason and every successor relation on the event announcing an inactivation.

**P10-4.46 (MUST) Unpinned expansion drift event.** An implementation must emit an event when a code system version change alters the membership an unpinned value set version would expand to.

**P10-4.47 (MUST) Withholding event distinct.** An implementation must emit a distinct event class for a delivery with a non zero withheld count.

**P10-4.48 (SHOULD) Unreported consumer signal.** An implementation should emit an event when a consumer passes its declared refresh interval without reporting.

## 5. State model

### 5.1 Seven state models

This component carries seven, which is more than any prior part, and the reason is that it holds two subjects with different lifecycles and a distribution apparatus with a lifecycle of its own. The registration status of a subject, the state of a version, the state of a concept, the state of a master record, the state of a merge assertion, the state of a consumption report and the state of a withholding are seven independent questions, and answering one with another is the error the section prevents.

**P10-5.1 (MUST) States held as transitions.** An implementation must hold every state as a sequence of recorded transitions and must not hold it as a mutable field.

**P10-5.2 (MUST) One state per axis per instant.** An implementation must not represent two states of one entity on one axis as simultaneously current.

**P10-5.3 (MUST NOT) No derivation of one axis from another.** An implementation must not derive registration status from version state, version state from concept state, or master record state from merge state.

**P10-5.4 (MUST) Transitions carry authorisation.** An implementation must record the authorising decision reference on every transition that requires one under section 4.

**P10-5.5 (MUST) Illegal transitions recorded.** An implementation must record every refused transition and must not discard the attempt.

**P10-5.6 (MUST NOT) No unlisted transition.** An implementation must not admit a transition this section does not list.

### 5.2 Registration status of a subject

Applies to a code system version, a value set version, a map version and a master domain.

| Status | Meaning | Terminal |
|---|---|---|
| `submitted` | Presented for registration, mandatory metadata possibly incomplete | no |
| `recorded` | All mandatory metadata complete and all mandatory associations instantiated | no |
| `qualified` | Recorded, sponsored by a steward and approved by the registration authority | no |
| `standardized` | Adopted as the standard subject for its scope | no |
| `preferred` | Designated preferred where several exist for one scope | no |
| `superseded` | A successor subject is preferred; remains readable and citable | no |
| `retired` | Withdrawn from use, retained and citable | yes |
| `rejected` | Refused at admission | yes |

Legal transitions: to `submitted` on registration; `submitted` to `recorded` on metadata completion; `submitted` to `rejected` or `retired` by authority act; `recorded` to `qualified` on steward sponsorship and authority approval; `qualified` to `standardized`; `standardized` to `preferred`; `preferred` to `standardized` on removal of preference; any of `recorded`, `qualified`, `standardized`, `preferred` to `superseded` on designation of a successor; any non terminal to `retired` by authority act.

**P10-5.7 (MUST) Recorded requires complete metadata.** An implementation must not progress a subject to `recorded` until every mandatory metadata attribute is complete and every mandatory association is instantiated. **Source.** ISO/IEC 11179-6:2023 clause 4.3.3.1.4 states that the Recorded status means all mandatory metadata attributes have been completed, all mandatory associations have been instantiated and all associated constraints are to be enforced, and that the rule applies to any and all attached items.

**P10-5.8 (MUST) Qualified requires steward and authority.** An implementation must require the sponsorship of a steward and the approval of the registration authority for progression to `qualified` or above. **Source.** ISO/IEC 11179-6:2023 requires that progression of administered items to a registration status of Qualified or higher require the sponsorship of a steward and the approval of the registration authority.

**P10-5.9 (MUST NOT) Recorded is not a quality claim.** An implementation must not represent `recorded` as a statement that the metadata meets quality requirements. **Source.** ISO/IEC 11179-6:2023 states that the contents of the mandatory metadata attributes of a Recorded item possibly do not conform to quality requirements.

**P10-5.10 (MUST) Superseded names its successor.** An implementation must name the successor subject on every transition to `superseded`.

**P10-5.11 (MUST) Retired subjects still resolve.** An implementation must continue to resolve a retired subject, since determinations citing it remain.

### 5.3 Version state

Applies to a code system version, a value set version and a map version.

| State | Meaning | Terminal |
|---|---|---|
| `draft` | Editable, not distributable, not citable by a published determination | no |
| `published` | Immutable, distributable, citable | no |
| `deprecated` | Not to be adopted for new use; remains distributable and citable | no |
| `sunset` | Not to be used; remains resolvable for citation and re-determination | no |
| `withdrawn` | Never to be used; resolvable only for the resolution of prior records | yes |

Legal transitions: to `draft` on creation; `draft` to `published`; `draft` to `withdrawn`; `published` to `deprecated`; `published` to `withdrawn` with a recorded reason; `deprecated` to `published` on reinstatement with a recorded reason; `deprecated` to `sunset`; `sunset` to `deprecated` on reinstatement with a recorded reason; `sunset` to `withdrawn`.

**P10-5.12 (MUST) Draft content not distributable.** An implementation must not include a version in `draft` in any release.

**P10-5.13 (MUST) Published content immutable.** An implementation must not alter the content of a version once published, and must express a correction as a new version.

**P10-5.14 (MUST) Deprecated content still determinable.** An implementation must continue to determine membership against a deprecated version, since instances written under it remain.

**P10-5.15 (MUST) Sunset requires the holder population.** An implementation must record which consumer registrations are known or believed to hold a version at the instant it is sunset, and must record the unreported population separately.

**P10-5.16 (MUST NOT) No withdrawal while consumers report holding.** An implementation must not withdraw a version while a current consumption report records a consumer holding it, unless the transition carries an authorisation reference naming the holdings it overrides.

**P10-5.17 (MUST) Withdrawal reason recorded.** An implementation must record a reason from an authority declared enumeration on every transition to `withdrawn` from `published`.

### 5.4 Concept state

| State | Meaning | Terminal |
|---|---|---|
| `active` | In current use, may be selected and asserted | no |
| `inactive` | Not for current use, remains resolvable and remains a member of historical expansions | no |
| `retired_key` | Inactive and reserved permanently against reassignment | yes |

Legal transitions: to `active` on addition in a draft version; `active` to `inactive` on inactivation with a reason; `inactive` to `active` on reactivation with a recorded reason; `inactive` to `retired_key` by authority act.

Inactivation reasons, closed enumeration: `erroneous`, being the concept should never have existed; `duplicate`, being another concept denotes the same meaning; `ambiguous`, being the meaning cannot be determined; `outdated`, being the meaning is no longer used; `moved`, being the concept now lives in another code system; `limited`, being the concept is retained for a restricted purpose only; `superseded_by_new_concept`, being a replacement exists.

**P10-5.18 (MUST) No terminal state that removes resolvability.** An implementation must resolve a concept in every state, including `retired_key`.

**P10-5.19 (MUST) Inactive concepts remain in historical expansions.** An implementation must not remove a concept from an expansion computed before its inactivation.

**P10-5.20 (MUST) Reactivation reasoned.** An implementation must record a reason for every reactivation and must not reactivate a concept whose inactivation reason was `erroneous` without a steward act.

**P10-5.21 (MUST NOT) No key release from retired_key.** An implementation must not admit any transition out of `retired_key` and must not permit the key to be assigned again.

### 5.5 Expansion state

| State | Meaning | Terminal |
|---|---|---|
| `computed` | Complete against its declared inputs | yes |
| `partial` | Computed and incomplete for a recorded cause | yes |
| `failed` | Not computed for a recorded cause | yes |

**P10-5.22 (MUST) Expansion states terminal.** An implementation must treat every expansion state as terminal and must express a recomputation as a new expansion.

**P10-5.23 (MUST) Partial expansions retained.** An implementation must retain a partial expansion with its cause and must not discard it in favour of a later complete one.

### 5.6 Master record state

| State | Meaning | Terminal |
|---|---|---|
| `provisional` | Created from contributions, not confirmed as denoting a distinct entity | no |
| `confirmed` | Confirmed as denoting a distinct entity | no |
| `absorbed` | Merged into another record, resolvable, identifier never reused | no |
| `disputed` | A contradiction is recorded and unresolved | no |
| `void` | Asserted to denote no entity | yes |

Legal transitions: to `provisional` on creation; `provisional` to `confirmed` on confirmation with a basis; `provisional` or `confirmed` to `absorbed` on merge; `absorbed` to `confirmed` or `provisional` on unmerge, restoring the prior state; `confirmed` or `provisional` to `disputed` on a recorded contradiction; `disputed` to `confirmed` on resolution; any non terminal to `void` on an assertion that no entity exists.

**P10-5.24 (MUST) Provisional distinguished from confirmed.** An implementation must distinguish a record created from a contribution from one confirmed as denoting a distinct entity, and must not present the first as the second.

**P10-5.25 (MUST) Absorbed records resolve.** An implementation must resolve an absorbed record and must return it with its merge assertion.

**P10-5.26 (MUST) Unmerge restores the prior state.** An implementation must restore the state a record held immediately before absorption when a merge is withdrawn.

**P10-5.27 (MUST) Void is terminal and resolvable.** An implementation must treat `void` as terminal and must continue to resolve a void record, since determinations citing it remain.

**P10-5.28 (MUST) Disputed exposed.** An implementation must expose the population of records in `disputed` and must assign each to the domain steward.

### 5.7 Merge assertion state

| State | Meaning | Terminal |
|---|---|---|
| `in_force` | The merge is current | no |
| `withdrawn` | The merge was withdrawn by an unmerge | yes |
| `superseded` | A later merge assertion covers the same pair | yes |

**P10-5.29 (MUST) Merge state separate from record state.** An implementation must hold the state of a merge assertion separately from the state of the records it concerns.

**P10-5.30 (MUST) Withdrawn merges retained.** An implementation must retain a withdrawn merge assertion with its instant and reason.

### 5.8 Consumption report state

| State | Meaning | Terminal |
|---|---|---|
| `current` | Received within the consumer's declared refresh interval | no |
| `stale` | The declared interval has elapsed since the last report | no |
| `never_reported` | The consumer has never reported | no |
| `unmeasurable` | The consumer declares no refresh interval | no |
| `incapable` | The consumer has declared it cannot report | no |

**P10-5.31 (MUST) Five states distinguished.** An implementation must distinguish the five states in section 5.8 and must not collapse them into a reported or not reported pair.

**P10-5.32 (MUST) Four states counted as unreported.** An implementation must count `stale`, `never_reported`, `unmeasurable` and `incapable` in the unreported population of clause P10-3.7.

**P10-5.33 (MUST NOT) No terminal consumption state.** An implementation must not treat any consumption report state as terminal, since a consumer may report at any time.

## 6. Execution semantics

### 6.1 Determinism and reproducibility

**P10-6.1 (MUST) Determination reproducible from its record.** An implementation must be able to re-perform any recorded membership determination from the inputs the record names and must obtain the same outcome.

**P10-6.2 (MUST) Expansion reproducible from its inputs.** An implementation must produce the same expansion given the same value set version, the same code system versions, the same closure mode and the same inactive inclusion declaration.

**P10-6.3 (MUST) Reproducibility set recorded.** An implementation must record, on every determination and expansion, the complete set of pinned inputs required to re-perform it.

**P10-6.4 (MUST) Non reproducibility reported.** An implementation must report `not_reproducible` where any input a record names cannot be resolved, and must not substitute a current input.

**P10-6.5 (MUST NOT) No clock in a determination.** An implementation must not consult the current instant in the evaluation of a membership, relation or map determination, and must use only the instant the caller supplies or the instant recorded on the expansion.

**P10-6.6 (MUST NOT) No ordering dependence in an expansion.** An implementation must not allow the order in which intensional rules are evaluated to affect the membership an expansion yields.

**P10-6.7 (MUST) Non confluent definition refused.** An implementation must refuse a value set version whose membership depends on the order in which its rules are applied, and must record the refusal.

### 6.2 The expansion algorithm

The algorithm is narrative and binds nothing except where a clause names a step.

Resolve the value set version. Resolve every code system version, taking the pinned versions where the binding is pinned and the caller supplied versions where it is unpinned, and refuse where an unpinned binding is presented with no caller supplied versions. Take one immutable snapshot of every resolved code system version. Evaluate the extensional members, refusing any whose key is not present in the named code system version. Evaluate each intensional rule against the snapshot, applying the closure mode the rule kind declares. Take the union, then remove every member the exclusion rules select. Apply the inactive inclusion declaration. Apply authorisation and distribution constraints, marking every excluded member as withheld and counting it. Apply the size bound, marking truncation if reached. Record the expansion with its inputs, its digest, its withheld count, its truncation flag and its outcome.

**P10-6.8 (MUST) One snapshot per expansion.** An implementation must evaluate every rule of one expansion against one immutable snapshot of each code system version and must not observe a change made during the computation.

**P10-6.9 (MUST) Unresolvable key refused.** An implementation must refuse an expansion whose extensional definition names a key not present in the named code system version, and must not silently drop the member.

**P10-6.10 (MUST) Exclusions applied after inclusions.** An implementation must apply exclusion rules after the union of inclusion rules and must record the order as fixed.

**P10-6.11 (MUST) Withholding applied last and counted.** An implementation must apply authorisation and distribution withholding after membership is determined, and must count the withheld members rather than reducing the total.

**P10-6.12 (MUST) Size bound declared.** An implementation must declare a maximum expansion size, must record it on every expansion, and must mark truncation where it is reached. The value is an implementation decision because the useful bound depends on the size of the code systems admitted, which this part does not constrain.

**P10-6.13 (MUST) Bound finite.** An implementation must declare a finite maximum expansion size.

### 6.3 Membership determination

**P10-6.14 (MUST) Determination against an expansion or a definition, declared.** An implementation must record whether a membership determination was answered from an expansion or computed against the definition, and must not leave the method unrecorded.

**P10-6.15 (MUST NOT) No determination from a stale expansion.** An implementation must not answer a determination from an expansion computed against code system versions other than those in force for the request, and must recompute or refuse.

**P10-6.16 (MUST) Inactive membership distinguished.** An implementation must return `member_inactive` for a value that is a member of the set and whose concept is inactive, and must not return either `member` or `not_a_member`.

**P10-6.17 (MUST NOT) Unknown code never non membership.** An implementation must not return `not_a_member` for a value the referenced code system version does not contain, and must return `code_unknown_to_system`. **Source.** `Part 7` section 7.2 refuses to return not applicable as deny for the same reason: a coverage gap reported as a negative is a gap that can never be found. This part is the second to take the position on its own subject and section 13.7 records the repetition.

**P10-6.18 (MUST NOT) No non membership on an unresolvable input.** An implementation must not return `not_a_member` where the value set version, a code system version or a required expansion could not be resolved, and must return the outcome naming the unresolvable input.

**P10-6.19 (MUST) Case handling declared and applied.** An implementation must apply the case sensitivity declared for the code system when comparing a value to a key and must record the declaration applied.

**P10-6.20 (MUST NOT) No normalisation of a submitted value.** An implementation must not normalise a submitted value before comparison beyond what the code system's declared key scheme specifies, and must record any normalisation applied.

**P10-6.21 (MUST) Determination cites the expansion.** An implementation must record the expansion identifier on every determination answered from one.

### 6.4 Relation traversal and the transitive closure

**P10-6.22 (MUST) Closure requested, never assumed.** An implementation must require a caller to declare whether direct relations or a transitive closure is wanted, and must not adopt a default. **Source.** SKOS declares the hierarchical properties non transitive by convention so that they assert only immediate links, and supplies separate transitive properties for inference. The two questions have different answers and this part refuses to guess which was asked.

**P10-6.23 (MUST) Closure over a declared kind only.** An implementation must compute a transitive closure only over a relation kind registered as transitive, and must refuse a closure request over a non transitive kind.

**P10-6.24 (MUST) Closure result marked as inferred.** An implementation must mark every member of a returned closure that is not a directly asserted relation as inferred.

**P10-6.25 (MUST) Cycles detected and reported.** An implementation must detect a cycle in a relation kind declared transitive and must report it as a defect of the code system version rather than iterating.

**P10-6.26 (MUST) Depth bound declared.** An implementation must declare a maximum traversal depth, must record the depth reached on every closure computation, and must report the bound being reached. The value is an implementation decision because the useful depth depends on the depth of the hierarchies admitted.

**P10-6.27 (MUST NOT) No closure across code systems.** An implementation must not traverse a relation from a concept of one code system to a concept of another, and must express any cross system relation as a map entry.

**P10-6.28 (MUST NOT) No associative relation in a closure.** An implementation must not include an associative relation in a hierarchical closure. **Source.** SKOS declares `skos:related` disjoint with `skos:broaderTransitive`, and by the symmetry of `skos:related` also with `skos:narrowerTransitive`.

### 6.5 Map application

**P10-6.29 (MUST) Map applied under a pinned version.** An implementation must apply a map only under a named map version and must refuse a translation request naming a map alone.

**P10-6.30 (MUST) Every applicable entry returned.** An implementation must return every entry of the map version applicable to the source concept and must not return one where several apply.

**P10-6.31 (MUST NOT) No selection among map entries.** An implementation must not select among several applicable map entries, and must return them all with their equivalence classes so that the caller decides. **Source.** This part refuses to arbitrate for the same reason `Part 2` reports a rule contradiction, `Part 5` returns an undecidable outcome, `Part 6` refuses to resolve a join by an undeclared order and `Part 7` returns indeterminate on multiplicity. This is the fifth part to refuse arbitration and section 13.7 records it.

**P10-6.32 (MUST) Ambiguity reported.** An implementation must report an ambiguity where a map version supplies more than one entry with the class `equivalent` for one source concept, since only one such entry can be true.

**P10-6.33 (MUST NOT) No inversion at application time.** An implementation must not answer a target to source translation from a source to target map version.

**P10-6.34 (MUST NOT) No chaining at application time.** An implementation must not answer a translation by chaining two map versions.

**P10-6.35 (MUST) Unmapped policy applied and recorded.** An implementation must apply the unmapped policy the map version declares and must record every application of a default or a source code passthrough.

**P10-6.36 (MUST) Conditional entry verdict obtained.** An implementation must obtain the `Part 2` verdict for a conditional map entry before applying it and must not apply the entry on a non verdict.

**P10-6.37 (MUST NOT) No non verdict treated as inapplicable.** An implementation must not treat a non verdict from `Part 2` as establishing that a conditional entry does not apply, and must return the outcome of section 7.4 naming the non verdict.

### 6.6 Matching and merging

**P10-6.38 (MUST) Matching deterministic given its inputs.** An implementation must produce the same match verdict given the same contributions, the same algorithm version and the same threshold.

**P10-6.39 (MUST) Algorithm version pinned.** An implementation must pin the version of any matching algorithm it uses and must record it on the assertion.

**P10-6.40 (MUST NOT) No re-run overwriting an assertion.** An implementation must not overwrite a match assertion when an algorithm is re-run, and must record a new assertion superseding it.

**P10-6.41 (MUST) Threshold change surfaces the affected population.** An implementation must report every existing match assertion whose verdict would change under a changed threshold, before the change takes effect.

**P10-6.42 (MUST) Transitive merge closure declared.** An implementation must declare whether merge assertions are treated as transitive within a domain, and must refuse an implicit transitive merge where the declaration is absent.

Clause P10-6.42 addresses the failure by which three records become one without any assertion that the first and third concern the same entity. If A matches B and B matches C, treating merge as transitive absorbs all three, and the A to C claim was never made or evaluated. Where the domain declares transitivity, the derived assertion must be recorded as inferred under clause P10-3.52's principle; where it does not, the third record stays separate until someone asserts the pair.

**P10-6.43 (MUST) Inferred merge recorded as inferred.** An implementation must record a merge assertion derived from transitivity as inferred and must name the assertions it was derived from.

**P10-6.44 (MUST) Unmerge recomputes the survivorship.** An implementation must recompute the survivorship of both records after an unmerge and must record the new determinations rather than restoring the prior presented values.

**P10-6.45 (MUST NOT) No survivorship from a merged away record without record.** An implementation must not present a value contributed to an absorbed record without recording that the value came from it.

### 6.7 Survivorship

**P10-6.46 (MUST) Rule evaluated per attribute.** An implementation must evaluate survivorship independently for each master attribute and must not apply one record's outcome to another attribute.

**P10-6.47 (MUST) Rule kinds registered.** An implementation must register every survivorship rule kind before use, and must not accept an unregistered kind.

**P10-6.48 (MUST) Recency rules use the asserted instant.** An implementation must use the asserted instant rather than the received instant in any survivorship rule expressed in terms of recency, and must record which instant was used.

**P10-6.49 (MUST) Source trust expressed as a declared weight.** An implementation must express any preference among sources as a declared, versioned weight per attribute and must not express it as a list position.

**P10-6.50 (MUST) Tie reported, never broken arbitrarily.** An implementation must report a tie under a declared survivorship rule as an unresolved conflict and must not break it by any undeclared means.

**P10-6.51 (MUST) Conflict does not suppress the attribute.** An implementation must continue to expose every contributed value for an attribute in conflict and must not present the attribute as absent.

### 6.8 Idempotence, concurrency and bounds

**P10-6.52 (MUST) Determination idempotent under a key.** An implementation must return the original determination when a determination is requested again under the same idempotency key.

**P10-6.53 (MUST) Publication serialised.** An implementation must serialise concurrent publications of one subject and must record the losing attempt as an illegal transition.

**P10-6.54 (MUST) Contribution ingestion concurrent and ordered per source.** An implementation must accept concurrent contributions from different sources and must preserve the order of contributions from one source for one entity.

**P10-6.55 (MUST) Merge serialised per record.** An implementation must serialise concurrent merge assertions concerning one record.

**P10-6.56 (MUST) Bounds recorded.** An implementation must record every bound it applied on every operation whose result the bound could have affected.

### 6.9 Retrospective revaluation is refused

**P10-6.57 (MUST NOT) No revaluation of a recorded determination.** An implementation must not recompute a recorded membership determination when its inputs change, and must leave the determination as recorded.

**P10-6.58 (MUST) Affected determinations exposed.** An implementation must expose every recorded determination whose cited inputs have since changed, so that the party that relied on it can decide whether to act.

**P10-6.59 (MUST NOT) No decision on the consequence.** An implementation must not decide what follows from a determination whose inputs have changed, and must leave the consequence to the party that relied on it.

**P10-6.60 (MUST) Change class stated with the exposure.** An implementation must state, for every affected determination, whether the change was an inactivation, an addition, a removal, a designation change, a relation change or a map change.

**P10-6.61 (MUST NOT) No retrospective application of a successor.** An implementation must not apply a successor relation to a determination recorded before the successor was asserted.

### 6.10 Coverage analysis

**P10-6.62 (MUST) Member coverage against consumers answerable.** An implementation must be able to report, for a stated version, the consumers known to hold it, the consumers known to hold an earlier version and the consumers whose holding is unknown.

**P10-6.63 (MUST) Full membership exposed for a consumer's own checks.** An implementation must expose the full membership of a pinned value set version to an authorised consumer, so that the consumer can test its own coverage against the set. **Source.** Required of this component by `Part 7` clause P7-12.28, which requires that component to report every member of a pinned value set version that no target addresses.

**P10-6.64 (MUST) Unused member reporting supported.** An implementation must report, where a consumer supplies the members it addresses, the members of the set that consumer does not address.

**P10-6.65 (MUST NOT) No coverage claim over an unenumerated population.** An implementation must not report a coverage figure over consumers it cannot enumerate, and must report the unenumerable population separately.

## 7. Outcome and failure taxonomy

### 7.1 Why the taxonomy is the specification

Every enumeration in this section is closed, and each has one member that a conventional implementation does not have. Those members are the specification. A registry with `member` and `not_a_member` and nothing else will answer `not_a_member` when a code is unknown, when a value set could not be resolved, when an expansion was truncated, when a member was withheld, and when a concept is inactive. Five different conditions with five different remedies arrive at the caller as one, and the caller refuses the transaction in every case, so nothing ever surfaces as a fault.

**P10-7.1 (MUST) One enumeration per value.** An implementation must draw every value it returns from exactly one enumeration in this section.

**P10-7.2 (MUST NOT) No value outside the enumerations.** An implementation must not return a value outside these enumerations and must not extend one marked closed.

**P10-7.3 (MUST) Properties of an outcome exposed.** An implementation must expose, for every membership outcome, the three properties in the table in section 7.7.

### 7.2 Membership outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `member` | The value is a member of the set and its concept is active |
| `member_inactive` | The value is a member of the set and its concept is inactive |
| `not_a_member` | The set was fully determined and the value is not in it |
| `code_unknown_to_system` | The referenced code system version does not contain the value |
| `system_not_referenced` | The value's code system is not one the value set version draws on |
| `code_system_unresolvable` | A required code system version could not be resolved |
| `value_set_unresolvable` | The value set version could not be resolved |
| `expansion_incomplete_truncated` | The determination rested on a truncated expansion |
| `expansion_incomplete_withheld` | The set contains members withheld from the caller |
| `expansion_incomplete_fragment` | The code system version's content completeness is other than complete |
| `binding_unpinned_unspecified` | The value set version is unpinned and the caller supplied no code system versions |
| `undecidable_case_rule` | The comparison could not be made because the case sensitivity declaration is absent |
| `not_evaluated` | The determination was requested and not performed |

**P10-7.4 (MUST) Not a member only on a complete determination.** An implementation must return `not_a_member` only where the set was fully determined, no member was withheld, no expansion was truncated and the code system content is complete.

**P10-7.5 (MUST NOT) No collapse to non membership.** An implementation must not return `not_a_member` in place of any other value in section 7.2.

**P10-7.6 (MUST NOT) No collapse to membership.** An implementation must not return `member` in place of `member_inactive` or in place of any incompleteness outcome.

**P10-7.7 (MUST) Three incompleteness causes distinguished.** An implementation must distinguish truncation, withholding and content fragmentation as three causes and must not report them as one.

**P10-7.8 (MUST) System not referenced distinguished from unknown code.** An implementation must distinguish a value whose code system the set does not draw on from a value unknown to a code system the set does draw on.

Clause P10-7.8 separates two conditions that are routinely reported as one and have opposite remedies. A value from an unreferenced code system means the caller sent the wrong kind of value or the set omits a system it should include. A value unknown to a referenced system means the code is wrong or the system's version is behind.

### 7.3 Expansion outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `expanded_complete` | Every rule was evaluated and no member was withheld or truncated |
| `expanded_withheld` | Complete but with a non zero withheld count |
| `expanded_truncated` | The declared size bound was reached |
| `expanded_partial_fragment` | A code system version's content is not complete |
| `expansion_refused_unpinned` | The binding is unpinned and no code system versions were supplied |
| `expansion_refused_unresolvable_key` | An extensional member names a key not present in the named version |
| `expansion_refused_non_confluent` | The definition's membership depends on rule order |
| `expansion_failed_cycle` | A cycle was detected in a relation kind declared transitive |
| `expansion_failed_depth` | The declared traversal depth bound was reached |
| `expansion_failed_unresolvable_system` | A code system version could not be resolved |

**P10-7.9 (MUST) Complete only when nothing was withheld or truncated.** An implementation must return `expanded_complete` only where the withheld count is zero, truncation is false and every code system version's content is complete.

**P10-7.10 (MUST NOT) No refusal reported as an empty expansion.** An implementation must not return an empty member list with a successful outcome where the expansion was refused or failed.

**P10-7.11 (MUST) Refusal distinguished from failure.** An implementation must distinguish a refusal, which is a defect of the definition, from a failure, which is a condition of the computation.

### 7.4 Map application outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `translated` | At least one entry applied and is returned with its equivalence class |
| `translated_multiple` | More than one entry applied and all are returned |
| `translated_ambiguous` | More than one entry with class `equivalent` applied, which cannot all be true |
| `unmatched_declared` | The map version declares the source concept unmatched |
| `source_not_covered` | The map version does not cover the source concept and declares no completeness over it |
| `unmapped_policy_applied` | No entry applied and the declared unmapped policy supplied a result |
| `map_version_unresolvable` | The map version could not be resolved |
| `condition_non_verdict` | A conditional entry's verdict was a non verdict from `Part 2` |
| `direction_unavailable` | The requested direction is not authored |
| `not_evaluated` | The translation was requested and not performed |

**P10-7.12 (MUST) Unmatched distinguished from not covered.** An implementation must distinguish a declared unmatched entry from the absence of coverage, since the first is an assertion by the map's author and the second is a gap in the map.

**P10-7.13 (MUST NOT) No empty result for an uncovered source.** An implementation must not return an empty result for a source concept the map does not cover, and must return `source_not_covered`.

**P10-7.14 (MUST) Direction unavailable, never inverted.** An implementation must return `direction_unavailable` where the requested direction is not authored and must not invert an authored direction.

### 7.5 Match outcomes

Closed enumeration.

| Value | Meaning |
|---|---|
| `same_entity` | Asserted to concern the same entity |
| `different_entity` | Asserted to concern different entities |
| `referred_for_adjudication` | The score falls within the declared referral band |
| `undetermined_threshold_absent` | No threshold is declared for the domain |
| `undetermined_insufficient_attributes` | The contributions share too few comparable attributes to evaluate |
| `undetermined_algorithm_unavailable` | The pinned algorithm version could not be resolved |
| `not_evaluated` | Matching was requested and not performed |

**P10-7.15 (MUST NOT) No undetermined match treated as different.** An implementation must not treat any undetermined outcome as `different_entity`, since a failure to match is not a finding that two records concern different entities.

**P10-7.16 (MUST) Referral is an outcome, not a delay.** An implementation must record `referred_for_adjudication` as an outcome with an owner and must not represent it as a pending computation.

**P10-7.17 (MUST) Insufficient attributes reported with the deficit.** An implementation must state which comparable attributes were absent when returning `undetermined_insufficient_attributes`.

### 7.6 Refusal codes

Open enumeration, extended under section 9.

| Value | Meaning |
|---|---|
| `applied` | The change was made |
| `applied_idempotent` | Already applied under the same key |
| `idempotency_conflict` | The key was seen with different arguments |
| `illegal_transition` | Not legal from the current state |
| `not_authorised` | `Part 7` denied the operation |
| `authorisation_unavailable` | `Part 7` could not be reached, and the operation was denied |
| `steward_absent` | The subject has no assigned steward |
| `document_identity_absent` | The version carries no `Part 1` document identity |
| `key_reuse_refused` | The key has denoted a different referent |
| `inactivation_reason_absent` | No inactivation reason was supplied |
| `successor_statement_absent` | Neither a successor nor its explicit absence was supplied |
| `equivalence_class_absent` | A map entry carries no equivalence class |
| `completeness_undeclared` | A map version's completeness over its source is undeclared |
| `retention_floor_not_passed` | Disposition or withdrawal was requested before the floor |
| `consumer_unregistered` | Distribution was requested to an unregistered consumer |
| `definition_uncited` | A concept carries no governed definition where one is required |
| `merge_without_match` | A merge was asserted with no supporting match assertion |
| `merge_in_referral_band` | A merge was asserted on a score requiring adjudication |
| `external_content_edit_refused` | An edit was attempted on externally authored content |
| `distribution_constraint_exceeded` | Delivery would exceed a recorded constraint |
| `malformed` | The request could not be interpreted |
| `system_fault` | A fault from section 7.8 |

**P10-7.18 (MUST) Authorisation denial distinguished from unavailability.** An implementation must distinguish `not_authorised` from `authorisation_unavailable`.

**P10-7.19 (MUST) Malformed distinguished from a determination.** An implementation must return `malformed` for an uninterpretable request and must not return a membership, map or match outcome. **Source.** `Part 7` clause P7-12.26 requires the same separation of a structural refusal from a substantive outcome.

### 7.7 What distinguishes each outcome from a negative

**P10-7.20 (MUST) Three properties exposed.** An implementation must expose the three properties in the following table with every membership outcome it returns.

| Outcome | Set fully determined | Value present in a referenced system | Caller may rely on a negative |
|---|---|---|---|
| `member` | yes | yes | not applicable |
| `member_inactive` | yes | yes | not applicable |
| `not_a_member` | yes | yes | yes |
| `code_unknown_to_system` | yes | no | no |
| `system_not_referenced` | not applicable | not applicable | no |
| `code_system_unresolvable` | no | unknown | no |
| `value_set_unresolvable` | no | unknown | no |
| `expansion_incomplete_truncated` | no | yes | no |
| `expansion_incomplete_withheld` | no | yes | no |
| `expansion_incomplete_fragment` | no | unknown | no |
| `binding_unpinned_unspecified` | no | unknown | no |
| `undecidable_case_rule` | no | unknown | no |
| `not_evaluated` | no | unknown | no |

Only one of the thirteen outcomes permits a caller to rely on a negative. Twelve do not, and a component that returns a boolean has told the caller that all twelve are the one that does.

### 7.8 System fault outcomes

Closed enumeration. These are the registry's own inability to proceed and are never a determination.

| Value | Meaning |
|---|---|
| `store_unavailable` | The record store could not be read or written |
| `dependency_unavailable` | A required component could not be reached |
| `snapshot_unavailable` | A required code system snapshot could not be taken |
| `artifact_unresolvable` | A release artifact's content address does not resolve |
| `internal_invariant_violated` | The registry detected a violation of its own invariants |

**P10-7.21 (MUST NOT) No fault reported as a determination.** An implementation must not report a system fault as a membership, expansion, map or match outcome.

**P10-7.22 (MUST) Invariant violation halts the subject.** An implementation must stop applying changes to the affected subject on detecting `internal_invariant_violated` and must raise the fault.

### 7.9 Propagation

**P10-7.23 (MUST) Outcome carried whole.** An implementation must return the outcome together with its qualifying counts and identifiers and must not return the outcome value alone.

**P10-7.24 (MUST NOT) No aggregation losing incompleteness.** An implementation must not aggregate determinations into a summary that loses the distinction between a complete determination and an incomplete one.

**P10-7.25 (MUST) Non result retained where unconsumed.** An implementation must retain a non result in the record of the affected determination where no consumer subscribes to it.

**P10-7.26 (MUST) Counts report non results as categories.** An implementation must report every non result value as its own category in any count it publishes over outcomes.

## 8. Observability and the audit record

### 8.1 Two records, one of them incomplete by construction

Section 3.2 established the position; this section states what follows for the audit record. The distribution record is complete because this component writes it. The consumption report set is incomplete because consumers write it. Every figure this component publishes about the state of the estate is therefore a figure about the intersection, and its honesty depends on stating the size of the part it cannot see.

**P10-8.1 (MUST) Completeness of each record declared.** An implementation must declare, for every population figure it publishes, whether the underlying record is complete by construction or incomplete by construction.

**P10-8.2 (MUST NOT) No estate figure without its unknown.** An implementation must not publish a figure about consumers without publishing the count of consumers whose state is unknown.

### 8.2 Grain

**P10-8.3 (MUST) Grain stated with every count.** An implementation must state the grain and the instant of computation with every count it reports.

**P10-8.4 (MUST) Concept counts state their state filter.** An implementation must state whether a concept count includes inactive concepts.

**P10-8.5 (MUST) Membership counts state their expansion.** An implementation must state the expansion identifier behind every membership count.

**P10-8.6 (MUST) Master counts state their record states.** An implementation must state which master record states a count of master records includes.

**P10-8.7 (MUST NOT) No count of entities that mixes kinds.** An implementation must not report one count spanning reference and master content without stating the split.

### 8.3 What must be recorded

**P10-8.8 (MUST) Every authoring act recorded.** An implementation must record every concept addition, inactivation, reactivation, designation change and relation assertion, at the grain of one record per act.

**P10-8.9 (MUST) Every version transition recorded.** An implementation must record every registration status and version state transition, at the grain of one record per transition.

**P10-8.10 (MUST) Every determination recorded.** An implementation must record every membership determination, at the grain of one determination per value per value set version per request.

**P10-8.11 (MUST) Every expansion recorded.** An implementation must record every expansion it computes, including truncated, partial and failed expansions.

**P10-8.12 (MUST) Every translation recorded.** An implementation must record every map application, at the grain of one record per source concept per map version per request.

**P10-8.13 (MUST) Every contribution recorded.** An implementation must record every contribution it receives, whether or not any value was selected.

**P10-8.14 (MUST) Every match and merge recorded.** An implementation must record every match assertion, merge assertion and unmerge, at the grain of one record per assertion.

**P10-8.15 (MUST) Every survivorship determination recorded.** An implementation must record every survivorship determination, at the grain of one record per attribute per evaluation.

**P10-8.16 (MUST) Every withholding recorded.** An implementation must record every withholding, at the grain of one record per delivered set per basis.

**P10-8.17 (MUST) Every distribution and report recorded.** An implementation must record every distribution per consumer and every consumption report received.

**P10-8.18 (MUST) Every refusal recorded.** An implementation must record every refused operation with its refusal code.

### 8.4 What must be reconstructable

**P10-8.19 (MUST) Content of a version at an instant.** A reader must be able to reconstruct the exact concept set, designations and relations of any code system version as it stood at any past instant.

**P10-8.20 (MUST) Membership of a value set at an instant.** A reader must be able to reconstruct the membership a value set version resolved to at any past instant, from the expansion recorded at that instant.

**P10-8.21 (MUST) Inputs of a determination.** A reader must be able to reconstruct every input of any recorded determination, resolved to versions and digests.

**P10-8.22 (MUST) Reason a concept ceased to be usable.** A reader must be able to reconstruct why a concept was inactivated, what succeeded it and under what association kind.

**P10-8.23 (MUST) Provenance of a presented master value.** A reader must be able to reconstruct which contribution supplied any presented master attribute value, from which source, asserted at which instant, and under which survivorship rule.

**P10-8.24 (MUST) Basis of a merge.** A reader must be able to reconstruct the match assertion, basis, score and threshold behind any merge, and the adjudicating party where one adjudicated.

**P10-8.25 (MUST) Withheld extent of a delivery.** A reader must be able to reconstruct how many members were withheld from any delivery, on what basis, and under whose authorisation.

**P10-8.26 (MUST) Holding of a consumer at an instant.** A reader must be able to reconstruct what a consumer reported holding at any past instant, and must be able to establish that a consumer reported nothing.

**P10-8.27 (MUST NOT) No reconstruction dependent on this component running.** An implementation must not require its own runtime to be available for any reconstruction in section 8.4, beyond the components holding the pinned targets.

### 8.5 Signals

Each signal names a population this component can count and cannot remedy.

**P10-8.28 (MUST) Unreported consumer population.** An implementation must expose the count and identity of registered consumers in the four unreported states of section 5.8.

**P10-8.29 (MUST) Stale holding population.** An implementation must expose the consumers whose reported holding is behind the current published version, per subject.

**P10-8.30 (MUST) Unpinned value set population.** An implementation must expose every published value set version whose code system version binding is unpinned.

**P10-8.31 (MUST) Withheld dependent set population.** An implementation must expose every value set version whose expansion carries a non zero withheld count for any consumer.

**P10-8.32 (MUST) Incomplete content population.** An implementation must expose every code system version whose content completeness is other than complete.

**P10-8.33 (MUST) Uncited version population.** An implementation must expose every version with no recorded retention floor.

**P10-8.34 (MUST) Unresolved survivorship conflict population.** An implementation must expose every master attribute in unresolved conflict with its steward.

**P10-8.35 (MUST) Disputed record population.** An implementation must expose every master record in `disputed`.

**P10-8.36 (MUST) Referral backlog population.** An implementation must expose every match referred for adjudication and not yet adjudicated, with its age.

**P10-8.37 (MUST) Provisional record population.** An implementation must expose every master record in `provisional`, since each denotes an entity whose existence rests on one source's assertion.

**P10-8.38 (MUST) Inactive member population.** An implementation must expose, per published value set version, the count of members whose concepts are inactive.

**P10-8.39 (MUST) Successorless inactive population.** An implementation must expose every inactive concept with no successor and no recorded statement that none exists.

**P10-8.40 (MUST) Affected determination population.** An implementation must expose the count of recorded determinations whose cited inputs have since changed.

**P10-8.41 (SHOULD) Divergent expansion signal.** An implementation should expose every case in which a consumer reported an expansion digest differing from the digest this component computed for the same value set version and code system versions.

### 8.6 The evidence package

**P10-8.42 (MUST) Package assemblable for a determination.** An implementation must be able to assemble, for any recorded determination, a package containing the determination, the expansion, the value set version definition, every code system version's relevant content, every withholding record and the authorisation reference.

**P10-8.43 (MUST) Package assemblable for a master value.** An implementation must be able to assemble, for any presented master attribute value, a package containing every contribution for that attribute, the survivorship determination, every match and merge assertion affecting the record and the record's state history.

**P10-8.44 (MUST) Package states what it omits.** An implementation must state, in every package, every element it could not include and why.

**P10-8.45 (MUST) Package integrity protected.** An implementation must integrity protect every package by a means governed by `Part 3`.

### 8.7 Retention

**P10-8.46 (MUST) Retention governed elsewhere, floors owned here.** An implementation must obtain retention schedules from `Part 1` and must own the retention floor of section 3.15.

**P10-8.47 (MUST NOT) No disposition of a determination record with its version retained.** An implementation must not dispose of a determination record while the version it cites is retained, since the version without the determinations that used it does not answer the question the retention exists for.

**P10-8.48 (MUST) Legal hold refuses disposition.** An implementation must refuse every disposition act affecting content under a legal hold and must record the refusal.

### 8.8 What cannot be changed

**P10-8.49 (MUST NOT) No alteration of a published version's content.** An implementation must not alter the content of a published version.

**P10-8.50 (MUST NOT) No alteration of a determination, expansion, contribution or assertion.** An implementation must not alter a recorded determination, expansion, contribution, match assertion, merge assertion, survivorship determination, withholding record, distribution record or consumption report.

**P10-8.51 (MUST NOT) No removal of a key from the register.** An implementation must not remove a key from the register of keys ever assigned in a code system.

## 9. Extension model

### 9.1 Closed sets and open sets

**P10-9.1 (MUST) Closed sets not extended.** An implementation must not extend the following: registration statuses, version states, concept states, inactivation reasons, expansion states, master record states, merge assertion states, consumption report states, membership outcomes, expansion outcomes, map application outcomes, match outcomes, system fault outcomes, equivalence classes, successor association kinds, withholding bases, match bases and existence bases.

**P10-9.2 (MUST) Open sets extended only through a registry.** An implementation must extend the following only through the registries of section 9.2: code systems, value sets, maps, master domains, relation kinds, designation kinds, intensional rule kinds, survivorship rule kinds, distribution constraint kinds, key schemes, marking vocabularies, source systems and refusal codes.

**P10-9.3 (MUST) Content enumerations open by construction.** An implementation must treat the concept membership of every code system as open by construction and must not close a code system against future concepts.

The outcomes and states are closed because they are the vocabulary in which this component's record speaks, and a consumer that meets an unlisted membership outcome has met a value no reader of section 7.7 can classify. The kinds are open because the whole subject of the component is the governance of content it did not author, and a component that cannot admit a new relation kind cannot hold the content that has one.

### 9.2 Registry mechanics

**P10-9.4 (MUST) Registration before use.** An implementation must require every open set member to be registered before content or an operation uses it.

**P10-9.5 (MUST) Definition mandatory at registration.** An implementation must require a definition of every registered kind's meaning and must refuse a registration with none.

**P10-9.6 (MUST) Registration attributable.** An implementation must record the registering party, the instant and the authorising decision for every registration.

**P10-9.7 (MUST NOT) No meaning change under a registered identifier.** An implementation must not alter the meaning of a registered kind and must express a change as a new kind.

**P10-9.8 (MUST) Retirement of a kind recorded, content retained.** An implementation must retain content using a retired kind and must not remove the kind from the register.

### 9.3 Relation kind registry

**P10-9.9 (MUST) Transitivity declared per kind.** An implementation must record a transitivity declaration of transitive, non transitive or undeclared for every relation kind.

**P10-9.10 (MUST) Hierarchical or associative declared.** An implementation must record whether a relation kind is hierarchical or associative and must refuse a closure request over an associative kind.

**P10-9.11 (MUST) Symmetry declared.** An implementation must record whether a relation kind is symmetric and must not infer the inverse of a non symmetric kind.

**P10-9.12 (MUST) Inverse named where one exists.** An implementation must name the inverse kind of every relation kind that has one and must not derive an inverse that is unnamed.

### 9.4 Intensional rule kind registry

**P10-9.13 (MUST) Rule kind semantics registered.** An implementation must register, for every intensional rule kind, the relation kind it traverses where it traverses one, its closure mode and whether it is inclusive or exclusive.

**P10-9.14 (MUST) Rule kind confluence declared.** An implementation must declare whether a rule kind is order sensitive with respect to other kinds and must refuse to register one that is.

**P10-9.15 (MUST) Rule kind bound declared.** An implementation must declare the traversal or evaluation bound applicable to each rule kind.

### 9.5 Survivorship rule kind registry

**P10-9.16 (MUST) Rule kind inputs registered.** An implementation must register, for every survivorship rule kind, the contribution attributes it consults, including which instant it uses.

**P10-9.17 (MUST) Tie behaviour registered.** An implementation must register the tie behaviour of every survivorship rule kind and must require it to be report rather than break.

**P10-9.18 (MUST NOT) No source order rule kind.** An implementation must not register a survivorship rule kind whose input is the position of a source in a list.

### 9.6 Consumer, source and constraint registries

**P10-9.19 (MUST) Source systems registered.** An implementation must register every contributing source system with its steward and its declared assertion semantics before accepting a contribution from it.

**P10-9.20 (MUST) Consumer capability registered.** An implementation must register the reporting capability of every consumer.

**P10-9.21 (MUST) Constraint kinds registered.** An implementation must register every distribution constraint kind with the restriction it expresses.

**P10-9.22 (MUST) Marking vocabulary registered.** An implementation must register every marking vocabulary used to express withholding.

### 9.7 Composition

**P10-9.23 (MUST) Supplements composed, not merged.** An implementation must express a local extension of externally authored content as a supplement with its own identity and must not merge it into the base version.

**P10-9.24 (MUST) Composed value set records its constituents.** An implementation must record every value set version a value set version draws on and must not flatten the composition.

**P10-9.25 (MUST NOT) No composed map without authorship.** An implementation must not register a map version as composed of two others without an authoring act asserting the composed entries.

**P10-9.26 (MUST) Composition depth bounded.** An implementation must declare a maximum composition depth for value sets and must refuse a definition exceeding it.

## 10. Standards and specifications

### 10.1 How the citations in this part are to be read

Each entry states what the source supplies, the edition established as current at the date of this part, and whether this part's account rests on specification text or on secondary sources. Section 13.1 lists the sources not obtained in full text.

This part's subject has a great deal of usable material and almost none of it is a standard for a registry of both kinds of content. The registration apparatus comes from a metadata registry standard that says nothing about codes. The concept and relation model comes from a knowledge organisation standard that says nothing about registration. The membership and expansion model comes from a domain specification in healthcare. The master data side has a quality standard and an identifier standard and, for matching and survivorship, only practice.

**P10-10.1 (MUST) Cited edition recorded.** An implementation must record the edition or version of every external standard it relies upon and must not cite a standard without its edition.

**P10-10.2 (MUST) Basis marked.** An implementation must record, for every control it adopts from a source named in this section, whether the basis is specification text or practice.

**P10-10.3 (MUST) External code system edition pinned.** An implementation must record the publisher's own edition designation for every externally authored code system version it holds, in addition to its own version identity.

### 10.2 The registration apparatus: ISO/IEC 11179

**Supplies.** The registration authority, the submitter, the steward, the registration status with its lifecycle and documentation categories, the conditions for progression, and the required procedures for submission, progression, harmonisation, modification, retirement and administration. Part 3 supplies the metamodel of registry common facilities and Part 6 the registration procedure. The fourth edition of Part 6 is dated 2023 and cancels the 2015 third edition.

**Does not supply.** Anything about codes as such, about value sets, about expansion, about maps, or about master data. It governs the registration of items and is silent on the semantics of what is registered.

**Basis.** Specification text for the Recorded status, the progression conditions and the quality caveat, quoted at clauses P10-5.7 to P10-5.9. Secondary for the full status enumeration, per section 13.1.

### 10.3 The concept and relation model: SKOS

**Supplies.** The concept scheme, the concept as the unit of identity distinct from its labels, the three designation kinds, the separation of direct hierarchical relations from their transitive closure, the associative relation and its disjointness from the hierarchical closure, and the five mapping properties with their transitivity and disjointness declarations. W3C Recommendation, 2009.

**Does not supply.** Registration, versioning, expansion, or any notion of a governed release. A concept scheme in SKOS has no versions.

**Basis.** Specification text for the non transitivity of the hierarchical properties, the convention that the transitive properties are for inference and not assertion, the transitivity of exact match and the non transitivity of close match, and the disjointness of the associative relation from the hierarchical closure.

### 10.4 The membership and expansion model: HL7 FHIR terminology

**Supplies.** The separation of a code system from a value set, the intensional and extensional definition of a value set, the expansion as an artifact distinct from the definition, the declaration of a code system's content completeness, the binding of an element to a value set at a declared strength, the concept map with equivalence classes, and the treatment of inactive concepts.

**Does not supply.** A general purpose registry. Its model is embedded in a healthcare interoperability specification and its identity conventions are adopted here at the level of pattern.

**Basis.** Secondary for this session. Section 13.1 records that the specification was not read in this session and that the account rests on the author's general knowledge of it.

### 10.5 Code list practice: ISO 3166 and its reuse of a code element

**Supplies.** The evidence for clause P10-3.21. The alpha-2 code element CS denoted Czechoslovakia until 1993 and was assigned to Serbia and Montenegro from 2003, and ISO's own register records the reuse in terms. The successor code register then assigned CSHH to Serbia and Montenegro although CSHH already denoted Czechoslovakia, and the collision was corrected in a subsequent newsletter to CSXX. Codes deleted from the standard are now transitionally reserved for at least fifty years before reassignment; a five year period was in force at the time of the reuse.

**Does not supply.** Any general rule. It is a single instance, and it is cited because it is an instance in which an international standards body operating a reservation regime nonetheless produced a code element denoting two different referents in two different intervals, and then produced a collision in the very register designed to disambiguate them.

**Basis.** Specification register text for the reuse and the reservation interval. Secondary for the newsletter history.

### 10.6 Master data: ISO 8000 and identifier schemes

**Supplies.** ISO 8000 supplies a vocabulary for data quality and, in its master data parts, a message format for characteristic data and requirements for identifiers. ISO 6523 and the legal entity identifier of ISO 17442 supply identifier schemes for organisations.

**Does not supply.** Matching, merging, survivorship or stewardship of a master record. No consulted standard specifies any of them.

**Basis.** Secondary. Section 13.1 records that no part of ISO 8000 was obtained.

### 10.7 Named conflicts

| Conflict | Position A | Position B | Resolution | Reason |
|---|---|---|---|---|
| Reuse of a key after a reservation interval | ISO 3166 permits reassignment after a transitional reservation, now fifty years | This part, clause P10-3.21: never | This part | A reservation interval bounds the exposure of systems that live shorter than the interval. It does nothing for a determination made over a span containing both referents, and this standard's retention obligations under `Part 1` routinely produce such spans |
| Whether hierarchical relations are transitive | SKOS declares them non transitive by convention, and provides separate transitive properties for inference | This part, clauses P10-3.51 and P10-6.22: the declaration is mandatory and the closure must be requested | This part extends rather than departs | SKOS states a convention; a registry that leaves it as a convention will have content that relies on it and content that does not, with no way to tell which |
| Whether an expansion may be reused | Practice reuses a cached expansion across code system versions for performance | This part, clause P10-3.40: never across different versions | This part | The saving is real and the failure is silent. A cached expansion is the mechanism by which a value set that changed appears not to have |
| Whether a membership answer may be boolean | Widespread practice and most interfaces return a boolean | This part, clause P10-3.106: a boolean may be a projection over a recorded outcome and never the record | This part | Section 7.7 shows twelve of thirteen outcomes are not a reliable negative. `Part 7` takes the same position on its own two valued interface and records the same open question |
| Whether a filtered set may be delivered as complete | Practice filters by authorisation and delivers what remains | This part, clause P10-3.44: withheld members are marked and counted | This part, as required of it by `Part 2`, `Part 3` and `Part 7` | A consumer computing non membership from a filtered set is wrong in the direction of refusing valid values, and nothing reports it |

### 10.8 What none of the standards supplies

**P10-10.4 (MUST) Requirements of this part alone identified.** An implementation must treat the following as requirements of this part alone, no consulted standard supplying them: the consumption report and the unreported population; the retention floor coupled to citing determinations; the prohibition on key reuse without exception; the membership outcome enumeration and its distinctions among incompleteness causes; the prohibition on automatic successor substitution; the withheld member marking as a condition of delivery; the existence basis of a master record; the prohibition on survivorship by source order; the requirement that a merge be an assertion with an unmerge; and the refusal of retrospective revaluation.

## 11. Anti patterns

### 11.1 The reused code

**Mechanism.** A code is withdrawn and later assigned to a different referent, after a reservation interval judged sufficient.

**Evidence.** ISO 3166-1 assigned CS to Czechoslovakia until 1993 and to Serbia and Montenegro from 2003, and ISO's register records the reuse. Its successor register then assigned CSHH to Serbia and Montenegro although the same code already denoted Czechoslovakia, and the collision required correction.

**Consequence.** A determination over data spanning both intervals cannot resolve the code without knowing the instant, and no interface that takes a code alone carries the instant. Every aggregate over the span is wrong and nothing fails.

**P10-11.1 (MUST NOT) No reuse.** An implementation must not reuse a key, per clause P10-3.21.

### 11.2 The unknown code returned as not a member

**Mechanism.** A membership check receives a code the code system does not contain and returns that it is not a member of the value set.

**Evidence.** The two valued interface is near universal and has no other value available.

**Consequence.** A wrong code and a valid code outside the set are the same answer, so a code system version that is behind looks exactly like a correct refusal. The gap is permanently invisible, which is the mechanism `Part 7` section 11.2 names for its own subject.

**P10-11.2 (MUST NOT) No unknown as non membership.** An implementation must not return non membership for a code unknown to a referenced code system version.

### 11.3 The silently filtered set

**Mechanism.** A consumer receives the members of a set it is authorised to see, with no indication that others exist.

**Evidence.** No consulted standard requires the withheld extent to be reported. `Part 2`, `Part 3` and `Part 7` each require the restricting component to mark rather than remove.

**Consequence.** The consumer computes non membership from an incomplete set and refuses values that are valid. The refusal looks like correct enforcement of a reference set.

**P10-11.3 (MUST) Withheld marked and counted.** An implementation must mark and count every withheld member, per clause P10-3.44.

### 11.4 The cached expansion

**Mechanism.** An expansion is computed once and reused, because expansion is expensive and the value set version has not changed.

**Evidence.** The value set version genuinely has not changed. Where its code system binding is unpinned, its membership has.

**Consequence.** Two consumers holding the same value set version compute different memberships and both are right. Neither can discover the divergence, because the only identity either holds is the value set version, which matches.

**P10-11.4 (MUST NOT) No expansion reuse across code system versions.** An implementation must not answer from an expansion computed against different code system versions.

### 11.5 The intensional set with an unpinned binding

**Mechanism.** A value set selects the descendants of a concept and does not pin the code system version, so its membership tracks the code system.

**Evidence.** This is the intended behaviour of an intensional definition and is often the reason for choosing one.

**Consequence.** The set changes with no change to it, no event, no version increment and no digest change. Whether this is a feature or a defect depends entirely on whether the consumers were told, and nothing tells them.

**P10-11.5 (MUST) Unpinned bindings exposed.** An implementation must expose every published value set version with an unpinned binding.

### 11.6 The automatic successor

**Mechanism.** An inactive code is silently replaced by its successor so that existing data continues to resolve.

**Evidence.** Successor associations carry kinds that differ in exactly this respect, and a `possibly_equivalent_to` successor asserts uncertainty.

**Consequence.** A recorded uncertainty becomes a recorded fact, and a replacement chosen for future use is applied to the past. The original code is no longer retrievable from the substituted record, so the substitution cannot be undone.

**P10-11.6 (MUST NOT) No automatic substitution.** An implementation must not substitute a successor concept in a determination.

### 11.7 The closure assumed

**Mechanism.** A hierarchy query returns descendants at every depth, or only immediate children, according to whatever the implementation does, and the caller assumes the other.

**Evidence.** SKOS separates the two deliberately and states that the transitive properties are for inference rather than assertion, precisely because the two questions differ.

**Consequence.** A value set defined as the descendants of a concept has a membership that differs by orders of magnitude depending on which was meant, and both are plausible.

**P10-11.7 (MUST) Closure declared on both sides.** An implementation must require the closure mode to be declared by the caller and by the rule kind.

### 11.8 The inverted map

**Mechanism.** A source to target map is used in reverse because a translation is needed in the other direction and the entries look symmetric.

**Evidence.** Four of the seven equivalence classes do not invert without changing the assertion.

**Consequence.** A narrower to broader entry, inverted, asserts that a broad concept may be substituted for a narrow one, which is the direction in which substitution loses information and gains false precision.

**P10-11.8 (MUST NOT) No inversion.** An implementation must not answer a reverse translation from a forward map.

### 11.9 The chained map

**Mechanism.** A map from A to B and a map from B to C are composed to translate A to C.

**Evidence.** SKOS declares close match non transitive while exact match is transitive, so chaining is valid for some relations and invalid for others; published analysis of SKOS mapping quality records that asserting relations through composed mappings produces inconsistency and unintended claims about another scheme.

**Consequence.** Two inexact mappings compose into an assertion nobody authored, and the resulting entry carries an equivalence class that was computed rather than asserted.

**P10-11.9 (MUST NOT) No composition at application time.** An implementation must not chain map versions.

### 11.10 The golden record as a record

**Mechanism.** Survivorship output is stored as the master record and the contributions behind it are discarded or archived out of reach.

**Evidence.** The presented value is the output of a rule over contributions and has no independent source.

**Consequence.** The provenance of every presented value is lost, a survivorship rule change cannot be applied retrospectively, and a wrong value cannot be traced to the source that supplied it.

**P10-11.10 (MUST) Golden view a projection only.** An implementation must expose the presented value as a projection with its contributions retrievable.

### 11.11 The destructive merge

**Mechanism.** Two records are found to concern one entity and one is deleted.

**Evidence.** No consulted standard requires reversibility of a merge.

**Consequence.** The merge cannot be undone when it turns out to be wrong, which it will be for a proportion of probabilistic matches equal to one minus the precision at the threshold. Every reference to the deleted identifier fails, and the contributions that were only in the deleted record are gone.

**P10-11.11 (MUST NOT) No deletion on merge.** An implementation must not delete an absorbed record or its identifier.

### 11.12 The survivorship by source precedence list

**Mechanism.** A configured ordering of sources decides which value is presented.

**Evidence.** This is the fifth part of this standard to encounter resolution by declaration order.

**Consequence.** The rule is invisible in the output, changes when the list is reordered for an unrelated reason, and cannot express that one source is authoritative for an address and another for a name.

**P10-11.12 (MUST NOT) No source order survivorship.** An implementation must not determine survivorship by source list position.

### 11.13 The distribution taken for consumption

**Mechanism.** The registry reports the current version as adopted because it was published and made available.

**Evidence.** Section 3.2. The registry writes the distribution record and consumers write the consumption reports.

**Consequence.** A reference data programme reports full adoption while an unmeasured portion of the estate runs on a superseded set. The figure is not wrong about what the registry did; it is wrong about what it claims.

**P10-11.13 (MUST NOT) No currency claim without reports.** An implementation must not report currency in a way that treats unreported consumers as current.

### 11.14 The consumer that cannot report, excluded from the count

**Mechanism.** Consumers unable to report are removed from the unreported population, since counting them is unactionable.

**Evidence.** The population exists to measure what is unknown.

**Consequence.** The figure improves and the knowledge does not. The estate's unknown portion is now unknown and uncounted.

**P10-11.14 (MUST NOT) No exclusion of the incapable.** An implementation must not exclude a consumer unable to report from the unreported population.

### 11.15 The retrospective revaluation

**Mechanism.** A code is inactivated and every determination that cited it is recomputed, so that the record is consistent with current content.

**Evidence.** The determinations were correct when made against the content then in force.

**Consequence.** The record no longer says what was determined, and a determination that was right becomes a determination that appears wrong. Where the determination supported an authorisation or an eligibility, the evidence for it is destroyed.

**P10-11.15 (MUST NOT) No revaluation.** An implementation must not recompute a recorded determination when its inputs change.

### 11.16 The local edit of external content

**Mechanism.** A code is added to an externally authored code system because it is needed and the publisher is slow.

**Evidence.** The publisher's next release does not contain it, and may contain the same key with a different meaning.

**Consequence.** The local content is silently destroyed at the next release, or it collides. Every determination made in the interval cited a version that the publisher never issued and that cannot be reproduced from the publisher's artifacts.

**P10-11.16 (MUST NOT) No edit of external content.** An implementation must not alter an externally authored code system version.

### 11.17 The value set that is a code system

**Mechanism.** A value set is authored with members that exist nowhere else, so it defines the concepts it selects.

**Evidence.** The distinction between the two is the basis of the entire model.

**Consequence.** The concepts have no definition, no state, no successor relations and no authority, and nothing can be mapped to them. They cannot be inactivated, because a value set version is immutable and a member removal is a new version with no statement about what happened to the member.

**P10-11.17 (MUST NOT) No concept definition in a value set.** An implementation must not permit a value set to define a concept.

### 11.18 The designation as the identity

**Mechanism.** Content refers to concepts by their labels, or a change of label is treated as a new concept.

**Evidence.** SKOS makes the concept the unit of identity and the label an attached designation, and permits multiple designations per concept per language.

**Consequence.** A translation, a spelling correction or a change of preferred term appears as a content change, and two systems holding the same concept under different preferred labels appear to disagree.

**P10-11.18 (MUST NOT) No identity in a designation.** An implementation must not treat a designation as the identity of a concept.

### 11.19 The fragment treated as the system

**Mechanism.** A subset of an external code system is loaded, because the full system is large or licensed, and membership is determined against it.

**Evidence.** FHIR carries a content completeness declaration on a code system for exactly this case.

**Consequence.** Every code outside the loaded fragment returns not a member or unknown, and the answer is indistinguishable from a correct one.

**P10-11.19 (MUST) Completeness declared and honoured.** An implementation must declare content completeness and must refuse a non membership determination against incomplete content.

### 11.20 The stewardship that is a permission

**Mechanism.** Stewardship of a subject is implemented as the right to change it.

**Evidence.** `Part 7` section 11.19 names the same anti pattern from the authorisation side.

**Consequence.** Accountability and entitlement become one, so removing someone's access removes their accountability, and the population of subjects with an accountable steward and no permissions cannot exist.

**P10-11.20 (MUST NOT) No entitlement from stewardship.** An implementation must not treat a stewardship assignment as conferring permission.

### 11.21 The master identifier that is a source identifier

**Mechanism.** The identifier of the system of record is adopted as the master identifier, since it already exists and is already referenced.

**Evidence.** The source assigns it under its own rules, reuses it under its own rules, and may retire the system.

**Consequence.** The estate's identity for an entity is controlled by a system that did not agree to the obligation, and a source that reuses its identifiers reuses the master identifier.

**P10-11.21 (MUST NOT) No source identifier as master.** An implementation must not adopt a source identifier as a master identifier.

### 11.22 The match threshold that is never examined

**Mechanism.** A probabilistic matching threshold is set at implementation and never revisited, and the assertions it produced are never re-examined when it changes.

**Evidence.** The threshold determines the false merge rate directly.

**Consequence.** Nobody can state how many merged records are wrongly merged, and a threshold change silently means that the existing population was matched under a rule that no longer applies.

**P10-11.22 (MUST) Threshold change surfaces the affected population.** An implementation must report every assertion whose verdict would change before a threshold change takes effect.

### 11.23 The provisional record presented as verified

**Mechanism.** A record created from one contribution is presented identically to a confirmed one.

**Evidence.** Section 3.10 requires an existence basis.

**Consequence.** An entity that may not exist is transacted with, and the estate's count of entities in a domain includes an unknown number of records that denote nothing.

**P10-11.23 (MUST) Existence basis presented.** An implementation must present the existence basis with every master record it exposes.

### 11.24 The transitive merge nobody asserted

**Mechanism.** A matches B and B matches C, so all three are one record.

**Evidence.** The A to C pair was never evaluated.

**Consequence.** Two entities that are demonstrably different are merged through an intermediary, and the assertion that joined them does not exist, so it cannot be reviewed or withdrawn.

**P10-11.24 (MUST) Transitivity declared or refused.** An implementation must declare whether merge is transitive within a domain and must not merge transitively where it does not.

## 12. Boundaries with other parts

Every subsection states what this component delegates, what it must not absorb, the naive conflation, and the reciprocal this part requires of the other. Subsection numbers correspond to part numbers; there is no 12.10 because this is Part 10.

### 12.1 Boundary with Part 1, controlled documents and records

**Delegated.** The approval, effective date, supersession as a document, retention schedule, disposition and point in time citation of every published version of this component's content.

**Must not absorb.** Document lifecycle. A code system version is a controlled document and this component does not govern its approval.

**Naive conflation.** This component implements its own approval and effective dating, because publication needs both, so a version has two effective dates that disagree and the question of which content was in force on a date has two answers.

**Reciprocal.** `Part 1` must declare that it owns document identity, approval, effective date and retention schedule for the versions this component publishes, that a determination record, expansion, contribution and assertion of this component are records in its sense and not revisable, and that its point in time citation resolves to the version in force at the cited instant rather than the current one.

**P10-12.1 (MUST) Document identity obtained.** An implementation must obtain a `Part 1` document identity for every version it publishes and must refuse publication without one.

**P10-12.2 (MUST NOT) No local effective dating.** An implementation must not maintain an effective date for a published version independently of `Part 1`.

**P10-12.3 (MUST) Determinations are records.** An implementation must treat every determination, expansion, contribution, match assertion, merge assertion and survivorship determination as a record in the `Part 1` sense and must not revise one.

### 12.2 Boundary with Part 2, business rules and constraint evaluation

**Delegated.** Every constraint whose evaluation is not a membership, relation or map determination over this component's own content, including the conditions attached to conditional map entries.

**Must not absorb.** Constraint evaluation. A membership determination is not a rule evaluation, and a rule that consults a membership is `Part 2`'s.

**Naive conflation.** A rule about which values are permitted in which circumstances is authored as a value set, so the value set acquires a condition and becomes a rule set with no verdict vocabulary and no non result.

**Reciprocal.** `Part 2` must declare that it owns rule identity, evaluation and verdicts, that it obtains membership determinations from this component by pin rather than enumerating members in a rule, that it accepts every outcome of section 7.2 without collapsing one to another, and that it identifies what it restricted as withheld rather than removing it, per clause P2-12.18 which this part discharges at section 3.8.

**P10-12.4 (MUST NOT) No conditional membership.** An implementation must not make the membership of a value set version conditional on a fact outside its own content, and must express such a condition as a `Part 2` rule over a membership determination.

**P10-12.5 (MUST) Conditional map verdicts obtained.** An implementation must obtain the `Part 2` verdict for every conditional map entry and must not evaluate the condition itself.

**P10-12.6 (MUST NOT) No non verdict absorbed.** An implementation must not convert a `Part 2` non verdict into a membership or map outcome that asserts a determination.

### 12.3 Boundary with Part 3, provenance and audit ledger

**Delegated.** The evidentiary chain, the integrity mechanism and the reconstruction of a determination that spans components.

**Must not absorb.** The role of system of record for reconstruction across components.

**Naive conflation.** This component's own event log is treated as the audit record, so a determination that relied on a membership can be reconstructed only as far as this component's boundary.

**Reciprocal.** `Part 3` must declare that it owns the evidentiary chain, that this component owns the authoritative statement of what content was published and what determination was made, that it retains the basis of a determination for at least as long as the determination, and that it identifies restricted content as withheld rather than removing it, per clause P3-12.18 which this part discharges at section 3.8.

**P10-12.7 (MUST) Events emitted to the ledger.** An implementation must emit every event of section 4.7 to `Part 3`.

**P10-12.8 (MUST NOT) No self assertion as the chain.** An implementation must not represent its own records as the evidentiary chain of a determination made by another component.

**P10-12.9 (MUST) Retention floor notified.** An implementation must accept notification from `Part 3` that a determination citing one of its versions is retained beyond that version's recorded retention floor, and must raise the floor.

### 12.4 Boundary with Part 4, metadata and model repository

**Delegated.** The meaning of every governed term, the data element and its conceptual domain, lineage and impact analysis.

**Must not absorb.** Meaning. A concept's definition text states what the concept denotes within its code system; the governed business meaning of the element that carries it is `Part 4`'s.

**Naive conflation.** The code system becomes the place where business meaning is recorded, because the definitions are there and the authors are there, so meaning is versioned by the code system's release cycle and cannot be cited by anything that is not a code.

**Reciprocal.** `Part 4` must declare that it owns the governed definition and its lineage, that a value domain's permissible values are held here and referenced by pin rather than enumerated there, that it accepts a citation from a concept to a definition, and that it exposes the reverse index so that a definition change surfaces the concepts carrying it.

**P10-12.10 (MUST) Concept cites its governed definition.** An implementation must record the `Part 4` definition reference of every concept whose meaning is a governed term, and must refuse publication of such a concept without one.

**P10-12.11 (MUST NOT) No governed meaning authored here.** An implementation must not author or version a governed business definition.

**P10-12.12 (MUST) Reverse index exposed.** An implementation must expose, for every `Part 4` definition, the concepts and value set versions citing it, so that `Part 4` can perform impact analysis.

**P10-12.13 (MUST) Definition change surfaces as a concept review.** An implementation must record a `Part 4` definition change affecting a concept as requiring a steward review and must not alter the concept automatically.

### 12.5 Boundary with Part 5, decision engine

**Delegated.** Any selection among candidate values that is a business outcome rather than a determination over this component's content.

**Must not absorb.** Business selection.

**Naive conflation.** Survivorship becomes a decision engine, or a decision engine becomes survivorship, because both select one value from several. Survivorship selects among assertions about one fact by a declared data rule; a decision selects an outcome from inputs by a governed business rule.

**Reciprocal.** `Part 5` must declare that it owns business outcome selection, that it obtains the admissible values of any input domain from this component by pin, and that it does not hold a value set.

**P10-12.14 (MUST) Survivorship distinguished from decision.** An implementation must record every survivorship determination as a data provenance determination and must not present it as a business decision.

**P10-12.15 (MUST NOT) No business selection performed.** An implementation must not select among candidate values where the selection depends on a governed business rule, and must obtain the selection from `Part 5`.

**P10-12.16 (MUST) Domain supplied by pin.** An implementation must supply the admissible values of an input domain to `Part 5` as a pinned value set version.

### 12.6 Boundary with Part 6, workflow and process orchestration

**Delegated.** The sequencing of the steps by which content is authored, reviewed, published and distributed, where that sequencing is a defined process.

**Must not absorb.** Process control flow. The registration status transitions of section 5.2 are state changes of a registered subject and not a process definition.

**Naive conflation.** The registration lifecycle is implemented as a workflow, so the state of a code system version is a process instance's position and cannot be read without the process engine.

**Reciprocal.** `Part 6` must declare that it owns process control flow, that a registration status is a fact held here and not a process state held there, and that it obtains the admissible values of any process data element from this component by pin.

**P10-12.17 (MUST) Status is a fact, not a position.** An implementation must hold every registration status and version state as its own fact and must not derive one from a process instance's position.

**P10-12.18 (MUST NOT) No process definition held.** An implementation must not define the control flow of an authoring or publication process.

### 12.7 Boundary with Part 7, policy decision point and authorisation

**Delegated.** Every decision on whether a party may read, author, publish, withdraw, merge, unmerge or adjudicate.

**Must not absorb.** Authorisation. This component applies a decision and does not make one.

**Naive conflation.** This component filters what a consumer may see and reports the filtered set as the set, which is the silent redaction `Part 7` section 11.9 names.

**Reciprocal, and its discharge.** `Part 7` section 12.10 requires this part to declare four things. Each is declared and the clause discharging it is named. That it owns value set membership and versioning: clauses P10-1.1 to P10-1.5. That it retains every superseded version for at least as long as the longest retained decision that read it: section 3.15, clauses P10-3.96 to P10-3.98. That it does not remove or reuse member keys: clauses P10-3.21 and P10-3.22. That it reports the addition or removal of a member so that target completeness can be checked: clause P10-4.44, with the full membership exposure of clause P10-6.63 supporting `Part 7` clause P7-12.28.

**P10-12.19 (MUST) Authorisation obtained per act.** An implementation must obtain an authorisation decision at the instant of every operation section 4.1 requires one for, and must not rely on a decision obtained earlier for a different act.

**P10-12.20 (MUST NOT) No authorisation decision rendered.** An implementation must not decide whether a party may read or change its content.

**P10-12.21 (MUST) Withholding marked, per the obligation.** An implementation must mark and count every member withheld on the basis of an authorisation decision, per clause P10-3.44, and must record the decision reference on the withholding record.

**P10-12.22 (MUST) Membership supplied by pin, never enumerated in a policy.** An implementation must supply a value set membership to `Part 7` as a pinned version and must expose the full membership of that version so that target completeness can be checked against it.

**P10-12.23 (MUST) Member change reported.** An implementation must report the addition or removal of a member of a published set to `Part 7`, per clause P10-4.44.

**P10-12.24 (MUST NOT) No stewardship as entitlement.** An implementation must not treat a stewardship assignment as an entitlement, per clause P10-3.93.

### 12.8 Boundary with Part 8, human task and case management

**Delegated.** The work by which a steward adjudicates a referred match, resolves a survivorship conflict, reviews a disputed record or reviews a concept affected by a definition change: the queue, the assignment and the case.

**Must not absorb.** Task management. This component records that an adjudication is required and that it was performed by a named act; it does not manage the doing.

**Naive conflation.** The referral and the task are one entity, so closing the task asserts the match. Or this component acquires the queue, so the adjudication backlog is a list nobody outside it can see.

**Reciprocal.** `Part 8` must declare that it owns the work item lifecycle, the queue and the case, that completing a work item does not itself assert a match or resolve a conflict, that every such assertion is effected by an operation here whose outcome the work item records, and that it obtains its own reference values, including party, group, role, organisational unit, capability and calendar, from this component by pin.

**P10-12.25 (MUST) Adjudication obtained, not managed.** An implementation must obtain the work by which a person adjudicates from `Part 8` and must record the work item reference on the resulting assertion.

**P10-12.26 (MUST NOT) No assertion from task closure.** An implementation must not treat the closure of a work item as asserting a match, resolving a conflict or confirming a record, and must require a recorded operation here naming the acting party.

**P10-12.27 (MUST) Organisational reference supplied by pin.** An implementation must supply party, group, role, organisational unit, capability and calendar content to `Part 8` as pinned versions, so that a candidate derivation can be re-performed. **Source.** `Part 8` clauses P8-12-17 and P8-12-18 require that component not to maintain an authoritative organisational model and to pin the snapshot used in every candidate derivation, which requires this component to supply a snapshot that is pinnable.

**P10-12.28 (MUST) Case scoped bindings not absorbed.** An implementation must not hold the binding of a party to a role for the life of one case, which `Part 8` clause P8-12-19 retains, and must hold only the organisational content the binding draws on.

### 12.9 Boundary with Part 9, schema and contract registry

**Delegated.** The identity, versioning and compatibility of the schemas of this component's release payloads, determination requests and responses, and events, and the validation of an instance against one.

**Must not absorb.** Schema validation and schema versioning.

**Naive conflation.** The permitted values of a field are enumerated in the schema rather than bound to a value set version, so the set exists twice and a member added in one is absent from the other.

**Reciprocal, and its discharge.** `Part 9` clauses P9-12-10 to P9-12-13 require that component not to hold value set membership, to hold a pinned value set version and a declared binding strength for every governed enumeration position, to report divergence between inlined members and the pinned version, and to obtain every membership determination from this component at validation time and record it as a binding finding. Each requires something of this component in return: a pinnable value set version, clauses P10-3.31 to P10-3.34; a membership determination available at validation time with the outcome vocabulary of section 7.2, clauses P10-1.5 and P10-6.14 to P10-6.21; and notification of member change so that divergence is detectable, clause P10-4.44.

**P10-12.29 (MUST) Membership determination available to validation.** An implementation must answer a membership determination for a validation request and must return an outcome from section 7.2 rather than a boolean.

**P10-12.30 (MUST NOT) No schema authority.** An implementation must not version a schema or validate an instance against one.

**P10-12.31 (MUST) Divergence detectable.** An implementation must expose the full membership of a pinned value set version so that `Part 9` can detect divergence between it and members inlined in a schema.

**P10-12.32 (MUST) Binding strength honoured in the outcome.** An implementation must return the outcome that names an incompleteness rather than a non membership where `Part 9` is determining a value against a binding of required strength, so that a validation is not failed on an incomplete set.

### 12.11 Boundary with Part 11, content addressed artifact store

**Delegated.** The storage, addressing, deduplication and retrieval of release artifact bytes.

**Must not absorb.** The bytes.

**Naive conflation.** Release artifacts are stored in this component's own records because it produces them, so the same artifact exists twice with no relation recorded and its integrity has two stories.

**Reciprocal.** `Part 11` must declare that it owns artifact content, addressing and retrieval, that a content address is immutable, and that it reports an unresolvable address rather than an absent one.

**P10-12.33 (MUST NOT) No artifact bytes held.** An implementation must not store the bytes of a release artifact.

**P10-12.34 (MUST) Content address held per version.** An implementation must hold the content address of the artifact conveying every published version.

**P10-12.35 (MUST) Unresolvable artifact reported.** An implementation must report a release whose artifact address does not resolve as unresolvable and must not delete the release record.

### 12.12 Boundary with Part 12, conformance and assurance harness

**Delegated.** The verification of this component's claims about itself, including the verification that its unreported population figure is honest.

**Must not absorb.** Self assessment presented as assurance.

**Naive conflation.** This component reports its own consumption coverage as assured, because it holds the reports.

**Reciprocal.** `Part 12` must declare that it verifies the claims this component makes, that it may obtain a consumption report by independent observation or attestation rather than from the consumer, and that it treats an unreported population figure as a claim requiring sampling rather than as a fact.

**P10-12.36 (MUST) State exposed for verification.** An implementation must expose the state required to verify every externally observable clause of this part.

**P10-12.37 (MUST NOT) No self assurance.** An implementation must not report its own conformance to this part as assurance.

**P10-12.38 (MUST) Attested reports accepted.** An implementation must accept a consumption report whose basis is attestation from `Part 12` and must record the basis rather than converting it to self reported.

### 12.13 Boundary with Part 13, model invocation and agent execution

**Delegated.** The invocation record of any model used in matching, deduplication, designation generation or mapping suggestion.

**Must not absorb.** Any assertion made on a model's output without a recorded basis.

**Naive conflation.** A model proposes a match, a map entry or a designation and the proposal is recorded as an assertion, because the output is well formed and plausible.

**Reciprocal.** `Part 13` must declare that it owns the invocation record, its cost and its non determinism, that a produced value is not a checked value, and that it does not assert content in this component.

**P10-12.39 (MUST) Model output recorded as a proposal.** An implementation must record a model produced match, map entry or designation as a proposal and must not record it as an assertion without a separate accepting act.

**P10-12.40 (MUST) Invocation reference recorded.** An implementation must record the `Part 13` invocation reference of every proposal a model produced.

**P10-12.41 (MUST NOT) No model authored concept.** An implementation must not admit a concept, an inactivation, a successor relation or an equivalence class asserted by a model without a recorded human accepting act.

**P10-12.42 (MUST) Accepting party recorded.** An implementation must record the party that accepted a model proposal and must not attribute the resulting assertion to the model.

### 12.14 Boundary with Part 0, system composition

**Delegated.** What happens when the components run at once: authority over facts more than one component touches, the seams at which values cross boundaries, the propagation of non results, and the pinning of versions across a unit of work spanning several components.

**Must not absorb.** Composition. This part states what it publishes and what it refuses to decide, and does not state what the estate does with an incomplete membership outcome beyond requiring the caller to read it.

**Reciprocal.** `Part 0` must declare that this component holds authority over code systems, concepts, value sets, expansions, maps, master records, contributions, match and merge assertions, survivorship determinations, distribution records and consumption reports, and over nothing else. It must state, for every seam, what must hold and how a violation appears here. It must in particular resolve the eight questions section 13.9 hands it.

**P10-12.43 (MUST) Authority declared, not assumed.** An implementation must not accept an assertion about a code system version, a concept state, a value set membership, an expansion, a map entry, a master identifier or a merge from another component, and must require every such fact to be established by its own operations.

**P10-12.44 (MUST) Non results returned unmodified.** An implementation must return every incompleteness and undetermined outcome unmodified regardless of whether the caller can represent it, and must not degrade one to a membership or a non membership to fit a caller's model.

**P10-12.45 (MUST) Consumption gap exposed to composition.** An implementation must make the unreported population, the stale holding population and the divergent expansion population available as signals, since none can be remedied within this component.

## 13. What could not be established

### 13.1 Sources not obtained in full text

**ISO/IEC 11179, all parts.** Paywalled. Obtained: the scope statements of Part 6 in its 2005, 2015 and 2023 editions, the front matter of the 2023 fourth edition establishing that it cancels the 2015 third edition, the quoted text of clause 4.3.3.1.4 on the Recorded status, the progression conditions for Qualified and above, the quality caveat on Recorded, and the description of the two status categories. Not obtained: the normative enumeration of registration statuses, the whole of the Part 3 metamodel, and Parts 31, 32, 33 and 35. The eight status enumeration in section 5.2 is therefore an adaptation. Its four progression statuses and the two documentation statuses are supported by the obtained text and by a national registration authority's published usage; `submitted` and `rejected` are this part's own and are not attributed.

**SKOS.** W3C Recommendation, obtained in relevant part. The reference text on the non transitivity of the hierarchical properties, the convention that the transitive properties are used for inference and not assertion, the transitivity of exact match, the non transitivity of close match, the disjointness of exact match from broad match and related match, and the disjointness of the associative relation from the hierarchical closure were all read in the specification's own words. The full property enumeration and the integrity conditions were not read in full.

**HL7 FHIR terminology resources.** Not obtained in this session. The account in section 10.4 rests on the author's general knowledge of the specification, and the content completeness declaration cited at clause P10-3.15 was not verified against specification text in this session. A reviewer should verify it before approval. The equivalence class enumeration of section 3.9 is this part's own and is deliberately not presented as that specification's, because the enumeration changed between two of its releases and this part did not establish which is current.

**ISO 8000, all parts.** Not obtained. Paywalled. The account in section 10.6 rests on general knowledge and no clause depends on it.

**ISO 3166.** The reuse of the code element CS and the reservation interval were read in ISO's own online register. The newsletter history of the successor code collision rests on secondary sources.

**ISO 25964, thesauri and interoperability with other vocabularies.** Not obtained. Paywalled. It is the standard most directly on the subject of section 3.9 and its absence is the most significant gap in this part's source base.

**Master data management practice.** No standard specifies matching, merging, survivorship or stewardship of a master record. Sections 3.12 and 6.6 rest on practice and on the internal logic of the model, and every clause in them is this part's own.

**Prior parts of this standard.** Parts 1 through 6 were not available in this session. Section 12.1 through 12.6 are therefore written from this part's own analysis of the boundary and from the reciprocal statements quoted in `Part 7`, and not from the text of those parts. Two reciprocals were recoverable at second hand, being clauses P2-12.18 and P3-12.18 as quoted in `Part 7`, and both are discharged at section 3.8. Every other reciprocal those six parts may require of this component is undischarged and unverified, and this is the most consequential gap in this part. `Part 7`, `Part 8` and `Part 9` were available and their reciprocals are discharged at sections 12.7, 12.8 and 12.9 with the discharging clauses named.

**P10-13.1 (MUST) Unverified reciprocals declared.** An implementation must not represent sections 12.1 through 12.6 as discharging a reciprocal statement of `Part 1` through `Part 6`, since the text of those parts was not read.

### 13.2 Whether a membership answer may be a boolean

Clause P10-3.106 refuses a boolean as the record and permits it as a projection. The refusal is inherited from `Part 7` section 3.16, which takes the same position on a two valued authorisation interface, and `Part 7` section 13.2 records that nothing about the cost of the refusal is costed. Nothing is costed here either.

The cost is concrete in this component in a way it is not in `Part 7`. A membership check is on the hot path of validation, and `Part 9` calls it once per bound position per instance. A thirteen valued outcome with counts and identifiers is a heavier object than a boolean by two orders of magnitude, and the caller that wants a boolean is not being unreasonable. The position stands on the argument of section 7.7, which is that twelve of the thirteen outcomes do not license a negative, and a reviewer may reasonably hold that the right answer is a two valued fast path with a mandatory recorded fuller outcome behind it. This part does not specify such a path.

### 13.3 The cost of the model

One determination record per value per value set version per request, at validation volumes, is the largest volume commitment in this part and it is uncosted. So is one contribution retained per source assertion per attribute set, one expansion artifact per distinct input combination, and one distribution record per consumer per release.

Two of these have a plausible bound. Expansions are bounded by the number of distinct input combinations, which is small where bindings are pinned. Distribution records are bounded by consumers times releases. The other two are unbounded in the volume of transactions and this part states no threshold, no sampling scheme and no aggregation that would preserve the distinctions of section 7 at lower cost. A reviewer should treat clause P10-8.10 as the clause most likely to be relaxed in implementation, and should require the relaxation to be declared rather than discovered.

### 13.4 Whether the consumption report can be more than a hope

This is the largest gap in the part, and it is the same gap `Part 7` section 13.5 records for the enforcement report.

This component cannot compel a consumer to report what it holds. Section 3.2 makes the honest position, which is that the unreported population is countable and is the measure of what is unknown, and sections 8.5 and 12.12 expose it. None of that causes a single consumer to report.

Three constructions were considered and none pursued. Observation at the point of distribution, which establishes what was fetched and not what is in use, and which fails entirely for a consumer that fetched once. Instrumentation of the determination interface, which establishes the version a consumer asked about and therefore works only for consumers that ask this component rather than holding a local copy, which are the consumers least at risk. And attestation through `Part 12`, which is the construction clause P10-12.38 admits and which is the only one that produces evidence rather than a signal.

Sampling with independent attestation is probably the right answer, exactly as `Part 7` concluded for its own case, and it is not designed here either. That two components have now reached the same undesigned conclusion is recorded in section 13.7.

### 13.5 The master data side has no standard and this part did not supply one

Sections 3.12 and 6.6 specify matching, merging, survivorship and their records without a source. The clauses are internally consistent and are not derived from anything, and a reviewer should read them as this part's design rather than as a codification.

Three specific things are unspecified. No matching algorithm, no comparison function and no blocking strategy, because specifying one would bind implementations to a technique. No threshold or referral band value, only the requirement that both be declared. And no treatment of the case in which two master records are found to be one and both have been cited by determinations in other components, where the merge changes what a past citation resolves to; clause P10-3.74 requires the absorbed identifier to resolve with its merge assertion, which makes the change visible and does not say what a citing component should do about it. That is handed to `Part 0` in section 13.9.

### 13.6 The boundary between survivorship and decision

Section 12.5 distinguishes a survivorship determination from a business decision on the ground that the first selects among assertions about one fact by a declared data rule and the second selects an outcome from inputs by a governed business rule. The distinction is real and the line is not derivable.

A rule that prefers the value from the source with the most recent assertion is clearly survivorship. A rule that prefers the address a customer confirmed over the address a data broker supplied, where the preference exists because the organisation has decided that customer confirmation is authoritative for correspondence, is a governed business rule wearing a survivorship rule's clothes. `Part 7` section 13.4 records the same problem for its own boundary with `Part 5` and concludes that a per operation declaration is probably better than a test. The same conclusion applies here and is not adopted, because adopting it would require this part to specify a declaration mechanism for a boundary the other part owns.

### 13.7 Repeated structure across the standard, now ten parts

`Part 4` recorded three repeated structures, `Part 5` five, `Part 6` six, `Part 7` eight and one divergence. Three further parts have been authored since. This section carries the register forward, adds to it, and records a second divergence which is of a different kind from the first: it is a divergence in the documentation of the standard rather than in its content.

**A divergence in clause convention and boundary numbering.** `Part 8` and `Part 9` were authored under a clause identifier of the pattern part, section, hyphen, zero padded ordinal, with the modality stated in upper case within the clause prose, a per clause basis marker of S, P or D, and section 12 subsections numbered in the order the boundaries were discussed rather than by part number. `Part 1` through `Part 7` use part, section, dot, unpadded ordinal, a parenthetical modality followed by a subject label, lower case prose, and section 12 subsections corresponding to part numbers with section 12.14 for `Part 0`. Three consequences follow. Cross part clause citations are not uniform, so a citation index over the standard requires two parsers. Neither `Part 8` nor `Part 9` exposes a section 12.10, so this part could not read a reciprocal from either and had to derive both boundaries from their content, which sections 12.8 and 12.9 record. And the per clause basis marker of those two parts is information the other eight do not carry. This part adopts the majority convention and records the divergence rather than propagating it. The remedy is mechanical for the identifier form and the boundary numbering and is a judgement for the basis marker, which this part considers worth adopting standard wide and has not adopted unilaterally because it would break the clause extraction the other parts' derived counts depend on.

**The authority that can prove what it did and not what happened.** This is no longer a vocabulary repetition; it is one structure in two components. `Part 7` can prove what it decided and not what was enforced. This component can prove what it published and not what is held. Both keep two records and never merge them, both treat the absence of the second as ordinary rather than as an error, both count the unreported population as the measure of the unknown, both expose it as a signal they cannot remedy, and both conclude in section 13 that sampling with independent attestation through `Part 12` is probably the answer and do not design it. Two components, two vocabularies, one asymmetry, and the same undesigned remedy reached independently. This is the strongest candidate in the register for being specified once.

**The refusal of order dependent resolution.** Now recorded in seven parts on this part's reading: `Part 2`'s salience, `Part 5`'s first match, `Part 6`'s branch order, `Part 7`'s first applicable, `Part 8`'s refusal to resolve a claim race by any property of the claimant, `Part 9`'s refusal to derive a compatibility conclusion from a version designation, and this part's refusal of survivorship by source list position. The last three are this part's attribution and a reviewer of those parts should confirm them. Seven refusals, seven vocabularies, one principle.

**The refusal to arbitrate.** Now five: `Part 2` reports a rule contradiction and refuses to resolve it, `Part 5` returns undecidable, `Part 6` refuses to resolve a join by an undeclared order, `Part 7` returns indeterminate on multiplicity, and this part returns every applicable map entry rather than choosing among them.

**The honest undeclared or unreported value.** Now ten parts. This part contributes `code_unknown_to_system`, `binding_unpinned_unspecified`, `undetermined_threshold_absent`, `unmeasurable` and `never_reported`.

**The immutable record with stateful assertions about it.** Now ten parts. This part's instance is the immutable code system version carrying concepts whose state changes, and the immutable contribution carrying master records whose presented values change.

**The declared completeness of a set.** Now eight parts. `Part 9`'s evaluated extent and this part's expansion completeness with its withheld count and truncation flag are the same structure: a set whose extent is not declared cannot be relied upon, and the declaration is the responsibility of whoever bounded it. This part adds a second dimension the others do not have, being that the bounding may be done by an authorisation decision or a licence rather than by the component itself.

**The residue model.** Still two, `Part 6` and `Part 7`. This part has no residue and does not add to it.

**The extended third value.** Still an inconsistency between `Part 5` and `Part 7` and still unresolved. This part does not adopt an extended form, because its non results name a cause rather than a set of values the determination could have been, and a reviewer may hold that the incompleteness outcomes of section 7.2 should carry the membership the determination would have reached had the set been complete. That would be an extended form and it is not adopted.

**The asymmetric bridge that disproves and cannot prove.** Two parts have one and three record that they should and do not. This part makes four without one. Its candidate is a set of recorded value set versions with the memberships their stewards assert they should have, expanded at publication, which would catch an intensional definition that does not select what its statement says it selects. Four consecutive parts have now identified the same missing device.

**The marking vocabulary for restricted content.** `Part 7` section 12.14 records that four parts consume the distinction between withheld and removed and each names it differently. This part is the fifth, and clause P10-3.47 requires the vocabulary to be registered without specifying it. Five parts, five vocabularies, one distinction.

**The retention obligation a component cannot discover.** New. the reciprocal statement of `Part 7` section 12.10 requires this component to retain a version for as long as the longest decision that read it, and this component cannot discover which decisions read it. Section 3.15 makes the floor a record that another component raises by notification. The same structure will arise for `Part 4`'s definitions and `Part 11`'s artifacts, and it is a composition device rather than a component requirement.

**Open.** All of it, and now with a second divergence of a different kind. This is the fifth consecutive part to record the question and the fourth to recommend acting before the next part. The register now contains eleven items across ten parts, two of them inconsistencies rather than repetitions, and one of the two concerns the form of the documents rather than their content.

**P10-13.2 (SHOULD) Register maintained.** An author of a subsequent part should carry this register forward, add to it, and state whether each entry is a repetition or an inconsistency.

### 13.8 What this part deliberately did not attempt

No conformance assessment of any system was performed or anticipated, per clause P10-1.30.

No matching algorithm, comparison function, blocking strategy or threshold value is specified, per section 13.5.

No schema or wire format is specified for a release artifact, a determination request or a determination response. The schemas are `Part 9`'s and this part states only what a payload must carry.

No expansion algorithm is specified beyond the ordering constraints of section 6.2 and the bounds of clauses P10-6.12 and P10-6.26. The evaluation of an individual intensional rule kind is left to the registered kind's own definition.

No treatment is given of a code system whose publisher does not version its releases, which is common among national and administrative code lists. This part requires a version and does not say what to do when the publisher supplies none.

No treatment is given of cross organisational reference data, where two organisations each hold an authoritative set for the same domain and neither can compel the other. This is the same gap `Part 7` section 13.8 records for authorisation across an organisational boundary.

No treatment is given of the language and translation lifecycle beyond the designation model of section 3.5. A translation programme has a workflow, a quality state and a coverage measure per language, and none is specified.

No performance or scale requirement is stated, and section 13.3 records the volume concern without a threshold.

**P10-13.3 (MUST) Gaps declared, not filled.** An implementation must not represent a matter listed in section 13.8 as specified by this part.

**P10-13.4 (SHOULD) Open questions carried forward.** A reviewer of this part should record a position on each open question in section 13, and where a position is adopted it should be recorded in the review outcome rather than by silent amendment of the clause it affects.

### 13.9 Questions handed to Part 0 rather than answered here

Whether the marking vocabulary for withheld content should be specified once for the estate. Five parts now consume the distinction and each names it differently, and this part registers a vocabulary without specifying one.

Who is accountable for a consumer that does not report what it holds, given that clause P10-3.7 makes the population countable and that this component has no authority over the consumer. `Part 7` hands forward the identical question about an enforcement point that does not report, and the two should be answered together or not at all.

Whether the response to an incomplete membership outcome is a per consumer declaration or an enterprise wide position. A heterogeneous set of responses means one value accepted by one consumer and refused by another from the same determination, which is the same shape as the question `Part 7` hands forward about not applicable.

How a unit of work spanning this component, `Part 2`, `Part 5`, `Part 7` and `Part 9` pins one code system version, one value set version, one map version, one rule set version, one criterion version, one policy version and one schema version together, so that a determination is not made against mixed vintages. `Part 7` hands forward the first four of these and this part adds three.

Whether the retention floor of section 3.15 should be a composition level device owned by `Part 0`, since every component that pins a version of another's content creates a retention obligation the pinned component cannot discover, and this part is the first to be given such an obligation explicitly.

Whether a master identifier is this component's identity for an entity or the estate's identity for it, given that `Part 3`, `Part 8` and `Part 11` all hold references to entities and that a merge changes what a past reference resolves to. Clause P10-3.74 makes the change visible and does not say what a citing component must do.

Whether a concept inactivation is an event other components must act on or a fact they may read. Four parts pin value set versions and none is required to react to an inactivation within a version it has pinned, which is correct for pinning and leaves the estate holding pinned sets containing concepts nobody should use.

Whether the eleven repeated structures now identified should each be specified once, per section 13.7, and in particular whether the divergence in clause convention between `Part 8`, `Part 9` and the other eight parts should be remedied before `Part 11` is authored.
