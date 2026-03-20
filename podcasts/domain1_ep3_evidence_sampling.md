# Domain 1 — Episode 1.3: Audit Evidence, Sampling & Documentation

**Series:** CISA Exam Preparation Podcast
**Domain:** 1 — Information Systems Auditing Process (21% of exam)
**Episode Duration:** 31:22
**Audience:** Senior IT audit practitioners preparing for CISA certification

---

## INTRODUCTION (0:00–2:15)

Welcome back to the CISA Exam Preparation Podcast. This is Episode 1.3, the final episode in our Domain 1 coverage — Information Systems Auditing Process. In Episode 1.1 we established the architecture: ISACA's role, the audit process lifecycle, the audit charter, and exam mechanics. In Episode 1.2 we went deep on planning and risk assessment — the audit risk model, materiality, quantitative and qualitative risk methodologies, and audit program development.

Today we complete the picture by addressing the three pillars of audit execution and delivery: evidence, sampling, and documentation. If planning is the blueprint and fieldwork is the construction, then evidence is the raw material, sampling is the engineering method that makes comprehensive assurance feasible, and documentation is the permanent record that gives your conclusions legal and professional weight.

This episode is densely packed with testable content. The CISA exam draws heavily from sampling methodology, evidence classification, and Computer-Assisted Audit Techniques. I will walk through each concept with the precision the exam demands, flag every trap I know ISACA sets in this area, and give you the mnemonics and frameworks that survive under exam pressure.

Let us begin with the foundation: audit evidence.

[SECTION BREAK]

## TYPES OF AUDIT EVIDENCE (2:15–8:30)

Audit evidence is the information gathered by the auditor to support audit conclusions and opinions. The quality of your conclusions is bounded by the quality of your evidence. The CISA exam recognizes four primary categories of audit evidence: physical, documentary, analytical, and testimonial.

Physical evidence is obtained through direct observation or inspection of tangible assets. Walking into a data center and observing that server racks are secured in locked cabinets, that environmental controls are functioning, and that physical access is restricted to authorized personnel — that is physical evidence. Inspecting a hardware asset and verifying its serial number against the asset inventory — physical evidence. Observing an operator executing a backup procedure — physical evidence. Physical evidence is generally considered reliable because it is obtained directly by the auditor through firsthand observation. However, physical evidence has an important limitation: it provides evidence about a point in time. Observing that the data center door is secured today does not confirm that it was secured last Tuesday. This temporal limitation must be addressed through complementary evidence.

Documentary evidence consists of records, documents, and data — both physical and electronic — that support audit conclusions. Examples include system logs, configuration files, change management tickets, access control lists, policy documents, contracts, and transactional records. Documentary evidence is the most abundant category of evidence in IS auditing because information systems generate enormous volumes of machine-readable records. The reliability of documentary evidence depends on its source. Externally generated documents — such as a third-party SOC 2 report or a vendor's security certification — are generally considered more reliable than internally generated documents because they are less susceptible to manipulation by the auditee's personnel. Internally generated documents that have been subject to independent review or verification are more reliable than those that have not.

Analytical evidence is derived from the auditor's analysis of data and relationships. Analytical procedures involve evaluating information through the study of plausible relationships — comparing current-period data to prior periods, comparing actual results to budgets or forecasts, evaluating ratios and trends, and identifying anomalies or outliers that may indicate control failures or errors. For example, analyzing server uptime statistics over a twelve-month period to identify patterns of unplanned downtime is an analytical procedure. Comparing the volume of database transactions to the volume of authorized change requests to identify unauthorized changes is an analytical procedure. Analytical evidence is valuable because it can reveal patterns and anomalies that discrete testing of individual transactions might miss.

Testimonial evidence is information obtained through interviews, questionnaires, and representations from auditee personnel. An interview with the database administrator about backup procedures, a written representation from management about the completeness of the system inventory, a response to an audit questionnaire about access control practices — all of these constitute testimonial evidence. Testimonial evidence is generally considered the least reliable category of audit evidence because it is subjective, susceptible to bias, and dependent on the knowledge and honesty of the individual providing the testimony. This does not mean testimonial evidence is without value — it is essential for understanding processes, identifying risks, and corroborating other evidence. But it should not be the sole basis for audit conclusions on critical matters.

Here is the reliability hierarchy, from most to least reliable: physical evidence and externally generated documentary evidence are at the top, followed by internally generated documentary evidence and analytical evidence, with testimonial evidence at the bottom. Mnemonic: "PDAs Tell stories" — Physical, Documentary, Analytical, Testimonial, in descending order of reliability.

Exam trap: ISACA loves to test evidence reliability. A common question pattern presents a scenario and asks which type of evidence provides the "best" or "most reliable" basis for the auditor's conclusion. Physical evidence or documentary evidence from an independent external source will almost always be the correct answer over testimonial evidence or unverified internal documents. If the question asks specifically about the "least reliable" form of evidence, testimonial evidence — particularly oral testimony without corroboration — is the correct answer.

Another exam trap: a question may ask whether the auditor should rely solely on management's representations about a control. The correct answer is no. Management representations are testimonial evidence and should be corroborated with other forms of evidence — documentary evidence such as system logs, physical evidence such as observation, or analytical evidence such as trend analysis.

[SECTION BREAK]

## EVIDENCE QUALITY — SUFFICIENCY, COMPETENCE, AND RELEVANCE (8:30–13:00)

Beyond categorization, audit evidence must meet three quality criteria: sufficiency, competence, and relevance. The CISA exam tests these criteria individually and in combination, and you must understand each with precision.

Sufficiency refers to the quantity of evidence. Is there enough evidence to support the audit conclusion? Sufficiency is a function of the sample size, the number of audit procedures performed, and the breadth of evidence sources. A conclusion based on a single observation or a single document is likely insufficiently supported. The auditor must gather enough evidence that a reasonable, experienced auditor reviewing the work would agree that the conclusion is adequately supported.

The determination of sufficiency is influenced by the risk level. Higher-risk areas require more evidence — larger samples, more procedures, more corroboration. Lower-risk areas may be adequately supported by less evidence. This connects directly to the audit risk model we covered in Episode 1.2: when inherent risk and control risk are high, the auditor must gather more evidence to reduce detection risk, which is a sufficiency determination.

Competence — sometimes called reliability — refers to the quality and trustworthiness of the evidence. Competent evidence is valid, objective, and obtained from reliable sources through reliable methods. The competence of evidence is influenced by its source, its nature, and the conditions under which it was obtained. Evidence obtained directly by the auditor — such as through observation, inspection, or re-performance — is more competent than evidence obtained indirectly through inquiry. Evidence obtained from independent external sources is more competent than evidence obtained from the auditee's internal sources. Evidence obtained from well-controlled systems is more competent than evidence obtained from systems with known control weaknesses.

That last point deserves emphasis because the exam tests it. If the auditor is gathering evidence from a system whose controls are under audit and those controls are found to be weak, the evidence obtained from that system is inherently less competent. For example, if you are auditing access controls over a database and you discover that the database's audit logging mechanism has been improperly configured, the logs themselves become less reliable as evidence because the mechanism that produced them is compromised.

Relevance refers to the relationship between the evidence and the audit objective. Evidence is relevant if it pertains to the specific control objective or assertion being tested. Evidence that is abundant and competent but unrelated to the audit objective is irrelevant and should not be used to support conclusions about that objective. For example, evidence that the organization has an excellent physical security program is not relevant to an audit conclusion about the effectiveness of logical access controls. The evidence may be high-quality, but it does not address the audit objective.

Mnemonic: SCR — Sufficient, Competent, Relevant. Think of it as "Screen" your evidence through three filters. If evidence fails any one of the three, it is inadequate for supporting audit conclusions. Sufficient means enough quantity. Competent means adequate quality. Relevant means proper alignment with the audit objective.

Exam trap: the exam may present a scenario where the auditor has gathered a large volume of evidence but the evidence does not directly relate to the control objective being tested. The question will ask whether the evidence is adequate. The correct answer is no — the evidence fails the relevance criterion regardless of its quantity or quality. Conversely, a question may present a scenario where the auditor has highly relevant evidence from a reliable source, but only a single instance. This evidence may fail the sufficiency criterion — one data point is rarely sufficient to support a conclusion about a control that operates continuously.

[SECTION BREAK]

## STATISTICAL SAMPLING (13:00–20:00)

Sampling is the mechanism that makes comprehensive assurance feasible. In most audit engagements, it is impractical or impossible to examine every transaction, record, or event in the population. Sampling allows the auditor to draw conclusions about the entire population by examining a representative subset. The CISA exam tests both statistical and non-statistical sampling methods, and you must understand the distinction, the specific techniques within each category, and the factors that influence sample size.

Statistical sampling uses mathematical probability theory to select samples and evaluate results. The defining characteristic of statistical sampling is that it allows the auditor to quantify sampling risk — the risk that the sample is not representative of the population. Because statistical sampling is grounded in probability theory, it produces results that are objective, defensible, and reproducible.

There are three statistical sampling methods the CISA exam expects you to know: attribute sampling, variable sampling, and stop-or-go sampling.

Attribute sampling is used to test the rate of occurrence of a specific characteristic — an attribute — within a population. In audit terms, attribute sampling answers the question: "What percentage of the population exhibits a particular condition?" For example, "What percentage of change requests were approved before deployment?" or "What percentage of user accounts have passwords that meet the complexity requirements?" Attribute sampling produces a conclusion expressed as a rate — the estimated error rate or deviation rate in the population. The auditor sets an expected error rate, a tolerable error rate, and a desired confidence level. These parameters determine the required sample size. If the sample results show an error rate that exceeds the tolerable rate, the auditor concludes that the control is not operating effectively.

Let me define those parameters precisely because the exam tests them. The expected error rate is the auditor's preliminary estimate of the actual error rate in the population, based on prior audit experience or preliminary testing. The tolerable error rate is the maximum error rate the auditor is willing to accept and still conclude that the control is effective. The confidence level — also called the reliability level — is the probability that the sample results accurately represent the population. A ninety-five percent confidence level means there is a five percent risk that the sample results do not accurately represent the population. That five percent is the sampling risk.

Variable sampling is used to estimate the monetary value or magnitude of a characteristic within a population. While attribute sampling asks "how many," variable sampling asks "how much." Variable sampling is more commonly used in financial auditing — for example, estimating the total dollar value of errors in an accounts receivable balance — but it appears in IS auditing when the auditor needs to estimate the magnitude of a condition. For example, estimating the total value of unauthorized transactions processed through an application during the audit period.

Stop-or-go sampling — also called sequential sampling — is a method designed to minimize sample size when the auditor expects very few errors. The auditor begins with a small initial sample. If no errors are found, the auditor may conclude that the control is effective without additional testing. If errors are found, the auditor increases the sample size and continues testing. This iterative approach is efficient when the expected error rate is very low because it avoids unnecessarily large samples.

Here is a critical concept: the relationship between confidence level, tolerable error rate, and sample size. Sample size increases when the desired confidence level increases — higher confidence requires a larger sample. Sample size increases when the tolerable error rate decreases — a tighter tolerance requires more testing. Sample size increases when the expected error rate increases — if more errors are expected, more items must be tested to accurately estimate the true error rate. Conversely, sample size decreases when the confidence level decreases, the tolerable error rate increases, or the expected error rate decreases.

Mnemonic: for factors that increase sample size, think "CHE" — Confidence level up, Higher expected errors, Exactness (lower tolerable error rate). All three push sample size up.

Exam trap: ISACA frequently tests the relationship between confidence level and sample size. A question may state that management wants "greater assurance" about a control and ask what impact this has on the audit. The correct answer is that the auditor must increase the confidence level, which increases the required sample size, which increases the audit effort. Greater assurance equals more testing — there is no shortcut.

Another exam trap: the exam may ask when stop-or-go sampling is most appropriate. The correct answer is when the expected error rate is very low. If the auditor expects a high error rate, stop-or-go sampling is inefficient because the auditor will repeatedly extend the sample, negating the efficiency advantage.

[SECTION BREAK]

## NON-STATISTICAL SAMPLING (20:00–22:15)

Non-statistical sampling — also called judgmental sampling — relies on the auditor's professional judgment rather than mathematical probability to select samples and evaluate results. Non-statistical sampling does not allow the auditor to quantify sampling risk, and its results cannot be extrapolated to the population with statistical precision. However, non-statistical sampling is widely used in practice and is accepted by ISACA standards when appropriately applied.

The two primary forms of non-statistical sampling are judgmental sampling and haphazard sampling.

Judgmental sampling involves the auditor deliberately selecting specific items for testing based on professional judgment. The auditor might select items that are above a certain monetary threshold, items associated with higher-risk transactions, items from specific time periods, or items that exhibit unusual characteristics. Judgmental sampling is efficient because it focuses on the items most likely to contain errors or irregularities. However, it introduces selection bias — the auditor's judgment may not produce a sample that is representative of the entire population. Consequently, judgmental sampling results cannot be generalized to the population.

Haphazard sampling involves selecting items without any deliberate pattern or bias, but also without using a statistically random selection method. The auditor selects items "at random" in the colloquial sense, but not in the statistical sense. Haphazard sampling attempts to approximate randomness but does not guarantee it.

Exam trap: the CISA exam may ask what the "primary disadvantage" of non-statistical sampling is. The correct answer is that the results cannot be projected to the population with measurable precision because sampling risk cannot be quantified. If the auditor needs to draw a conclusion about the entire population — for example, "the error rate in the population is less than two percent with ninety-five percent confidence" — statistical sampling is required.

Another frequently tested distinction: statistical sampling is not inherently superior to non-statistical sampling. The appropriate method depends on the audit objective. If the objective requires a population-level conclusion with quantifiable confidence, use statistical sampling. If the objective is to identify specific instances of control failure for reporting purposes, judgmental sampling may be appropriate and more efficient.

[SECTION BREAK]

## COMPUTER-ASSISTED AUDIT TECHNIQUES (22:15–27:00)

Computer-Assisted Audit Techniques — CAATs — are tools and techniques that use technology to perform audit procedures more efficiently and comprehensively than manual methods. CAATs are one of the most heavily tested topics in Domain 1, and you must understand the major categories and their appropriate applications.

Generalized audit software — GAS — is a category of software tools that allows auditors to access, extract, analyze, and manipulate data from the auditee's systems without requiring specialized programming skills. Examples include ACL Analytics (now Galvanize), IDEA (Interactive Data Extraction and Analysis), and similar tools. GAS enables the auditor to perform functions such as data extraction and querying — pulling specific records from databases based on defined criteria. File comparison — comparing two datasets to identify discrepancies, such as comparing the authorized user list to the list of users with actual system access. Statistical analysis — computing summary statistics, identifying outliers, and performing stratification. Duplicate detection — identifying duplicate records that may indicate processing errors or fraud. Gap detection — identifying missing items in a sequence, such as missing invoice numbers that may indicate deleted or suppressed transactions. And re-computation — independently recalculating values to verify accuracy, such as recalculating interest charges or depreciation amounts.

The power of GAS is that it allows the auditor to analyze the entire population of transactions rather than relying on sampling. When you can examine one hundred percent of the transactions, you eliminate sampling risk entirely. This is a significant advantage that the exam expects you to recognize.

The test data method involves the auditor creating a set of transactions with known characteristics — including both valid and invalid transactions — and processing them through the auditee's production system or a copy of the production system to verify that the system's controls function as expected. For example, the auditor might submit a transaction with an invalid account number to verify that the system rejects it, or submit a transaction that exceeds an authorization threshold to verify that it triggers the appropriate approval workflow.

There are two variations of the test data method. Running test data through the production system provides direct evidence about the controls in the actual production environment, but it creates the risk of contaminating production data with test transactions. The auditor must ensure that all test transactions are identified and reversed after testing. Running test data through a copy of the production system eliminates the contamination risk but introduces the question of whether the copy accurately mirrors the production environment.

The integrated test facility — ITF — is a more sophisticated technique in which the auditor establishes a fictitious entity — such as a dummy department, a fictional employee, or a test account — within the organization's live production system. Transactions associated with the fictitious entity are processed alongside real transactions through the normal production processing cycle. This allows the auditor to test the system's controls on an ongoing basis, using real processing conditions, without disrupting actual business operations. The critical requirement is that the fictitious entity's transactions must be identified and excluded from financial and operational reports to prevent distortion of real results.

Exam trap: the exam frequently asks about the risks associated with different CAATs. For the test data method, the primary risk is contamination of production data. For the integrated test facility, the primary risk is that the fictitious entity's transactions may not be properly excluded from financial reports, leading to misstatement of actual results. For generalized audit software, a common exam point is that the auditor must verify the integrity and completeness of the data extracted — if the data extraction is incomplete or corrupted, the audit analysis will be flawed. The principle is garbage in, garbage out.

Another exam trap: the exam may ask what the IS auditor should do "before" using CAATs. The correct answer typically involves verifying the integrity and reliability of the source data and ensuring that the audit software functions as intended — for example, by testing the software against a dataset with known results. The auditor should not blindly trust the output of a CAAT without validating both the input data and the tool itself.

Mnemonic for the major CAATs: "GITI" — Generalized audit software, Integrated test facility, Test data method, and (data) Integrity verification. GITI. Four techniques, four letters.

[SECTION BREAK]

## AUDIT DOCUMENTATION AND WORKING PAPERS (27:00–29:30)

Audit documentation — commonly called working papers — is the written record that supports the auditor's findings, conclusions, and recommendations. Documentation is not an administrative afterthought; it is a professional requirement and, in many jurisdictions, a legal obligation. ISACA IS Auditing Standard 1204 states that the IS auditor should document sufficient information to enable an informed, prudent professional with no previous connection with the audit to ascertain what work was performed, the evidence obtained, and the conclusions reached.

That standard is worth internalizing because it defines the documentation sufficiency test. The question is not whether you understand your own work — it is whether a qualified stranger reviewing your documentation would understand it. This is the "informed, prudent professional" test, and it is directly tested on the CISA exam.

Working papers should include the following elements. The audit plan and program — documenting the scope, objectives, and procedures. Evidence gathered — documents, screenshots, data extracts, interview notes, and analysis results. Testing results — the outcome of each audit procedure, including the population tested, the sample selected, the results of testing, and the conclusions drawn. Findings and exceptions — each control deficiency identified, with supporting evidence. Conclusions — the auditor's overall assessment of the control environment. Recommendations — suggested corrective actions for each finding. And management responses — the auditee's agreement or disagreement with findings and their proposed remediation plan.

Working papers are owned by the audit function, not by the auditee. The auditee does not have the right to alter, suppress, or remove working papers. Working papers should be retained in accordance with the organization's document retention policy and applicable regulatory requirements. In many regulated industries, audit working papers must be retained for a minimum of five to seven years.

Exam trap: ISACA may ask who owns the audit working papers. The correct answer is the audit organization — not the auditee, not the individual auditor, and not management. The working papers are organizational assets of the audit function.

Another exam trap: a question may ask about the disposition of working papers when an auditor leaves the organization. The working papers remain with the audit function. They do not leave with the departing auditor. This preserves institutional knowledge and ensures continuity of the audit process.

[SECTION BREAK]

## AUDIT FINDINGS, RECOMMENDATIONS, AND MANAGEMENT RESPONSE (29:30–31:00)

The culmination of the audit process is the development of findings and recommendations and the solicitation of management responses. A well-structured audit finding has five components, commonly known as the five attributes of a finding: condition, criteria, cause, effect, and recommendation.

Condition describes what the auditor found — the factual observation. Criteria describes what should be — the standard, policy, regulation, or control objective against which the condition is evaluated. Cause explains why the condition exists — the root cause of the control deficiency. Effect describes the actual or potential impact of the condition — the risk or consequence of the deficiency. Recommendation describes what the auditor suggests should be done to remediate the condition.

Mnemonic: "CCCR plus E" — Condition, Criteria, Cause, effect (Consequence), Recommendation. Or think of it as "4 Cs and an R" if you group Effect under Consequence.

After the auditor develops findings and recommendations, management is given the opportunity to respond. The management response should indicate whether management agrees or disagrees with the finding, the planned corrective action, the responsible party, and the target completion date. If management disagrees with a finding, the auditor should consider management's rationale, but the auditor is not obligated to remove or modify the finding based solely on management's disagreement. If the auditor's evidence supports the finding, it stands.

The CISA exam may also test your understanding of risk acceptance. If management acknowledges a finding but decides to accept the associated risk rather than implement corrective action, the auditor must ensure that the risk acceptance is documented and approved by an appropriate level of management. Risk acceptance is a legitimate management response — the auditor's role is to ensure that it is an informed, deliberate decision made at the appropriate authority level, not an inadvertent oversight or an attempt to avoid remediation.

[SECTION BREAK]

## EPISODE SUMMARY AND DOMAIN 1 WRAP-UP (31:00–31:22)

We have now completed our coverage of Domain 1. Across three episodes, we have systematically addressed the Information Systems Auditing Process from foundation to finish. We covered audit evidence — physical, documentary, analytical, and testimonial — and the quality criteria of sufficiency, competence, and relevance. We worked through statistical sampling — attribute, variable, and stop-or-go — and non-statistical sampling. We examined CAATs — generalized audit software, test data, and integrated test facilities. We addressed documentation standards, working paper requirements, and the five-attribute finding structure.

As you study Domain 1, remember these key themes. First, planning drives everything — the audit risk model, risk-based planning, and the audit program are the foundation. Second, evidence quality determines conclusion quality — screen every piece of evidence through the sufficiency, competence, and relevance filters. Third, sampling methodology must match the audit objective — statistical sampling when population-level conclusions are needed, judgmental sampling when targeted testing is appropriate. Fourth, documentation must pass the informed, prudent professional test — if a stranger could not understand your work from your papers, your documentation is inadequate.

Domain 1 accounts for twenty-one percent of the CISA exam. Master these three episodes, practice the ALE calculations until they are reflexive, memorize the sampling relationships, and you will be well-positioned to capture those forty-two questions.

In our next episode, we move to Domain 2: Governance and Management of IT. We will examine IT governance structures, organizational roles and responsibilities, IT strategy, and the frameworks that tie IT management to business objectives. That is where the audit process we have studied meets the governance context in which it operates.

This has been Episode 1.3 of the CISA Exam Preparation Podcast. Thank you for your attention, and I will see you in Domain 2.

---
*This episode references content aligned with the ISACA CISA Review Manual (27th/28th Edition), ISACA IS Auditing Standards (Standard 1204: Documentation, Standard 1205: Evidence), ISACA IS Auditing Guidelines on Audit Evidence (G2), Sampling (G10), and the Use of Computer-Assisted Audit Techniques (G3). Additional references include AICPA AU-C Section 530 (Audit Sampling), NIST SP 800-53A (Assessing Security and Privacy Controls), and ISO 19011 (Guidelines for Auditing Management Systems).*
