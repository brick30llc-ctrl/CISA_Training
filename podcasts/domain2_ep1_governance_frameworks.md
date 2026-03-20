# Episode 2.1 — IT Governance Frameworks: COBIT, ITIL, and Enterprise Architecture

**Domain 2: Governance and Management of IT**
**Duration: 45:00**
**Series: CISA Exam Mastery Podcast**

---

## INTRODUCTION (0:00 – 2:30)

Welcome back to the CISA Exam Mastery Podcast. This is Episode 2.1, and we are entering Domain 2 — Governance and Management of IT. This domain accounts for sixteen percent of the CISA exam, which translates to roughly thirty-two questions. If Domain 1 was about understanding the audit process, Domain 2 is about understanding *what you are auditing* — the governance structures, the management frameworks, and the strategic alignment mechanisms that determine whether an organization's IT function actually serves the enterprise or merely consumes its resources.

In this episode, we are going to spend a full forty-five minutes dissecting IT governance frameworks. We will begin with the foundational distinction between governance and management — a distinction that ISACA treats as non-negotiable and that the exam will test you on in subtle, sometimes adversarial ways. We will then perform a deep technical walkthrough of COBIT 2019, ITIL 4, enterprise architecture frameworks including TOGAF and Zachman, and the organizational structures — steering committees, balanced scorecards, strategic alignment models — that bring governance from theory into operational practice. We will close with regulatory and compliance governance, particularly the IT implications of SOX and GDPR.

Let me be direct with you: this episode is dense. The governance domain is where ISACA distinguishes between candidates who memorized definitions and those who understand how enterprise IT actually operates. I am going to give you the depth you need to be in the latter category.

Let us begin.

[SECTION BREAK]

## SECTION 1: IT GOVERNANCE VS. IT MANAGEMENT — THE FOUNDATIONAL DISTINCTION (2:30 – 8:00)

The single most important conceptual distinction in Domain 2 is between governance and management. ISACA draws this line with surgical precision, and the CISA exam will test whether you understand it at a functional level, not merely a definitional one.

IT governance is the system by which the board of directors and executive leadership evaluate, direct, and monitor the use of information technology to support enterprise objectives. Notice the three operative verbs: evaluate, direct, monitor. These are governance activities. They belong to the governing body — the board, the audit committee, executive leadership. Governance answers the question: *Are we doing the right things?*

IT management, by contrast, is the system by which management plans, builds, runs, and monitors IT activities in alignment with the direction set by the governing body. The operative verbs here are plan, build, run, monitor. Notice that "monitor" appears in both — but governance monitoring is oversight of management performance, while management monitoring is operational oversight of IT activities. Management answers the question: *Are we doing things right?*

This distinction comes directly from ISO/IEC 38500, the international standard for governance of information technology, and ISACA has adopted it wholesale into the CISA Review Manual and COBIT 2019. When you see an exam question that asks "whose responsibility is it to ensure IT strategy aligns with business objectives," the answer is the governing body. When the question asks "whose responsibility is it to implement the IT strategy," the answer is management.

Here is the exam trap, and I want you to internalize this: the exam will present scenarios where management is performing governance activities, or where the board is performing management activities, and ask you to identify the problem. A common scenario is a CIO who sets IT strategic direction without board approval. The issue is not that the CIO lacks competence — the issue is that strategic direction-setting is a governance activity that requires governing body involvement. Conversely, if the board is approving individual project timelines or selecting specific vendors, they are performing management activities and have crossed the governance boundary.

The practical implication for the IS auditor is significant. When you audit IT governance, you are not auditing whether servers are patched or whether change management tickets are properly documented. You are auditing whether the organization has structures, processes, and relational mechanisms that ensure IT decisions are made at the appropriate level, with appropriate accountability, in alignment with enterprise objectives. You are auditing the *system of governance*, not the technical controls.

Let me give you a real-world anchoring example. Consider a large financial services firm. The board has an IT strategy committee that meets quarterly to review IT investment portfolios, assess alignment with the firm's digital transformation strategy, and evaluate key risk indicators related to technology. That is governance. The CIO, reporting to that committee, manages a portfolio management office that prioritizes projects, allocates resources, and tracks delivery metrics. That is management. If the IS auditor finds that the IT strategy committee has not met in two quarters and the CIO has been making strategic investment decisions unilaterally, the audit finding is a governance deficiency — specifically, a failure of the governing body to fulfill its evaluate-direct-monitor responsibilities.

One more nuance before we move on. ISACA distinguishes between governance *of* IT and governance *through* IT. Governance of IT is what we have been discussing — oversight of the IT function. Governance through IT refers to situations where IT enables broader enterprise governance — for example, an enterprise GRC platform that enables compliance monitoring, or a data analytics capability that supports board-level decision-making. The exam may test this distinction, though it does so infrequently.

[SECTION BREAK]

## SECTION 2: COBIT 2019 — COMPREHENSIVE FRAMEWORK WALKTHROUGH (8:00 – 22:00)

We now turn to COBIT 2019, which is ISACA's flagship governance framework and the single most heavily tested framework in Domain 2. If you learn one framework thoroughly for the CISA exam, it must be COBIT.

COBIT stands for Control Objectives for Information and Related Technologies. The 2019 version — sometimes referred to as COBIT 2019 to distinguish it from COBIT 5, which preceded it — represents a significant evolution in how ISACA conceptualizes IT governance. Let me walk you through its architecture systematically.

**The Governance System and Its Principles**

COBIT 2019 is built on a governance system that operates according to six principles. These six principles replace the five principles of COBIT 5, and the exam will expect you to know them. They are: first, provide stakeholder value; second, holistic approach; third, dynamic governance system; fourth, governance distinct from management; fifth, tailored to enterprise needs; sixth, end-to-end governance system.

Let me unpack the ones most likely to appear on the exam.

The first principle — provide stakeholder value — establishes that the governance system exists to create value for stakeholders. Value in COBIT is defined through a benefits-risk-resource optimization triangle. The governance system must optimize the realization of benefits, the optimization of risk, and the optimization of resource utilization. When the exam asks about the primary purpose of IT governance, the answer traces back to stakeholder value creation through this tripartite optimization.

The third principle — dynamic governance system — is new to COBIT 2019 and reflects a recognition that governance cannot be static. When design factors change — and we will discuss design factors momentarily — the governance system must adapt. This principle is ISACA's acknowledgment that a governance framework designed for a stable manufacturing firm in 2015 may be inadequate for the same firm in 2025 after it has undergone digital transformation, cloud migration, and significant regulatory change. The practical implication for the IS auditor is that you should evaluate not only whether a governance system is adequate today, but whether it has mechanisms to adapt as the enterprise evolves.

The fourth principle — governance distinct from management — is the distinction we discussed in the previous section, now enshrined as a core COBIT principle.

**The Components of the Governance System**

COBIT 2019 identifies seven components that constitute a governance system. In COBIT 5, these were called "enablers." The terminology change is important — the exam may try to trick you by using the old term.

The seven components are: processes; organizational structures; principles, policies, and frameworks; information; culture, ethics, and behavior; people, skills, and competencies; and services, infrastructure, and applications.

Let me emphasize processes because they receive the most exam attention. COBIT 2019 defines forty governance and management objectives, organized into five domains. The governance domain is called "Evaluate, Direct and Monitor" — abbreviated EDM — and it contains five objectives, EDM01 through EDM05. The four management domains are: Align, Plan and Organize (APO), with fourteen objectives; Build, Acquire and Implement (BAI), with eleven objectives; Deliver, Service and Support (DSS), with six objectives; and Monitor, Evaluate and Assess (MEA), with four objectives.

You do not need to memorize all forty objectives for the exam, but you need to understand the domain structure and be able to identify which domain a given activity belongs to. For example, if a question describes an organization defining its IT risk appetite, that falls under EDM03 — Ensured Risk Optimization — in the governance domain. If a question describes an organization implementing a new ERP system, that falls under BAI in the management domain.

Here is a mnemonic for the five COBIT 2019 domains: "Every Day Makes A Better Delivery System, Monitored Efficiently Always." EDM, APO, BAI, DSS, MEA. Alternatively, simply remember the verbs: Evaluate-Direct-Monitor for governance, and the management cycle of Align-Build-Deliver-Monitor.

**The Goals Cascade**

The COBIT goals cascade is a mechanism for translating stakeholder needs into specific, actionable governance and management objectives. It operates through a four-level hierarchy: stakeholder drivers and needs cascade into enterprise goals, which cascade into alignment goals (called IT-related goals in COBIT 5), which cascade into governance and management objectives.

The goals cascade is critical because it provides the traceability that auditors need. When an IS auditor asks "why does this IT process exist?" the answer should be traceable through the goals cascade to a stakeholder need. If a process cannot be traced to stakeholder value, the auditor should question whether resources allocated to that process are optimally deployed.

Let me give you a concrete example. Suppose a stakeholder need is regulatory compliance with data protection laws. That stakeholder need maps to an enterprise goal such as "compliance with external laws and regulations." That enterprise goal maps to an alignment goal such as "IT compliance with internal policies." That alignment goal maps to governance and management objectives such as MEA03 — Managed Compliance with External Requirements — and APO01 — Managed IT Management Framework. The goals cascade gives you this traceability.

For the exam, understand the cascade conceptually and know that it flows from stakeholder needs downward to specific objectives. You will not be asked to reproduce the mapping tables, but you may be asked to identify the purpose of the goals cascade or to trace a specific scenario through the hierarchy.

**Design Factors**

Design factors are one of the most significant additions in COBIT 2019 compared to COBIT 5. There are eleven design factors that influence how an organization should design its governance system. They include enterprise strategy, enterprise goals, risk profile, IT-related issues, threat landscape, compliance requirements, role of IT, sourcing model for IT, IT implementation methods, technology adoption strategy, and enterprise size.

Design factors make COBIT 2019 explicitly tailorable. Rather than prescribing a one-size-fits-all governance system, COBIT 2019 recognizes that a small startup with a cloud-first, agile IT function requires a fundamentally different governance system than a global bank with legacy infrastructure and extensive regulatory obligations.

For the IS auditor, design factors provide a basis for evaluating whether an organization's governance system is appropriately calibrated. If an organization has a high-risk profile and extensive compliance requirements but has implemented a lightweight governance system designed for a low-risk environment, that is an audit finding. The governance system does not match the design factors.

**Focus Areas**

COBIT 2019 introduces the concept of focus areas — specific topics or domains that can be addressed by a collection of governance and management objectives. Examples include cybersecurity, digital transformation, cloud computing, DevOps, and small and medium enterprise governance. Focus areas provide additional guidance layers on top of the core COBIT framework.

The exam relevance of focus areas is limited, but you should know that they exist and understand that they represent ISACA's mechanism for keeping COBIT current with emerging technology and business trends without requiring a full framework revision.

**COBIT Exam Traps**

Let me flag several COBIT-specific exam traps.

First, the exam may present COBIT 5 terminology — enablers, process reference model — and expect you to know that COBIT 2019 uses updated terminology — components, governance and management objectives. If a question references "enablers," it is either testing COBIT 5 knowledge or testing whether you can identify the outdated terminology.

Second, the exam will test whether you understand that COBIT is a governance framework, not a technical standard. COBIT tells you *what* to govern and manage; it does not prescribe *how* to implement specific technical controls. If a question asks "which framework provides detailed technical implementation guidance for IT controls," COBIT is not the answer — you would look to NIST SP 800-53, CIS Controls, or similar technical frameworks.

Third, remember that COBIT is explicitly designed to coexist with other frameworks. COBIT for governance, ITIL for service management, TOGAF for enterprise architecture, ISO 27001 for information security management — these are complementary, not competing. The exam may present scenarios where an organization is debating whether to adopt COBIT or ITIL, and the correct answer is typically "both, for different purposes."

[SECTION BREAK]

## SECTION 3: ITIL 4 — THE SERVICE VALUE SYSTEM (22:00 – 31:00)

We now shift from governance to service management, and specifically to ITIL 4, the most widely adopted IT service management framework globally. While COBIT tells you what to govern, ITIL tells you how to manage IT services effectively.

ITIL — the Information Technology Infrastructure Library — has undergone significant evolution. ITIL 4, released in 2019, represents a fundamental reconceptualization of IT service management around the Service Value System. For the CISA exam, you need to understand ITIL 4 at a structural level and in depth on several key practices.

**The ITIL 4 Service Value System**

The Service Value System, or SVS, is the overarching model in ITIL 4. It describes how all the components and activities of an organization work together to facilitate value creation. The SVS has five components: the guiding principles, governance, the service value chain, practices, and continual improvement.

The service value chain is the central element — it is an operating model with six activities: plan, improve, engage, design and transition, obtain/build, and deliver and support. These activities are not sequential stages; they are interconnected and can be combined in different sequences to create value streams. This is a significant departure from the linear service lifecycle of ITIL v3, and the exam may test this distinction.

**The Guiding Principles**

ITIL 4 defines seven guiding principles: focus on value, start where you are, progress iteratively with feedback, collaborate and promote visibility, think and work holistically, keep it simple and practical, and optimize and automate.

For the exam, the most important of these is "focus on value" — everything the service provider does should map back to value for the consumer. This aligns directly with COBIT's first principle of providing stakeholder value, which is not coincidental — both frameworks have converged on value creation as the foundational objective.

**Key ITIL 4 Practices**

ITIL 4 defines thirty-four practices, organized into three categories: general management practices, service management practices, and technical management practices. The CISA exam focuses on several specific practices that are audit-relevant.

*Incident Management* is the practice of minimizing the negative impact of incidents by restoring normal service operation as quickly as possible. From an audit perspective, you evaluate whether the organization has defined incident categorization and prioritization schemes, whether escalation procedures are documented and followed, whether incident response times align with service level agreements, and whether incident records are complete and accurate. A key audit concern is whether the organization distinguishes between incidents and service requests — ITIL 4 treats these as separate practices, and the exam expects you to understand the distinction.

*Problem Management* is the practice of reducing the likelihood and impact of incidents by identifying actual and potential causes and managing workarounds and known errors. The critical distinction for the exam is that incident management is reactive — restore service — while problem management is proactive and investigative — find and address root causes. A common exam trap presents a scenario where an organization resolves incidents repeatedly without conducting root cause analysis, and asks you to identify the missing practice. The answer is problem management.

*Change Enablement* — note the name change from "change management" in ITIL v3 to "change enablement" in ITIL 4 — is the practice of maximizing successful IT changes by ensuring that risks are properly assessed, authorizing changes to proceed, and managing the change schedule. ITIL 4 defines three types of changes: standard changes, which are pre-authorized, low-risk, and follow documented procedures; normal changes, which require assessment and authorization through the change authority; and emergency changes, which must be implemented urgently and are typically authorized by a designated emergency change authority with post-implementation review.

For the IS auditor, change enablement is one of the most critical practices to evaluate because inadequate change management is a root cause of service disruptions, security vulnerabilities, and compliance failures. Audit concerns include: Are all changes recorded? Is there appropriate segregation between those requesting, authorizing, and implementing changes? Are emergency changes subject to post-implementation review? Is there evidence that risk assessment occurs before change authorization?

*Service Desk* is the practice of capturing demand for incident resolution and service requests. The service desk is the single point of contact between the service provider and its users. From an audit perspective, you evaluate whether the service desk is appropriately staffed, whether first-contact resolution rates are tracked, and whether the service desk has adequate tools and information to fulfill its function. The exam may test whether you understand that the service desk is a practice, not merely a function — ITIL 4 treats it as an integrated practice that connects to incident management, service request management, and other practices.

**ITIL 4 Exam Traps**

Be alert to terminology changes between ITIL v3 and ITIL 4. The service lifecycle stages of ITIL v3 — Service Strategy, Service Design, Service Transition, Service Operation, Continual Service Improvement — are replaced by the service value chain in ITIL 4. "Processes" in ITIL v3 are now "practices" in ITIL 4, reflecting a broader scope that includes people, technology, and information in addition to process activities. "Change management" is now "change enablement." If the exam uses ITIL v3 terminology, it is either testing legacy knowledge or testing whether you can identify outdated terminology.

Also remember that ITIL 4 explicitly embraces Agile, DevOps, and Lean methodologies. The service value chain is designed to support various ways of working, including traditional waterfall, Agile sprints, and continuous delivery pipelines. If a question asks whether ITIL 4 is compatible with Agile or DevOps practices, the answer is unequivocally yes.

[SECTION BREAK]

## SECTION 4: ENTERPRISE ARCHITECTURE FRAMEWORKS — TOGAF AND ZACHMAN (31:00 – 36:00)

Enterprise architecture provides the structural blueprint for how an organization's business processes, data, applications, and technology infrastructure relate to one another and support enterprise objectives. For the CISA exam, you need to understand two frameworks: TOGAF and Zachman.

**TOGAF — The Open Group Architecture Framework**

TOGAF is the most widely adopted enterprise architecture framework. Its core component is the Architecture Development Method, or ADM, which provides a structured approach to developing enterprise architecture through iterative phases.

The ADM phases are: Preliminary (establishing the architecture capability), Architecture Vision (Phase A), Business Architecture (Phase B), Information Systems Architecture (Phase C, covering both data and application architectures), Technology Architecture (Phase D), Opportunities and Solutions (Phase E), Migration Planning (Phase F), Implementation Governance (Phase G), and Architecture Change Management (Phase H), with Requirements Management at the center, interacting with all phases.

For the IS auditor, TOGAF is relevant because it provides a basis for evaluating whether an organization's IT architecture is aligned with business strategy, whether architecture governance processes are effective, and whether architecture decisions are documented and traceable. If an organization claims to use TOGAF, the auditor should expect to find architecture artifacts such as the Architecture Repository, the Architecture Board governance structure, and evidence that the ADM is being followed — even if adapted to the organization's specific context.

A key TOGAF concept for the exam is the Architecture Repository, which is the structured store of all architecture artifacts, including the Architecture Landscape (showing the current and target states), the Standards Information Base (governing technology standards), and the Reference Library. If a question asks where architecture standards are maintained in a TOGAF environment, the answer is the Architecture Repository, specifically the Standards Information Base.

**The Zachman Framework**

The Zachman Framework is an ontology — a classification scheme — for enterprise architecture. Unlike TOGAF, which is a process-oriented methodology, Zachman is a taxonomy that organizes architecture artifacts along two dimensions: perspectives (rows representing stakeholders — planner, owner, designer, builder, implementer, worker) and interrogatives (columns representing the fundamental questions — what, how, where, who, when, why).

The Zachman Framework does not prescribe a methodology or process for creating architecture; it simply provides a comprehensive classification of the artifacts that should exist. For the exam, the key distinction is that Zachman is a classification framework (what artifacts exist) while TOGAF is a process framework (how to create them). They are complementary, and an organization could use the Zachman taxonomy to classify artifacts produced through the TOGAF ADM.

The exam is unlikely to test Zachman in depth, but it may present a question asking you to distinguish between a framework that provides a classification scheme for architecture artifacts and one that provides a methodology for developing architecture. If so, Zachman is the classification scheme and TOGAF is the methodology.

[SECTION BREAK]

## SECTION 5: ORGANIZATIONAL GOVERNANCE STRUCTURES (36:00 – 41:00)

Governance frameworks are only as effective as the organizational structures that implement them. In this section, we address the key governance structures that the CISA exam expects you to understand.

**The IT Steering Committee**

The IT steering committee is the primary organizational mechanism for ensuring IT-business alignment at the strategic level. Typically chaired by a senior business executive — not the CIO — the steering committee includes representation from major business units, finance, IT, and sometimes external advisors.

The steering committee's responsibilities include: reviewing and approving the IT strategic plan, prioritizing IT investments and major projects, monitoring IT performance against strategic objectives, reviewing significant IT risks and ensuring appropriate mitigation, and ensuring that IT resource allocation aligns with business priorities.

For the IS auditor, the steering committee is a critical governance mechanism to evaluate. Audit concerns include: Does the steering committee have a formal charter? Does it meet regularly, with documented minutes? Is membership representative of the enterprise, not dominated by IT? Are decisions documented and traceable to strategic objectives? Does the committee receive adequate information — including KPIs, KRIs, and project status reports — to fulfill its oversight function?

An important exam trap: the IT steering committee provides strategic direction and oversight, but it does not manage IT operations. If a question describes a steering committee approving individual purchase orders or managing helpdesk escalations, the committee has overstepped its governance role into operational management.

**The IT Balanced Scorecard**

The IT balanced scorecard adapts Kaplan and Norton's balanced scorecard concept to IT governance. It evaluates IT performance across four perspectives: the corporate contribution perspective (how does management view IT?), the user orientation perspective (how do users view IT?), the operational excellence perspective (how effective and efficient are IT processes?), and the future orientation perspective (how well is IT positioned to meet future needs?).

The balanced scorecard is a governance tool because it provides the governing body with a multidimensional view of IT performance, not just financial metrics. For the exam, understand that the balanced scorecard is about *balanced* measurement — if an organization measures only financial performance or only operational metrics, the scorecard is incomplete and the governing body lacks the information needed to fulfill its evaluate-direct-monitor responsibilities.

**The Strategic Alignment Model**

Henderson and Venkatraman's Strategic Alignment Model, while not always explicitly named in CISA materials, underlies ISACA's treatment of IT-business alignment. The model posits four domains — business strategy, IT strategy, organizational infrastructure and processes, and IT infrastructure and processes — and argues that alignment must occur across multiple dimensions: strategic fit (between strategy and infrastructure) and functional integration (between business and IT).

For the exam, the practical takeaway is that IT-business alignment is not a one-time activity but an ongoing process that requires alignment across strategy, structure, and operations. If a question presents an organization with a well-defined IT strategy but poor operational execution, the alignment gap is between strategy and infrastructure, not between business and IT at the strategic level.

**Value Delivery and Resource Management**

Value delivery ensures that IT investments produce the benefits promised in business cases. The exam expects you to understand that value delivery requires: business case development before investment, benefits realization management during and after implementation, and post-implementation review to verify that promised benefits were achieved.

Resource management ensures that IT resources — people, information, infrastructure, and applications — are optimally acquired, allocated, and utilized. The governance question is not "do we have enough resources?" but "are our resources deployed in a way that maximizes stakeholder value?" An IS auditor evaluating resource management would examine capacity planning processes, skills gap analyses, asset management practices, and resource allocation alignment with strategic priorities.

**Board-Level IT Oversight**

Increasingly, boards of directors are expected to exercise direct oversight of IT governance, particularly in regulated industries. This includes understanding the organization's IT risk profile, reviewing cybersecurity posture, and ensuring that IT strategy supports enterprise strategy. The IS auditor should evaluate whether the board has sufficient IT competence — either through board member expertise or access to external advisors — to fulfill this oversight responsibility. A board that rubber-stamps IT strategies it does not understand is failing in its governance duty, regardless of how comprehensive the IT strategy document may be.

[SECTION BREAK]

## SECTION 6: REGULATORY AND COMPLIANCE GOVERNANCE — SOX AND GDPR (41:00 – 44:00)

Governance does not exist in a vacuum — it operates within a regulatory and legal framework that imposes specific requirements on how organizations govern and manage IT.

**SOX IT Implications**

The Sarbanes-Oxley Act, enacted in 2002 in response to corporate accounting scandals, has profound IT governance implications, particularly Section 404, which requires management to assess and report on the effectiveness of internal controls over financial reporting. Because financial data flows through IT systems, SOX Section 404 effectively requires organizations to implement and maintain IT general controls — including access controls, change management controls, computer operations controls, and program development controls — for any system that processes, stores, or transmits financial data.

For the IS auditor, SOX compliance is a governance issue because it requires: management accountability for internal controls (not just IT's responsibility), board-level oversight through the audit committee, documented control frameworks (typically COSO for internal controls, mapped to COBIT for IT controls), and regular assessment and testing of control effectiveness.

The exam may test whether you understand that SOX does not prescribe specific IT controls — it requires effective internal controls, and the organization must determine which IT controls are necessary to support that requirement. COBIT provides a framework for making that determination, which is why COBIT and SOX are frequently discussed together.

**GDPR IT Implications**

The General Data Protection Regulation imposes governance requirements on any organization that processes personal data of EU residents. From an IT governance perspective, GDPR requires: a Data Protection Officer in certain circumstances, privacy impact assessments for high-risk processing activities, data protection by design and by default (meaning privacy must be built into systems architecture, not bolted on afterward), breach notification within seventy-two hours, and documented records of processing activities.

For the IS auditor, GDPR compliance requires evaluating whether IT governance structures address data protection requirements — not merely whether technical controls exist, but whether governance mechanisms (policies, organizational structures, accountability frameworks) ensure ongoing compliance. The governance challenge with GDPR is that it is not a point-in-time compliance exercise; it requires continuous governance oversight of data processing activities.

[SECTION BREAK]

## SUMMARY AND BRIDGE (44:00 – 45:00)

Let us consolidate what we have covered. IT governance is the system by which the governing body evaluates, directs, and monitors IT — distinct from IT management, which plans, builds, runs, and monitors. COBIT 2019 provides the governance framework with six principles, seven components, forty objectives across five domains, design factors for tailoring, and the goals cascade for traceability. ITIL 4 provides the service management framework with the Service Value System, the service value chain, and thirty-four practices — with incident management, problem management, change enablement, and service desk being the most audit-relevant. Enterprise architecture is structured through TOGAF's ADM methodology and Zachman's classification taxonomy. And governance structures — steering committees, balanced scorecards, strategic alignment models — translate framework theory into organizational practice.

Here is your master mnemonic for this episode: "Governance Evaluates, Management Executes — COBIT Cascades, ITIL Creates Value, Architecture Aligns." Commit that to memory.

In Episode 2.2, we move from governance structures to risk and compliance management. We will cover IT risk management frameworks including ISO 31000 and NIST RMF, quantitative and qualitative risk analysis, risk treatment strategies, Key Risk Indicators, and the regulatory compliance landscape including SOX Section 404, PCI-DSS, HIPAA, and GDPR. We will also address third-party risk management and vendor risk assessments — areas of increasing exam emphasis as organizations rely more heavily on external service providers.

Thank you for your attention and your commitment to mastering this material. I will see you in Episode 2.2.

---

*This episode references: ISACA CISA Review Manual (27th Edition), COBIT 2019 Framework: Introduction and Methodology, COBIT 2019 Framework: Governance and Management Objectives, ITIL 4 Foundation (AXELOS), TOGAF Standard (The Open Group), ISO/IEC 38500:2015 — Governance of IT for the Organization, Henderson & Venkatraman Strategic Alignment Model.*
