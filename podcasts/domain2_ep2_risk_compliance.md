# Episode 2.2 — IT Risk Management & Compliance

**Domain 2: Governance and Management of IT**
**Duration: 38:45**
**Series: CISA Exam Mastery Podcast**

---

## INTRODUCTION (0:00 – 2:15)

Welcome to Episode 2.2 of the CISA Exam Mastery Podcast. In the previous episode, we established the governance frameworks — COBIT, ITIL, TOGAF — that provide the structural foundation for IT oversight. In this episode, we turn to what many practitioners consider the operational heart of IT governance: risk management and compliance.

Risk management is not an isolated function. It is embedded in every governance decision, every IT investment, every change to the technology landscape. When the board approves an IT strategy, it is implicitly accepting a risk profile. When management deploys a new cloud service, it is implicitly modifying the organization's threat surface. The question for the IS auditor is whether these risk implications are identified, assessed, treated, and monitored with the rigor that the enterprise's risk appetite demands.

In the next thirty-eight minutes, we will cover IT risk management frameworks — ISO 31000, the NIST Risk Management Framework, and ISACA's Risk IT. We will perform a detailed walkthrough of risk identification, risk analysis (both quantitative and qualitative), and risk treatment. We will address organizational constructs including risk appetite, risk tolerance, Key Risk Indicators, and the risk register. Then we will shift to IT compliance management, covering the regulatory landscape — SOX Section 404, PCI-DSS, HIPAA, and GDPR — and the relationship between internal audit, external audit, and compliance functions. We will close with third-party risk management, which has become an increasingly prominent exam topic as organizations extend their risk perimeters through outsourcing, cloud services, and vendor dependencies.

This is material the exam tests at an applied level. You will not simply be asked to define "risk appetite." You will be presented with a scenario and asked to determine whether the organization's risk management practices are adequate. Let us build the analytical framework you need.

[SECTION BREAK]

## SECTION 1: IT RISK MANAGEMENT FRAMEWORKS (2:15 – 10:00)

Three risk management frameworks dominate the CISA exam: ISO 31000, the NIST Risk Management Framework, and ISACA's Risk IT. Each serves a different purpose, and the competent IS auditor understands when and how each applies.

**ISO 31000 — Risk Management Guidelines**

ISO 31000 provides a universal framework for risk management that is not specific to IT. It is important precisely because it establishes the enterprise-wide risk management principles within which IT risk management operates. The current version, ISO 31000:2018, defines risk as the "effect of uncertainty on objectives" — notice that this definition is neutral. Risk is not inherently negative; it encompasses both threats (negative effects) and opportunities (positive effects). The CISA exam occasionally tests this nuance.

ISO 31000 establishes eight principles for risk management: it should be integrated into organizational processes, structured and comprehensive, customized to the organization, inclusive of stakeholders, dynamic and responsive to change, based on the best available information, cognizant of human and cultural factors, and subject to continual improvement.

The framework itself defines three core components: principles (why you manage risk), a framework (how you structure risk management), and a process (what you do). The risk management process follows a sequence: scope-context-criteria definition, risk assessment (comprising risk identification, risk analysis, and risk evaluation), risk treatment, and then monitoring-review and communication-consultation as ongoing activities that interact with all process steps.

For the IS auditor, ISO 31000 provides the basis for evaluating whether an organization's IT risk management is integrated with enterprise risk management. A common audit finding is IT risk managed in a silo — the CISO maintains a risk register that is disconnected from the enterprise risk register, risk appetite for IT is not derived from the board-level risk appetite statement, and IT risk reporting does not flow into enterprise risk reporting. ISO 31000 integration means IT risk is a subset of enterprise risk, governed by the same principles and reported through the same structures.

**NIST Risk Management Framework (RMF)**

The NIST Risk Management Framework, codified in NIST Special Publication 800-37 Revision 2, provides a structured process for integrating security, privacy, and cyber supply chain risk management into the system development lifecycle. While originally designed for U.S. federal information systems, the NIST RMF has been widely adopted by private sector organizations, particularly those in regulated industries.

The RMF consists of seven steps, and I strongly recommend committing them to memory for the exam. They are: Prepare, Categorize, Select, Implement, Assess, Authorize, and Monitor.

Step one — Prepare — establishes the context and priorities for managing security and privacy risk at both the organization level and the system level. This step, added in Revision 2, reflects the recognition that risk management requires organizational preparation before system-level activities begin.

Step two — Categorize — determines the security categorization of the information system based on the potential impact of a loss of confidentiality, integrity, or availability. This uses the methodology defined in FIPS 199 and NIST SP 800-60. The categorization drives the entire RMF process because it determines the baseline set of security controls.

Step three — Select — identifies the security controls for the system based on the categorization, tailoring the baseline controls as appropriate and supplementing them with additional controls based on organizational risk assessment.

Step four — Implement — puts the selected controls into operation within the information system and its operational environment.

Step five — Assess — evaluates whether the controls are implemented correctly, operating as intended, and producing the desired outcome with respect to meeting security and privacy requirements.

Step six — Authorize — is the risk acceptance decision. A senior official — the Authorizing Official — reviews the security assessment results and determines whether the residual risk is acceptable. This is a critical governance decision: the Authorizing Official is explicitly accepting accountability for the risk associated with operating the system.

Step seven — Monitor — provides ongoing awareness of the security and privacy posture of the information system through continuous monitoring of controls, changes to the system and environment, and compliance with legislation, regulations, and policies.

Here is a mnemonic for the seven RMF steps: "People Can Select Intelligent Approaches, Authorizing Monitoring." Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor. Alternatively, more simply: "Please Can Someone Implement A Authorize Monitor" — though I recommend the first version for precision.

For the exam, the most important concept in the RMF is the authorization decision in step six. The Authorizing Official does not need to eliminate all risk — that is impossible. The Authorizing Official determines whether the residual risk, after controls are implemented, falls within the organization's risk tolerance. This is a governance decision, not a technical decision, and the exam expects you to understand that distinction.

**ISACA Risk IT Framework**

ISACA's Risk IT framework — now integrated into COBIT 2019 — provides IT-specific risk management guidance. Risk IT defines three domains: Risk Governance (ensuring that IT risk management practices are embedded in the enterprise), Risk Evaluation (ensuring that IT-related risks and opportunities are identified, analyzed, and presented in business terms), and Risk Response (ensuring that IT-related risk issues, opportunities, and events are responded to in a cost-effective manner aligned with business priorities).

The key contribution of Risk IT, and the aspect most likely to appear on the exam, is its insistence that IT risk must be expressed in business terms. A statement like "we have three unpatched critical vulnerabilities on internet-facing servers" is a technical finding. A Risk IT-compliant risk statement would be: "failure to patch critical vulnerabilities on internet-facing servers exposes the organization to potential data breach resulting in estimated financial impact of two to five million dollars and regulatory sanctions." The IS auditor should evaluate whether IT risk reporting translates technical findings into business impact language that governance bodies can act upon.

**Exam Trap**: The exam may present a scenario where an organization has implemented ISO 27005 for information security risk management and ask whether a separate IT risk framework is needed. ISO 27005 addresses information security risk specifically; Risk IT and ISO 31000 address IT risk more broadly, including project risk, investment risk, and service delivery risk. Security risk is a subset of IT risk, and a comprehensive risk management approach requires more than security risk assessment alone.

[SECTION BREAK]

## SECTION 2: RISK IDENTIFICATION TECHNIQUES (10:00 – 15:00)

Risk identification is the process of finding, recognizing, and describing risks. It is the first step in risk assessment, and its quality determines the quality of everything that follows. You cannot analyze or treat a risk you have not identified.

**Threat Modeling**

Threat modeling is a structured approach to identifying threats to information systems and the vulnerabilities that those threats might exploit. Several methodologies exist — STRIDE, PASTA, VAST, and attack trees among them — but the CISA exam focuses on the concept rather than specific methodologies.

STRIDE, developed by Microsoft, categorizes threats into six types: Spoofing identity, Tampering with data, Repudiation, Information disclosure, Denial of service, and Elevation of privilege. The mnemonic is the word STRIDE itself. This taxonomy provides a structured checklist for identifying threats to a system or application.

For the IS auditor, the audit question is not "did the organization use STRIDE?" but "did the organization systematically identify threats, or did they rely on ad hoc, incomplete threat identification?" A threat model should be documented, reviewed, and updated when the system changes. If an organization deploying a new customer-facing web application cannot produce a threat model or equivalent threat identification artifact, the auditor should question whether the associated risks have been adequately identified and assessed.

**Vulnerability Assessment**

Vulnerability assessment identifies weaknesses in systems, networks, and applications that could be exploited by threats. This includes technical vulnerability scanning (using tools such as Nessus, Qualys, or OpenVAS), configuration reviews, code reviews, and architecture reviews.

The IS auditor evaluates not only whether vulnerability assessments are performed, but whether they are performed with adequate scope, frequency, and follow-through. Common audit findings include: vulnerability scans that exclude critical systems, assessments performed annually when the risk profile warrants quarterly or continuous assessment, and vulnerability findings that remain unaddressed for extended periods without documented risk acceptance.

A critical nuance for the exam: vulnerability assessment identifies weaknesses, while penetration testing attempts to exploit them. Vulnerability assessment tells you "this weakness exists"; penetration testing tells you "this weakness is exploitable and here is the potential impact." The exam expects you to distinguish between the two and understand that a comprehensive risk identification program includes both.

**Other Risk Identification Techniques**

Beyond threat modeling and vulnerability assessment, risk identification techniques include: risk workshops and brainstorming sessions with business and IT stakeholders, analysis of historical incident data and loss event databases, scenario analysis (postulating plausible risk events and tracing their potential impact), control self-assessments (where process owners evaluate the effectiveness of controls within their areas), and review of external threat intelligence feeds and industry risk reports.

The IS auditor should evaluate whether the organization uses multiple risk identification techniques appropriate to its risk profile and whether risk identification is an ongoing process rather than an annual exercise. In a dynamic threat landscape, an organization that identifies risks only during annual risk assessments is almost certainly operating with an incomplete risk picture.

[SECTION BREAK]

## SECTION 3: RISK ANALYSIS — QUANTITATIVE AND QUALITATIVE (15:00 – 23:00)

Once risks are identified, they must be analyzed to determine their magnitude and priority. Risk analysis takes two fundamental forms: quantitative and qualitative. The CISA exam tests both extensively, and the quantitative formulas are among the most frequently tested calculations in the entire exam.

**Quantitative Risk Analysis**

Quantitative risk analysis expresses risk in monetary terms. It requires three foundational values.

The Single Loss Expectancy, or SLE, is the expected monetary loss each time a risk event occurs. It is calculated as: SLE equals Asset Value multiplied by the Exposure Factor. The Exposure Factor, or EF, is the percentage of asset value lost when the risk event occurs, expressed as a decimal between zero and one.

The Annualized Rate of Occurrence, or ARO, is the estimated frequency with which a risk event will occur per year. An event expected to occur twice per year has an ARO of 2. An event expected to occur once every five years has an ARO of 0.2.

The Annualized Loss Expectancy, or ALE, is the expected annual monetary loss from a specific risk. It is calculated as: ALE equals SLE multiplied by ARO. Alternatively, ALE equals Asset Value multiplied by Exposure Factor multiplied by ARO.

Let me work through a concrete example. An organization has a database server valued at five hundred thousand dollars. A risk assessment identifies the risk of a hard drive failure that would destroy thirty percent of the data before recovery from backups. The exposure factor is 0.30. The SLE is five hundred thousand multiplied by 0.30, which equals one hundred fifty thousand dollars. Historical data suggests this type of failure occurs approximately once every three years, so the ARO is 0.33. The ALE is one hundred fifty thousand multiplied by 0.33, which equals approximately forty-nine thousand five hundred dollars per year.

Now, the real power of quantitative analysis becomes apparent when evaluating controls. Suppose a RAID storage upgrade costing twenty thousand dollars per year would reduce the exposure factor from 0.30 to 0.05. The new SLE would be twenty-five thousand dollars, the new ALE would be approximately eight thousand two hundred fifty dollars, and the annual risk reduction would be forty-nine thousand five hundred minus eight thousand two hundred fifty, equaling forty-one thousand two hundred fifty dollars. Since the control costs twenty thousand dollars per year and provides forty-one thousand two hundred fifty dollars in annual risk reduction, the control is cost-effective with a net benefit of approximately twenty-one thousand two hundred fifty dollars per year.

This cost-benefit analysis is fundamental to the IS auditor's evaluation of control adequacy. A control that costs more than the risk it mitigates is not cost-effective — unless there are regulatory or reputational considerations that justify the expenditure beyond pure financial analysis.

**Exam Trap on Quantitative Analysis**: The exam may present a scenario where the calculated ALE is lower than the cost of a proposed control and ask what the auditor should recommend. The straightforward answer is that the control is not cost-effective based on quantitative analysis alone. However — and this is the trap — the exam may include additional context suggesting regulatory requirements or reputational risk that cannot be easily quantified. In such cases, the correct answer acknowledges that quantitative analysis supports one conclusion but qualitative factors may justify a different decision. Never treat quantitative analysis as the sole basis for risk decisions when the scenario includes non-quantifiable factors.

**Qualitative Risk Analysis**

Qualitative risk analysis assesses risk using descriptive scales rather than monetary values — typically scales such as high-medium-low or one-through-five. The most common qualitative tool is the risk heat map, which plots risks on a two-dimensional matrix with likelihood on one axis and impact on the other.

Qualitative analysis is used when: quantitative data is unavailable or unreliable, the risk involves intangible impacts (reputational damage, loss of customer trust) that resist monetary quantification, or the organization needs a rapid initial assessment to prioritize risks for more detailed analysis.

The IS auditor should understand that qualitative and quantitative approaches are complementary, not competing. A mature risk management program uses qualitative analysis for initial screening and prioritization, then applies quantitative analysis to the highest-priority risks where data supports monetary estimation. Organizations that rely exclusively on qualitative analysis may lack the precision needed for cost-benefit decisions. Organizations that insist on quantifying everything may waste resources trying to monetize risks that are better assessed qualitatively.

For the exam, remember the following distinction: qualitative analysis is *subjective* but *efficient*, while quantitative analysis is *objective* but *data-intensive*. The exam may present a scenario where an organization lacks historical loss data and ask which risk analysis approach is more appropriate. The answer is qualitative, because quantitative analysis requires historical frequency and impact data that is unavailable.

**Risk Evaluation**

After analysis, risks must be evaluated — that is, compared against risk criteria to determine which risks require treatment and in what priority. Risk evaluation uses the organization's risk appetite and risk tolerance as the benchmarks. Risks that exceed the risk appetite require treatment; risks within the risk appetite may be accepted. We will discuss risk appetite and tolerance in detail shortly.

[SECTION BREAK]

## SECTION 4: RISK TREATMENT OPTIONS (23:00 – 27:00)

Risk treatment is the process of selecting and implementing measures to modify risk. ISO 31000 and ISACA identify four fundamental risk treatment options, and the exam expects you to apply them to scenarios with precision.

**Risk Mitigation** (also called risk reduction or risk modification) involves implementing controls to reduce the likelihood or impact of a risk event. This is the most common treatment option and the one IS auditors evaluate most frequently. Examples include implementing access controls to reduce the likelihood of unauthorized access, deploying backup systems to reduce the impact of data loss, and hardening server configurations to reduce vulnerability exposure. The key audit question is whether the selected controls reduce risk to within the organization's risk tolerance in a cost-effective manner.

**Risk Transfer** (also called risk sharing) involves shifting the financial consequence of a risk to a third party. The most common forms are insurance and contractual transfer (such as indemnification clauses in vendor contracts). Outsourcing operational risk to a managed service provider is another form of risk transfer, though — and this is a critical exam point — outsourcing transfers operational execution but does not transfer accountability. The organization remains accountable for the risk even when a third party is performing the operational function. If a question asks "does outsourcing a function eliminate the organization's risk," the answer is emphatically no. Risk transfer shifts financial consequences; it does not eliminate risk or accountability.

**Risk Acceptance** involves consciously deciding to retain a risk without additional treatment, typically because the risk falls within the organization's risk appetite or because the cost of treatment exceeds the potential benefit. Risk acceptance must be a deliberate, documented decision made by an individual with appropriate authority — not a passive failure to address risk. The IS auditor should verify that accepted risks have been formally documented, approved by appropriate management (commensurate with the magnitude of the risk), and are subject to periodic reassessment. An organization that has not formally accepted a risk but has not treated it either has an unmanaged risk — which is an audit finding.

**Risk Avoidance** involves eliminating the activity or condition that gives rise to the risk. Examples include discontinuing a product line that creates unacceptable regulatory risk, declining to enter a market that presents unmanageable operational risks, or choosing not to adopt a technology that introduces risks the organization is not prepared to manage. Risk avoidance is appropriate when the risk exceeds the organization's risk appetite and cannot be adequately reduced through mitigation or transfer. The IS auditor should recognize that risk avoidance has an opportunity cost — by avoiding the risk, the organization also forgoes the potential benefits of the activity.

**Exam Trap on Risk Treatment**: The exam may present a scenario where management decides to "ignore" a risk or "hopes it won't happen." Neither of these constitutes a valid risk treatment option. Risk acceptance is a valid option, but it requires conscious deliberation, documented rationale, and appropriate authorization. Ignoring a risk is not acceptance — it is a governance failure.

[SECTION BREAK]

## SECTION 5: RISK APPETITE, RISK TOLERANCE, AND KEY RISK INDICATORS (27:00 – 31:00)

**Risk Appetite vs. Risk Tolerance**

These terms are frequently confused, and the exam tests the distinction explicitly.

Risk appetite is the broad-based amount of risk an organization is willing to accept in pursuit of its objectives. It is set by the governing body — the board — and reflects the organization's strategic posture toward risk. A risk appetite statement might read: "The organization accepts moderate risk in pursuit of growth opportunities but has zero appetite for risk that could result in regulatory sanctions or material financial misstatement."

Risk tolerance is the acceptable variation in outcomes relative to a specific objective. It is more granular and quantifiable than risk appetite. For example, within an overall moderate risk appetite, a specific risk tolerance might be: "system downtime shall not exceed four hours per quarter" or "financial losses from cybersecurity incidents shall not exceed one hundred thousand dollars per year."

The relationship is hierarchical: risk appetite is the enterprise-level statement set by the board; risk tolerance is the objective-level threshold set by management within the boundaries of the risk appetite. An IS auditor evaluates whether risk tolerances are defined for key IT objectives, whether they are consistent with the board-level risk appetite, and whether actual risk exposure is monitored against defined tolerances.

Here is a practical mnemonic: Risk appetite is *how hungry you are for risk* (strategic, qualitative, board-level). Risk tolerance is *how much you can actually stomach* (operational, quantitative, management-level).

**Key Risk Indicators (KRIs)**

Key Risk Indicators are metrics that provide early warning of increasing risk exposure. They differ from Key Performance Indicators (KPIs) in their orientation: KPIs measure performance against objectives (backward-looking), while KRIs signal potential future risk events (forward-looking).

Effective KRIs have several characteristics: they are measurable, they correlate with specific risks, they have defined thresholds that trigger management action, and they are reported at an appropriate frequency. Examples of IT KRIs include: number of critical vulnerabilities unpatched beyond SLA, percentage of systems with outdated antivirus signatures, number of failed access attempts exceeding baseline, staff turnover rate in critical IT positions, and number of change-related incidents as a percentage of total changes.

For the IS auditor, the audit of KRIs focuses on whether: KRIs are defined for the organization's most significant IT risks, thresholds are calibrated to provide adequate early warning (too sensitive causes alert fatigue, too insensitive fails to provide timely warning), KRIs are regularly monitored and reported to appropriate governance bodies, and escalation procedures are defined and followed when KRI thresholds are breached.

**The Risk Register**

The risk register is the central repository for all identified risks, their assessments, treatment plans, owners, and status. It is a living document — or, more commonly, a database record in a GRC platform — that must be maintained and updated as risks evolve.

A well-maintained risk register includes, for each risk: a unique identifier, a description of the risk event, the risk category, the risk owner (a named individual accountable for managing the risk), the inherent risk rating (before controls), the control environment and its effectiveness, the residual risk rating (after controls), the risk treatment plan, the status of treatment actions, and the date of last review.

The IS auditor evaluates the risk register for completeness (are all significant risks captured?), accuracy (are ratings current and defensible?), ownership (are risk owners appropriate and actively engaged?), and timeliness (is the register reviewed and updated at appropriate intervals?). A risk register that has not been updated in twelve months is, for practical purposes, unreliable, and the auditor should note this as a finding.

[SECTION BREAK]

## SECTION 6: IT COMPLIANCE MANAGEMENT AND THE REGULATORY LANDSCAPE (31:00 – 35:30)

**The Compliance Management Function**

IT compliance management ensures that the organization meets its legal, regulatory, contractual, and policy obligations related to information technology. In mature organizations, compliance management is a structured function with defined processes for: identifying applicable requirements, mapping requirements to controls, assessing compliance status, remediating gaps, and reporting compliance status to governance bodies.

The IS auditor evaluates whether the compliance function is adequately resourced, whether the organization maintains a current inventory of applicable requirements, and whether there is a systematic process for translating regulatory requirements into operational controls. A common audit finding is that compliance is treated as a periodic exercise — assessed before an audit and then neglected — rather than as a continuous management responsibility.

**SOX Section 404 — IT Implications in Depth**

We introduced SOX in the previous episode from a governance perspective. Here, we examine it from a compliance and risk perspective. Section 404 requires management's annual assessment of internal controls over financial reporting, attested by the external auditor.

For IT, this means that IT general controls — access controls, change management, computer operations, and program development — must be documented, tested, and evidenced for all systems in the financial reporting chain. The IS auditor plays a critical role in evaluating these controls and identifying deficiencies. Deficiencies are classified as: a control deficiency (a weakness that does not rise to the level of a significant deficiency), a significant deficiency (a deficiency or combination of deficiencies that is less severe than a material weakness but warrants attention from those responsible for oversight), or a material weakness (a deficiency or combination that creates a reasonable possibility that a material misstatement will not be prevented or detected on a timely basis).

Understanding this classification hierarchy is essential for the exam, because the classification determines the reporting obligation and the urgency of remediation.

**PCI-DSS**

The Payment Card Industry Data Security Standard applies to any organization that processes, stores, or transmits cardholder data. PCI-DSS defines twelve requirements organized under six control objectives: build and maintain a secure network and systems, protect cardholder data, maintain a vulnerability management program, implement strong access control measures, regularly monitor and test networks, and maintain an information security policy.

For the IS auditor, PCI-DSS is notable because it is prescriptive — unlike SOX, which requires effective controls without specifying exactly what they must be, PCI-DSS specifies detailed technical requirements such as encryption standards, password policies, and log retention periods. The audit approach differs accordingly: SOX audits evaluate whether controls are effective regardless of implementation specifics, while PCI-DSS assessments verify compliance with specific prescribed requirements.

**HIPAA**

The Health Insurance Portability and Accountability Act applies to covered entities and their business associates that handle protected health information. The HIPAA Security Rule requires administrative, physical, and technical safeguards to ensure the confidentiality, integrity, and availability of electronic protected health information. Unlike PCI-DSS, HIPAA safeguards are expressed as "addressable" or "required" — addressable safeguards must be implemented or the organization must document why an equivalent alternative is appropriate. This flexibility introduces audit judgment into HIPAA compliance assessments.

**GDPR Compliance Operations**

From a compliance operations perspective, GDPR requires organizations to demonstrate accountability through documented policies and procedures, records of processing activities, data protection impact assessments for high-risk processing, and evidence of "privacy by design and by default." The seventy-two-hour breach notification requirement imposes operational demands on incident response processes, and the IS auditor should evaluate whether the incident response plan includes GDPR notification procedures and whether the organization can realistically detect, assess, and report a breach within the seventy-two-hour window.

**Internal vs. External Audit Coordination**

The IS auditor must understand the relationship between internal and external audit in the compliance context. Internal audit provides independent assurance to management and the board. External audit provides assurance to external stakeholders — shareholders, regulators, the public. While their mandates differ, coordination between internal and external audit improves efficiency and reduces audit fatigue.

The audit committee plays a critical role in this coordination, ensuring that internal and external audit plans are aligned, that audit findings are tracked and remediated, and that both functions have adequate independence and resources. The IS auditor should evaluate whether the audit committee has sufficient IT competence to oversee IT-related audit activities and whether it receives regular reporting on IT risk, control effectiveness, and compliance status.

**Management's Role in Risk Ownership**

A principle the exam tests repeatedly is that risk ownership belongs to management, not to the IS auditor or the IT function. The board sets risk appetite, management owns risk within that appetite, and the IS auditor provides independent assurance on the effectiveness of risk management. If a question asks "who is responsible for managing IT risk," the answer is management — specifically, the risk owners identified in the risk register, supported by the CISO for security risks and the CIO for broader IT risks. The IS auditor identifies and reports on risk management deficiencies but does not own or manage risks.

[SECTION BREAK]

## SECTION 7: THIRD-PARTY RISK MANAGEMENT (35:30 – 38:00)

Third-party risk management has become one of the most significant topics in IT governance and one of increasing emphasis on the CISA exam. As organizations outsource IT functions, adopt cloud services, and rely on complex supply chains, the risk perimeter extends well beyond organizational boundaries.

**Vendor Risk Assessment**

Vendor risk assessment is the process of evaluating the risks associated with engaging a third-party service provider. The assessment should occur before contract execution (due diligence), during the engagement (ongoing monitoring), and at contract termination (exit management).

Pre-contract due diligence includes: evaluating the vendor's financial stability, reviewing the vendor's security posture (through questionnaires, certifications such as SOC 2 Type II reports, and potentially on-site assessments), assessing the vendor's regulatory compliance status, evaluating the vendor's business continuity and disaster recovery capabilities, and reviewing the vendor's subcontracting practices (fourth-party risk).

The IS auditor evaluates whether the organization has a structured vendor risk assessment process, whether assessments are commensurate with the criticality of the service and the sensitivity of data involved, and whether assessment results influence vendor selection decisions. An organization that performs due diligence after contract execution has inverted the process — risk assessment should inform the engagement decision, not validate it after the fact.

**Ongoing Vendor Monitoring**

Due diligence at contract inception is necessary but insufficient. The risk profile of a vendor relationship changes over time as the vendor's own risk environment evolves, as the services provided expand or contract, and as the regulatory landscape shifts. Ongoing monitoring mechanisms include: periodic reassessment (annually at minimum for critical vendors), review of SOC reports and security certifications, monitoring of vendor performance against SLAs, tracking vendor-related incidents, and maintaining awareness of vendor financial stability and market position.

**Contractual Risk Provisions**

The contract is the primary risk management tool in a vendor relationship. From an IS audit perspective, critical contractual provisions include: right to audit clauses (enabling the organization or its auditor to examine the vendor's controls), data protection and security requirements, incident notification obligations (aligned with the organization's regulatory obligations such as GDPR's seventy-two-hour requirement), business continuity and disaster recovery commitments, data ownership and portability provisions (ensuring the organization retains ownership of its data and can retrieve it upon contract termination), subcontracting restrictions (controlling fourth-party risk), and termination and transition assistance provisions.

**Exam Trap on Third-Party Risk**: The exam may present a scenario where an organization argues that because it has outsourced a function to a reputable vendor with strong security certifications, the associated risk has been eliminated. This is incorrect. Outsourcing transfers operational execution but not accountability. The organization remains responsible for ensuring that the vendor manages risk in accordance with the organization's requirements. The IS auditor should verify that this accountability is understood and operationalized through contractual provisions, monitoring activities, and governance oversight.

A useful mnemonic for third-party risk management: "DCOM" — Due diligence before, Contractual provisions during, Ongoing monitoring throughout, and Management accountability always.

[SECTION BREAK]

## SUMMARY AND BRIDGE (38:00 – 38:45)

Let us consolidate this episode. IT risk management operates within a framework hierarchy: ISO 31000 provides enterprise-wide risk management principles, the NIST RMF provides a structured seven-step process for system-level risk management, and ISACA Risk IT provides IT-specific risk governance guidance. Risk assessment comprises identification (threat modeling, vulnerability assessment), analysis (quantitative using ALE equals SLE times ARO, and qualitative using heat maps and ordinal scales), and evaluation (comparing analyzed risks against risk appetite and tolerance). Risk treatment offers four options: mitigate, transfer, accept, or avoid — and acceptance requires deliberate, documented, authorized decision-making, not passive neglect. Key Risk Indicators provide forward-looking risk metrics, and the risk register serves as the central repository for risk information. Compliance management ensures adherence to SOX, PCI-DSS, HIPAA, GDPR, and other applicable requirements, coordinated through internal and external audit functions overseen by the audit committee. And third-party risk management extends the risk management perimeter to vendors and service providers through due diligence, contractual provisions, and ongoing monitoring.

Your master mnemonic for this episode: "Identify, Analyze, Treat, Monitor — Appetite Governs, Tolerance Bounds, Owners Manage, Auditors Assure."

This concludes Domain 2 of the CISA Exam Mastery Podcast. In Domain 3, we will turn to Information Systems Acquisition, Development, and Implementation — the domain that examines how organizations build, buy, and deploy information systems. We will cover the system development lifecycle, project management methodologies, business case development, and the IS auditor's role throughout the acquisition and implementation process.

Thank you for your discipline in working through this material. The governance and risk management concepts we have covered in these two episodes provide the analytical foundation for every audit engagement you will encounter — both on the exam and in practice.

---

*This episode references: ISACA CISA Review Manual (27th Edition), ISO 31000:2018 — Risk Management Guidelines, NIST SP 800-37 Rev. 2 — Risk Management Framework for Information Systems and Organizations, NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments, ISACA Risk IT Framework, FIPS 199 — Standards for Security Categorization, SOX Section 404, PCI-DSS v4.0, HIPAA Security Rule (45 CFR Part 164), GDPR (Regulation EU 2016/679), ISO/IEC 27005:2022 — Information Security Risk Management.*
