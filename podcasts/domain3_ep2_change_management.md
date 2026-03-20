# Episode 3.2 — Change Management & Quality Assurance

**Domain 3: Information Systems Acquisition, Development, and Implementation**
**Duration: 29:50**
**CISA Exam Weight: Domain 3 represents 18% (~36 questions)**

---

## INTRODUCTION (0:00 – 2:15)

Welcome back to the CISA Exam Mastery Series. This is Episode 3.2, and we are continuing our exploration of Domain 3 — Information Systems Acquisition, Development, and Implementation. In our previous episode, we walked through the entire Systems Development Life Cycle, from feasibility study through post-implementation review, and we compared development methodologies including Waterfall, Agile, and DevOps.

Today we turn to two interrelated topics that the CISA exam treats as cornerstones of IS governance: change management and quality assurance. If the SDLC is the framework for building systems correctly the first time, change management is the framework for modifying them correctly every time thereafter. And quality assurance is the discipline that verifies correctness itself — the standards, metrics, and processes that define what "good enough" means and how we prove we have achieved it.

These topics are deeply intertwined. Every change to a production system introduces the potential for defects, security vulnerabilities, and business disruption. Quality assurance processes exist to detect these problems before they reach end users. The IS auditor's role is to verify that both frameworks — change management and quality assurance — are designed effectively, operating consistently, and producing auditable evidence.

Let me be direct about the exam significance: change management is one of the most frequently tested topics across the entire CISA examination, not just Domain 3. If you understand change management deeply, you will answer correctly on questions that appear in Domains 1, 2, 4, and 5 as well, because change management is a cross-cutting control that touches governance, security, operations, and business continuity. Let us begin.

[SECTION BREAK]

## THE CHANGE MANAGEMENT PROCESS (2:15 – 8:00)

Change management is the formalized process by which modifications to information systems are requested, evaluated, approved, implemented, and reviewed. The ISACA CISA Review Manual frames change management as a critical general control — a control that applies across all systems and applications rather than to a single application. When change management fails, the consequences cascade: unauthorized changes can introduce security vulnerabilities, destabilize production systems, violate regulatory requirements, and erode the integrity of financial reporting.

The change management process begins with a Request for Change, commonly abbreviated as RFC. An RFC is a formal document that describes the proposed change, its justification, its scope, its risk assessment, its implementation plan, its rollback plan, and its testing requirements. The RFC is the foundational artifact of change management — it creates the auditable record that a change was formally proposed rather than informally implemented.

Here is an exam concept you must internalize: every change to a production system should originate with an RFC. There are no exceptions to this principle in the exam's framework, although we will discuss emergency changes momentarily. If a question describes a scenario where changes are being made without RFCs, the IS auditor's finding is a control deficiency regardless of whether the changes themselves were technically sound.

The RFC is submitted to the Change Advisory Board, or CAB. The CAB is a cross-functional body that evaluates proposed changes and makes approval, deferral, or rejection decisions. The CAB typically includes representatives from IT operations, application development, security, business stakeholders, and — for significant changes — senior management. The composition of the CAB should reflect the scope and risk of the changes being evaluated.

The CAB evaluates each RFC against several criteria: business justification, technical feasibility, risk to existing systems and services, resource requirements, scheduling implications, and alignment with the organization's change calendar. The change calendar is a tool that provides visibility into all planned changes, enabling the CAB to identify scheduling conflicts and aggregate risk. For example, implementing three major changes to interdependent systems on the same weekend multiplies risk in ways that implementing them on separate weekends does not.

Changes are classified by their risk and impact profile. The CISA Review Manual and ITIL — which provides the most widely adopted change management framework — identify three primary classifications. Standard changes are pre-authorized, low-risk changes that follow a documented procedure and do not require individual CAB approval. Examples include password resets, user account provisioning following established procedures, or applying approved patches to non-critical systems on a defined schedule. Normal changes follow the full RFC and CAB approval process. Emergency changes bypass the standard approval process due to urgency — typically to restore a failed service or address a critical security vulnerability.

The classification of changes is itself a control that the IS auditor should evaluate. If the organization classifies too many changes as standard, it reduces CAB oversight and increases the risk of inadequately evaluated changes reaching production. If it classifies too many changes as emergency, it creates a pattern of bypassing controls that undermines the entire change management framework.

Let me give you a mnemonic for the change management process flow: "REQUEST, REVIEW, RELEASE, REFLECT." The RFC is the Request. The CAB performs the Review. Release management deploys the change. And the post-implementation review is the Reflect. Four R's, four stages, one controlled process.

[SECTION BREAK]

## EMERGENCY CHANGE PROCEDURES (8:00 – 11:00)

Emergency changes deserve special attention because they represent a controlled exception to the standard process, and the CISA exam tests your understanding of how that exception should be governed.

An emergency change is one that must be implemented immediately to restore a failed service, prevent imminent service failure, or address an actively exploited security vulnerability. The defining characteristic of an emergency change is that the standard approval process cannot be followed in its entirety before implementation because the delay would cause unacceptable business impact.

The critical point — and this is where many candidates lose marks — is that an emergency change is not an uncontrolled change. The emergency change process should still include authorization, implementation, documentation, and review. The difference is the sequencing and the delegation of authority.

In the standard process, the CAB authorizes the change before implementation. In the emergency process, a designated authority — often the change manager, the IT director, or an on-call manager — authorizes the change before implementation, and the full CAB reviews the change after implementation. This retrospective review is essential. If the exam asks what is the most important control for emergency changes, the answer is the post-implementation review by the CAB. The retrospective review verifies that the emergency change was genuinely necessary, that it was implemented correctly, that documentation has been completed, and that any temporary measures have been replaced with permanent solutions.

Here is the exam trap: the CISA exam may present a scenario where an organization has a high volume of emergency changes — say, thirty percent or more of all changes are classified as emergencies. This is a red flag. A high rate of emergency changes typically indicates one of three problems: the standard change process is too slow or bureaucratic, prompting staff to misclassify changes to bypass it; the organization has inadequate problem management processes, causing recurring incidents that require emergency fixes rather than root cause resolution; or the change classification criteria are poorly defined, allowing routine changes to be labeled as emergencies. The IS auditor should investigate the root cause and recommend corrective action.

Another exam scenario: a developer implements an emergency change to a production system and later submits the RFC documentation. Is this acceptable? Yes — provided the emergency change process was followed, including verbal or electronic authorization from the designated authority before the change was made, and the retrospective documentation and CAB review occur within a defined timeframe, typically twenty-four to forty-eight hours. The IS auditor's concern is not the sequence of paperwork but whether authorization occurred before implementation and whether retrospective review occurred after.

[SECTION BREAK]

## CONFIGURATION MANAGEMENT AND CMDB (11:00 – 14:30)

Configuration management is the discipline that maintains an accurate record of all components in the IT environment and their relationships. If change management answers "what changed and why," configuration management answers "what exists and how does it connect." The two disciplines are inseparable — you cannot evaluate the risk of a proposed change if you do not have an accurate inventory of what exists and how it is interconnected.

The Configuration Management Database, or CMDB, is the authoritative repository that stores configuration items and their relationships. A configuration item, or CI, is any component that needs to be managed in order to deliver IT services. CIs include hardware — servers, network devices, storage arrays — software — applications, operating systems, middleware — documentation, and even service level agreements. Each CI has defined attributes: name, version, location, owner, status, and relationships to other CIs.

The CMDB's value lies not just in inventorying individual CIs but in mapping their dependencies. When a change is proposed to a database server, the CMDB should reveal which applications depend on that server, which business processes depend on those applications, and which users and customers are affected. This dependency mapping enables accurate impact analysis during the change evaluation process.

From an IS audit perspective, the CMDB introduces its own control requirements. The IS auditor should verify that the CMDB is accurate — meaning it reflects the actual state of the IT environment. CMDB accuracy degrades rapidly if updates are not performed as changes occur. The auditor should verify that CMDB updates are integrated into the change management process — every approved change should trigger a corresponding CMDB update. The auditor should also verify that periodic reconciliation is performed — comparing the CMDB against the actual environment through automated discovery tools to identify discrepancies.

A baseline is a formally approved configuration of a system at a specific point in time. Baselines serve as reference points for change management — any deviation from the baseline constitutes an unauthorized change. The IS auditor should verify that baselines are established for critical systems, that baseline comparisons are performed periodically, and that deviations trigger investigation and remediation.

The CISA exam may ask about configuration management in the context of security hardening. A security baseline defines the approved security configuration for a system — which services are enabled, which ports are open, which accounts exist, which patches are applied. Compliance with security baselines is a key control that the IS auditor should evaluate, and deviation from security baselines is a finding that should be reported.

[SECTION BREAK]

## RELEASE MANAGEMENT AND PATCH MANAGEMENT (14:30 – 17:30)

Release management is the process of planning, scheduling, and controlling the movement of releases to test and production environments. A release is a collection of changes that are tested and deployed together. Release management ensures that individual changes, which may have been approved and tested independently, work correctly when combined and that the deployment to production is coordinated and controlled.

The relationship between change management and release management is important for the exam. Change management governs individual changes. Release management governs the packaging and deployment of those changes. A single release may contain multiple approved changes, and release management ensures that the aggregate risk of deploying them together is evaluated — not just the risk of each individual change.

Version control is the mechanism that tracks different iterations of software components. Every modification creates a new version, and the version control system maintains a complete history. The IS auditor should verify that version numbering follows a consistent convention, that the production version can always be identified unambiguously, and that the version control system prevents unauthorized modifications through access controls and integrity checks.

Patch management is a specialized form of change management that addresses vendor-supplied corrections to software defects and security vulnerabilities. The patch management lifecycle proceeds through several stages: monitoring for available patches from vendors and security advisories, evaluating each patch for applicability and risk, testing patches in a non-production environment to verify compatibility with the organization's configuration, approving patches through the change management process, deploying patches to production systems, and verifying successful installation.

The IS auditor's interest in patch management centers on timeliness and completeness. Critical security patches should be deployed within a defined timeframe — often measured in days or weeks depending on severity — and the IS auditor should verify that the organization tracks its patching metrics against its defined service levels. The auditor should also verify that all systems are included in the patching scope — unpatched systems are a common finding in IS audits, particularly for systems that are perceived as non-critical or that run legacy software.

Here is an exam trap on patch management: the question may ask whether patches should be applied to production systems immediately upon release by the vendor. The answer is no. Even critical security patches should be tested before production deployment to verify that they do not introduce compatibility issues or disrupt business operations. The exception would be an actively exploited zero-day vulnerability where the risk of exploitation exceeds the risk of an untested patch — but even then, the patch should be tested if time permits, and the emergency change process should be followed.

[SECTION BREAK]

## SOFTWARE QUALITY ASSURANCE (17:30 – 20:30)

Software Quality Assurance, or SQA, is the systematic process of ensuring that software development and maintenance processes, standards, and procedures are followed. Note the distinction between quality assurance and quality control. Quality assurance is process-oriented — it focuses on preventing defects by ensuring that processes are adequate and followed. Quality control is product-oriented — it focuses on detecting defects in the deliverables through testing and inspection. Both are necessary, but the CISA exam emphasizes quality assurance because it aligns with the auditor's process-evaluation role.

The Capability Maturity Model Integration, or CMMI, is a process improvement framework that the CISA exam references as a benchmark for evaluating an organization's software development maturity. CMMI defines five maturity levels. Level 1, Initial, is characterized by ad hoc and chaotic processes — success depends on individual effort rather than repeatable processes. Level 2, Managed, establishes basic project management processes — projects are planned, tracked, and controlled, but processes are not standardized across the organization. Level 3, Defined, standardizes processes across the organization — a standard process exists, and projects tailor it to their specific needs. Level 4, Quantitatively Managed, uses statistical and quantitative techniques to control processes — performance is predictable and measured. Level 5, Optimizing, focuses on continuous process improvement through innovative ideas and technologies.

For the CISA exam, remember the progression: from chaotic (Level 1) to optimized (Level 5). The IS auditor might evaluate an organization's CMMI level as part of assessing its software development capability. A Level 1 organization presents higher risk than a Level 3 organization because its processes are less predictable and less controlled.

Here is a mnemonic for the five CMMI levels: "I Must Define Quantitative Optimization" — Initial, Managed, Defined, Quantitatively managed, Optimizing. The first letter of each word matches the first letter of each level.

ISO 9001 is the international standard for quality management systems. While CMMI is specific to software and systems engineering, ISO 9001 is industry-agnostic. ISO 9001 requires organizations to establish a quality management system that includes quality policies, quality objectives, documented procedures, internal audits, management reviews, and continuous improvement. ISO 9001 certification provides external assurance that an organization's quality management system meets international standards. The IS auditor should understand that ISO 9001 certification addresses process quality, not product quality — a certified organization follows defined processes, but certification does not guarantee that every product is defect-free.

[SECTION BREAK]

## TESTING METHODOLOGIES AND QUALITY METRICS (20:30 – 24:30)

Building on the testing concepts introduced in Episode 3.1, let us now examine testing methodologies and quality metrics from the quality assurance perspective.

Black box testing, as we discussed, examines the system's external behavior without reference to its internal structure. The tester provides inputs and verifies that outputs match expected results derived from requirements specifications. Equivalence partitioning and boundary value analysis are black box techniques that the exam may reference. Equivalence partitioning divides input data into classes where all values in a class should produce equivalent behavior, then tests one representative value from each class. Boundary value analysis tests values at the edges of equivalence partitions, where defects most commonly occur — the minimum, the maximum, and values just inside and just outside the boundaries.

White box testing examines the internal logic of the system. Statement coverage ensures every line of code is executed at least once. Branch coverage — also called decision coverage — ensures every decision point evaluates to both true and false. Path coverage ensures every possible execution path through the code is tested. The levels of coverage increase in rigor: statement coverage is the weakest, path coverage is the strongest but often impractical for complex systems due to the combinatorial explosion of possible paths.

Regression testing verifies that changes have not broken previously working functionality. After any modification — a defect fix, an enhancement, a patch — regression tests are executed to confirm that existing functions continue to work correctly. In modern development environments, regression test suites are automated and integrated into the CI/CD pipeline. The IS auditor should verify that regression testing is mandatory before any release to production and that the regression test suite is maintained as the system evolves.

Stress testing pushes the system beyond its expected operational capacity to identify failure modes and breaking points. The objective is not to verify that the system meets its performance requirements — that is performance testing — but to determine what happens when those limits are exceeded. Does the system degrade gracefully, queuing requests and maintaining data integrity? Or does it fail catastrophically, corrupting data or crashing without recovery? The IS auditor's interest in stress testing results relates to business continuity — understanding failure modes informs disaster recovery planning.

Performance testing verifies that the system meets its non-functional performance requirements under expected load. This includes response time testing, throughput testing, and scalability testing. The IS auditor should verify that performance testing was conducted under conditions representative of the production environment and that the results demonstrate compliance with performance requirements specified during the requirements definition phase.

Code review and static analysis deserve attention as quality assurance techniques. Static analysis tools examine source code without executing it, identifying potential defects, security vulnerabilities, coding standard violations, and code complexity issues. Static analysis is particularly valuable for security because it can identify common vulnerability patterns — SQL injection, cross-site scripting, buffer overflows — before the code is tested or deployed. The IS auditor should verify that static analysis is integrated into the development process and that findings are tracked and remediated.

Quality metrics provide quantitative measures of software quality. Two metrics the exam references are defect density and cyclomatic complexity.

Defect density measures the number of confirmed defects per unit of software size — typically defects per thousand lines of code or defects per function point. Higher defect density indicates lower quality. The IS auditor can use defect density trends to evaluate the effectiveness of quality assurance processes — declining defect density over successive releases suggests improving quality processes.

Cyclomatic complexity measures the structural complexity of a module by counting the number of independent paths through its code. Higher cyclomatic complexity indicates more complex logic, which is harder to test, harder to maintain, and more likely to contain defects. A cyclomatic complexity above ten for a single module is generally considered high risk, and modules with complexity above twenty are strong candidates for refactoring. The IS auditor can use cyclomatic complexity metrics to identify high-risk modules that warrant additional testing or code review.

[SECTION BREAK]

## SEPARATION OF DUTIES IN DEVELOPMENT ENVIRONMENTS (24:30 – 27:00)

Separation of duties in development environments is one of the most heavily tested concepts in Domain 3. The principle is straightforward but its implementation has nuances that the exam explores in detail.

The fundamental rule is that three environments should exist — development, testing, and production — and that access to each environment should be restricted based on role. Developers should have full access to the development environment, limited access to the testing environment, and no access to the production environment. Testers should have full access to the testing environment but should not have access to modify source code in the development environment. Operations staff should have access to the production environment but should not have the ability to modify source code or test scripts.

The rationale is control over the integrity of production systems. If a developer can directly modify production code, there is no independent verification that the modification is correct, authorized, and properly tested. If a tester can modify source code, there is no assurance that the tested version matches the deployed version.

The migration of code between environments should be controlled by an independent function — typically a release management or configuration management team — that verifies authorization and completeness before promoting code from one environment to the next. Automated deployment pipelines can serve this function, provided the pipeline enforces authorization gates and audit logging.

The IS auditor should verify these separations through access control reviews. Specifically, the auditor should obtain user access lists for each environment and verify that no individual has write access to both the development and production environments. The auditor should also review logs for evidence of direct modifications to production — any such modifications constitute a control violation that should be reported.

Here is the exam scenario you should anticipate: a question describes a small IT department where the same person develops, tests, and deploys code. What is the IS auditor's primary concern? The answer is inadequate separation of duties. The follow-up question: what compensating controls should the auditor recommend? The answer includes independent code reviews, enhanced audit logging with management review, after-the-fact change verification by management, and periodic independent audits of production changes. These compensating controls do not eliminate the risk but reduce it to an acceptable level when full separation of duties is not feasible.

[SECTION BREAK]

## THE AUDITOR'S ROLE IN CHANGE MANAGEMENT REVIEW (27:00 – 29:00)

The IS auditor's review of change management is one of the most structured audit exercises in the CISA domain. Let me walk you through the key audit procedures.

First, the auditor should evaluate the change management policy and procedures for completeness. The policy should define the change management process, roles and responsibilities — including the CAB composition and authority — change classification criteria, emergency change procedures, and documentation requirements. The procedures should provide step-by-step guidance for each type of change.

Second, the auditor should test compliance with the policy by selecting a sample of changes and tracing each one through the process. For each sampled change, the auditor should verify that an RFC was submitted and documented, that the RFC was evaluated and approved by the appropriate authority — the CAB for normal changes, the designated authority for emergency changes — that testing was performed and documented, that the change was implemented as approved, that the CMDB was updated to reflect the change, and that a post-implementation review was conducted.

Third, the auditor should look for unauthorized changes by comparing the authorized change log against actual changes detected in the environment. This can be accomplished by comparing system configurations against baselines, reviewing system and application logs for modification timestamps, or using file integrity monitoring tools that detect unauthorized modifications.

Fourth, the auditor should evaluate the effectiveness of the change management process by analyzing metrics: the ratio of successful to failed changes, the ratio of emergency to normal changes, the frequency of changes that require rollback, and the average time from RFC submission to implementation. Deteriorating metrics indicate process weaknesses.

If the audit identifies unauthorized changes — changes that were implemented without following the change management process — this is a significant finding that should be reported to senior management. Unauthorized changes undermine the integrity of the production environment and may indicate fraud, negligence, or systemic process failures.

[SECTION BREAK]

## SUMMARY AND BRIDGE TO EPISODE 3.3 (29:00 – 29:50)

Let us recap the critical concepts. Change management is a general control that governs all modifications to production systems through a structured process of request, review, release, and reflection. The CAB is the governing body that evaluates and approves changes. Emergency changes are controlled exceptions that require retrospective review. Configuration management maintains an accurate record of IT components and their relationships through the CMDB. Release management coordinates the deployment of changes. Patch management addresses vendor-supplied corrections with an emphasis on timeliness and testing.

Quality assurance prevents defects through process rigor, while quality control detects defects through testing and inspection. CMMI provides a five-level maturity model for evaluating process capability. Testing methodologies — black box, white box, regression, stress, performance — serve different purposes within the quality framework. Quality metrics such as defect density and cyclomatic complexity provide quantitative evidence of software quality. Separation of duties between development, testing, and production environments is a fundamental control that the IS auditor must verify.

In Episode 3.3, we complete Domain 3 with project management for information systems. We will examine PMBOK and PRINCE2 frameworks, earned value management, function point analysis, and the auditor's role in evaluating project governance. Project management is the discipline that ensures SDLC activities are planned, resourced, and controlled — it is the management wrapper around everything we have discussed in Episodes 3.1 and 3.2.

Thank you for your focused attention, and I will see you in Episode 3.3.

---

*End of Episode 3.2 — Change Management & Quality Assurance*
*Next: Episode 3.3 — Project Management for IS*
