# Episode 4.1 — IT Service Management & Operations
## CISA Mastery Podcast | Domain 4: Information Systems Operations and Business Resilience
### Duration: 36:40

---

Welcome back to the CISA Mastery Podcast. This is Episode 4.1, and we are now entering Domain 4 — Information Systems Operations and Business Resilience. This domain accounts for roughly twenty percent of the CISA examination, which translates to approximately forty questions. That is a substantial weight, and for good reason: operations and resilience represent the day-to-day reality of information systems. Governance frameworks, audit charters, and acquisition methodologies are meaningless if the systems they govern cannot run reliably, recover gracefully, and serve the business without interruption.

In this first episode of the domain, we are going to cover IT service management and operations — the foundational machinery that keeps enterprise technology functioning. We will work through ITIL service management practices, service level agreements and their supporting constructs, capacity and performance management, IT operations including job scheduling and lights-out processing, systems monitoring and event management, help desk and service desk operations, incident versus problem management, asset management and the configuration management database, data center operations from environmental controls through physical security, media management and data handling procedures, end-user computing controls, and the audit procedures that tie all of this together.

Let us begin.

[SECTION BREAK]

## ITIL 4 Service Management Practices

The IT Infrastructure Library — ITIL — remains the dominant framework for IT service management worldwide, and ISACA's CISA Review Manual references it extensively when discussing operational best practices. As an IS auditor, you are not expected to hold an ITIL certification, but you absolutely must understand its core principles and how they inform audit criteria for IT operations.

ITIL 4, the current iteration, moved away from the rigid process-centric lifecycle of ITIL v3 and adopted a more flexible, value-driven approach built around the Service Value System. At the center of this system sits the Service Value Chain — a set of six interconnected activities: Plan, Improve, Engage, Design and Transition, Obtain/Build, and Deliver and Support. These are not sequential stages but rather activities that can be combined in various sequences called value streams to respond to different types of demand.

For the CISA examination, the critical concept is that ITIL provides a structured approach to managing IT services that creates value for the business. When you are auditing IT operations, you are fundamentally asking whether the organization has adopted recognized practices — whether ITIL, COBIT, ISO 20000, or a hybrid — and whether those practices are actually functioning as designed.

Here is your first exam trap for this episode. The CISA exam does not test ITIL terminology for its own sake. It tests whether you understand the underlying principles. If a question describes a scenario where changes are being made to production systems without a formal review process, the correct answer will reference the need for change management controls — not specifically "ITIL change enablement." The exam uses framework-neutral language whenever possible. Do not select an answer simply because it mentions ITIL by name.

ITIL 4 organizes its guidance into thirty-four management practices across three categories: general management practices such as risk management, information security management, and continual improvement; service management practices including incident management, problem management, change enablement, service level management, and service desk; and technical management practices covering deployment management, infrastructure and platform management, and software development and management.

As an auditor, you should be particularly attuned to the maturity of these practices within an organization. A common finding in IT operations audits is that organizations have adopted ITIL terminology — they call their support function a "service desk," they have an "incident management process" documented — but the actual execution bears little resemblance to structured service management. Documentation without execution is a control deficiency, and you should report it as such.

[SECTION BREAK]

## Service Level Management: SLAs, OLAs, and Underpinning Contracts

Service level management is the practice of setting clear, business-based targets for service performance and measuring actual delivery against those targets. This practice produces three key documents that you must understand for the exam, and more importantly, that you must know how to evaluate as an auditor.

The Service Level Agreement — the SLA — is the formal agreement between the IT service provider and the business customer. It defines what services will be delivered, the agreed performance targets, the responsibilities of both parties, and the remedies or penalties for non-performance. A well-constructed SLA specifies measurable targets: system availability of 99.95 percent during business hours, incident response within fifteen minutes for priority-one issues, monthly reporting of service performance metrics, and clearly defined escalation procedures.

Beneath the SLA sits the Operational Level Agreement — the OLA. This is an internal agreement between IT groups that supports the delivery of the SLA commitments. For example, if the SLA promises that the ERP system will be available 99.95 percent of the time, there may be OLAs between the database administration team, the network operations team, and the application support team specifying each group's responsibilities and response times. The OLA translates customer-facing commitments into internal operational obligations.

The third construct is the Underpinning Contract — the UC. This is the contract between the IT service provider and an external third-party supplier. If you outsource your network connectivity to a telecommunications provider, the contract with that provider is an underpinning contract. It must contain commitments that are at least as stringent as the corresponding SLA commitments, because if the external supplier fails to perform, the IT organization will fail to meet its SLA.

Here is a mnemonic for you: SLA-OLA-UC flows from the outside in. The SLA faces the business customer — it is the outermost layer. The OLA faces internal IT teams — it is the middle layer. The UC faces external suppliers — it is the innermost layer that underpins everything else. Think of it as a three-layer cake: the customer sees the frosting on top, but the structural integrity depends on every layer.

From an audit perspective, the most common findings in service level management relate to three areas. First, SLAs that contain vague or unmeasurable targets — statements like "the system will be highly available" or "support will be responsive" are not auditable commitments. Second, disconnects between SLA commitments and supporting OLAs or UCs — the SLA promises 99.99 percent availability, but the underpinning contract with the hosting provider only guarantees 99.9 percent. Third, lack of monitoring and reporting — SLAs exist on paper, but no one is actually measuring performance against the agreed targets.

An exam trap to watch for: the CISA exam may present a scenario where an organization has strong SLAs but no OLAs. The correct observation is that the SLA commitments are at risk because there is no internal accountability mechanism to ensure that the various IT teams collaborate effectively to meet the customer-facing targets. The absence of OLAs is a control gap, not merely an administrative oversight.

[SECTION BREAK]

## Capacity Management and Performance Monitoring

Capacity management ensures that IT infrastructure and services can meet current and future business demands in a cost-effective manner. This practice operates at three levels that ISACA expects you to understand.

Business capacity management focuses on translating business plans and forecasts into IT capacity requirements. If the business plans to launch in three new markets next quarter, what does that mean for server capacity, network bandwidth, storage, and user licensing? This level requires close collaboration between IT and business stakeholders, and its absence is a frequent audit finding — IT capacity planning that occurs in isolation from business planning.

Service capacity management monitors and analyzes the performance and throughput of live IT services against SLA targets. It asks: are we meeting our committed service levels, and where are the bottlenecks? This level produces the dashboards and reports that service level management uses to demonstrate compliance with SLAs.

Component capacity management focuses on the individual infrastructure components — servers, storage arrays, network switches, database instances — monitoring their utilization and performance characteristics. This is the most technically granular level and produces data about CPU utilization, memory consumption, disk I/O, network throughput, and similar metrics.

Performance monitoring is the tactical execution arm of capacity management. Modern enterprise environments deploy a range of monitoring tools — from infrastructure monitoring platforms like Nagios, Zabbix, or Datadog to application performance management solutions like Dynatrace or New Relic to log aggregation platforms like Splunk or the ELK stack. As an auditor, you are not evaluating which tool is best. You are evaluating whether the monitoring regime is comprehensive, whether alerting thresholds are appropriate, whether monitoring data is retained for trend analysis, and whether capacity planning decisions are informed by actual performance data rather than assumptions.

A critical audit concern in capacity management is the concept of capacity on demand or cloud bursting. Organizations that have migrated to cloud infrastructure often assume that capacity is infinite and that capacity management is therefore unnecessary. This is a dangerous misconception. Cloud capacity still has financial constraints — auto-scaling without cost controls can produce budget-destroying bills — and even cloud services have limits and quotas. An auditor should verify that cloud-based environments still have capacity management processes, including cost monitoring and alerting, auto-scaling policies with appropriate upper bounds, and regular reviews of resource utilization to identify waste.

For the exam, remember that capacity management is fundamentally about balance — ensuring sufficient capacity to meet demand without over-provisioning and wasting resources. The ideal state is right-sizing: having just enough capacity to meet current demand with appropriate headroom for growth and unexpected spikes.

[SECTION BREAK]

## IT Operations Management

IT operations management encompasses the day-to-day activities required to manage the IT infrastructure and deliver IT services. This is the engine room of IT, and for the CISA exam, there are several specific operational domains you must understand.

Job scheduling is the automated sequencing and execution of batch processing tasks. In large enterprise environments — particularly those running ERP systems, financial applications, or data warehousing platforms — hundreds or thousands of batch jobs execute nightly, weekly, or monthly. These jobs handle payroll processing, general ledger posting, data extraction and transformation, report generation, and system maintenance tasks. Enterprise job scheduling tools like Control-M, AutoSys, or Tivoli Workload Scheduler manage the complex dependencies between these jobs, ensuring that they execute in the correct sequence, that predecessor jobs complete successfully before dependent jobs begin, and that failures are detected and escalated.

As an auditor, your primary concerns with job scheduling include: Are job schedules documented and approved? Are changes to job schedules subject to change management controls? Are job completion statuses monitored and are failures investigated? Are sensitive jobs — particularly those involving financial data — subject to appropriate access controls so that unauthorized personnel cannot modify or execute them? Is there a process for handling job failures, including restart and recovery procedures?

Batch processing controls are closely related to job scheduling. Batch processing involves collecting transactions over a period and processing them as a group. The key controls for batch processing include batch balancing — ensuring that the number of transactions entering the batch equals the number processed — and run-to-run totals, where the closing balance of one batch run is reconciled with the opening balance of the next. These are fundamental integrity controls that ISACA considers essential knowledge.

Lights-out operations refers to the practice of operating data centers or IT environments with minimal or no on-site human presence during off-hours. The facility runs autonomously, with automated monitoring, alerting, and in some cases, automated remediation. For the CISA exam, understand that lights-out operations introduce specific risks: delayed response to physical incidents such as hardware failures, environmental excursions, or security breaches; dependence on remote monitoring and alerting systems — if the alerting system fails, no one knows; and the need for robust automated failover capabilities. An auditor evaluating lights-out operations should verify that monitoring and alerting systems are themselves monitored for availability, that on-call personnel are clearly identified and reachable, that automated remediation scripts are tested and subject to change management, and that physical access during unstaffed hours is tightly controlled and logged.

Here is a practical exam scenario for you. A question describes an organization that runs nightly batch processing to update its general ledger. The batch job failed at two in the morning, but the failure was not detected until staff arrived at eight in the morning. What is the primary control deficiency? The answer is not the batch job failure — failures happen. The deficiency is the lack of automated alerting for batch job failures. Six hours of undetected failure in a financial processing job represents a significant operational and financial risk.

[SECTION BREAK]

## Systems Monitoring and Event Management

Systems monitoring and event management form the nervous system of IT operations. An event, in ITIL terminology, is any change of state that has significance for the management of an IT service or infrastructure component. Events can be informational — a user logged in, a backup completed successfully — or they can indicate warnings or exceptions that require attention.

Event management is the process of detecting events, making sense of them, and determining the appropriate control action. This sounds straightforward, but in a modern enterprise environment, the volume of events is staggering. A midsized organization might generate millions of events per day across its infrastructure. The challenge is not collecting events — it is filtering, correlating, and prioritizing them to identify the handful that actually require human attention.

This is where Security Information and Event Management — SIEM — platforms enter the picture. Tools like Splunk, IBM QRadar, Microsoft Sentinel, or LogRhythm aggregate events from across the infrastructure, apply correlation rules and analytics to identify patterns that indicate real issues, and generate alerts for the operations or security teams. As an auditor, you should evaluate whether the SIEM is configured to collect events from all critical systems, whether correlation rules are regularly reviewed and updated, whether the team has the capability to investigate and respond to alerts in a timely manner, and whether alert fatigue — the condition where so many false positives are generated that genuine alerts are ignored — is being managed.

A critical distinction for the exam is between monitoring, which is the continuous observation of systems, and event management, which is the interpretation of and response to observed changes. Monitoring is the data collection mechanism. Event management is the intelligence layer that determines what the data means and what to do about it. An organization can have excellent monitoring — collecting terabytes of log data — and terrible event management — never actually analyzing that data or responding to what it reveals. When auditing, verify both capabilities, not just the existence of monitoring tools.

The exam may also test your understanding of threshold-based versus anomaly-based monitoring. Threshold-based monitoring generates alerts when a predefined threshold is crossed — CPU utilization exceeds ninety percent, disk space falls below ten percent. Anomaly-based monitoring uses baselines of normal behavior and alerts when observed behavior deviates significantly from the baseline — network traffic at three in the morning is four hundred percent above the established baseline, even though it has not crossed an absolute threshold. Both approaches have value, and mature organizations employ both.

[SECTION BREAK]

## Help Desk and Service Desk Operations

The distinction between a help desk and a service desk is one that ISACA draws clearly, and it may appear on the exam. A help desk is primarily reactive — it responds to incidents and user queries, focusing on break-fix activities. A service desk is a broader concept that serves as the single point of contact between the IT service provider and the users, handling not only incidents but also service requests, access requests, and communication about planned changes or outages.

ITIL 4 positions the service desk as a critical practice that facilitates communication and ensures that users have a consistent, reliable channel for all interactions with IT. From an audit perspective, the service desk is a rich source of evidence. Incident logs reveal recurring problems, SLA compliance data, user satisfaction trends, and the effectiveness of IT controls. If the same type of incident appears repeatedly in the service desk logs, it suggests an underlying problem that is not being addressed — which leads us to the next topic.

The service desk also serves a critical control function as the gatekeeper for incident logging and tracking. Every incident should be logged, categorized, prioritized, and tracked through to resolution. When you audit the service desk, verify that all incidents are logged — including those reported by email, phone, walk-up, and self-service portal — and that no incidents are resolved "off the books" without creating a ticket. Unlogged incidents represent a loss of management information and potentially a circumvention of controls.

Key metrics that an auditor should review include first-contact resolution rate, which measures the percentage of incidents resolved at first contact without escalation; mean time to resolve, broken down by priority level; customer satisfaction scores; incident backlog trends; and the ratio of incidents to service requests, which can indicate whether the IT environment is stable or problematic.

[SECTION BREAK]

## Incident Management vs. Problem Management

This is one of the most frequently tested distinctions in Domain 4, and it trips up candidates who have not internalized the difference. Let me be absolutely clear about the definitions.

Incident management is the practice of restoring normal service operation as quickly as possible following an unplanned interruption or reduction in quality. The keyword is restore. Incident management is about getting the service back to the user. It is reactive, tactical, and time-sensitive. When a production server crashes at ten in the morning and the sales team cannot access the CRM, incident management is the process that gets the CRM back online — whether by restarting the server, failing over to a backup, or implementing a workaround.

Problem management is the practice of identifying and managing the root causes and potential causes of incidents. The keywords are root cause. Problem management is about understanding why the server crashed in the first place and implementing a permanent fix so it does not crash again. It is analytical, investigative, and focused on long-term improvement rather than immediate restoration.

Here is the mnemonic: Incidents are about restoring service NOW. Problems are about preventing recurrence LATER. Incident management treats the symptom. Problem management cures the disease.

Problem management has two modes of operation that the exam may test. Reactive problem management investigates the root causes of incidents that have already occurred. Proactive problem management analyzes incident trends and monitoring data to identify and address potential problems before they cause incidents. Both are important, but proactive problem management represents a higher level of maturity.

The concept of a known error is critical to understand. A known error is a problem that has been diagnosed — the root cause is understood — but has not yet been permanently resolved. Known errors are documented in a Known Error Database, or KEDB, along with their associated workarounds. When a new incident occurs that matches a known error, the service desk can immediately apply the documented workaround to restore service quickly, while the permanent fix is developed and deployed through the change management process.

Exam trap: a question may describe a scenario where the same type of incident keeps recurring, and the IT team keeps applying the same fix each time. The question will ask what process is deficient. The answer is problem management, not incident management. The team is successfully restoring service each time — incident management is working. What is failing is the investigation of the root cause and implementation of a permanent fix — that is problem management.

Another exam trap: a question may ask about the relationship between incident, problem, and change management. The correct relationship is that incidents trigger problem investigations, problem investigations identify root causes and solutions, and those solutions are implemented through the change management process. These three practices form a tightly coupled triad that you should understand holistically.

[SECTION BREAK]

## Asset Management and the Configuration Management Database

IT asset management is the practice of tracking and managing the lifecycle of IT assets — hardware, software, and related components — from acquisition through retirement. This includes maintaining an accurate inventory, managing software licenses, tracking asset locations and assignments, and ensuring proper disposal at end of life.

The Configuration Management Database — CMDB — is a more sophisticated construct than a simple asset inventory. The CMDB stores information about configuration items — CIs — and the relationships between them. A configuration item is any component that needs to be managed in order to deliver an IT service: servers, applications, databases, network devices, documentation, SLAs, and even personnel in some implementations. The critical differentiator of a CMDB is that it captures not just what exists, but how things relate to each other.

For example, a simple asset inventory might tell you that server PROD-DB-01 exists, is located in rack A3, and runs Oracle Database 19c. A CMDB would additionally tell you that PROD-DB-01 hosts the production instance of the ERP database, which is used by the ERP application running on servers PROD-APP-01 through PROD-APP-04, which together deliver the "ERP Service" as defined in SLA-2024-017, and that this service is critical to the Finance, Procurement, and HR business units. This relationship mapping is what makes the CMDB invaluable for impact analysis — if PROD-DB-01 fails, you can immediately identify every service, application, and business unit affected.

From an audit perspective, the CMDB is only valuable if it is accurate. An inaccurate CMDB is arguably worse than no CMDB at all, because it creates false confidence in impact assessments and change evaluations. When you audit the CMDB, verify that there is a defined process for maintaining its accuracy — typically through a combination of automated discovery tools and manual verification. Look for evidence that the CMDB is actually used in operational processes — change management should consult the CMDB to assess the impact of proposed changes, incident management should consult it to understand the scope of outages, and capacity management should use it to plan infrastructure expansion.

A common audit finding is "CMDB drift" — the gradual divergence between the CMDB's recorded state and the actual state of the infrastructure. This typically occurs when changes are made to the infrastructure without updating the CMDB, either because the change management process was bypassed or because the CMDB update step was skipped. Regular reconciliation audits — comparing the CMDB against actual infrastructure using automated discovery — are the primary control for detecting and correcting CMDB drift.

For the exam, remember that the CMDB supports multiple ITIL practices, not just configuration management. It is a shared resource used by change management for impact assessment, incident management for scope determination, problem management for root cause analysis, and service level management for understanding which CIs underpin which services. It is a foundational data store for mature IT service management.

[SECTION BREAK]

## Data Center Operations

Data center operations is a broad topic that encompasses environmental controls, power management, fire suppression, and the physical infrastructure required to house and protect IT systems. For the CISA exam, you need a solid understanding of each area and the associated audit considerations.

Environmental controls maintain the operating conditions required by IT equipment. The primary concerns are temperature and humidity. Enterprise IT equipment typically operates optimally between eighteen and twenty-seven degrees Celsius, with humidity maintained between forty and sixty percent relative humidity. Temperatures above the operating range cause equipment to overheat, potentially resulting in hardware failure, data loss, or fire. Temperatures below the range can cause condensation when systems warm up, leading to short circuits. Humidity that is too high causes condensation and corrosion. Humidity that is too low creates static electricity discharge risk, which can damage sensitive electronic components.

Cooling systems in data centers typically employ a hot aisle/cold aisle configuration, where server racks are arranged so that the front of each rack — where cold air is drawn in — faces a cold aisle, and the back of each rack — where hot air is exhausted — faces a hot aisle. This separation prevents hot exhaust air from being recirculated into equipment intakes and improves cooling efficiency. More advanced data centers may use containment systems — physical barriers that fully enclose either the hot or cold aisles — to further improve efficiency.

An auditor should verify that environmental monitoring is in place, that alerting thresholds are configured, and that there are documented procedures for responding to environmental excursions. Ask to see the environmental monitoring logs and look for excursion events — if the temperature in the data center spiked to thirty-five degrees last month and no one noticed for four hours, that is a significant finding.

Fire suppression in data centers requires special consideration because traditional water-based sprinkler systems will destroy the very equipment they are supposed to protect. Data centers typically employ clean agent fire suppression systems — gaseous agents like FM-200 (heptafluoropropane), Novec 1230, or in older installations, halon — that extinguish fires without leaving residue and without damaging electronic equipment. These systems work by either removing heat from the fire or by chemically interrupting the combustion process.

For the CISA exam, understand the difference between pre-action sprinkler systems and clean agent systems. A pre-action sprinkler system is a water-based system that requires two triggers before water is released — typically both a smoke detector activation and a sprinkler head melting. This double-trigger design prevents accidental water discharge from a single broken sprinkler head. Pre-action systems are sometimes used in data center areas as a backup to clean agent systems. Clean agent systems are the primary suppression method for areas housing critical IT equipment.

Exam trap: if a question asks what type of fire suppression is most appropriate for a data center housing critical servers, the answer is a clean agent system such as FM-200 or Novec 1230 — not a water-based system, not CO2 (which is lethal to personnel), and not dry chemical (which leaves corrosive residue). If halon is listed as an option, note that while it is effective, it is being phased out under the Montreal Protocol due to its ozone-depleting properties, and new halon systems are generally not installed.

Power management is the third leg of the data center infrastructure triad. The power chain for a well-designed data center includes utility power as the primary source, an Uninterruptible Power Supply — UPS — to provide immediate, seamless power during the transition from utility power to generator power, and diesel or gas generators to provide extended power during prolonged utility outages.

The UPS serves a critical bridging function. When utility power fails, the UPS — typically a battery-based system for smaller installations or a rotary UPS for larger ones — provides clean, uninterrupted power for a finite duration, usually fifteen to thirty minutes. This window allows the generators to start up and stabilize their output. Once the generators are running at full capacity, the UPS hands off the load to generator power.

An auditor should verify that UPS batteries are regularly tested and replaced on schedule — batteries degrade over time and their actual runtime may be significantly less than their rated runtime if they are not maintained. Generator testing is equally critical. Generators should be tested under load on a regular schedule — typically monthly — not just started and run at idle. A generator that starts successfully under no-load conditions may fail to carry the full data center load when it matters. Fuel supplies should be verified, and contracts with fuel suppliers should include priority delivery provisions for emergency situations.

Power Distribution Units — PDUs — distribute power from the UPS and generators to individual racks and equipment. Redundant power feeds — often called A-feed and B-feed — provide two independent power paths to each piece of critical equipment. Servers and network devices with dual power supplies connect one supply to each feed, so that the failure of either power path does not cause an outage. An auditor should verify that dual-fed equipment is actually connected to both feeds, not just one — this is a surprisingly common misconfiguration.

[SECTION BREAK]

## Physical Security Controls for Data Centers

Physical security for data centers operates on the principle of defense in depth — multiple layers of security controls that an attacker must penetrate to reach the critical assets. These layers typically include perimeter security, building access controls, and computer room access controls.

Perimeter security includes fencing, walls, barriers, lighting, and surveillance cameras. The perimeter defines the boundary of the physical security zone and provides the first layer of deterrence and detection. Fencing should be at least eight feet high with barbed or razor wire for critical facilities. Lighting should eliminate shadows and dark areas that could conceal unauthorized activity. CCTV cameras should provide coverage of all access points and vulnerable areas, with recordings retained for a defined period.

Building access controls include locked doors, reception areas, visitor management procedures, and access control systems. The most common technologies are card-based access systems using proximity cards or smart cards, biometric systems using fingerprint, palm, iris, or facial recognition, and increasingly, multi-factor combinations such as card-plus-PIN or card-plus-biometric. For the exam, understand the difference between authentication methods: something you have (card), something you know (PIN), and something you are (biometric). Strong access control combines at least two of these factors.

The computer room — the space where servers, storage, and network equipment are housed — should have the most restrictive access controls. Access should be limited to personnel whose roles require physical access to the equipment. All access should be logged, and logs should be reviewed regularly. Mantrap or airlock-style entrances — two interlocking doors where the first must close before the second opens — prevent tailgating, the practice of following an authorized person through a secured door without presenting credentials.

An audit procedure that you should know for the exam is the physical access review. This involves obtaining the list of personnel with access to the data center, comparing it against job roles to verify that each individual's access is justified, reviewing access logs for unusual patterns — access at unusual hours, access by personnel who should not need physical access — and verifying that terminated personnel have had their access revoked promptly. This review should be performed at least annually, and more frequently for highly sensitive environments.

Visitor management procedures should require that all visitors are pre-authorized, sign in upon arrival, are issued temporary access badges that are visually distinct from permanent employee badges, are escorted at all times within restricted areas, sign out and return their badges upon departure, and are logged in a visitor register that is retained for audit purposes.

[SECTION BREAK]

## Media Management and Data Handling

Media management encompasses the controls over physical and electronic media throughout their lifecycle — from creation through use, storage, transport, and eventual destruction. In an era of cloud computing and digital transformation, it is tempting to dismiss media management as a legacy concern. That would be a mistake. Organizations still rely on backup tapes, removable drives, optical media, and paper documents, and even "born-digital" data stored on solid-state drives and flash storage requires lifecycle management.

Classification-based handling is the foundational principle. Media should be labeled according to the sensitivity of the data it contains, and handling procedures should correspond to the classification level. A backup tape containing unclassified test data does not require the same protections as a tape containing customer financial records or personally identifiable information. The organization's data classification policy should define the classification levels, and media handling procedures should specify the storage, transport, and destruction requirements for each level.

Media transport controls are a specific exam-relevant concern. When sensitive media must be transported — for example, backup tapes being sent to an offsite storage facility — controls should include encryption of the data on the media, tamper-evident packaging, authorized and bonded couriers, chain-of-custody documentation, and verification of receipt. The exam may test whether you recognize that encrypting data on transported media is a critical control — if an unencrypted backup tape is lost in transit, the organization faces a data breach.

Media sanitization and destruction is the process of rendering data on media unrecoverable when the media is being repurposed or disposed of. NIST Special Publication 800-88, "Guidelines for Media Sanitization," defines three methods in order of increasing assurance: Clear, which uses logical techniques such as overwriting to sanitize data and protects against simple non-invasive data recovery techniques; Purge, which uses physical or logical techniques that render data recovery infeasible using state-of-the-art laboratory techniques, including degaussing for magnetic media and cryptographic erase for self-encrypting drives; and Destroy, which renders the media physically unusable, typically through shredding, disintegration, or incineration.

For the CISA exam, understand that the appropriate sanitization method depends on the sensitivity of the data and the destination of the media. If the media will be reused within the same organization at the same security level, clearing may be sufficient. If the media will leave the organization's control — through sale, donation, or disposal — purging or destruction is required for sensitive data. Destruction is the only method that provides absolute assurance.

[SECTION BREAK]

## End-User Computing Controls

End-user computing — EUC — refers to the development and use of information systems by personnel outside the formal IT department. The most common examples are spreadsheets, desktop databases, macros, scripts, and increasingly, low-code or no-code applications developed by business users. EUC has proliferated because it allows business users to solve immediate operational needs without waiting for IT to develop formal solutions. However, it introduces significant risks that an IS auditor must understand.

The primary risks of end-user computing include lack of development controls — EUC applications are often built without requirements documentation, design reviews, testing, or quality assurance; lack of change controls — changes to critical spreadsheets or databases are made without review, approval, or version control; data integrity risks — EUC applications frequently contain formula errors, hardcoded values, or circular references that produce incorrect results; single points of failure — EUC applications are often developed and maintained by a single individual, creating key-person dependency; and lack of security controls — sensitive data in EUC applications may not be subject to the same access controls, encryption, and backup procedures as data in enterprise systems.

The CISA exam specifically emphasizes the risks of spreadsheet-based financial models and reporting. Studies have consistently shown that a significant percentage of spreadsheets used in business decision-making contain material errors. When these spreadsheets feed into financial reporting, regulatory compliance, or risk management processes, the consequences of errors can be severe.

Controls for end-user computing that an auditor should look for include an EUC policy that defines the organization's requirements for identifying, classifying, and controlling EUC applications; an inventory of critical EUC applications, particularly those that support financial reporting or regulatory compliance; change controls for critical EUC applications, including version control and review of changes by someone other than the developer; input validation controls to prevent data entry errors; cell and worksheet protection to prevent unauthorized or accidental modification of formulas and critical data; regular reconciliation of EUC outputs against authoritative data sources; and backup procedures for critical EUC files.

A particularly important audit consideration is the migration path from EUC to enterprise systems. When an EUC application becomes critical to business operations — when the entire treasury department depends on a single spreadsheet to manage cash positions, for example — the auditor should recommend that the organization evaluate whether the application should be re-engineered as a formal IT solution with full development and operational controls. The risk profile of a business-critical spreadsheet maintained by one person with no change controls, no testing, and no backup is fundamentally unacceptable.

[SECTION BREAK]

## IT Operations Audit Procedures

Let me bring together everything we have discussed in this episode by walking through the key audit procedures for IT operations. When you are assigned to audit IT operations, your work program should address the following areas.

For service level management, obtain and review the SLA portfolio. Verify that SLAs contain measurable performance targets. Obtain service level performance reports and compare actual performance against SLA targets. Review the process for handling SLA breaches, including escalation and remediation. Verify that OLAs and underpinning contracts align with SLA commitments.

For capacity management, review the capacity plan and verify it is aligned with business growth forecasts. Obtain performance monitoring reports and look for trends indicating capacity constraints. Review the process for capacity-related changes — how are decisions made to add capacity? Evaluate whether cloud auto-scaling policies include appropriate cost controls and upper limits.

For IT operations management, review the job scheduling framework, including documentation of job dependencies and approved schedules. Obtain job completion reports and verify that failures are detected, reported, and resolved. Evaluate the controls over lights-out operations, including monitoring, alerting, and on-call procedures. Review batch processing controls, including batch balancing and run-to-run totals.

For systems monitoring and event management, verify that monitoring covers all critical infrastructure components and applications. Review alerting thresholds and evaluate whether they are appropriate. Assess the organization's capability to investigate and respond to alerts. Evaluate the effectiveness of the SIEM platform, including the currency of correlation rules and the false-positive rate.

For service desk operations, review incident logs and look for patterns — recurring incidents, SLA breaches, backlogs. Evaluate the first-contact resolution rate and mean time to resolve. Verify that all incidents are logged regardless of reporting channel. Review the escalation process and ensure it functions as designed.

For incident and problem management, verify the existence and execution of both processes — many organizations have incident management but lack formal problem management. Review problem records and verify that root cause analysis is being performed. Check the Known Error Database for completeness and accuracy. Look for evidence that problem management is driving permanent fixes through change management.

For asset management and the CMDB, verify the accuracy of the asset inventory and CMDB through sample testing. Review the process for maintaining CMDB accuracy, including automated discovery and manual verification. Assess whether the CMDB is actually used in change, incident, and problem management processes. Verify software license compliance by comparing installed software against license entitlements.

For data center operations, conduct a physical inspection of the data center, assessing environmental controls, fire suppression systems, power infrastructure, and physical security. Review environmental monitoring logs for excursion events. Verify UPS battery testing and generator load testing records. Review physical access logs and verify that access is limited to authorized personnel. Assess media management procedures, including labeling, handling, transport, and destruction.

For end-user computing, verify the existence of an EUC policy and an inventory of critical EUC applications. For high-risk EUC applications, evaluate the adequacy of development, change, and security controls. Review EUC applications used in financial reporting for accuracy and integrity. Assess whether critical EUC applications should be migrated to formal enterprise systems.

[SECTION BREAK]

## Summary and Bridge

Let me draw this episode together. IT service management and operations form the operational backbone of enterprise technology. As an IS auditor, you must understand how ITIL and related frameworks structure the management of IT services, how SLAs, OLAs, and underpinning contracts create a hierarchy of accountability, how capacity management ensures infrastructure can meet business demand, how job scheduling, batch processing, and lights-out operations run the engine of daily IT, how monitoring and event management provide visibility into system health, how the service desk functions as the single point of contact for users, why the distinction between incident management and problem management is critical, how asset management and the CMDB provide the foundational data for service management, what environmental, fire suppression, power, and physical security controls protect the data center, how media management and end-user computing controls address often-overlooked risk areas, and how to structure your audit procedures to evaluate all of these domains.

For exam preparation, burn these key distinctions into your memory. Incident management restores service; problem management eliminates root causes. SLAs face the customer; OLAs face internal IT; underpinning contracts face external suppliers. Clean agent fire suppression protects equipment; water-based systems destroy it. The CMDB tracks configuration items and their relationships; an asset inventory only tracks assets. Monitoring collects data; event management interprets and acts on it.

In our next episode — Episode 4.2 — we move from normal operations to abnormal operations: Business Continuity and Disaster Recovery. We will cover the BCP lifecycle, business impact analysis, the critical RTO/RPO/MTD definitions that the exam loves to test, recovery site options, backup strategies, DRP testing methodologies, and the auditor's role in evaluating an organization's resilience posture. If this episode was about keeping the engine running smoothly, the next episode is about what happens when the engine fails — and how you ensure the business survives.

I will see you there.

---
*Episode 4.1 — IT Service Management & Operations*
*CISA Mastery Podcast — Domain 4: Information Systems Operations and Business Resilience*
*Duration: 36:40*
