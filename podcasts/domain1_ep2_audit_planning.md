# Domain 1 — Episode 1.2: Audit Planning & Risk Assessment

**Series:** CISA Exam Preparation Podcast
**Domain:** 1 — Information Systems Auditing Process (21% of exam)
**Episode Duration:** 42:10
**Audience:** Senior IT audit practitioners preparing for CISA certification

---

## INTRODUCTION (0:00–2:45)

Welcome back to the CISA Exam Preparation Podcast. This is Episode 1.2, and we are staying in Domain 1 — Information Systems Auditing Process — to tackle what I consider the single most exam-dense topic in the entire domain: audit planning and risk assessment.

In Episode 1.1 we established the architecture of the IS audit process and positioned planning as the phase that ISACA examines most aggressively. Today we are going to justify that claim by drilling into the mechanics of risk-based audit planning with a level of rigor that will prepare you not only for exam day but for the moments in your career when the quality of your planning determines whether an engagement delivers value or wastes organizational resources.

Here is what we will cover. We will begin with the philosophy and methodology of risk-based audit planning — why auditors plan based on risk rather than convenience or tradition. We will then decompose the audit risk model into its three constituent components: inherent risk, control risk, and detection risk. We will examine materiality — what it means, how it is determined, and why it matters. We will walk through the engagement letter and the audit planning memorandum as the formal documents that anchor the planning phase. We will then pivot to risk assessment methodologies, working through both qualitative and quantitative approaches, with particular attention to the Annual Loss Expectancy formula that ISACA loves to test. We will cover audit program development, control objectives mapping, COBIT alignment, and preliminary survey techniques. And throughout, I will highlight the exam traps, give you mnemonics, and ground every concept in enterprise reality.

This is a dense episode. Stay with me. Every minute is exam-relevant.

[SECTION BREAK]

## RISK-BASED AUDIT PLANNING — THE PHILOSOPHY (2:45–7:30)

Risk-based audit planning is the foundational principle that governs how modern audit functions allocate their limited resources. The principle is deceptively simple: audit effort should be directed toward the areas of greatest risk. But the execution of that principle requires rigorous methodology, and the CISA exam tests that methodology extensively.

Why risk-based planning? Consider the alternative. An audit function could plan engagements on a cyclical basis — auditing every system, process, and business unit on a fixed rotation. In a small organization with a limited technology footprint, this might be feasible. But in an enterprise environment with hundreds of applications, dozens of business processes, multiple data centers, extensive third-party relationships, and a constantly evolving regulatory landscape, cyclical planning is inadequate. There are simply too many auditable entities and too few auditor hours. If you audit everything equally, you audit nothing thoroughly.

Risk-based planning solves this problem by establishing a prioritization framework. Areas with higher risk receive more frequent and more intensive audit coverage. Areas with lower risk are audited less frequently or may be excluded from the annual plan entirely. This is not neglect — it is strategic resource allocation guided by a systematic assessment of where the organization faces its greatest vulnerabilities.

ISACA's IS Auditing Standard 1202, Planning, states that the IS audit function should use an appropriate risk assessment approach and supporting methodology to develop the overall IS audit plan and determine priorities for the effective allocation of IS audit resources. Notice the language: "appropriate risk assessment approach" and "supporting methodology." The standard does not mandate a specific methodology — it requires that whatever methodology is used, it be appropriate for the organization and that it be systematic and documented.

In practice, risk-based audit planning involves several key activities. First, the audit function must maintain an up-to-date audit universe — the comprehensive inventory of auditable entities we discussed in Episode 1.1. Second, each element in the audit universe must be assessed against a set of risk factors — factors such as the complexity of the system, the sensitivity of the data it processes, the regulatory requirements it supports, the results of prior audits, the time elapsed since the last audit, and changes in the operating environment. Third, these risk assessments must be synthesized into a risk-ranked inventory that drives the selection and scheduling of audit engagements. Fourth, the resulting audit plan must be approved by the audit committee or equivalent governing body.

Here is an enterprise example. Consider a global financial services organization. Its audit universe might include several hundred elements — core banking applications, payment processing systems, treasury management platforms, customer relationship management systems, data warehouses, cloud infrastructure, third-party service providers, and so on. The audit function might have twenty auditors and the capacity to execute perhaps forty to fifty engagements per year. Risk-based planning is the mechanism that determines which fifty of those several hundred auditable entities receive attention this year.

Exam trap: ISACA may ask what should be the "primary basis" for selecting audit engagements. The correct answer is risk assessment. Not management request, not regulatory requirement, not time since last audit — risk assessment. While all of these factors inform risk assessment, the primary basis is the risk assessment itself. This distinction matters on the exam.

[SECTION BREAK]

## THE AUDIT RISK MODEL — INHERENT, CONTROL, AND DETECTION RISK (7:30–16:00)

The audit risk model is one of the most conceptually important and most frequently tested frameworks in Domain 1. You must understand it not just as a formula, but as a way of thinking about audit strategy.

Audit risk is defined as the risk that the auditor will issue an inappropriate opinion — specifically, the risk that the auditor will conclude that controls are adequate when they are actually deficient, or that a material misstatement exists when it does not. The audit risk model decomposes this overall risk into three components: inherent risk, control risk, and detection risk.

The relationship is expressed as: Audit Risk equals Inherent Risk multiplied by Control Risk multiplied by Detection Risk. In notation: AR = IR × CR × DR.

Let me define each component with precision, because the exam will test whether you can distinguish among them and apply them correctly.

Inherent risk is the susceptibility of an assertion, account balance, transaction class, or — in the IS audit context — a system or process to error or irregularity that could be material, assuming there are no related internal controls. Read that definition again carefully. Inherent risk is assessed in the absence of controls. It is the raw, unmitigated exposure that exists because of the nature of the item being audited. A system that processes high-volume financial transactions has higher inherent risk than a system that stores static reference data, simply because of the nature and volume of the transactions involved. A system that is highly complex has higher inherent risk than a simple, well-understood system. A system that has undergone recent significant changes has higher inherent risk than a stable system. Inherent risk is driven by factors intrinsic to the audit subject, not by the quality of the controls around it.

Control risk is the risk that a material error or irregularity will not be prevented or detected on a timely basis by the internal control system. Control risk is a function of the design and operating effectiveness of the organization's internal controls. If controls are well-designed and operating effectively, control risk is low. If controls are weak, poorly designed, or inconsistently applied, control risk is high. Critically, control risk is assessed by the auditor but is not something the auditor can directly change. The auditor evaluates control risk; management is responsible for establishing and maintaining the controls.

Detection risk is the risk that the auditor's own procedures will fail to detect a material error or irregularity that exists and has not been prevented or detected by internal controls. This is the component that the auditor directly controls. Detection risk is a function of the nature, timing, and extent of the auditor's procedures. More extensive testing reduces detection risk. More effective audit techniques — such as substantive testing versus inquiry alone — reduce detection risk. Better sampling strategies reduce detection risk.

Now, here is the critical conceptual relationship that the exam tests repeatedly. The auditor cannot directly control inherent risk or control risk. Inherent risk is determined by the nature of the audit subject. Control risk is determined by management's controls. The auditor can only control detection risk — by adjusting the nature, timing, and extent of audit procedures. This means that when inherent risk and control risk are high, the auditor must reduce detection risk by performing more extensive and more rigorous testing. Conversely, when inherent risk and control risk are low, the auditor can accept a higher level of detection risk and perform less extensive testing.

Let me make this concrete with an enterprise example. Suppose you are auditing an organization's payroll processing system. The system processes tens of thousands of transactions monthly, each involving financial calculations — high inherent risk. Management has recently replaced the payroll application, and the new controls have not yet been tested over a full operating cycle — elevated control risk. Given high inherent risk and elevated control risk, you must reduce detection risk. You would respond by increasing your sample sizes, performing more substantive testing, extending the period covered by your testing, and perhaps employing computer-assisted audit techniques to analyze the full population of transactions rather than relying solely on sampling.

Conversely, suppose you are auditing a stable, well-established document management system that stores non-sensitive internal communications. Inherent risk is low. The system has mature, well-tested access controls and has had clean audit results for three consecutive years — low control risk. In this scenario, you can accept higher detection risk, which means you can perform less extensive testing, use smaller sample sizes, and rely more heavily on inquiry and walkthrough procedures.

Exam trap: ISACA will present scenarios and ask you to identify the appropriate audit response. The key pattern is this: when inherent risk and control risk are assessed as high, detection risk must be low, which means the auditor must perform more extensive testing. When inherent risk and control risk are assessed as low, detection risk can be higher, which means the auditor can perform less extensive testing. If the exam presents a scenario with high inherent and control risk and asks what the auditor should do, the correct answer will involve increasing the extent of substantive testing — not reducing audit procedures or relying on management's representations.

Here is another exam trap. The exam may ask whether the auditor can eliminate audit risk entirely. The answer is no. Audit risk can be reduced to an acceptably low level, but it cannot be eliminated. There is always some residual risk that the auditor's procedures will fail to detect a material error. This is a fundamental concept in auditing theory, and the exam expects you to know it.

A mnemonic for the audit risk model: ICE — Inherent, Control, (and the auditor must manage) Exposure through detection. Or more directly: "I Can't Directly change inherent or control risk — only Detection risk." The initial letters I, C, D map to the three components.

[SECTION BREAK]

## MATERIALITY IN IS AUDITING (16:00–19:30)

Materiality is a concept borrowed from financial auditing that applies with equal force in the IS audit context, though it manifests differently. In financial auditing, materiality is typically expressed in monetary terms — a misstatement is material if its magnitude could influence the economic decisions of users of the financial statements. In IS auditing, materiality extends beyond monetary thresholds to encompass factors such as the sensitivity of data, the criticality of systems, the impact of control failures on business operations, and the regulatory consequences of noncompliance.

ISACA's IS Auditing Standards require auditors to consider materiality and its relationship to audit risk when determining the nature, timing, and extent of audit procedures. Materiality is not a fixed threshold — it is a matter of professional judgment that must be calibrated to the specific context of the engagement.

Let me illustrate. Consider an audit of an organization's identity and access management system. A finding that three users out of ten thousand have inappropriate access to a non-sensitive internal communications platform may not be material. But a finding that three users have unauthorized administrative access to the production database containing personally identifiable information for ten million customers is almost certainly material — not because of the number of users involved, but because of the potential impact of the access if exploited.

In IS auditing, materiality considerations include the financial impact of a control failure, the volume and sensitivity of data at risk, the regulatory implications of noncompliance, the potential for reputational damage, and the extent to which the finding indicates a systemic control weakness versus an isolated anomaly. A single access control exception might be immaterial. But if that exception reveals a systemic failure in the provisioning process — meaning that similar exceptions likely exist across the user population — the finding becomes material because it indicates a broader control deficiency.

Exam trap: the CISA exam may test whether you understand that materiality in IS auditing is not solely a monetary concept. If a question presents a scenario where a control failure has no direct financial impact but exposes sensitive personal data, and asks whether the finding is material, the correct answer is likely yes — because materiality in IS auditing encompasses data sensitivity and regulatory risk, not just financial impact.

Another frequently tested concept: the relationship between materiality and audit risk is inverse. As the materiality threshold decreases — meaning smaller errors are considered significant — audit risk increases, and the auditor must perform more extensive testing to achieve reasonable assurance. Conversely, a higher materiality threshold means fewer items will be considered significant, which reduces the required extent of testing. In practice, the auditor sets the materiality threshold during planning based on the nature of the engagement, and this threshold influences the design of audit procedures throughout fieldwork.

[SECTION BREAK]

## ENGAGEMENT LETTERS AND AUDIT PLANNING MEMORANDA (19:30–23:15)

Two formal documents anchor the planning phase of an IS audit engagement: the engagement letter and the audit planning memorandum. The CISA exam expects you to understand the purpose and content of both.

The engagement letter is the formal agreement between the audit function and the auditee that defines the terms of the engagement. In an internal audit context, the engagement letter is sometimes called an audit notification or engagement notification. Regardless of terminology, the document serves the same purpose: it establishes mutual understanding of the audit's scope, objectives, timeline, and the responsibilities of both the audit team and the auditee's management.

The engagement letter should include the following elements. First, the audit objectives — a clear statement of what the audit is intended to achieve. Second, the audit scope — a precise delineation of what is included in the engagement and, equally important, what is excluded. Scope exclusions are critical because they manage expectations and prevent disputes about what the audit should have covered. Third, the timeline — the expected start date, key milestones, and the anticipated date of the final report. Fourth, the identification of key contacts — both on the audit team and within the auditee's organization. Fifth, the responsibilities of the auditee — typically including providing timely access to personnel, systems, and documentation. Sixth, the confidentiality provisions — how audit information will be protected and to whom findings will be communicated.

The audit planning memorandum — sometimes called the audit plan or planning document — is the internal working document that guides the audit team's execution of the engagement. Unlike the engagement letter, which is shared with the auditee, the planning memorandum is typically an internal audit document.

The planning memorandum should include a description of the audit subject, the risk assessment that justified the engagement's inclusion in the annual plan, the specific control objectives that will be evaluated, the audit procedures that will be performed to test each control objective, the resources required — staff assignments, specialized tools, subject matter experts — the budget in terms of hours and calendar time, and any known limitations or constraints that may affect the engagement.

Here is a critical distinction the exam tests. The engagement letter communicates the terms of the engagement to the auditee and establishes mutual agreement. The audit planning memorandum guides the audit team's internal execution. The engagement letter is external-facing; the planning memorandum is internal-facing. Questions may present a scenario and ask which document should contain a particular element. If the element involves communication with the auditee — such as the timeline or scope — it belongs in the engagement letter. If the element involves internal audit strategy — such as the specific audit procedures or staff assignments — it belongs in the planning memorandum.

Exam trap: a question may ask what the "most important" component of the engagement letter is. The correct answer is typically the audit scope. The scope defines the boundaries of the engagement, and ambiguity in scope is the single most common source of disputes between auditors and auditees. A clearly defined scope protects both parties and is the foundation upon which the entire engagement rests.

[SECTION BREAK]

## RISK ASSESSMENT METHODOLOGIES — QUALITATIVE AND QUANTITATIVE (23:15–30:00)

Risk assessment is the engine that drives audit planning, and the CISA exam tests two fundamental approaches: qualitative risk assessment and quantitative risk assessment. You must understand both, including their strengths, limitations, and appropriate use cases.

Qualitative risk assessment relies on descriptive, non-numeric categorizations of risk. Risks are typically rated using ordinal scales — such as high, medium, and low — or using scoring systems that assign numerical values to qualitative judgments but do not claim mathematical precision. Qualitative risk assessment is the more commonly used approach in practice because it is faster to execute, requires less data, and is more accessible to non-technical stakeholders.

A typical qualitative risk assessment might evaluate each element in the audit universe against several risk factors — such as data sensitivity, system complexity, regulatory exposure, change frequency, and prior audit results — assign a rating of high, medium, or low for each factor, and then aggregate the ratings to produce an overall risk score. Elements with higher aggregate scores receive priority in the audit plan.

The strength of qualitative risk assessment is its practicality. Its limitation is subjectivity. Two auditors assessing the same system against the same risk factors may arrive at different ratings because the ratings are inherently judgmental. To mitigate this limitation, organizations should use clearly defined rating criteria — for example, defining precisely what constitutes "high" data sensitivity versus "medium" data sensitivity — and should calibrate ratings through discussion and consensus among the audit team.

Quantitative risk assessment uses numerical values to express risk in measurable terms — typically financial terms. The canonical quantitative risk assessment framework for the CISA exam is the Annual Loss Expectancy model.

Let me walk through this model with precision, because it is directly testable.

The model begins with Asset Value — the monetary value of the asset at risk. For a database containing customer records, the asset value might be expressed in terms of the cost to reconstruct the data, the revenue dependent on the data's availability, or the regulatory penalties associated with the data's compromise.

The next concept is the Exposure Factor, or EF. The exposure factor is the percentage of the asset value that would be lost in a single occurrence of a specific threat event. If a ransomware attack would render sixty percent of the database inaccessible, the exposure factor is zero point six, or sixty percent.

The Single Loss Expectancy, or SLE, is calculated as Asset Value multiplied by Exposure Factor. SLE equals AV times EF. If the asset value is one million dollars and the exposure factor is sixty percent, the single loss expectancy is six hundred thousand dollars. This represents the expected financial loss from a single occurrence of the threat event.

The Annualized Rate of Occurrence, or ARO, represents the estimated frequency with which the threat event is expected to occur in a given year. If the organization estimates that a ransomware attack is likely to occur once every two years, the ARO is zero point five — one occurrence per two years equals zero point five occurrences per year.

The Annual Loss Expectancy, or ALE, is calculated as SLE multiplied by ARO. ALE equals SLE times ARO. Using our example: SLE of six hundred thousand dollars multiplied by ARO of zero point five equals an ALE of three hundred thousand dollars. This means the organization can expect to lose approximately three hundred thousand dollars per year from ransomware attacks against this database.

The ALE is then used to make risk-informed decisions. If a control that would effectively mitigate the ransomware risk costs two hundred thousand dollars per year, and the ALE without the control is three hundred thousand dollars, the control provides a net benefit of one hundred thousand dollars per year. This cost-benefit analysis is a direct application of quantitative risk assessment.

Now, here is a critical formula chain for the exam. Let me give you the sequence: AV times EF equals SLE. SLE times ARO equals ALE. You need to be able to compute any of these values given the others. The exam may give you the ALE and ARO and ask you to calculate the SLE, or give you the SLE and AV and ask you to calculate the EF.

Mnemonic for the quantitative risk formulas: "Always Verify Every Single Likely Annual Risk Outcome." The capitalized first letters give you AV, EF, SLE, ARO — the four key variables.

Or more directly: "SLE is the Single hit. ALE is the Annual total." SLE asks: "How much do we lose if it happens once?" ALE asks: "How much do we lose per year?"

Exam trap: the exam frequently presents word problems that require you to calculate ALE. Practice these calculations until they are automatic. A common mistake is confusing ARO with the reciprocal of the return period. If a threat event occurs once every four years, the ARO is zero point two-five — one divided by four. Candidates sometimes mistakenly use four as the ARO, which produces a dramatically incorrect ALE.

Another exam trap: the exam may ask about the limitations of quantitative risk assessment. The primary limitation is data dependency. Quantitative risk assessment requires reliable data on asset values, exposure factors, and annualized rates of occurrence. In many organizations, this data is difficult to obtain, particularly for emerging threats with limited historical data. When reliable data is not available, qualitative risk assessment may be more appropriate.

The exam may also ask which approach — qualitative or quantitative — is "better." The correct answer is that neither is inherently superior. The appropriate approach depends on the context, the availability of data, and the needs of the decision-makers. In practice, most organizations use a combination of both approaches.

[SECTION BREAK]

## AUDIT PROGRAM DEVELOPMENT (30:00–34:30)

The audit program is the detailed procedural document that translates the planning phase into actionable fieldwork. It specifies the audit procedures that will be performed, the evidence that will be gathered, the personnel responsible for each procedure, and the timeline for completion. The audit program is the bridge between planning and execution, and the CISA exam tests your understanding of how it is constructed and what it contains.

The audit program is developed after the auditor has assessed risk, defined audit objectives, and identified the control objectives that will be evaluated. Each audit procedure in the program should be traceable to a specific control objective, and each control objective should be traceable to a specific audit objective. This traceability is not bureaucratic formality — it is the mechanism that ensures audit work is focused, efficient, and complete.

An audit procedure can be one of several types. Inquiry involves asking management and staff about controls, processes, and events. Inquiry alone is generally considered the weakest form of audit evidence because it relies on the representations of interested parties. Observation involves watching a process or control in operation. Observation provides evidence about a point in time but does not confirm that the control operates consistently over the full audit period. Inspection involves examining documents, records, and physical assets. Re-performance involves the auditor independently executing a control procedure to verify that it produces the expected results. Re-performance is generally considered one of the strongest forms of audit evidence because it provides direct confirmation of control operation. Analytical procedures involve evaluating information through analysis of plausible relationships among financial and non-financial data.

The audit program should also specify the sampling methodology that will be used — which we will cover in depth in Episode 1.3 — and the criteria for evaluating results. For each procedure, the program should define what constitutes a pass, what constitutes a finding, and what the threshold is for escalation.

Here is an enterprise example of audit program development. Suppose the audit objective is to evaluate the effectiveness of the organization's change management process for production applications. The relevant control objectives might include: all changes are authorized before implementation, all changes are tested in a non-production environment before deployment, all changes are documented and tracked in the change management system, and emergency changes are subject to retroactive authorization within a defined timeframe.

For each control objective, the audit program would specify one or more audit procedures. For the authorization control objective, the procedure might be: "Select a sample of N changes deployed to production during the audit period. For each change, verify that authorization was obtained from the change advisory board prior to deployment. Document any changes deployed without proper authorization." The program would specify the sample size, the data source for selecting the sample, the documentation that constitutes evidence of authorization, and the responsible auditor.

Exam trap: ISACA may ask what drives the development of the audit program. The correct answer is the audit objectives and the risk assessment. The audit program is not developed in isolation — it is driven by the audit objectives, which are defined during planning, and informed by the risk assessment, which determines where audit effort should be concentrated. A question that asks "what should the IS auditor do FIRST when developing the audit program?" is testing whether you understand that defining objectives and assessing risk precede procedure design.

[SECTION BREAK]

## CONTROL OBJECTIVES MAPPING AND COBIT ALIGNMENT (34:30–38:15)

Control objectives are the specific goals that internal controls are designed to achieve. In the IS audit context, control objectives typically relate to the confidentiality, integrity, and availability of information and information systems. Mapping audit procedures to control objectives ensures that the audit provides comprehensive coverage of the risks relevant to the audit subject.

COBIT — Control Objectives for Information and Related Technology — is ISACA's proprietary framework for IT governance and management, and it is the framework most directly relevant to the CISA exam. COBIT 2019, the current version, organizes IT management and governance activities into forty governance and management objectives across five domains: Evaluate, Direct, and Monitor (EDM); Align, Plan, and Organize (APO); Build, Acquire, and Implement (BAI); Deliver, Service, and Support (DSS); and Monitor, Evaluate, and Assess (MEA).

For the CISA exam, you do not need to memorize all forty objectives, but you must understand the framework's structure and how it relates to audit planning. Specifically, you should understand that COBIT provides a comprehensive set of control objectives that can be used as the basis for developing audit programs. When an IS auditor uses COBIT as the reference framework, the audit program maps its procedures to the relevant COBIT governance and management objectives.

For example, if the audit subject is the organization's IT change management process, the auditor would reference COBIT BAI06 — Managed IT Changes. This management objective describes the control activities that an effective change management process should include — request, classification, prioritization, authorization, testing, implementation, and documentation. The auditor's procedures would then test whether the organization's change management process achieves these control objectives.

COBIT alignment offers several advantages for audit planning. First, it provides a standardized, comprehensive framework that reduces the risk of overlooking critical control areas. Second, it facilitates communication with management and the audit committee because COBIT is widely recognized and understood. Third, it enables benchmarking — comparing the organization's controls against an industry-accepted standard.

However, COBIT alignment is not the only approach. Other frameworks — such as ISO 27001 for information security management, NIST Cybersecurity Framework for cybersecurity risk management, or ITIL for IT service management — may be more appropriate depending on the audit subject and the organization's context. The CISA exam may test whether you understand that the auditor should select the framework most appropriate to the audit subject, rather than defaulting to COBIT in all circumstances.

Exam trap: if a question asks which framework the IS auditor should use as the basis for an information security audit, COBIT is a valid answer — but ISO 27001 may be more directly relevant if the question specifies information security management. Read the question carefully to determine which framework best fits the described scenario.

Mnemonic for the COBIT 2019 domains: "Every Auditor Builds Delivered Metrics." E for EDM, A for APO, B for BAI, D for DSS, M for MEA. Five domains, five words.

[SECTION BREAK]

## PRELIMINARY SURVEY TECHNIQUES (38:15–40:30)

The preliminary survey — sometimes called the preliminary review or planning review — is the initial information-gathering phase that precedes the development of the detailed audit program. During the preliminary survey, the auditor builds an understanding of the audit subject that is sufficient to assess risk, define scope, and design audit procedures.

Preliminary survey techniques include reviewing prior audit reports and management's responses to prior findings. This is often the auditor's first action because prior audit history reveals known control weaknesses, management's track record of remediation, and areas that may require follow-up. The auditor should also review relevant organizational policies, procedures, and standards. Reviewing the organizational chart and understanding reporting relationships helps the auditor assess the governance structure and identify potential independence or segregation-of-duties concerns.

Interviewing key personnel is another essential preliminary survey technique. During planning, the auditor conducts interviews with management and key staff to understand the business processes, technology environment, and control structure. These interviews are not audit tests — they are information-gathering activities that inform the audit plan. The auditor should approach these interviews with professional skepticism, recognizing that management's representations may not fully reflect operational reality.

Walkthroughs are a particularly valuable preliminary survey technique. A walkthrough involves tracing a single transaction or event through the entire process — from initiation to recording — to understand the process flow, identify control points, and verify that the process operates as documented. Walkthroughs help the auditor identify disconnects between documented procedures and actual practice.

Reviewing system documentation — including system architecture diagrams, data flow diagrams, network topology maps, and configuration documentation — provides the auditor with the technical understanding necessary to design appropriate audit procedures. For complex IT environments, the auditor may also request and review security assessment reports, penetration testing results, and vulnerability scan reports.

Exam trap: the exam may ask what the IS auditor should review "first" during the preliminary survey. The correct answer is typically prior audit reports or organizational policies and procedures — sources that provide the auditor with context and background before engaging with personnel or conducting walkthroughs. The sequence matters: review documentation first, then interview personnel, then conduct walkthroughs. This sequence ensures that the auditor arrives at interviews and walkthroughs with sufficient background knowledge to ask informed questions and identify anomalies.

[SECTION BREAK]

## EPISODE SUMMARY AND BRIDGE TO NEXT EPISODE (40:30–42:10)

Let us consolidate. We began with the philosophy of risk-based audit planning — the principle that audit effort follows risk. We decomposed the audit risk model into inherent risk, control risk, and detection risk, and established that the auditor's primary lever is detection risk — adjusted by varying the nature, timing, and extent of audit procedures. We examined materiality as a context-dependent judgment that extends beyond monetary thresholds in IS auditing. We distinguished the engagement letter — external-facing, scope-defining — from the audit planning memorandum — internal-facing, execution-guiding. We worked through qualitative and quantitative risk assessment, drilling into the ALE formula: Asset Value times Exposure Factor equals Single Loss Expectancy, and SLE times Annualized Rate of Occurrence equals Annual Loss Expectancy. We constructed the audit program as the procedural bridge between planning and fieldwork, traceable from procedures to control objectives to audit objectives. We mapped control objectives to COBIT 2019 and other frameworks. And we surveyed preliminary survey techniques — prior reports, policies, interviews, walkthroughs, and system documentation.

In Episode 1.3, we will complete Domain 1 by examining audit evidence, sampling, and documentation. We will classify evidence types, evaluate evidence quality along the dimensions of sufficiency, competence, and relevance, and then go deep on statistical and non-statistical sampling — attribute sampling, variable sampling, stop-or-go sampling, and the relationship between confidence levels and sample sizes. We will also cover Computer-Assisted Audit Techniques, generalized audit software, the test data method, and integrated test facilities. Finally, we will address audit documentation standards, working paper requirements, and the process for developing findings and recommendations.

Before the next episode, practice ALE calculations. Set up several scenarios with different asset values, exposure factors, and annualized rates of occurrence, and compute the ALE for each. Speed and accuracy on these calculations will earn you easy points on exam day.

This has been Episode 1.2 of the CISA Exam Preparation Podcast. I will see you in the next episode.

---
*This episode references content aligned with the ISACA CISA Review Manual (27th/28th Edition), ISACA IS Auditing Standards (Standard 1202: Planning, Standard 1203: Performance and Supervision), COBIT 2019, NIST SP 800-30 (Guide for Conducting Risk Assessments), and ISO 27005 (Information Security Risk Management). All framework references are traceable to the cited publications.*
