# Episode 3.1 — Systems Development Life Cycle (SDLC)

**Domain 3: Information Systems Acquisition, Development, and Implementation**
**Duration: 41:30**
**CISA Exam Weight: Domain 3 represents 18% (~36 questions)**

---

## INTRODUCTION (0:00 – 2:30)

Welcome to Episode 3.1 of the CISA Exam Mastery Series. I am your host, and today we begin our deep exploration of Domain 3 — Information Systems Acquisition, Development, and Implementation. This domain carries an eighteen percent weight on the CISA examination, which translates to approximately thirty-six questions. Among the five domains, this one demands perhaps the broadest technical literacy, because it spans the entire life cycle of an information system — from the first spark of a business need through to post-implementation review and eventual retirement.

In this episode, we tackle the foundational pillar of Domain 3: the Systems Development Life Cycle, commonly referred to as the SDLC. If Domain 1 was about governing the information systems function and Domain 2 was about protecting information assets, Domain 3 is about building and changing those assets in a controlled, auditable, and repeatable manner. The IS auditor's role here is not to write code or manage projects — it is to provide independent assurance that the processes by which systems are conceived, designed, built, tested, and deployed meet organizational objectives while maintaining adequate controls throughout.

We will work through the traditional SDLC phases in sequence, then expand outward to compare development methodologies — Waterfall, iterative, spiral, Agile, and DevOps — because the CISA exam expects you to know not just what each methodology prescribes, but where each one introduces unique risks and where audit controls must be embedded. By the end of this episode, you will have a command of SDLC concepts that is both exam-ready and enterprise-applicable.

Let us begin.

[SECTION BREAK]

## THE TRADITIONAL SDLC: AN OVERVIEW (2:30 – 5:30)

The Systems Development Life Cycle is a structured framework that defines the activities performed at each stage of a system's development. The ISACA CISA Review Manual identifies seven canonical phases: feasibility study, requirements definition, system design, development, testing, implementation, and post-implementation review with ongoing maintenance. Some references collapse these into five or six phases; others expand them. For the CISA exam, you should be comfortable with the seven-phase model while recognizing that real-world implementations vary.

The critical concept that the exam tests repeatedly is this: the SDLC is a control framework, not merely a development process. Each phase has defined inputs, activities, outputs — which ISACA calls deliverables — and control checkpoints. These checkpoints exist so that management and, by extension, auditors can verify that the system being developed will meet its stated objectives, that risks have been identified and mitigated, and that the organization has not committed irreversible resources to a flawed concept.

Think of the SDLC as a series of gates. At each gate, a decision is made: proceed, revise, or terminate. The IS auditor's role is to verify that these gates exist, that they are functioning as designed, and that the evidence of gate reviews is documented and retained. This concept — verifiable decision points with documented evidence — is the thread that runs through every SDLC question on the CISA exam.

Let me walk you through each phase in detail.

[SECTION BREAK]

## PHASE 1: FEASIBILITY STUDY (5:30 – 9:00)

The feasibility study is the first formal phase of the SDLC, and it answers a deceptively simple question: should this system be built? This phase is sometimes called the preliminary investigation or the business case phase. Regardless of label, its purpose is to evaluate whether a proposed system is technically feasible, economically justified, operationally viable, and consistent with the organization's strategic direction.

The CISA Review Manual identifies four dimensions of feasibility. Technical feasibility asks whether the required technology exists, whether the organization possesses or can acquire the necessary technical skills, and whether the proposed system can integrate with existing infrastructure. Economic feasibility performs a cost-benefit analysis, comparing the total cost of ownership against quantified benefits over a defined time horizon. Common techniques here include net present value, internal rate of return, and payback period analysis. Operational feasibility examines whether the organization can actually absorb the proposed system — do end users have the capacity and willingness to adopt new processes? And schedule feasibility assesses whether the project can be completed within an acceptable timeframe.

From the auditor's perspective, the feasibility study is where the most consequential decisions are made with the least information. This creates an inherent risk. The IS auditor should verify that the feasibility study was conducted with appropriate rigor, that assumptions are documented and reasonable, that alternative solutions were evaluated rather than a single predetermined outcome being rubber-stamped, and that senior management formally approved the decision to proceed.

Here is your first exam trap for this episode. The CISA exam frequently asks: at what point in the SDLC should the IS auditor first become involved? The answer is the feasibility study. Not requirements. Not testing. The feasibility study. The rationale, per ISACA, is that the auditor's early involvement allows control requirements to be built into the system from inception rather than bolted on after the fact. This is a recurring ISACA philosophy — controls are most effective and least expensive when incorporated early.

A related exam trap: the feasibility study is where the initial risk assessment for the project should occur. If the exam asks when project risks should first be formally identified, the answer points here — not to a later phase.

Let me give you a mnemonic for the four feasibility dimensions: TEOS — Technical, Economic, Operational, Schedule. Think of it as "TEOS" — The Evaluation Of Systems. Four letters, four dimensions, one decision gate.

[SECTION BREAK]

## PHASE 2: REQUIREMENTS DEFINITION (9:00 – 13:30)

Once the feasibility study concludes with a decision to proceed, the project enters requirements definition. This is arguably the most important phase of the entire SDLC, because errors introduced here propagate through every subsequent phase. Research consistently demonstrates that the cost of correcting a requirements defect increases by an order of magnitude with each subsequent phase. A requirements error caught during design costs ten times more to fix than one caught during requirements. The same error caught during testing costs a hundred times more. Caught in production? A thousand times more.

Requirements definition has two major sub-activities: gathering requirements and documenting them.

Requirements gathering techniques are a frequent exam topic. Joint Application Development, or JAD, is a facilitated workshop approach where business users, IT professionals, and other stakeholders collaborate intensively over a compressed timeframe — typically two to five days — to define system requirements. The key advantage of JAD is that it reduces the elapsed time for requirements gathering and produces higher-quality requirements because conflicts and ambiguities are resolved in real time with all parties present. The key risk is that JAD sessions can be dominated by senior or more vocal participants, potentially suppressing valid requirements from less assertive stakeholders.

Prototyping is another gathering technique where a working model of the proposed system is built rapidly to help users visualize and refine their requirements. Prototyping is particularly valuable when users cannot articulate their needs in abstract terms but can react effectively to a tangible demonstration. The risk with prototyping is scope creep — users may treat the prototype as the final system and resist starting formal development. The IS auditor should verify that prototypes are clearly labeled as disposable artifacts and that management controls exist to prevent prototype code from migrating into production.

Other gathering techniques include interviews, questionnaires, observation of existing workflows, and analysis of existing documentation. The CISA exam does not typically test these in depth, but you should know that a robust requirements process uses multiple techniques to triangulate and validate requirements.

Now, requirements themselves are classified into two categories that the exam tests explicitly: functional requirements and non-functional requirements.

Functional requirements describe what the system must do. They define specific behaviors, calculations, data manipulations, and business rules. For example: the system shall calculate sales tax based on the shipping destination's jurisdiction. That is a functional requirement — it describes a specific system behavior.

Non-functional requirements describe how the system must perform. They define quality attributes such as performance, scalability, availability, security, usability, and maintainability. For example: the system shall support five hundred concurrent users with a response time of less than two seconds for any transaction. That is a non-functional requirement — it constrains how the system delivers its functionality.

Here is the exam trap: when the CISA exam asks about security requirements, the correct classification is non-functional requirements. Security is a quality attribute of the system, not a specific business function. This catches many candidates who intuitively associate security with functional behavior. Similarly, audit trail requirements — the ability to log and trace system activities — are non-functional requirements.

The deliverable of this phase is the Software Requirements Specification, or SRS. The IS auditor should verify that the SRS has been formally reviewed and approved by business stakeholders, that requirements are traceable — meaning each requirement has a unique identifier that can be linked forward to design elements, test cases, and implementation artifacts — and that the SRS includes acceptance criteria that will be used during User Acceptance Testing.

Requirements traceability is a concept you must know cold. A requirements traceability matrix maps every requirement to its origin (which stakeholder requested it), its design implementation, its test case, and its deployment status. This matrix is the auditor's primary tool for verifying that no requirements were dropped, added without authorization, or inadequately tested. If the exam asks how an IS auditor can best verify that all business requirements were implemented and tested, the answer is the requirements traceability matrix.

[SECTION BREAK]

## PHASE 3: SYSTEM DESIGN (13:30 – 17:00)

With requirements defined and approved, the project moves into system design. This phase translates the what of requirements into the how of technical architecture. System design has two distinct levels: logical design and physical design.

Logical design, sometimes called the conceptual design, describes what the system will do without specifying the technology that will implement it. It defines data flows, entity relationships, process models, and business logic at an abstract level. Logical design artifacts include data flow diagrams, entity-relationship diagrams, and process specifications. The advantage of separating logical design from physical design is that it allows designers to optimize the business logic independently of technology constraints, and it creates a stable reference point that survives technology changes.

Physical design translates the logical design into a technology-specific blueprint. It specifies hardware platforms, operating systems, database management systems, network architectures, programming languages, user interface layouts, and security architectures. Physical design produces artifacts such as database schemas, network topology diagrams, screen layouts, and interface specifications.

The IS auditor's concern during design is primarily about controls. Specifically, the auditor should verify that application controls — input controls, processing controls, and output controls — are designed into the system, not treated as afterthoughts. Input controls include validation checks, authorization requirements, and error handling for data entry. Processing controls include audit trails, run-to-run totals, and reconciliation procedures. Output controls include distribution lists, report balancing, and retention schedules.

The design phase is also where security architecture should be formally specified. Per NIST Special Publication 800-64, which provides guidance on security considerations in the SDLC, security controls should be designed during this phase based on the risk assessment performed earlier and the security requirements captured during requirements definition. The IS auditor should look for evidence that security design was informed by a threat model and that the principle of least privilege was applied to access control design.

An important exam concept here is the distinction between general controls and application controls. General controls operate at the infrastructure level — access controls to the operating system, change management procedures, backup and recovery processes. Application controls operate within the application itself — input validation, processing logic, output reconciliation. During the design phase, both categories of controls should be addressed. The IS auditor should verify that the design documentation explicitly addresses how the application will interact with general controls in the production environment.

One more design concept the exam tests: the distinction between coupled and decoupled architectures. Tightly coupled systems have strong interdependencies between components, meaning a change in one component can cascade unpredictably to others. Loosely coupled systems minimize interdependencies through well-defined interfaces and abstraction layers. From an audit perspective, loosely coupled architectures are preferred because they reduce the risk of unintended side effects during changes and make it easier to isolate and test individual components.

[SECTION BREAK]

## PHASE 4: DEVELOPMENT (17:00 – 20:30)

The development phase is where the system is actually built — where code is written, databases are created, interfaces are configured, and the abstract designs of the previous phase become tangible software. For the IS auditor, the development phase introduces a specific set of risks related to coding practices, access controls, and separation of duties.

Let us address programming languages and paradigms briefly, because the CISA exam does test conceptual understanding. You are not expected to write code, but you should understand the distinction between procedural programming, which executes instructions sequentially; object-oriented programming, which encapsulates data and behavior into objects that interact through defined interfaces; and scripting languages, which are typically interpreted rather than compiled and are used for automation and rapid prototyping. From an audit perspective, the key concern is not which paradigm is used but whether coding standards exist, whether they are enforced, and whether the chosen approach supports maintainability and security.

Code review is a critical control during development. Code reviews can be formal — structured walkthroughs or inspections with defined roles and documented findings — or informal — peer reviews where a second developer examines the code. The CISA exam emphasizes that code reviews serve dual purposes: they detect defects earlier than testing can, and they verify compliance with coding standards. The IS auditor should verify that code reviews are mandatory, that review findings are documented and tracked to resolution, and that the person who wrote the code is not the sole reviewer — this is a basic separation of duties control.

Separation of duties in development environments is an exam favorite. The foundational principle is this: developers should not have access to production environments, and production support staff should not have the ability to modify source code. The ISACA guidance is explicit — the same individual should not be responsible for coding, testing, and migrating code to production. In practice, this means maintaining separate environments for development, testing, and production, with formal procedures and approvals for promoting code between environments.

Here is an exam scenario you should prepare for: a small organization argues that it cannot afford to maintain separate environments due to resource constraints. What should the IS auditor recommend? The answer is compensating controls. If full separation of duties is not feasible, compensating controls include enhanced logging and monitoring, independent code reviews, and after-the-fact audit reviews of changes. The auditor should document the control deficiency and the compensating controls in the audit report.

Version control systems — also called source code management systems — are essential controls during development. A version control system maintains a complete history of all changes to source code, including who made each change, when, and why. This provides accountability and the ability to roll back problematic changes. The IS auditor should verify that all source code is managed through a version control system, that check-in and check-out procedures are enforced, and that access to the version control system is restricted based on role.

One more development phase concept: the build process. Modern development practices use automated build tools that compile source code, link libraries, and package the application for deployment. The IS auditor should verify that the build process is automated and repeatable — meaning the same source code always produces the same build output — and that build artifacts are stored in a controlled repository with integrity verification such as cryptographic hashes.

[SECTION BREAK]

## PHASE 5: TESTING (20:30 – 26:00)

Testing is the phase where the CISA exam concentrates some of its most detailed and nuanced questions. The reason is straightforward: testing is the primary mechanism for verifying that a system meets its requirements, that controls function as designed, and that defects are identified before the system reaches production. The IS auditor must understand the testing hierarchy, testing techniques, and the governance of the testing process.

The testing hierarchy, from narrowest to broadest scope, proceeds through four levels: unit testing, integration testing, system testing, and user acceptance testing.

Unit testing verifies individual components — typically individual modules, functions, or classes — in isolation. Unit tests are written and executed by developers, and they focus on verifying that each component produces correct outputs for given inputs. The key characteristic of unit testing is isolation: the component under test is separated from its dependencies, which are replaced by stubs or mock objects. From an audit perspective, the IS auditor typically does not review individual unit tests but should verify that a unit testing standard exists and that code coverage metrics indicate adequate testing.

Integration testing verifies that components work correctly when combined. After individual units have passed their tests, integration testing focuses on the interfaces between components — do they exchange data correctly? Do they handle error conditions at boundaries appropriately? There are two common strategies for integration testing: top-down, where testing begins with higher-level components and progressively incorporates lower-level components using stubs; and bottom-up, where testing begins with lower-level components and progressively incorporates higher-level components using drivers. The IS auditor should verify that integration test plans explicitly address interface specifications and error handling.

System testing verifies the complete, integrated system against its requirements specification. This is the first level of testing that exercises the system as a whole, and it includes multiple sub-types. Functional testing verifies that the system performs its required functions correctly. Performance testing — also called load testing — verifies that the system meets its performance requirements under expected load conditions. Stress testing pushes the system beyond its expected load to identify breaking points and failure behaviors. Security testing verifies that security controls function as designed and attempts to identify vulnerabilities. Regression testing verifies that changes to one part of the system have not introduced defects in previously working functionality. Recovery testing verifies that the system can be restored to operation after a failure.

Here is a critical exam distinction: the difference between system testing and user acceptance testing. System testing is performed by the IT organization, typically a dedicated QA team, against the technical requirements specification. User acceptance testing, or UAT, is performed by business users against the business requirements. The purpose of UAT is to verify that the system meets business needs as understood by the people who will actually use it. UAT is the final testing gate before the system is approved for production deployment.

The CISA exam tests this distinction in a specific way. If the exam asks who should perform final acceptance testing before a system is deployed to production, the answer is always the business users — not IT, not QA, not the development team. This is because only the business users can verify that the system actually meets business needs. The IS auditor should verify that UAT was performed by actual end users, that test cases were derived from business requirements, and that formal sign-off was obtained before deployment was authorized.

Now let us discuss testing techniques that the exam references frequently.

Black box testing treats the system as an opaque box — the tester provides inputs and observes outputs without any knowledge of internal logic. Black box testing is based on requirements and specifications. It is effective for validating external behavior but may miss internal logic errors.

White box testing — also called glass box or structural testing — examines the internal logic of the system. The tester has access to source code and designs test cases to exercise specific code paths, branches, and conditions. White box testing is more thorough for detecting logic errors but requires technical skill and access to source code.

The exam may ask which type of testing is more appropriate for an IS auditor to perform or evaluate. The answer depends on context. When auditing application controls, the auditor might use black box testing — providing test transactions and verifying outputs. When auditing code quality or security, the auditor might evaluate white box testing results or use static analysis tools that examine source code without executing it.

One more testing concept that appears on the exam: test data management. Test data should be representative of production data but should not contain actual sensitive information. If production data is used for testing, it must be masked or anonymized. The IS auditor should verify that test data management procedures exist, that sensitive data is protected in test environments, and that test data is refreshed periodically to maintain relevance.

Let me give you a mnemonic for the testing hierarchy: UISU — Unit, Integration, System, UAT. Think "You I See You" — you see the system from the inside out, expanding scope at each level.

[SECTION BREAK]

## PHASE 6: IMPLEMENTATION (26:00 – 31:00)

Implementation — also called deployment or conversion — is the phase where the tested system is placed into the production environment and made available to users. This phase carries significant risk because it involves changing the production environment, and errors during implementation can disrupt business operations. The IS auditor must understand the four implementation strategies and their risk profiles.

The first strategy is parallel operation, also called parallel running. Under this approach, the old system and the new system run simultaneously for a defined period, processing the same transactions. Outputs from both systems are compared to verify that the new system produces correct results. Parallel operation is the safest implementation strategy because the old system remains fully operational throughout the transition. If the new system fails or produces incorrect results, the organization simply continues using the old system. The disadvantage is cost — running two systems simultaneously requires double the processing resources, and staff must perform duplicate data entry or reconciliation. Parallel operation is most appropriate for critical systems where the cost of failure is high.

The second strategy is phased implementation, also called modular implementation. Under this approach, the new system is deployed in stages — perhaps one module at a time, one department at a time, or one geographic location at a time. Phased implementation reduces risk compared to a big-bang deployment because problems are contained within the scope of the current phase and can be corrected before the next phase proceeds. The disadvantage is complexity — the organization must manage temporary interfaces between old and new system components, and the implementation timeline is extended.

The third strategy is pilot implementation. Under this approach, the new system is deployed to a limited group of users — a single department, location, or business unit — while the rest of the organization continues using the old system. The pilot group serves as a proving ground, and lessons learned from the pilot inform the broader rollout. Pilot implementation is sometimes confused with phased implementation, but the distinction is important: phased implementation deploys different modules sequentially, while pilot implementation deploys the complete system to a limited audience. The IS auditor should verify that the pilot group is representative of the broader user population and that success criteria for the pilot are defined before deployment.

The fourth strategy is direct cutover, also called the big bang or abrupt changeover. Under this approach, the old system is decommissioned and the new system is activated in a single transition. Direct cutover is the riskiest implementation strategy because there is no fallback — if the new system fails, the organization has no operational system. However, it is also the least expensive and fastest approach. Direct cutover may be the only feasible strategy when the old and new systems are so fundamentally different that parallel operation or phased implementation is impractical. The IS auditor should verify that extensive testing was performed, that rollback procedures exist, and that contingency plans address the scenario where the new system fails after the old system has been decommissioned.

Here is the exam trap on implementation strategies, and it appears with remarkable frequency: the CISA exam will describe a scenario and ask which implementation strategy carries the least risk. The answer is always parallel operation. If the question asks which strategy carries the most risk, the answer is always direct cutover. If the question describes a constraint — limited budget, incompatible systems, tight timeline — it may point to a different strategy as the most appropriate, but the risk ranking remains constant: parallel is safest, direct cutover is riskiest, with phased and pilot in between.

Data conversion is a critical activity during implementation that the exam also tests. When a new system replaces an existing system, data must be migrated from old formats to new formats. The IS auditor should verify that data conversion procedures include validation checks to ensure completeness and accuracy of migrated data. Common validation techniques include record count reconciliation, control total comparison, and sample verification of converted records against source data. Data conversion errors are a frequent source of post-implementation problems, and the IS auditor should specifically test whether converted data maintains its integrity.

Another implementation activity is user training. The IS auditor should verify that training was conducted before the system was deployed, that training materials are consistent with the system's actual functionality, and that training effectiveness was assessed. A system that is technically perfect but poorly understood by its users will fail to deliver business value and may introduce operational risks through user errors.

A concept that bridges implementation and the next phase: the implementation plan should define explicit criteria for declaring the implementation successful. These criteria should be measurable, time-bound, and agreed upon by both IT and business stakeholders before deployment begins. The IS auditor should verify that these criteria exist and that they are evaluated during the post-implementation review.

[SECTION BREAK]

## PHASE 7: POST-IMPLEMENTATION REVIEW AND MAINTENANCE (31:00 – 34:00)

The post-implementation review, or PIR, is the final formal phase of the SDLC, and it is one of the most frequently neglected phases in practice. The PIR is conducted after the system has been operational for a sufficient period — typically three to six months — to evaluate whether the system achieved its intended objectives, whether actual costs and benefits align with projections from the feasibility study, whether control objectives are being met, and whether users are satisfied with the system.

The IS auditor has a particular interest in the PIR because it provides evidence of whether the SDLC process itself is effective. If the PIR reveals significant gaps between requirements and delivered functionality, it suggests weaknesses in the requirements definition or testing phases. If it reveals cost overruns, it suggests weaknesses in project estimation or scope management. The PIR is, in effect, an audit of the development process as much as it is an assessment of the delivered system.

From an exam perspective, you should know that the PIR should be conducted by a party independent of the development team. This could be the IS audit function, an independent project review team, or an external reviewer. The independence requirement exists because the development team has an inherent bias toward reporting success.

Maintenance is the ongoing phase that follows the PIR and continues for the operational life of the system. Maintenance activities include corrective maintenance — fixing defects discovered during operation — adaptive maintenance — modifying the system to accommodate changes in the business or technical environment — perfective maintenance — enhancing the system to improve performance or usability — and preventive maintenance — modifying the system to prevent future problems. The IS auditor should verify that maintenance activities follow the same change management controls as new development, a topic we will explore in depth in Episode 3.2.

[SECTION BREAK]

## DEVELOPMENT METHODOLOGIES: WATERFALL (34:00 – 35:30)

Having covered the seven phases of the traditional SDLC, let us now examine how different methodologies structure the progression through these phases. The CISA exam tests your understanding of five major methodologies and their implications for audit and control.

The Waterfall model is the classical approach, and it maps most directly to the seven-phase SDLC we just discussed. In the Waterfall model, each phase is completed in its entirety before the next phase begins, and there is no backward movement — once a phase is complete, the project does not revisit it. The Waterfall model produces extensive documentation at each phase, which provides a strong audit trail. Its primary advantage is predictability: the sequential structure makes progress easy to measure and manage.

The Waterfall model's primary disadvantage is rigidity. Because requirements are frozen early in the process, the Waterfall model handles changing requirements poorly. If business needs evolve during a lengthy development cycle, the delivered system may not match current needs. This makes the Waterfall model most appropriate for projects where requirements are well understood, stable, and unlikely to change — for example, regulatory compliance systems where the requirements are defined by law or regulation.

The exam trap here: if a question describes a project with stable, well-defined requirements and asks which methodology is most appropriate, Waterfall is a strong candidate. If the question describes evolving or uncertain requirements, Waterfall is the wrong answer.

[SECTION BREAK]

## DEVELOPMENT METHODOLOGIES: ITERATIVE, SPIRAL, AND AGILE (35:30 – 39:30)

The iterative model addresses Waterfall's rigidity by repeating the SDLC phases in cycles, or iterations. Each iteration produces a working version of the system with increasing functionality. The iterative model accommodates changing requirements because each iteration can incorporate feedback from previous iterations.

The spiral model, proposed by Barry Boehm, adds a distinctive feature: explicit risk analysis at the beginning of each iteration. The project proceeds through four quadrants in each spiral: determine objectives and alternatives, evaluate alternatives and identify risks, develop and verify the product, and plan the next iteration. The spiral model is particularly appropriate for large, high-risk projects because the risk analysis at each iteration allows the project to be terminated early if risks become unacceptable. For the CISA exam, remember that the spiral model's distinguishing characteristic is its emphasis on risk analysis. If a question asks which methodology explicitly incorporates risk assessment into its iterative process, the answer is the spiral model.

Agile methodology represents a fundamental departure from the plan-driven approaches of Waterfall and spiral. Agile is built on the principles articulated in the Agile Manifesto of 2001: individuals and interactions over processes and tools, working software over comprehensive documentation, customer collaboration over contract negotiation, and responding to change over following a plan. Note the deliberate phrasing — the manifesto values the items on the left more than the items on the right, but it does not eliminate the items on the right entirely.

Scrum is the most widely adopted Agile framework, and the CISA exam expects you to know its key elements. A Scrum team consists of a Product Owner, who represents business stakeholders and prioritizes the product backlog; a Scrum Master, who facilitates the process and removes impediments; and the Development Team, which is self-organizing and cross-functional. Work is organized into sprints — fixed-duration iterations typically lasting two to four weeks. Each sprint begins with sprint planning, where the team selects items from the product backlog and commits to delivering them within the sprint. Daily stand-up meetings — limited to fifteen minutes — keep the team synchronized. At the end of each sprint, a sprint review demonstrates completed work to stakeholders, and a sprint retrospective examines the team's process and identifies improvements.

User stories are the primary unit of work in Agile. A user story follows the format: "As a [role], I want [capability] so that [benefit]." User stories are deliberately brief because they serve as placeholders for conversations between the development team and stakeholders, not as comprehensive specifications.

From an IS audit perspective, Agile presents a specific challenge: it produces less formal documentation than Waterfall, which can make the audit trail thinner. The IS auditor must adapt by looking for alternative evidence of control — automated test suites that serve as living specifications, version control histories that document changes, sprint artifacts that demonstrate stakeholder involvement, and retrospective records that demonstrate process improvement. The auditor should not reject Agile simply because it does not produce traditional SDLC documentation; rather, the auditor should evaluate whether the controls embedded in the Agile process achieve the same objectives as traditional SDLC controls through different means.

DevOps extends Agile principles into operations by breaking down the traditional wall between development and operations teams. DevOps practices include continuous integration, where developers merge code changes into a shared repository frequently — often multiple times per day — with automated build and test processes verifying each integration. Continuous delivery extends continuous integration by automating the deployment pipeline so that code changes can be released to production at any time with a manual approval gate. Continuous deployment removes the manual gate, deploying every change that passes automated testing directly to production.

CI/CD pipelines — continuous integration and continuous delivery or deployment — are automated workflows that build, test, and deploy code. The IS auditor should verify that CI/CD pipelines include adequate quality gates — automated tests, code analysis, security scans — and that pipeline configurations are managed under version control with change management controls.

DevSecOps integrates security practices into the DevOps pipeline. Rather than treating security as a separate phase or gate, DevSecOps embeds security testing — static analysis, dynamic analysis, dependency scanning, container image scanning — into the automated pipeline. Every code change is automatically evaluated for security vulnerabilities before it can progress toward production. The IS auditor should verify that security tools in the DevSecOps pipeline are current, that their findings are tracked and remediated, and that the pipeline cannot be bypassed.

Here is a mnemonic for comparing methodologies by their distinguishing characteristic: "WISARD" — Waterfall Is Sequential, Agile Responds to change, Spiral manages Risk, DevOps Deploys continuously. Each methodology's name maps to its primary differentiator.

[SECTION BREAK]

## SUMMARY AND EXAM PREPARATION (39:30 – 41:30)

Let us consolidate what we have covered. The SDLC provides a structured framework for developing information systems with embedded controls at each phase. The feasibility study determines whether a project should proceed and is where the IS auditor should first become involved. Requirements definition is the most critical phase because errors here propagate with exponentially increasing cost. Design translates requirements into technical architecture with both logical and physical components. Development introduces risks around coding standards, separation of duties, and version control. Testing progresses from unit to integration to system to UAT, with user acceptance testing performed by business users as the final gate. Implementation strategies range from parallel operation, which is safest, to direct cutover, which is riskiest. Post-implementation review provides independent verification that the system achieved its objectives.

Among methodologies, Waterfall is sequential and documentation-heavy, suitable for stable requirements. Iterative approaches cycle through phases repeatedly. The spiral model distinguishes itself through explicit risk analysis. Agile and Scrum prioritize working software and stakeholder collaboration with shorter delivery cycles. DevOps and DevSecOps extend these principles into operations and security.

For the exam, remember these key principles: the IS auditor should be involved from the feasibility study onward; the requirements traceability matrix is the auditor's primary tool for verifying complete and accurate implementation; separation of duties between development, testing, and production is a fundamental control; and user acceptance testing by business users is the final gate before production deployment.

In our next episode, Episode 3.2, we will dive into change management and quality assurance — the controls that govern how systems are modified after initial deployment, and the quality frameworks that ensure software meets defined standards throughout its life cycle. Change management is, in many ways, the ongoing application of SDLC principles to a living system, and it is one of the most heavily tested topics in Domain 3.

Thank you for your attention, and I will see you in Episode 3.2.

---

*End of Episode 3.1 — Systems Development Life Cycle (SDLC)*
*Next: Episode 3.2 — Change Management & Quality Assurance*
