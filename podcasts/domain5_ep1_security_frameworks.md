# Domain 5, Episode 1 — Information Security Frameworks

**CISA Exam Preparation Podcast — Protection of Information Assets**
**Episode Duration: 44:10**

---

Welcome back to the CISA Mastery Podcast. You are listening to Episode One of Domain Five — Protection of Information Assets. This domain accounts for thirteen percent of the CISA examination, translating to approximately twenty-six questions. Over the next five episodes, we will systematically dismantle every examinable concept in this domain, beginning with the foundational layer that underpins everything else: information security frameworks.

If you have been following the series through Domains One through Four, you have already built a commanding understanding of governance, IT management, acquisition, and operations. Domain Five is where all of that operational knowledge meets the sharp edge of security. And security, as any seasoned practitioner knows, does not begin with firewalls or encryption keys. It begins with governance, strategy, and frameworks.

Let us begin.

[SECTION BREAK]

## Governance Versus Management — The ISACA Distinction

Before we examine any specific framework, we need to settle a definitional matter that the CISA exam tests relentlessly: the difference between information security governance and information security management.

ISACA draws a hard line here. Information security governance is the responsibility of the board of directors and senior executive management. It is the system by which the organization's information security activities are directed and controlled. Governance sets the strategic direction, ensures that objectives are achieved, determines that risk is managed appropriately, and verifies that the organization's resources are used responsibly. Governance asks the question: are we doing the right things?

Information security management, by contrast, is the responsibility of operational and tactical leadership — your CISOs, your security architects, your IT directors. Management is concerned with executing the security strategy defined by governance. It designs, implements, monitors, and improves the security controls. Management asks: are we doing things right?

This distinction is not merely academic. On the CISA exam, you will encounter scenarios where an auditor must determine whether a deficiency is a governance gap or a management gap. If the board has not established a security policy or has not defined risk appetite for information assets, that is a governance failure. If the security team has not implemented multi-factor authentication despite a board-approved policy requiring it, that is a management failure.

The IS auditor's role intersects both. When auditing governance, you evaluate whether the board has established appropriate security direction, whether there is a charter for the information security function, whether security strategy aligns with business strategy, and whether there are defined metrics for measuring security effectiveness. When auditing management, you evaluate whether controls are designed and operating effectively, whether incidents are handled according to procedure, and whether security configurations meet the organization's standards.

ISACA's CISM framework — which overlaps substantially with CISA Domain Five — identifies four domains of information security management: information security governance, information risk management, information security program development and management, and information security incident management. While CISM is a separate certification, the CISA exam expects you to understand these domains at the level of an auditor assessing their adequacy.

One more nuance that catches candidates: governance is about accountability, while management is about responsibility. The board is accountable for security outcomes even though management is responsible for executing security operations. This accountability cannot be delegated. The board can delegate authority to a CISO, but it cannot delegate the accountability for a breach that results from inadequate governance oversight.

[SECTION BREAK]

## ISO/IEC 27001:2022 — The International Standard for Information Security Management Systems

Let us turn to the most widely adopted information security standard on the planet: ISO/IEC 27001. The 2022 revision brought significant structural changes that the CISA exam now reflects, so if your study materials still reference the 2013 version, you need to update your understanding.

ISO 27001 specifies the requirements for establishing, implementing, maintaining, and continually improving an information security management system — the ISMS. The standard follows a risk-based approach, meaning that the controls an organization implements should be proportional to the risks it faces. There is no one-size-fits-all prescription.

The structure of ISO 27001:2022 follows the Harmonized Structure, formerly known as Annex SL, which aligns it with other ISO management system standards such as ISO 9001 for quality and ISO 22301 for business continuity. This harmonized structure contains ten clauses. Clauses One through Three are introductory — scope, normative references, and terms and definitions. The mandatory requirements begin at Clause Four.

Clause Four is Context of the Organization. You must understand the organization's internal and external context, identify interested parties and their requirements, and define the scope of the ISMS. This is not a trivial exercise. The scope defines the boundaries of the ISMS — which business processes, information assets, locations, and technology systems are covered. A poorly scoped ISMS is one of the most common findings in certification audits.

Clause Five is Leadership. Top management must demonstrate leadership and commitment, establish the information security policy, and assign roles, responsibilities, and authorities. The security policy established here is the apex of the policy hierarchy — we will discuss that hierarchy shortly.

Clause Six is Planning. This is where risk assessment and risk treatment live. The organization must define its risk assessment methodology, identify information security risks, analyze and evaluate those risks, and then select risk treatment options. The Statement of Applicability — the SOA — is produced here. The SOA is a critical document that maps every control in Annex A and declares whether it is applicable, how it is implemented, and the justification for any exclusions.

Clause Seven is Support. This covers resources, competence, awareness, communication, and documented information. Documented information is the ISO term for what we historically called documentation and records.

Clause Eight is Operation. This is where the rubber meets the road — the organization executes its risk treatment plans, implements controls, and manages operational security processes.

Clause Nine is Performance Evaluation. This requires monitoring, measurement, analysis, evaluation, internal audit, and management review. The internal audit function here should be familiar to you as CISA candidates — ISO 27001 requires regular internal audits of the ISMS using auditors who are objective and impartial.

Clause Ten is Improvement. Nonconformities must be addressed through corrective action, and the ISMS must be continually improved.

Now, Annex A. This is where the control set lives. The 2022 revision reorganized the controls dramatically. The 2013 version had fourteen control domains containing one hundred fourteen controls. The 2022 version consolidated these into four themes containing ninety-three controls. The four themes are: Organizational controls — thirty-seven controls; People controls — eight controls; Physical controls — fourteen controls; and Technological controls — thirty-four controls.

Several new controls were introduced in the 2022 revision that reflect the evolving threat landscape. These include threat intelligence, information security for use of cloud services, ICT readiness for business continuity, physical security monitoring, configuration management, information deletion, data masking, data leakage prevention, monitoring activities, web filtering, and secure coding.

For the CISA exam, you do not need to memorize all ninety-three controls. But you absolutely must understand the structure, the concept of the Statement of Applicability, the risk-based approach to control selection, and the continuous improvement cycle. You should also understand that ISO 27001 certification is granted by accredited certification bodies through a two-stage audit process. Stage One is a documentation review and readiness assessment. Stage Two is an on-site assessment of implementation and effectiveness.

A companion standard, ISO/IEC 27002:2022, provides implementation guidance for the controls listed in Annex A. While 27001 tells you what controls to consider, 27002 tells you how to implement them. Think of 27001 as the requirements standard and 27002 as the guidance standard.

[SECTION BREAK]

## NIST Cybersecurity Framework 2.0

If ISO 27001 is the international gold standard, the NIST Cybersecurity Framework is the dominant framework in North American practice and increasingly in global use. Version 2.0, released in February 2024, introduced a significant structural change that you must know for the exam.

The original NIST CSF had five functions: Identify, Protect, Detect, Respond, and Recover. Version 2.0 added a sixth function at the top: Govern. This addition reflects the maturation of cybersecurity as a discipline — the recognition that governance is not peripheral to cybersecurity but foundational to it.

Here is your mnemonic for the six functions of NIST CSF 2.0: "Governments Identify Protective Detectives Responding Resourcefully." Govern, Identify, Protect, Detect, Respond, Recover. Commit this to memory.

Let me walk through each function with the depth the exam demands.

The Govern function establishes and monitors the organization's cybersecurity risk management strategy, expectations, and policy. It encompasses organizational context, risk management strategy, roles and responsibilities, policies, oversight, and cybersecurity supply chain risk management. The Govern function is deliberately placed as the overarching function that informs and directs the other five. This mirrors ISACA's emphasis on governance as the foundation of effective security.

The Identify function develops the organizational understanding needed to manage cybersecurity risk to systems, people, assets, data, and capabilities. This includes asset management — you cannot protect what you do not know you have — risk assessment, and improvement planning. An IS auditor evaluating the Identify function would look for a comprehensive asset inventory, a defined risk assessment methodology, and evidence that risk assessments are performed regularly and after significant changes.

The Protect function implements safeguards to ensure delivery of critical services. This includes identity management and access control, awareness and training, data security, platform security, and technology infrastructure resilience. When auditing Protect, you assess whether controls are designed and operating effectively to mitigate identified risks.

The Detect function develops and implements activities to identify the occurrence of a cybersecurity event. This covers continuous monitoring and adverse event analysis. An IS auditor evaluates whether the organization has adequate detection capabilities — security information and event management systems, intrusion detection systems, anomaly detection — and whether alerts are triaged and escalated appropriately.

The Respond function takes action regarding a detected cybersecurity incident. This includes incident management, incident analysis, incident response reporting and communication, and incident mitigation. We will cover incident response in depth in Episode Five of this domain.

The Recover function restores capabilities or services that were impaired due to a cybersecurity incident. This includes incident recovery plan execution and incident recovery communication. Recovery is tightly linked to business continuity and disaster recovery planning.

The NIST CSF operates on a tiered maturity model with four tiers: Tier One is Partial — ad hoc and reactive; Tier Two is Risk Informed — risk management is approved but not organization-wide; Tier Three is Repeatable — policies are formalized and consistently applied; and Tier Four is Adaptive — the organization adapts based on lessons learned and predictive indicators. The exam may ask you to identify the characteristics of each tier or to assess which tier an organization has achieved based on a scenario.

A critical distinction between ISO 27001 and NIST CSF: ISO 27001 is a certifiable standard — organizations can achieve formal certification through third-party audit. NIST CSF is a framework — it provides structure and guidance but there is no formal NIST CSF certification. Organizations self-assess against it or use it as a reference model.

[SECTION BREAK]

## COBIT 2019 — APO13 and DSS05

As CISA candidates, you must understand how COBIT 2019 addresses information security, because COBIT is ISACA's own governance framework and it permeates the exam.

Two COBIT 2019 management objectives are directly relevant to information security: APO13 — Managed Security, and DSS05 — Managed Security Services.

APO13, Managed Security, sits within the Align, Plan, and Organize domain. It focuses on defining, operating, and monitoring a system for information security management. APO13 explicitly references alignment with ISO 27001, stating that the ISMS should be established, implemented, and maintained in accordance with recognized standards. The practices under APO13 include establishing and maintaining an ISMS, defining and managing an information security risk treatment plan, and monitoring and reviewing the ISMS. If you are auditing an organization that uses COBIT as its governance framework, APO13 is where you look for the security governance structure.

DSS05, Managed Security Services, sits within the Deliver, Service, and Support domain. It is more operational than APO13. DSS05 focuses on protecting enterprise information to maintain the level of information security risk acceptable to the enterprise. Its practices include protecting against malware, managing network and connectivity security, managing endpoint security, managing user identity and logical access, managing physical access to IT assets, managing sensitive documents and output devices, and monitoring the infrastructure for security-related events.

The relationship between APO13 and DSS05 mirrors the governance-versus-management distinction we discussed earlier. APO13 is strategic — it establishes the security management system. DSS05 is operational — it executes the day-to-day security services. An auditor who finds that an organization has robust DSS05 controls but no APO13 governance structure has identified a significant gap: operational security without strategic direction.

COBIT 2019 also introduces design factors that allow organizations to customize their governance system. Relevant design factors for security include the threat landscape, compliance requirements, role of IT, and enterprise risk profile. These design factors influence which management objectives are prioritized and what capability levels are targeted.

[SECTION BREAK]

## Defense in Depth — People, Process, Technology

With the frameworks established, let us discuss the architectural principle that underlies all security implementations: defense in depth.

Defense in depth is a strategy that employs multiple layers of security controls so that if one layer fails, another layer continues to provide protection. The concept originates from military strategy — a series of defensive positions rather than a single fortified line. In information security, it means that no single control should be the sole barrier between a threat actor and a critical information asset.

The three dimensions of defense in depth are people, process, and technology.

People are simultaneously the strongest and weakest link in information security. Security awareness training, background checks, separation of duties, and clear role definitions are all people-layer controls. An IS auditor evaluating the people dimension assesses training completion rates, phishing simulation results, security culture survey outcomes, and whether personnel with access to sensitive systems have undergone appropriate vetting.

Process controls include documented policies and procedures, change management, incident response procedures, access review processes, and vendor management protocols. An IS auditor evaluating the process dimension reviews documentation, observes process execution, and tests whether deviations from defined processes are detected and corrected.

Technology controls are the most visible layer — firewalls, encryption, intrusion detection systems, endpoint protection, data loss prevention, and security information and event management systems. An IS auditor evaluating the technology dimension assesses configurations against baselines, reviews vulnerability scan results, tests access controls, and evaluates whether technology controls are monitored and maintained.

The critical concept for the exam is that defense in depth requires all three dimensions working in concert. An organization with state-of-the-art technology controls but poorly trained staff and inadequate processes is not secure. Conversely, an organization with excellent policies and training but outdated technology controls is equally vulnerable.

Defense in depth also implies layering within each dimension. In the technology layer, for example, you would have perimeter security through firewalls and DMZ architecture, network security through segmentation and intrusion detection, host security through endpoint protection and hardening, application security through secure coding and web application firewalls, and data security through encryption and data loss prevention. Each layer provides independent protection, and an attacker must defeat multiple layers to reach the target.

[SECTION BREAK]

## The Security Policy Hierarchy

Now let us address a topic that generates an outsized number of exam questions relative to its apparent simplicity: the security policy hierarchy. The hierarchy consists of four tiers — policy, standard, procedure, and guideline — and the exam tests whether you can distinguish between them with surgical precision.

A policy is a high-level statement of management's intent, direction, and objectives regarding information security. Policies define what must be accomplished but do not specify how. They are mandatory, approved by senior management or the board, and apply broadly across the organization. Example: "All sensitive data must be encrypted in transit and at rest." The policy does not specify which encryption algorithm, what key length, or which tool to use. It simply establishes the requirement.

A standard specifies mandatory requirements for technology, processes, or configurations. Standards define how much or which — they quantify the policy. They are also mandatory. Example: "Encryption must use AES-256 or stronger. TLS 1.2 is the minimum acceptable version. RSA key length must be at least 2048 bits." The standard translates the policy's intent into specific, measurable requirements.

A procedure is a step-by-step instruction for performing a specific task. Procedures define how — the detailed operational instructions. They are mandatory for personnel performing the relevant task. Example: "To encrypt a database, open the database management console, navigate to the encryption settings, select AES-256-GCM, generate a new key using the enterprise key management system, apply encryption, and verify by running the validation script." Procedures are granular, actionable, and leave no ambiguity about execution.

A guideline is a recommendation or suggestion for best practice. Unlike the three tiers above, guidelines are not mandatory. They provide advice and flexibility. Example: "When selecting encryption tools for non-regulated data, consider using the enterprise-approved encryption toolkit for ease of management, though equivalent alternatives may be used with security team approval." Guidelines acknowledge that professional judgment may dictate variations.

Here is the exam trap you must internalize. The exam will present a scenario and ask which type of document is most appropriate. The key discriminator is the level of specificity and mandatory nature. If the document says "you must" at a high level without specifics, it is a policy. If it specifies exact thresholds, configurations, or quantifiable requirements, it is a standard. If it provides step-by-step instructions, it is a procedure. If it recommends without requiring, it is a guideline.

A particularly devious exam question might describe a document that specifies "passwords must be at least twelve characters" and ask whether this is a policy or standard. This is a standard — it specifies a quantifiable requirement. A policy would say "passwords must meet complexity requirements sufficient to protect organizational assets." See the difference? The policy states the intent; the standard quantifies the implementation.

Another common trap: the exam may ask who approves each level. Policies are approved by the board or senior executive management. Standards are typically approved by the CISO or IT steering committee. Procedures are approved by the operational manager responsible for the process. Guidelines may be published by any competent authority within the organization without formal executive approval.

[SECTION BREAK]

## Real-World Case Study — Enterprise ISMS Implementation at a Financial Institution

Let me bring all of these concepts together with a real-world scenario that illustrates how frameworks, governance, and policy hierarchies intersect in practice.

Consider a mid-sized financial institution — a regional bank with forty branches, three thousand employees, and a rapidly growing digital banking platform. The bank is subject to regulatory requirements from its national banking regulator, PCI DSS for payment card processing, and contractual obligations from correspondent banking relationships that require ISO 27001 certification.

The bank's board of directors establishes an information security governance structure. They appoint a Chief Information Security Officer who reports to the Chief Risk Officer with a dotted-line reporting relationship to the board's Risk Committee. This reporting structure is a governance decision — it ensures that the CISO has organizational independence and board-level visibility.

The bank adopts ISO 27001:2022 as its primary ISMS framework, supplemented by NIST CSF 2.0 as a complementary reference for operational cybersecurity capabilities. This dual-framework approach is increasingly common in practice. ISO 27001 provides the certifiable management system structure, while NIST CSF provides the operational function-based lens.

The ISMS scope is defined to include all digital banking systems, core banking applications, payment processing infrastructure, customer data repositories, and the supporting network and data center infrastructure. Branch office networks are included in scope but physical branch security — guards, locks, safes — is managed under a separate physical security program, with defined interfaces between the two.

The bank develops a policy hierarchy. The Information Security Policy — approved by the board — establishes twelve policy domains including access control, cryptography, network security, incident management, and business continuity. Beneath each policy domain, standards are developed: the Access Control Standard specifies RBAC as the required model, defines privileged access criteria, and mandates quarterly access reviews. Procedures are developed for each operational process: the User Access Provisioning Procedure details the steps for creating accounts, obtaining manager approval through the workflow system, mapping roles in the identity management platform, and notifying the user. Guidelines are published for areas where flexibility is appropriate: the Mobile Device Security Guideline recommends specific MDM configurations but allows departments to choose among approved MDM solutions.

Risk assessment is performed using a methodology aligned with ISO 27005. The assessment identifies one hundred forty-three information security risks, which are evaluated against the board-defined risk appetite. Sixty-two risks are treated with controls selected from ISO 27001 Annex A. Twenty-three risks are mitigated through contractual risk transfer to third parties, including cyber insurance. Fifty-one risks are accepted by the appropriate risk owners with documented justification. Seven risks are avoided by discontinuing the associated business activities. The Statement of Applicability documents the disposition of all ninety-three Annex A controls.

Now, picture yourself as the IS auditor engaged to assess this ISMS before the certification audit. You would evaluate governance by confirming that the board has approved the security policy, that the CISO reporting structure provides adequate independence, that security metrics are reported to the board at least quarterly, and that risk appetite is defined and communicated.

You would evaluate risk management by reviewing the risk assessment methodology for completeness and consistency, sampling risk assessments for accuracy, and validating that risk treatment decisions align with risk appetite. You would evaluate controls by testing a sample of implemented controls for design adequacy and operating effectiveness. You would evaluate continuous improvement by reviewing the management review minutes, verifying that internal audit findings are tracked to closure, and confirming that corrective actions address root causes rather than symptoms.

The defense-in-depth principle manifests throughout: people controls include mandatory security awareness training with phishing simulations for all employees and specialized secure coding training for developers; process controls include change management with security impact assessments, vendor risk assessments for all third-party service providers, and incident response procedures tested through tabletop exercises; technology controls include next-generation firewalls with intrusion prevention, endpoint detection and response on all workstations, SIEM with twenty-four-seven monitoring through a managed security service provider, and encryption of all data at rest and in transit.

This case study illustrates why frameworks are not academic exercises — they are the structural foundation that makes systematic security possible.

[SECTION BREAK]

## Exam Strategy and Key Takeaways

Let us consolidate the critical knowledge for exam day.

First, governance versus management. The board governs — sets direction, defines risk appetite, approves policy. Management executes — implements controls, manages operations, reports to governance. The auditor assesses both but must recognize which level a deficiency belongs to.

Second, ISO 27001:2022. Remember the ten-clause Harmonized Structure, the four Annex A control themes — Organizational, People, Physical, Technological — the ninety-three controls, the Statement of Applicability, and the two-stage certification audit. ISO 27001 is certifiable; it specifies requirements.

Third, NIST CSF 2.0. Six functions: Govern, Identify, Protect, Detect, Respond, Recover. Remember the mnemonic: "Governments Identify Protective Detectives Responding Resourcefully." Four tiers of maturity from Partial to Adaptive. NIST CSF is a framework, not a certifiable standard.

Fourth, COBIT 2019. APO13 for strategic security governance, DSS05 for operational security services. APO13 aligns with ISO 27001.

Fifth, defense in depth. People, process, and technology — all three dimensions, layered within each dimension. No single point of failure.

Sixth, the policy hierarchy. Policy states the what. Standard states the how much. Procedure states the how. Guideline states the should. Policies and standards are mandatory. Procedures are mandatory for the relevant task. Guidelines are advisory. This distinction is exam gold — expect at least two or three questions directly testing it.

[SECTION BREAK]

## Bridge to Episode 2

In our next episode, we move from frameworks and governance to the control domain that generates the most audit findings in practice: access control and identity management. We will dissect the access control models — DAC, MAC, RBAC, and ABAC — examine the identity lifecycle from provisioning through de-provisioning, confront the critical distinctions between segregation of duties and dual control, and explore how privileged access management has become the frontline of enterprise security. That is Episode Two — Access Control and Identity Management. I will see you there.

---
*End of Episode 5.1 — Information Security Frameworks*
*CISA Domain 5: Protection of Information Assets*
