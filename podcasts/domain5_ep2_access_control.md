# Domain 5, Episode 2 — Access Control & Identity Management

**CISA Exam Preparation Podcast — Protection of Information Assets**
**Episode Duration: 39:30**

---

Welcome back to the CISA Mastery Podcast. This is Episode Two of Domain Five — Protection of Information Assets. In the previous episode, we established the governance frameworks and policy structures that underpin information security. Now we move into the control domain that, in my experience, generates more audit findings than any other: access control and identity management.

Access control is deceptively simple in concept — ensure that the right people have the right access to the right resources at the right time for the right reasons. In practice, it is an extraordinarily complex discipline that touches every system, every user, every business process. It is the domain where governance aspirations collide with operational reality, and the collision points are exactly where the CISA exam likes to focus.

Let us get into it.

[SECTION BREAK]

## Access Control Models — DAC, MAC, RBAC, ABAC

The CISA exam expects you to identify, compare, and evaluate four primary access control models. Each model embodies a different philosophy about who decides access, how decisions are enforced, and what tradeoffs are accepted.

Your mnemonic for these four models, plus the Bell-LaPadula model we will touch on: "Don't Make Rules About Behaviour" — DAC, MAC, RBAC, ABAC, Bell-LaPadula. Let me walk through each in depth.

Discretionary Access Control — DAC — is the most permissive model. Under DAC, the owner of a resource determines who can access that resource. If you create a file, you decide who can read it, modify it, or delete it. Most commercial operating systems — Windows NTFS permissions, Unix file permissions — implement DAC natively. The advantage of DAC is flexibility: resource owners can make rapid, contextual access decisions without waiting for a central authority. The disadvantage is equally clear: security is only as strong as the judgment of every individual resource owner. In an enterprise with thousands of file shares, DAC invariably leads to over-permissioned access because owners tend to grant access liberally and almost never revoke it.

From an audit perspective, DAC environments are inherently difficult to assess because there is no central authority enforcing a consistent access policy. An IS auditor evaluating a DAC environment would look for whether data classification policies exist to guide owner decisions, whether periodic access reviews are conducted, and whether there are compensating controls — such as data loss prevention — to mitigate the risks of over-permissioning.

Mandatory Access Control — MAC — is the opposite extreme. Under MAC, access decisions are made by a central authority based on security labels and clearance levels, not by individual resource owners. Every subject — user, process, system — is assigned a clearance level. Every object — file, database, application — is assigned a classification level. Access is granted only when the subject's clearance meets or exceeds the object's classification and the subject has a demonstrated need to know.

MAC is the model used in military and intelligence environments. The Bell-LaPadula model is a formal mathematical model that implements MAC with two key rules. The Simple Security Property, also known as "no read up," states that a subject cannot read an object at a higher classification level. The Star Property, also known as "no write down," states that a subject cannot write information to an object at a lower classification level. Together, these rules prevent information from flowing from higher classification levels to lower ones.

For the CISA exam, understand that MAC provides the strongest access control guarantees but at the cost of flexibility and usability. MAC environments require significant administrative overhead to maintain security labels, and they resist the rapid, ad hoc access changes that business operations often demand. Very few commercial enterprises implement full MAC. It is predominantly a government and defense model.

Role-Based Access Control — RBAC — is the dominant model in enterprise environments today. Under RBAC, access is granted based on the role a user holds within the organization, not based on the user's individual identity. Roles are defined to align with job functions — accounts payable clerk, system administrator, branch manager — and permissions are assigned to roles rather than to individuals. When a user is assigned a role, they inherit all permissions associated with that role.

RBAC offers several advantages that the exam expects you to articulate. It simplifies access administration: when an employee transfers departments, you change their role assignment rather than modifying dozens of individual permissions. It supports the principle of least privilege: roles can be designed to contain only the minimum permissions necessary for the job function. It facilitates access reviews: instead of reviewing thousands of individual access grants, auditors can review role definitions and role assignments. And it supports segregation of duties: mutually exclusive roles can be defined so that no single user can hold conflicting roles.

The IS auditor's concerns with RBAC include role explosion — the proliferation of narrowly defined roles that approaches individual access grants, defeating the purpose of RBAC — and role creep — users accumulating roles over time as they change positions without losing their previous roles. An effective RBAC implementation requires regular role review and cleanup, which many organizations neglect.

Attribute-Based Access Control — ABAC — is the most granular and flexible model. Under ABAC, access decisions are based on attributes of the subject, attributes of the resource, attributes of the action being requested, and attributes of the environment. For example, an ABAC policy might state: "A user with the attribute 'department=finance' can access a document with the attribute 'classification=confidential' if the action is 'read' and the environment attribute 'time' is within business hours and the environment attribute 'location' is 'corporate network.'"

ABAC subsumes DAC, MAC, and RBAC — any policy expressible in those models can be expressed in ABAC, plus policies that none of those models can express. The tradeoff is complexity: ABAC policies can become extremely intricate, difficult to audit, and challenging to troubleshoot when access is unexpectedly denied or granted. ABAC is increasingly common in cloud environments, where traditional network-perimeter-based access controls are insufficient and fine-grained, context-aware access decisions are necessary.

For the exam, know that ABAC supports dynamic, context-aware access control that is particularly well-suited to Zero Trust architectures — which we will discuss in Episode Four. An IS auditor evaluating ABAC would examine the attribute sources for accuracy and integrity, review the policy definitions for correctness, and test boundary conditions where attribute combinations might produce unintended access decisions.

[SECTION BREAK]

## Least Privilege and Need-to-Know

Two foundational principles govern access control regardless of which model is implemented: least privilege and need-to-know.

Least privilege states that every user, process, and system should be granted only the minimum access rights necessary to perform their authorized function, and only for the duration necessary. This principle applies horizontally — a user should not have access to systems unrelated to their job — and vertically — a user should not have elevated privileges beyond what their role requires. A database administrator needs privileged access to the database management system, but that does not mean they need domain administrator rights to the Active Directory or root access to every Linux server.

Need-to-know adds a classification dimension. Even if a user has the clearance or role that would technically permit access, they should not access information unless they have a demonstrated, legitimate business reason to do so. Need-to-know is particularly relevant in environments handling sensitive data — classified information in government contexts, patient health information in healthcare, material non-public information in financial services.

The practical challenge is that least privilege and need-to-know are principles, not self-implementing mechanisms. They require deliberate, continuous effort to enforce. Users request access when they join the organization or start a project. If access is not revoked when the project ends or the user changes roles, privileges accumulate. This phenomenon — known as privilege creep or entitlement creep — is one of the most common access control findings in CISA audits.

[SECTION BREAK]

## IAM Lifecycle — Provisioning, Review, De-provisioning

The Identity and Access Management lifecycle is a three-phase process that the exam tests from both a design and an audit perspective.

Provisioning is the process of creating a user's digital identity and granting them the access rights necessary for their role. Effective provisioning requires several elements: a formal access request process, ideally through an automated workflow system; approval from the user's manager confirming the business need; approval from the data or system owner confirming the appropriateness of the access; role assignment based on the user's job function, with permissions inherited from the role definition; and logging of the provisioning event for audit trail purposes.

The IS auditor evaluating provisioning looks for segregation of duties between the person requesting access, the person approving access, and the person implementing access. The auditor also verifies that provisioning follows a formal, documented process rather than ad hoc requests via email or verbal communication. A mature provisioning process integrates with the organization's HR system, so that new hire events in HR automatically trigger identity creation and role assignment in the identity management platform.

Access review — also called access recertification — is the periodic validation that existing access rights remain appropriate. ISACA guidance and most regulatory frameworks require access reviews at defined intervals. The frequency depends on the risk level: access to high-risk systems such as financial applications, privileged accounts, and systems containing personally identifiable information should be reviewed at least quarterly, while access to lower-risk systems may be reviewed semi-annually or annually.

An effective access review requires the reviewer — typically the user's manager or the system owner — to attest that each access right is still necessary and appropriate. The reviewer must be someone who understands the user's current job function and can make an informed judgment. Rubber-stamping — approving all access without genuine review — is a common finding and a significant control deficiency.

The IS auditor evaluating access reviews examines several dimensions: Are reviews conducted on schedule? Is the reviewer qualified to make access decisions? Is there evidence of genuine review rather than blanket approval? Are identified discrepancies — access that is no longer appropriate — remediated within a defined timeframe? Is the remediation verified?

De-provisioning is the process of revoking access when it is no longer needed. The most critical de-provisioning event is employee termination. When an employee leaves the organization, all access must be revoked promptly — ideally on the same day, and certainly within twenty-four hours for standard users and immediately for privileged users. Delayed de-provisioning is a severe control weakness. A terminated employee who retains system access — even for a few days — represents a significant insider threat risk.

De-provisioning should also occur for internal transfers. When a user moves from the finance department to marketing, their finance system access should be revoked even as their marketing system access is provisioned. This is where privilege creep originates — organizations are generally good at granting access and poor at revoking it.

The IS auditor evaluating de-provisioning tests the timeliness and completeness of access revocation. Common audit procedures include comparing the list of terminated employees from HR records against active user accounts in critical systems. Any terminated employee who still has active access represents a de-provisioning failure.

[SECTION BREAK]

## Privileged Access Management and Separation of Duties

Privileged access — also called elevated access, administrative access, or superuser access — presents the highest risk of any access category. Privileged users can modify system configurations, access all data regardless of ownership, create or delete other user accounts, disable security controls, and cover their tracks by modifying logs. The compromise of a privileged account is the single most damaging access control event an organization can suffer.

Privileged Access Management — PAM — is a suite of controls specifically designed to manage and monitor privileged access. Key PAM capabilities include privileged account discovery — identifying all privileged accounts across the environment, including service accounts and shared accounts that are often overlooked; credential vaulting — storing privileged credentials in an encrypted vault rather than allowing administrators to know or manage their own privileged passwords; session recording — recording and logging all privileged sessions for monitoring and forensic review; just-in-time access — granting privileged access only when needed and for a defined time window, automatically revoking it when the time expires; and privilege elevation — allowing standard users to perform specific privileged operations without granting them full administrative access.

The exam will test your understanding of PAM in the context of audit findings. A common scenario: the auditor discovers that system administrators use their privileged accounts for everyday activities — browsing the web, reading email, performing non-administrative tasks. This violates least privilege and creates unnecessary risk. The correct audit recommendation is that administrators should use standard accounts for daily activities and elevate to privileged accounts only when performing administrative functions, with that elevation logged and monitored.

Separation of duties — also known as segregation of duties — is the principle that no single individual should control all phases of a critical process. In the access control context, separation of duties means that the person who requests access should not be the same person who approves it. The person who approves access should not be the same person who implements it. The person who develops application code should not be the same person who deploys it to production.

Now, here is the exam trap that catches many candidates: the distinction between segregation of duties and dual control. Segregation of duties divides a process into separate steps performed by different individuals. Dual control requires two or more individuals to act simultaneously to complete a single step. The classic dual control example is a bank safe deposit box that requires two keys held by two different people — neither person can open the box alone, and the action requires both of them at the same time.

Segregation of duties prevents fraud by ensuring that no single person can both perpetrate and conceal a fraudulent act. Dual control prevents unauthorized action by requiring collusion between two or more individuals. Both are important controls, but they address different risks and operate differently. The exam may present a scenario and ask which principle is being applied — read carefully to determine whether the control divides a process into sequential steps performed by different people, which is segregation of duties, or requires simultaneous action by multiple people, which is dual control.

[SECTION BREAK]

## SSO, MFA, and Federated Identity

Single sign-on, multi-factor authentication, and federated identity are three identity management capabilities that the exam addresses both technically and from a risk perspective.

Single sign-on — SSO — allows a user to authenticate once and gain access to multiple systems without re-authenticating. SSO improves usability, reduces password fatigue, and can improve security by eliminating the need for users to maintain multiple passwords, which often leads to password reuse or weak passwords. However, SSO also concentrates risk: if the SSO credential is compromised, the attacker gains access to all systems the user is authorized for. This single point of failure must be mitigated with strong authentication controls.

Multi-factor authentication — MFA — requires users to present two or more factors from different categories: something you know, such as a password or PIN; something you have, such as a hardware token, smart card, or mobile device; and something you are, such as a fingerprint, facial recognition, or iris scan. The factors must come from different categories — two passwords are not MFA because they are both "something you know."

The exam expects you to know that MFA significantly reduces the risk of credential compromise. A stolen password alone is insufficient if the attacker does not also possess the user's hardware token or biometric. MFA is required or strongly recommended by virtually every security framework and regulatory standard for privileged access, remote access, and access to sensitive data.

A common exam question involves the combination of SSO and MFA. The strongest practical approach is to require MFA for the initial SSO authentication, so that the single authentication event is strongly protected, and then allow SSO to provide seamless access to downstream systems. This combines the usability benefits of SSO with the security benefits of MFA.

Federated identity extends SSO across organizational boundaries. In a federated identity architecture, organizations establish trust relationships that allow users authenticated by one organization — the identity provider — to access resources at another organization — the service provider — without creating separate accounts. Standards such as SAML 2.0, OAuth 2.0, and OpenID Connect enable federated identity.

The IS auditor evaluating federated identity examines the trust relationship — is the identity provider's authentication sufficiently rigorous? — the token or assertion security — are SAML assertions signed and encrypted? — the attribute mapping — do the attributes passed by the identity provider correctly map to access rights at the service provider? — and the termination provisions — if the trust relationship is dissolved, are all federated access rights promptly revoked?

[SECTION BREAK]

## Logical Versus Physical Access Controls

The exam draws a clear distinction between logical and physical access controls, and an IS auditor must understand both.

Logical access controls govern access to information systems, applications, databases, and data. They include user authentication through passwords, tokens, and biometrics; authorization through access control lists and role assignments; encryption to protect data confidentiality; and audit logging to record access events.

Physical access controls govern access to facilities, data centers, server rooms, and hardware. They include perimeter controls such as fences, gates, and guards; building access through card readers, PIN pads, and biometric scanners; environmental controls such as fire suppression, climate control, and water detection; and surveillance through CCTV and motion sensors.

Physical and logical controls must work in concert. The strongest logical access controls are ineffective if an attacker can physically access a server and remove its hard drive. Conversely, physical security cannot prevent a remote attacker from exploiting a software vulnerability. An IS auditor evaluating access controls must assess both dimensions and identify gaps where one type of control is not adequately supported by the other.

A common audit finding is inconsistency between physical and logical access: a terminated employee's logical access is revoked, but their physical access badge remains active. Or a contractor's physical access to the server room is granted without a corresponding audit of their logical access to the servers within that room.

[SECTION BREAK]

## Real-World Case Study — Privileged User Access Review at a Healthcare Organization

Let me illustrate these concepts with a scenario drawn from healthcare, where access control failures can directly harm patients and trigger severe regulatory penalties.

A large regional health system with twelve hospitals and ninety clinics operates an electronic health record — EHR — system containing protected health information for three million patients. The organization is subject to HIPAA in the United States, which mandates strict access controls for protected health information.

An IS auditor is engaged to assess the organization's privileged access controls for the EHR system. The audit scope includes: identification and inventory of all privileged accounts, appropriateness of privileged access assignments, monitoring and logging of privileged activities, and the access review process for privileged users.

The auditor begins by requesting a complete list of all accounts with privileged access to the EHR system. The IT department provides a list of forty-two accounts. However, the auditor independently queries the EHR system's access control database and identifies sixty-one accounts with elevated privileges. Nineteen accounts are undocumented — a significant finding indicating that the organization does not have complete visibility into its own privileged access landscape.

Of the sixty-one privileged accounts, the auditor finds: eight are associated with employees who left the organization between three and fourteen months ago — a de-provisioning failure; six are shared accounts used by multiple individuals, making individual accountability impossible; twelve have privileges that exceed their job function — role creep that was never corrected; and four are service accounts with hard-coded passwords that have not been rotated in over two years.

The auditor reviews the access review process and finds that quarterly reviews are required by policy but have only been performed twice in the past eighteen months. When reviews were performed, the reviewer — a single IT manager — approved all access without requesting justification from system owners or managers, suggesting rubber-stamping rather than genuine review.

The auditor also discovers that privileged session logging is enabled but the logs are stored on the same server that the privileged users administer — meaning privileged users could potentially modify or delete their own audit logs. This violates the principle that logging must be tamper-resistant and that privileged users should not be able to cover their tracks.

The audit findings are mapped to specific control deficiencies: the undocumented accounts represent a failure in privileged account discovery, which is a PAM gap; the terminated employee accounts represent a de-provisioning failure linked to inadequate integration between HR and IT processes; the shared accounts represent a violation of individual accountability; the excessive privileges represent role creep compounded by ineffective access reviews; the unrotated service account passwords represent a key management failure; and the self-administered logs represent a segregation of duties violation.

The recommendations include implementing a PAM solution with automated privileged account discovery, integrating the EHR system's identity management with the HR termination workflow, eliminating shared accounts and assigning individual privileged accounts with unique credentials, re-establishing the quarterly access review with multiple qualified reviewers and mandatory justification for each access right, implementing automated service account password rotation, and forwarding privileged session logs to a centralized SIEM that privileged EHR users cannot access or modify.

This case study illustrates why access control auditing demands thoroughness and skepticism. The organization believed it had forty-two privileged accounts. The reality was sixty-one. That gap of nineteen accounts — nearly a third of the total — represents nineteen potential vectors for unauthorized access to three million patients' most sensitive health information.

[SECTION BREAK]

## Exam Strategy and Key Takeaways

Let me distill the essential knowledge for exam day.

Access control models: DAC gives owners discretion — flexible but inconsistent. MAC uses labels and clearance — strong but rigid. RBAC uses roles — the enterprise standard. ABAC uses attributes — the most granular and context-aware. Remember: "Don't Make Rules About Behaviour."

Least privilege and need-to-know are complementary but distinct. Least privilege limits the scope of access rights. Need-to-know limits access based on legitimate business purpose. Both must be actively enforced and regularly verified.

The IAM lifecycle has three phases: provisioning, review, and de-provisioning. The most common failures occur in de-provisioning and review. Privilege creep results from granting access without revoking prior access when roles change.

PAM is critical for managing the highest-risk accounts. Key capabilities are discovery, vaulting, session recording, just-in-time access, and privilege elevation. Privileged accounts should never be used for non-administrative activities.

Segregation of duties divides a process across multiple people sequentially. Dual control requires multiple people to act simultaneously. These are different controls addressing different risks — do not confuse them on the exam.

MFA requires factors from different categories. Two passwords are not MFA. SSO plus MFA combines usability with security. Federated identity extends trust across organizations.

Logical and physical controls must be aligned. De-provisioning must address both. A terminated employee with an active badge is a finding, even if their logical access is revoked.

[SECTION BREAK]

## Bridge to Episode 3

In our next episode, we enter the mathematical heart of information security: cryptography and public key infrastructure. We will examine symmetric and asymmetric encryption algorithms, hashing functions, digital signatures, the PKI trust model, key management lifecycle, and the critical exam distinctions between confidentiality, integrity, authentication, and non-repudiation. The cryptography episode is one that many candidates find challenging, but I assure you we will make it rigorous and clear. That is Episode Three — Cryptography and PKI. I will see you there.

---
*End of Episode 5.2 — Access Control & Identity Management*
*CISA Domain 5: Protection of Information Assets*
