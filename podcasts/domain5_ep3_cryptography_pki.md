# Domain 5, Episode 3 — Cryptography & PKI

**CISA Exam Preparation Podcast — Protection of Information Assets**
**Episode Duration: 35:18**

---

Welcome back to the CISA Mastery Podcast. This is Episode Three of Domain Five — Protection of Information Assets. We are now entering the domain of cryptography and public key infrastructure, the mathematical foundation upon which confidentiality, integrity, authentication, and non-repudiation are built.

Many CISA candidates approach cryptography with apprehension. Let me be direct: the CISA exam does not require you to perform mathematical operations or understand the internal mechanics of encryption algorithms. What it does require — and requires thoroughly — is that you understand what each cryptographic mechanism achieves, when each is appropriate, how they relate to information security objectives, and how an IS auditor evaluates their implementation. That is our focus today.

Let us begin with a critical framework that will anchor everything in this episode.

[SECTION BREAK]

## The CIA-NR Framework — Mapping Cryptographic Mechanisms to Security Objectives

Before we examine any specific algorithm, you need a mental model that maps cryptographic mechanisms to the security objectives they serve. I call this the CIA-NR framework, and it is your mnemonic for this episode.

Confidentiality — ensuring that information is accessible only to authorized parties — is achieved through encryption. Whether symmetric or asymmetric, encryption transforms readable plaintext into unreadable ciphertext. Only parties possessing the correct key can reverse the transformation.

Integrity — ensuring that information has not been altered during storage or transmission — is achieved through hashing. A hash function produces a fixed-length digest from input data of any size. Any change to the input — even a single bit — produces a dramatically different digest. By comparing hash values, you can detect whether data has been modified.

Authentication — verifying the identity of a party — is achieved through digital signatures and certificates. A digital signature proves that a message was created by a specific sender and has not been altered since signing.

Non-repudiation — preventing a party from denying an action they performed — is also achieved through digital signatures. If a user digitally signs a transaction, they cannot later credibly deny having authorized it, because only they possess the private key that produced the signature.

Here is the exam trap, stated plainly: encryption provides confidentiality but does not inherently provide integrity or authentication. Hashing provides integrity but does not provide confidentiality. Digital signatures provide authentication, integrity, and non-repudiation but do not provide confidentiality. The exam will test whether you can correctly identify which security objective a given mechanism addresses. Do not conflate them.

[SECTION BREAK]

## Symmetric Encryption

Symmetric encryption uses the same key for both encryption and decryption. The sender encrypts the plaintext with a secret key, and the recipient decrypts the ciphertext with the identical key. The fundamental challenge of symmetric encryption is key distribution — both parties must possess the same key, and that key must be exchanged securely. If the key is intercepted during distribution, all encrypted communications are compromised.

The Advanced Encryption Standard — AES — is the dominant symmetric encryption algorithm in use today. AES was adopted by NIST in 2001 after a multi-year public competition to replace the Data Encryption Standard. AES operates on 128-bit blocks and supports key lengths of 128, 192, and 256 bits. AES-256 — AES with a 256-bit key — is the standard for protecting classified information and is the de facto requirement in most enterprise security standards.

AES is computationally efficient, well-studied, and has no known practical vulnerabilities when properly implemented. The qualifier "when properly implemented" is important for auditors. AES can be used in several modes of operation, including Electronic Codebook — ECB — which is insecure for most purposes because identical plaintext blocks produce identical ciphertext blocks, enabling pattern analysis. Cipher Block Chaining — CBC — and Galois/Counter Mode — GCM — are considered secure modes. An IS auditor evaluating encryption implementations should verify not just that AES is used, but that it is used in an appropriate mode.

The Data Encryption Standard — DES — was the predecessor to AES, adopted in 1977. DES uses a 56-bit key, which is woefully insufficient by modern standards. A 56-bit key can be brute-forced in hours or even minutes with modern hardware. DES is deprecated and should not be used for any purpose. If an IS auditor discovers DES in use, it should be reported as a significant finding.

Triple DES — 3DES, also written as TDEA — applies the DES algorithm three times to each data block, using either two or three independent keys, yielding an effective key length of 112 or 168 bits. While significantly more secure than DES, 3DES is slower than AES and has been formally deprecated by NIST as of 2023. Organizations still using 3DES should be migrating to AES. An IS auditor finding 3DES in use should verify that a migration plan exists and assess the risk in the interim.

For the exam, the key facts about symmetric encryption are: same key for encryption and decryption; fast and efficient for large volumes of data; key distribution is the primary challenge; AES-256 is the current standard; DES is deprecated; 3DES is deprecated and being phased out.

[SECTION BREAK]

## Asymmetric Encryption

Asymmetric encryption — also called public key cryptography — uses a mathematically related key pair: a public key and a private key. Data encrypted with the public key can only be decrypted with the corresponding private key, and vice versa. The public key is distributed openly; the private key is kept secret by its owner.

Asymmetric encryption solves the key distribution problem that plagues symmetric encryption. If I want to send you a confidential message, I encrypt it with your public key — which I can obtain from a public directory or certificate — and only you can decrypt it with your private key. No secret key exchange is required.

RSA — named after its inventors Rivest, Shamir, and Adleman — is the most widely deployed asymmetric algorithm. RSA's security is based on the mathematical difficulty of factoring the product of two large prime numbers. Current best practice requires RSA key lengths of at least 2048 bits, with 4096 bits recommended for high-security applications. NIST guidance indicates that RSA-2048 is expected to provide adequate security through 2030.

Elliptic Curve Cryptography — ECC — achieves equivalent security to RSA with significantly shorter key lengths. A 256-bit ECC key provides security roughly equivalent to a 3072-bit RSA key. Shorter keys mean faster computation and less bandwidth consumption, making ECC particularly attractive for mobile devices, IoT devices, and high-throughput applications. The ECC curves most commonly used include P-256, P-384, and Curve25519.

The critical disadvantage of asymmetric encryption is performance. Asymmetric algorithms are orders of magnitude slower than symmetric algorithms. Encrypting a large file with RSA would be impractical. This is why, in practice, asymmetric and symmetric encryption are used together in a hybrid approach.

The hybrid approach works as follows. The sender generates a random symmetric key — called a session key. The sender encrypts the data with the session key using a fast symmetric algorithm like AES. The sender then encrypts the session key with the recipient's public key using RSA or ECC. Both the encrypted data and the encrypted session key are transmitted. The recipient decrypts the session key with their private key, then uses the session key to decrypt the data. This hybrid approach combines the efficiency of symmetric encryption for bulk data with the key distribution advantage of asymmetric encryption for the session key.

TLS — Transport Layer Security — which we will discuss shortly, uses exactly this hybrid approach for every secure web connection you make.

[SECTION BREAK]

## Hashing — SHA-256 and SHA-3

A cryptographic hash function takes input data of arbitrary size and produces a fixed-length output — the hash value, hash digest, or simply the hash. Cryptographic hash functions have three essential properties.

First, determinism: the same input always produces the same output. Second, avalanche effect: a tiny change in the input produces a dramatically different output — changing a single character in a document completely alters the hash. Third, one-way property: it is computationally infeasible to derive the original input from the hash output. You cannot reverse a hash.

Additionally, a secure hash function must be collision-resistant: it should be computationally infeasible to find two different inputs that produce the same hash output.

SHA-256 is a member of the SHA-2 family, designed by the National Security Agency and published by NIST. SHA-256 produces a 256-bit hash digest. It is the workhorse of modern integrity verification, used in digital signatures, certificate validation, blockchain, password storage when combined with salting and key stretching, and file integrity monitoring.

SHA-3 is the newest member of the Secure Hash Algorithm family, standardized by NIST in 2015. SHA-3 is based on the Keccak algorithm, which uses a fundamentally different internal structure — a sponge construction — from SHA-2. SHA-3 was designed not because SHA-2 has known vulnerabilities, but as a contingency: if a practical attack against SHA-2 were discovered, SHA-3 provides an algorithmically distinct alternative. SHA-3 supports the same output lengths as SHA-2 — 224, 256, 384, and 512 bits.

For the exam, understand that MD5 and SHA-1 are considered broken for cryptographic purposes. MD5 produces 128-bit digests and has known collision vulnerabilities — two different inputs can be engineered to produce the same MD5 hash. SHA-1 produces 160-bit digests and was formally deprecated by NIST in 2011 after collision attacks were demonstrated. If an IS auditor finds MD5 or SHA-1 used for integrity verification, digital signatures, or certificate hashing, this is a finding that requires remediation.

The core exam concept: hashing provides integrity verification. It does not provide confidentiality — hashing does not hide data, because anyone with the same hash function can compute the hash. It does not provide authentication — a hash alone does not prove who created the data. Hashing proves that data has not been altered since the hash was computed, nothing more and nothing less.

[SECTION BREAK]

## Digital Signatures — Authentication, Non-Repudiation, and Integrity

Digital signatures combine asymmetric cryptography with hashing to provide authentication, integrity, and non-repudiation simultaneously. Understanding the digital signature process is critical for the exam.

The signing process works as follows. The sender computes a hash of the message using a hash function such as SHA-256. The sender then encrypts the hash with their private key. The encrypted hash is the digital signature. The sender transmits the original message along with the digital signature.

The verification process works as follows. The recipient computes their own hash of the received message using the same hash function. The recipient decrypts the digital signature using the sender's public key, recovering the original hash. The recipient compares the two hashes. If they match, the signature is valid.

A valid digital signature proves three things. First, authentication: the message was signed by the holder of the private key corresponding to the public key used for verification. Since only the sender should possess their private key, this authenticates the sender. Second, integrity: the message has not been altered since it was signed. Any modification to the message would change its hash, causing the comparison to fail. Third, non-repudiation: the sender cannot credibly deny having signed the message. Since only they possess the private key, only they could have produced the signature.

Note what digital signatures do not provide: confidentiality. The message itself is transmitted in plaintext alongside the signature. A digital signature proves who sent the message and that it was not altered, but it does not prevent an eavesdropper from reading it. If confidentiality is also required, the message must be encrypted separately.

This is a high-frequency exam trap. A question might describe a scenario where a digital signature is applied and ask whether confidentiality is ensured. The answer is no. Digital signatures provide authentication, integrity, and non-repudiation — not confidentiality. You must encrypt the message separately if you want to protect its contents from unauthorized disclosure.

[SECTION BREAK]

## Public Key Infrastructure — The Trust Model

Public key cryptography raises an immediate question: how do you know that a public key actually belongs to the entity it claims to represent? If an attacker substitutes their own public key for the legitimate recipient's public key, you would unknowingly encrypt your message with the attacker's key, and the attacker could decrypt it. This is the man-in-the-middle problem, and Public Key Infrastructure — PKI — is the solution.

PKI is a framework of policies, processes, technologies, and entities that binds public keys to the identities of their owners through digital certificates. The core components of PKI are the Certificate Authority, the Registration Authority, digital certificates, certificate revocation mechanisms, and the certificate repository.

The Certificate Authority — CA — is the trusted third party that issues digital certificates. The CA verifies the identity of the certificate applicant and then digitally signs the certificate, binding the applicant's public key to their identity. The CA's own public key — distributed through the CA's own certificate, which is pre-installed in operating systems and browsers — allows anyone to verify that a certificate was genuinely issued by that CA.

PKI operates in a hierarchical trust model. At the top is the Root CA, which is self-signed — it signs its own certificate because there is no higher authority to vouch for it. The Root CA's certificate is the ultimate trust anchor. Below the Root CA are one or more Intermediate CAs — also called Subordinate CAs — which are certified by the Root CA. The Intermediate CAs issue certificates to end entities — users, servers, devices. This hierarchy allows the Root CA to be kept offline and highly secured, while Intermediate CAs handle the operational volume of certificate issuance.

The certificate lifecycle encompasses several stages. Certificate enrollment or application: the entity generates a key pair and submits a certificate signing request — CSR — to the CA. Certificate issuance: the CA verifies the applicant's identity and issues a signed certificate. Certificate usage: the certificate is deployed to the entity's systems and used for authentication, encryption, or signing. Certificate renewal: before the certificate expires, the entity applies for a new certificate, which may involve generating a new key pair. Certificate revocation: if a certificate must be invalidated before its expiration — for example, if the private key is compromised — the CA revokes the certificate.

Certificate revocation is tested heavily on the CISA exam, particularly the two primary mechanisms: Certificate Revocation Lists and the Online Certificate Status Protocol.

A Certificate Revocation List — CRL — is a list published by the CA containing the serial numbers of all revoked certificates. Relying parties download the CRL and check whether a certificate's serial number appears on the list. CRLs have several disadvantages: they can become very large, they are only published periodically — meaning there is a window between revocation and CRL publication during which a revoked certificate appears valid — and they must be downloaded in full even if only one revocation is being checked.

The Online Certificate Status Protocol — OCSP — allows relying parties to query the CA in real time to check the revocation status of a specific certificate. OCSP is more timely than CRLs because the response reflects the current revocation status. However, OCSP introduces a dependency on the availability of the OCSP responder — if the responder is down, the relying party must decide whether to accept or reject the certificate, and OCSP queries reveal the user's browsing patterns to the OCSP responder, raising privacy concerns. OCSP stapling addresses the privacy and performance issues by having the server periodically fetch its own OCSP response and "staple" it to the TLS handshake.

For the exam: CRL is batch-based and periodic with potential staleness; OCSP is real-time and specific but creates availability and privacy dependencies. Know both, and understand the tradeoffs.

[SECTION BREAK]

## TLS/SSL and Transport Security

Transport Layer Security — TLS — is the protocol that secures communication over networks, most visibly in HTTPS for web traffic but also in email, VPN, and countless other applications. TLS is the successor to Secure Sockets Layer — SSL. All versions of SSL and TLS versions prior to 1.2 are considered insecure and have been formally deprecated. Current best practice requires TLS 1.2 as a minimum, with TLS 1.3 preferred.

The TLS handshake exemplifies the hybrid cryptographic approach we discussed earlier. In simplified terms: the client and server negotiate the cipher suite — the combination of algorithms they will use. The server presents its digital certificate, which the client validates against trusted CAs. Using asymmetric cryptography, they establish a shared session key. All subsequent communication is encrypted with the session key using symmetric encryption.

TLS 1.3, finalized in 2018, brought significant improvements: it removed support for legacy cryptographic algorithms that had proven insecure; it simplified the handshake to reduce latency — TLS 1.3 completes in one round trip versus two for TLS 1.2; and it mandated forward secrecy through ephemeral key exchange, meaning that even if the server's long-term private key is later compromised, past session traffic cannot be decrypted.

An IS auditor assessing TLS implementation evaluates several dimensions: Are deprecated protocol versions — SSL, TLS 1.0, TLS 1.1 — disabled? Are weak cipher suites disabled? Are certificates valid, not expired, and issued by trusted CAs? Is the server configured to prefer strong cipher suites? Is certificate pinning used for critical applications? Are HSTS — HTTP Strict Transport Security — headers implemented to prevent protocol downgrade attacks?

[SECTION BREAK]

## Key Management Lifecycle

Cryptographic controls are only as strong as the management of the keys that underpin them. Key management is a discipline in itself, and the CISA exam tests it from the perspective of the IS auditor assessing whether key management practices are adequate.

The key management lifecycle encompasses key generation, key distribution, key storage, key usage, key rotation, key archival, and key destruction.

Key generation must use cryptographically secure random number generators. Keys generated from predictable sources — such as system clocks or sequential numbers — are vulnerable to attack. The IS auditor should verify that key generation uses hardware security modules — HSMs — or software implementations certified to NIST or FIPS standards.

Key distribution must ensure that keys are transmitted securely between parties. For symmetric keys, this is the fundamental challenge — the key must be shared without exposure. Methods include key wrapping, where the symmetric key is encrypted with another key before transmission, and out-of-band distribution, where the key is delivered through a separate channel from the encrypted data.

Key storage must protect keys from unauthorized access. Keys should never be stored in plaintext on general-purpose file systems. Best practice is to store keys in HSMs, which are tamper-resistant hardware devices designed specifically for key storage and cryptographic operations. At minimum, keys should be stored in encrypted key vaults with strict access controls.

Key usage policies should restrict each key to a single purpose — a key used for encryption should not also be used for signing. This separation limits the impact of a key compromise.

Key rotation — periodically replacing keys with new ones — limits the amount of data encrypted with any single key, reducing the impact of key compromise and the volume of data available for cryptanalysis. Rotation frequency depends on the sensitivity of the protected data and the organization's risk appetite, but annual rotation is a common minimum for encryption keys.

Key archival preserves keys that are no longer in active use but may be needed to decrypt archived data. Archived keys must be protected with the same rigor as active keys.

Key destruction must ensure that retired keys are irrecoverably eliminated when they are no longer needed. This includes securely wiping all copies — primary, backup, and escrowed copies. If a key is destroyed while encrypted data that depends on it still exists and may need to be accessed, the data becomes permanently inaccessible.

An IS auditor assessing key management examines whether the organization has a documented key management policy, whether key generation uses approved methods and adequate randomness, whether keys are stored in approved locations with appropriate access controls, whether key rotation is performed on schedule, and whether key destruction is documented and verified.

[SECTION BREAK]

## Real-World Case Study — PKI Deployment for E-Government

Let me illustrate these cryptographic concepts with a real-world scenario: the deployment of a PKI infrastructure for an e-government initiative.

A national government undertakes a digital transformation initiative to provide citizens with online access to government services — tax filing, permit applications, social benefit claims, and business registrations. The initiative requires strong authentication of citizens, integrity protection for submitted documents, non-repudiation for legally binding transactions, and confidentiality for sensitive personal data.

The government establishes a national PKI with a three-tier CA hierarchy. The Root CA is an offline, air-gapped system housed in a hardened facility with multi-person physical access controls — dual control, requiring two authorized personnel with separate access credentials to enter the Root CA room. The Root CA issues certificates only to Intermediate CAs and is powered on only when needed for this purpose.

Two Intermediate CAs operate online: one for citizen certificates and one for government entity certificates. The citizen CA issues certificates to individuals, embedded in national identity smart cards. The government entity CA issues certificates to government servers, applications, and authorized officials.

Citizens use their smart card certificates for authentication when accessing government services — providing something they have, the smart card, and something they know, the PIN, satisfying multi-factor authentication. When a citizen submits a tax filing, the filing is digitally signed with the citizen's private key, stored on the smart card and never extracted. This provides authentication — the filing is attributable to the citizen; integrity — the filing cannot be altered after signing; and non-repudiation — the citizen cannot deny having submitted the filing.

Communication between the citizen's browser and the government portal is encrypted using TLS 1.3. The portal's server certificate, issued by the government entity CA, authenticates the server to the citizen — confirming they are communicating with the legitimate government portal, not a phishing site. The session key negotiated during the TLS handshake encrypts all data in transit, providing confidentiality.

The IS auditor engaged to assess this PKI would evaluate several areas. Root CA security: is the Root CA air-gapped? Are physical access controls adequate? Is the Root CA key ceremony documented and auditable? Key ceremony refers to the formal, witnessed process of generating the Root CA's key pair — a critical event that must be meticulously documented.

Certificate policy and practice statement: does the organization have a formal Certificate Policy — CP — and Certification Practice Statement — CPS? The CP defines what the certificates mean and what obligations they create. The CPS describes how the CA operates — how it verifies identities, how it protects its keys, how it handles revocation. These documents are the governance foundation of the PKI.

Revocation infrastructure: is OCSP available and reliable? Are CRLs published on schedule? What happens if the OCSP responder is unavailable — does the system fail open, accepting potentially revoked certificates, or fail closed, denying all certificate-based transactions?

Key management: are HSMs used for CA key storage? What is the rotation schedule for CA keys? How are citizen certificates revoked if a smart card is lost or stolen? What is the maximum time between revocation request and effective revocation?

Cryptographic algorithm governance: are the algorithms and key lengths compliant with current standards? Is there a migration plan for post-quantum cryptography — the next horizon in cryptographic evolution, where quantum computers may eventually threaten RSA and ECC?

This case study demonstrates that cryptography in practice is not merely a technical discipline — it is a governance, operational, and audit discipline. The algorithms may be mathematically sound, but the PKI is only as trustworthy as its weakest operational process.

[SECTION BREAK]

## Exam Strategy and Key Takeaways

Let me consolidate the critical knowledge.

Symmetric encryption: same key for encrypt and decrypt. AES-256 is the standard. DES and 3DES are deprecated. Fast for bulk data. Key distribution is the challenge.

Asymmetric encryption: key pair — public and private. RSA and ECC are the primary algorithms. Solves the key distribution problem. Slower than symmetric. Used in hybrid with symmetric for practical applications.

Hashing: one-way function producing a fixed-length digest. SHA-256 and SHA-3 are current standards. MD5 and SHA-1 are broken. Provides integrity only.

Digital signatures: hash encrypted with private key. Provides authentication, integrity, and non-repudiation. Does not provide confidentiality.

Remember the CIA-NR mapping: encryption equals confidentiality; hashing equals integrity; digital signatures equal authentication plus integrity plus non-repudiation. This mapping will directly answer multiple exam questions.

PKI: CA hierarchy — Root CA, Intermediate CA, end entity. Certificate lifecycle — enrollment, issuance, usage, renewal, revocation. CRL is periodic and batch; OCSP is real-time and specific. The Statement of Applicability — wait, that is ISO 27001. Do not confuse your documents. In PKI, the key governance documents are the Certificate Policy and Certification Practice Statement.

TLS: minimum version 1.2, prefer 1.3. Hybrid approach — asymmetric for key exchange, symmetric for data encryption. All SSL versions and TLS below 1.2 are deprecated.

Key management: generation with secure randomness, storage in HSMs or encrypted vaults, rotation on schedule, destruction when no longer needed. Keys are the foundation — if key management is weak, all cryptographic controls built upon those keys are compromised.

[SECTION BREAK]

## Bridge to Episode 4

In our next episode, we shift from cryptographic theory to network architecture and defense. We will examine network segmentation including DMZ design and micro-segmentation, firewall types from packet filtering through next-generation firewalls, the critical distinction between intrusion detection and intrusion prevention systems, VPN architectures, Zero Trust networks, and wireless security. That is Episode Four — Network Security and Firewalls. I will see you there.

---
*End of Episode 5.3 — Cryptography & PKI*
*CISA Domain 5: Protection of Information Assets*
