# Episode 3.3 — Project Management for IS

**Domain 3: Information Systems Acquisition, Development, and Implementation**
**Duration: 33:15**
**CISA Exam Weight: Domain 3 represents 18% (~36 questions)**

---

## INTRODUCTION (0:00 – 2:30)

Welcome to Episode 3.3, the final installment in our Domain 3 series. I am your host, and today we bring together everything we have covered in this domain by examining project management for information systems. In Episode 3.1, we dissected the Systems Development Life Cycle — the phases and methodologies through which systems are built. In Episode 3.2, we explored change management and quality assurance — the controls that govern modifications and ensure standards are met. Now we address the management discipline that wraps around all of those activities: project management.

Project management is not a technical discipline in the traditional sense. It does not specify how code should be written or how tests should be designed. Instead, it provides the governance structure, the planning tools, the tracking mechanisms, and the decision frameworks that determine whether an SDLC effort succeeds or fails. Research consistently shows that the most common cause of IS project failure is not technical complexity — it is management failure. Inadequate scope definition, unrealistic schedules, insufficient stakeholder engagement, poor risk management, and lack of executive sponsorship destroy more projects than any programming language limitation or hardware constraint ever has.

The IS auditor evaluates project management practices to provide assurance that the organization's investment in information systems development is being managed responsibly. This means verifying that projects are properly authorized, adequately planned, appropriately resourced, actively monitored, and formally closed. The CISA exam tests these concepts through scenario-based questions that require you to identify project management deficiencies, recommend corrective actions, and evaluate project health using quantitative indicators.

Let us work through the key frameworks, tools, and techniques.

[SECTION BREAK]

## PROJECT MANAGEMENT FRAMEWORKS: PMBOK AND PRINCE2 (2:30 – 7:00)

Two project management frameworks dominate the CISA exam landscape: PMBOK and PRINCE2.

The Project Management Body of Knowledge, or PMBOK, is published by the Project Management Institute and is the most widely adopted framework in North America. PMBOK defines project management through five process groups — Initiating, Planning, Executing, Monitoring and Controlling, and Closing — and ten knowledge areas: Integration Management, Scope Management, Schedule Management, Cost Management, Quality Management, Resource Management, Communications Management, Risk Management, Procurement Management, and Stakeholder Management.

The CISA exam does not expect you to memorize all ten knowledge areas in detail, but you should understand the framework's structure and be able to apply its concepts. The five process groups are sequential but overlapping — planning continues during execution, and monitoring and controlling spans the entire project lifecycle. This is different from the Waterfall SDLC, where phases are strictly sequential. A project can be in the executing process group for one deliverable while still in the planning process group for another.

PRINCE2 — Projects IN Controlled Environments — is the dominant framework in Europe, the United Kingdom, and much of the Commonwealth. PRINCE2 is structured around seven principles, seven themes, and seven processes. Its distinguishing characteristics include a strong emphasis on business justification — every project must have a continuously validated business case — management by exception — where each management level delegates authority within defined tolerances and only escalates when those tolerances are threatened — and defined management stages — the project is planned and authorized one stage at a time, with formal approval required before proceeding to the next stage.

For the CISA exam, the most important distinction between PMBOK and PRINCE2 is philosophical. PMBOK is a knowledge framework — it describes what project management encompasses and provides tools and techniques, but it does not prescribe a specific process sequence. PRINCE2 is a methodology — it prescribes a specific process sequence with defined roles, responsibilities, and deliverables at each stage. An organization using PMBOK has flexibility in how it structures its project management processes. An organization using PRINCE2 follows a defined process model.

From the IS auditor's perspective, either framework is acceptable provided it is implemented consistently and produces auditable evidence of project governance. The auditor's concern is not which framework is used but whether a framework exists, whether it is followed, and whether it provides adequate controls over the project lifecycle.

[SECTION BREAK]

## PROJECT GOVERNANCE AND AUTHORIZATION (7:00 – 10:30)

Project governance is the structure of authority, accountability, and decision-making that oversees a project. Effective project governance requires clear roles: a project sponsor who provides executive authority and resources, a project steering committee that makes strategic decisions, a project manager who manages day-to-day execution, and project team members who perform the work.

The project charter is the foundational governance document. It formally authorizes the project's existence, names the project manager and grants them authority to apply organizational resources, defines the project's objectives and high-level scope, identifies key stakeholders, and establishes the project's relationship to the organization's strategic objectives. The IS auditor should verify that a project charter exists, that it was approved by appropriate management — typically the project sponsor at a minimum — and that the project manager's authority is clearly defined.

The scope statement elaborates on the charter by defining in detail what the project will deliver and, equally important, what it will not deliver. Scope definition is critical because scope creep — the uncontrolled expansion of project scope — is one of the most common causes of project failure. The IS auditor should verify that the scope statement includes explicit exclusions and that a formal scope change process exists. Any change to scope should follow a process analogous to change management: a formal request, impact analysis, approval by the steering committee, and adjustment of the project plan to reflect the additional work.

Here is an exam trap that surfaces regularly: the CISA exam may describe a project where additional requirements are being incorporated without formal scope change approval. The question asks what the IS auditor should identify as the primary risk. The answer is scope creep leading to schedule and budget overruns. Not security risk, not technical risk — scope management risk. The exam consistently frames uncontrolled scope expansion as a governance failure.

The Work Breakdown Structure, or WBS, is the tool that decomposes the scope statement into manageable work packages. The WBS is a hierarchical decomposition of the total work required — starting from the project's major deliverables and breaking each one down into progressively smaller components until each component can be reliably estimated, assigned, and tracked. The lowest level of the WBS is called a work package, and each work package should have a defined scope, duration, cost estimate, and assigned resource.

The IS auditor should verify that a WBS exists and that it comprehensively covers the project scope. A WBS that omits work — particularly testing, documentation, training, or data conversion — will produce optimistic estimates and unrealistic schedules. If the exam asks how an IS auditor can best verify that a project plan is comprehensive, the answer often points to reviewing the WBS for completeness against the scope statement.

[SECTION BREAK]

## PROJECT SCHEDULING: GANTT, CRITICAL PATH, AND PERT (10:30 – 15:30)

Project scheduling translates the WBS into a time-bound plan. Three scheduling techniques are tested on the CISA exam: Gantt charts, the Critical Path Method, and PERT.

A Gantt chart is a bar chart that displays project activities against a timeline. Each activity is represented by a horizontal bar whose length corresponds to the activity's duration and whose position on the timeline indicates its start and end dates. Gantt charts are effective for communicating the project schedule to stakeholders because they are visually intuitive. However, traditional Gantt charts do not explicitly show dependencies between activities — you can see that Activity B starts after Activity A ends, but the chart does not make explicit that Activity B depends on Activity A's completion. Modern Gantt chart tools address this limitation by overlaying dependency arrows, but the CISA exam treats the basic Gantt chart as a communication tool rather than an analytical tool.

The Critical Path Method, or CPM, is the analytical technique that identifies the longest sequence of dependent activities through the project — the critical path. The critical path determines the minimum possible duration of the project. If any activity on the critical path is delayed, the entire project is delayed by the same amount. Activities not on the critical path have float — also called slack — which is the amount of time they can be delayed without affecting the project's completion date.

Understanding the critical path is essential for the IS auditor because it identifies where schedule risk is concentrated. The IS auditor should verify that the project manager has identified the critical path, that critical path activities are receiving appropriate management attention and resources, and that schedule buffers or contingencies exist for high-risk critical path activities.

Here is the exam trap on critical path: the CISA exam will present a network diagram with activity durations and dependencies, and it will ask you to identify the critical path. To solve this, you trace every possible path through the network, sum the durations along each path, and identify the longest one. The critical path is the longest path, not the shortest. This counterintuitive definition catches candidates who associate "critical" with "shortest" — in fact, the critical path is the constraint that determines the project's minimum duration.

Let me walk through an example. Suppose a project has five activities. Activity A takes three days and has no predecessors. Activity B takes five days and depends on A. Activity C takes four days and depends on A. Activity D takes two days and depends on both B and C. Activity E takes three days and depends on D. Path A-B-D-E has a total duration of three plus five plus two plus three, which equals thirteen days. Path A-C-D-E has a total duration of three plus four plus two plus three, which equals twelve days. The critical path is A-B-D-E at thirteen days, because it is the longest path. Activity C has one day of float — it can be delayed by one day without affecting the project's completion date.

PERT — the Program Evaluation and Review Technique — extends CPM by incorporating uncertainty into duration estimates. Instead of a single duration estimate for each activity, PERT uses three estimates: optimistic, most likely, and pessimistic. The expected duration is calculated using a weighted average formula: optimistic plus four times most likely plus pessimistic, all divided by six. This formula gives the most likely estimate four times the weight of the optimistic and pessimistic estimates.

For the CISA exam, you should be able to apply the PERT formula. If an activity has an optimistic estimate of four days, a most likely estimate of six days, and a pessimistic estimate of fourteen days, the expected duration is four plus twenty-four plus fourteen, divided by six, which equals forty-two divided by six, which equals seven days. Note that the expected duration of seven days is higher than the most likely estimate of six days — this is because the pessimistic estimate of fourteen days is further from the most likely than the optimistic estimate of four days, creating a right-skewed distribution.

The IS auditor's interest in PERT relates to the realism of project schedules. If a project schedule is based on single-point estimates — which are typically optimistic — the project is likely to overrun. PERT-based schedules, by incorporating uncertainty, are more realistic. The auditor should note whether the organization uses single-point or range-based estimates and whether contingency time has been incorporated into the schedule.

[SECTION BREAK]

## RESOURCE ALLOCATION, BUDGETING, AND EARNED VALUE MANAGEMENT (15:30 – 21:00)

Resource allocation assigns personnel, equipment, and facilities to project activities based on the schedule and the resource requirements of each work package. The IS auditor's concern with resource allocation is whether the project has adequate resources to meet its schedule commitments and whether resource conflicts — the same resource assigned to multiple concurrent activities — have been identified and resolved.

Project budgeting translates the resource plan into financial terms. The project budget should include direct costs — labor, hardware, software, facilities — indirect costs — overhead, administrative support — and contingency reserves for identified risks. The IS auditor should verify that the budget is based on the WBS and resource plan rather than a top-down allocation, that assumptions are documented, and that a formal process exists for budget change requests.

Earned Value Management, or EVM, is the quantitative technique for measuring project performance that the CISA exam tests most rigorously. EVM integrates scope, schedule, and cost into a single measurement framework, providing objective indicators of project health. You must know four fundamental EVM metrics and two forecasting calculations.

Planned Value, or PV — formerly called Budgeted Cost of Work Scheduled — is the authorized budget for the work scheduled to be completed by a specific date. It represents how much work should have been done.

Earned Value, or EV — formerly called Budgeted Cost of Work Performed — is the authorized budget for the work actually completed by a specific date. It represents how much work has been done, measured in budgetary terms.

Actual Cost, or AC — formerly called Actual Cost of Work Performed — is the actual expenditure incurred for the work completed by a specific date. It represents how much was actually spent.

From these three metrics, EVM derives two critical performance indices.

The Cost Performance Index, or CPI, equals Earned Value divided by Actual Cost. CPI measures cost efficiency. A CPI of 1.0 means the project is exactly on budget. A CPI greater than 1.0 means the project is under budget — it is getting more work done per dollar than planned. A CPI less than 1.0 means the project is over budget — it is getting less work done per dollar than planned.

The Schedule Performance Index, or SPI, equals Earned Value divided by Planned Value. SPI measures schedule efficiency. An SPI of 1.0 means the project is exactly on schedule. An SPI greater than 1.0 means the project is ahead of schedule. An SPI less than 1.0 means the project is behind schedule.

Let me illustrate with a concrete example. A project has a total budget of one hundred thousand dollars and a twelve-month timeline. At the six-month point, the planned value is fifty thousand dollars — the project should be half complete. The earned value is forty thousand dollars — the project has actually completed forty percent of the work. The actual cost is forty-five thousand dollars — the project has spent forty-five thousand dollars to complete that forty percent.

The CPI is forty thousand divided by forty-five thousand, which equals 0.89. This means the project is getting only eighty-nine cents of work for every dollar spent — it is twelve percent over budget on an efficiency basis.

The SPI is forty thousand divided by fifty thousand, which equals 0.80. This means the project has completed only eighty percent of the work it should have completed by this point — it is twenty percent behind schedule.

The Estimate at Completion, or EAC, forecasts the total cost of the project based on current performance. The simplest EAC formula divides the Budget at Completion, or BAC, by the CPI. In our example, EAC equals one hundred thousand divided by 0.89, which equals approximately one hundred twelve thousand four hundred dollars. If current cost efficiency continues, the project will cost about twelve percent more than budgeted.

Here is the exam trap on EVM: the CISA exam frequently asks which EVM metric the IS auditor should use to determine if a project is delivering value for money. The answer is CPI. If the question asks which metric indicates whether the project will meet its deadline, the answer is SPI. If the question asks for the best overall indicator of project health, some formulations point to CPI because research shows that CPI stabilizes early in a project and is a reliable predictor of final cost performance — once a project's CPI drops below 1.0, it rarely recovers.

A mnemonic for EVM indices: "CPI is Cash, SPI is Speed." CPI tells you about cost efficiency — your cash. SPI tells you about schedule efficiency — your speed. Both should be at or above 1.0 for a healthy project.

[SECTION BREAK]

## PROJECT RISK AND STAKEHOLDER MANAGEMENT (21:00 – 24:00)

Project risk management follows the same general framework as enterprise risk management but is scoped to the project context. The process includes risk identification, qualitative analysis — assessing probability and impact to prioritize risks — quantitative analysis — modeling the aggregate effect of risks on project objectives — risk response planning, and risk monitoring throughout the project.

The four fundamental risk responses for negative risks, or threats, are avoid, transfer, mitigate, and accept. Avoidance eliminates the risk by changing the project plan — for example, using a proven technology instead of an emerging one. Transfer shifts the risk to a third party — for example, through insurance or a fixed-price contract with a vendor. Mitigation reduces the probability or impact of the risk — for example, adding testing resources to reduce the risk of quality defects. Acceptance acknowledges the risk and takes no proactive action — this is appropriate when the cost of response exceeds the expected impact.

For the CISA exam, remember that risk acceptance should be a conscious decision documented in the risk register, not a default resulting from failure to identify or analyze the risk. The IS auditor should verify that a project risk register exists, that it is actively maintained throughout the project, and that risk responses are implemented and monitored.

Stakeholder management is a knowledge area that has gained prominence in recent PMBOK editions and is increasingly tested on the CISA exam. Stakeholders are individuals or groups with an interest in or influence over the project. Effective stakeholder management requires identifying all stakeholders, analyzing their interests and influence, developing engagement strategies, and managing their expectations throughout the project.

The IS auditor's interest in stakeholder management relates to project governance. If key stakeholders are not engaged, critical requirements may be missed, resistance to the system may develop, and the project may lack the executive support needed to resolve conflicts and secure resources. The auditor should verify that a stakeholder register exists, that stakeholder communication is planned and executed, and that stakeholder concerns are documented and addressed.

A project communication plan defines what information will be shared with which stakeholders, through what channels, at what frequency. The IS auditor should verify that the communication plan exists and covers all identified stakeholders. Inadequate communication is a root cause of stakeholder disengagement and is a legitimate audit finding.

[SECTION BREAK]

## PROJECT QUALITY MANAGEMENT AND CLOSURE (24:00 – 26:30)

Project quality management ensures that the project delivers results that meet the defined quality standards. It encompasses three activities: quality planning — defining quality standards and metrics; quality assurance — auditing the process to verify that standards are being followed; and quality control — inspecting deliverables to detect defects.

The CISA exam may ask about the relationship between project quality management and the quality assurance concepts covered in Episode 3.2. The relationship is hierarchical: project quality management plans and governs the quality activities — testing, code review, standards compliance — that we discussed previously. The quality management plan defines what testing will be performed, what standards will apply, what acceptance criteria will be used, and how quality metrics will be collected and reported.

Project closure is the final process group, and it is frequently neglected in practice and frequently tested on the exam. Project closure includes obtaining formal acceptance of deliverables from the project sponsor, closing contracts with vendors and service providers, releasing project resources, archiving project documentation, and conducting a lessons learned review.

The lessons learned review is particularly important from an IS audit perspective. It captures what worked well and what did not during the project, creating organizational knowledge that improves future projects. The IS auditor should verify that lessons learned reviews are conducted and that their findings are documented and disseminated. If the exam asks what is the primary purpose of a post-project lessons learned review, the answer is to improve future project performance — not to assign blame, not to evaluate individual performance, but to capture organizational learning.

Here is an exam trap: the exam may ask when the project manager's responsibility ends. The answer is after formal project closure — not after implementation, not after UAT, not after the system goes live. The project is not complete until the closure activities are finished and the project sponsor has formally accepted the deliverables and approved the project's closure.

[SECTION BREAK]

## SOFTWARE ESTIMATION: FUNCTION POINTS AND COCOMO (26:30 – 29:00)

Software estimation is the discipline of predicting the effort, duration, and cost required to develop or maintain a software system. The CISA exam tests two estimation techniques: Function Point Analysis and COCOMO.

Function Point Analysis, or FPA, measures the functional size of a software system from the user's perspective. It quantifies functionality by counting five types of function points: External Inputs — data entering the system from outside its boundary; External Outputs — data leaving the system; External Inquiries — interactive queries that retrieve data without modifying it; Internal Logical Files — data stored and maintained within the system; and External Interface Files — data referenced by the system but maintained by another system.

Each function point is classified by complexity — simple, average, or complex — and assigned a weight. The raw function point count is adjusted by a Value Adjustment Factor that accounts for fourteen general system characteristics including data communications, distributed processing, performance, heavily used configuration, and transaction rate. The adjusted function point count provides a technology-independent measure of the system's size.

The IS auditor's interest in function points relates to estimation accuracy. If a project's estimate was based on function point analysis and the actual function point count can be measured after completion, the auditor can evaluate the accuracy of the estimating process. Significant discrepancies between estimated and actual function points suggest weaknesses in the estimation process.

Here is a mnemonic for the five function point types: "I Only Inquire Into External" — Inputs, Outputs, Inquiries, Internal logical files, External interface files. Five types, five words.

COCOMO — the Constructive Cost Model — is an algorithmic estimation model developed by Barry Boehm. COCOMO takes the estimated size of a software system — typically measured in thousands of lines of code or function points — and applies mathematical formulas that incorporate project complexity factors to estimate effort in person-months, duration in calendar months, and team size. COCOMO exists in three levels of detail: Basic COCOMO uses a simple formula with size as the only input; Intermediate COCOMO adds fifteen cost driver attributes that adjust the estimate based on factors like product reliability, database size, analyst capability, and development environment; and Detailed COCOMO applies cost drivers at the individual module level for greater accuracy.

For the CISA exam, you do not need to apply COCOMO formulas. You should understand that COCOMO is a parametric estimation model — it uses mathematical relationships between historical data and project parameters to produce estimates — and that its accuracy depends on the quality of the historical data and the applicability of the cost driver assessments.

[SECTION BREAK]

## OUTSOURCING, VENDOR MANAGEMENT, AND CONTRACTS (29:00 – 32:00)

Many IS development projects involve third-party vendors, whether for complete system development, component development, specialized services, or staff augmentation. The CISA exam tests your understanding of vendor management controls and contract types.

When an organization outsources system development, it transfers execution risk but retains accountability for the system's controls and security. This is a fundamental principle: outsourcing does not outsource accountability. The IS auditor should verify that the organization maintains adequate oversight of vendor activities, including the right to audit the vendor's processes, access to vendor-controlled environments for testing and verification, and contractual requirements for security, quality, and compliance.

Contract types define how risk is allocated between the organization and the vendor. Three contract types appear on the CISA exam.

A fixed-price contract, also called a firm fixed-price or lump-sum contract, specifies a total price for the defined deliverables. The vendor bears the risk of cost overruns — if the work costs more than expected, the vendor absorbs the difference. The organization bears the risk of scope definition — if the scope is poorly defined, the vendor will deliver exactly what was specified, which may not be what the organization actually needs. Fixed-price contracts are most appropriate when requirements are well defined and stable, because the price is based on the defined scope. Change requests under a fixed-price contract typically incur additional charges.

A time-and-materials contract, or T&M contract, pays the vendor for actual time spent and materials consumed. The organization bears the cost risk — if the project takes longer than expected, the organization pays more. T&M contracts provide flexibility because the scope can evolve during the project, but they also provide less cost certainty. T&M contracts are most appropriate when the scope is uncertain or evolving, such as during early phases of a project where requirements are being explored.

A cost-plus contract reimburses the vendor for actual costs plus a defined fee or percentage. Like T&M, the organization bears the cost risk. Cost-plus contracts are typically used for research and development projects where costs are genuinely unpredictable, and they provide the vendor with the least incentive to control costs because the vendor's fee is earned regardless of efficiency.

Here is the exam trap on contract types: the CISA exam frequently asks which contract type presents the greatest cost risk to the organization. The answer is cost-plus, followed by T&M, with fixed-price presenting the least cost risk to the organization. Conversely, fixed-price presents the greatest cost risk to the vendor.

Service Level Agreements, or SLAs, define measurable performance targets that the vendor must meet. SLAs should specify what is measured — availability, response time, resolution time, defect rates — how it is measured — the data source and calculation method — what the target is — the numerical threshold — and what the consequences are for missing the target — service credits, remediation plans, or contract termination rights.

The IS auditor should verify that SLAs are defined, that they are monitored, and that consequences for non-performance are enforced. An SLA that is never measured or whose violations are never addressed provides no actual control over vendor performance.

[SECTION BREAK]

## THE AUDITOR'S REVIEW OF PROJECT MANAGEMENT AND DOMAIN 3 SUMMARY (32:00 – 33:15)

The IS auditor's review of project management practices encompasses the entire project lifecycle. Key audit procedures include reviewing the project charter for proper authorization and scope definition; evaluating the project plan for completeness, including the WBS, schedule, budget, and risk register; assessing project governance structures — the steering committee, the project sponsor, the communication plan; reviewing EVM metrics for cost and schedule performance; evaluating change control over project scope; verifying that project risks are identified, assessed, and managed; reviewing vendor contracts and SLA monitoring; and confirming that project closure includes lessons learned and formal acceptance.

Let me close our Domain 3 series with a synthesis. Domain 3 is about the controlled creation and modification of information systems. The SDLC provides the phase framework. Development methodologies determine how we progress through those phases. Change management controls how production systems are modified. Quality assurance ensures that standards are met. Project management provides the governance wrapper that plans, resources, monitors, and controls the entire effort. And throughout all of these activities, the IS auditor provides independent assurance that controls are adequate, processes are followed, and organizational objectives are met.

For your exam preparation, I recommend focusing on the decision points — which implementation strategy, which methodology, which contract type — because the CISA exam is fundamentally a test of professional judgment, not rote memorization. Understand the principles, know the key metrics and formulas — especially EVM and PERT — and practice applying them to scenarios.

This concludes our coverage of Domain 3. In our next series, we move to Domain 4 — Information Systems Operations and Business Resilience — where we will examine IT service management, incident management, business continuity, and disaster recovery.

Thank you for your dedication to mastering this material. I will see you in Domain 4.

---

*End of Episode 3.3 — Project Management for IS*
*End of Domain 3: Information Systems Acquisition, Development, and Implementation*
*Next: Domain 4, Episode 4.1 — Information Systems Operations and Business Resilience*
