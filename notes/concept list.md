### foundational resources
Shallow conceptual overview for each concept [https://cdn.governance.ai/Garfinkel_Tour_Of_Emerging_Cryptographic_Technologies.pdf](https://cdn.governance.ai/Garfinkel_Tour_Of_Emerging_Cryptographic_Technologies.pdf)

Fundamentals of Cryptography Main sources: Intro to cryptography: (1.5h) [https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg](https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg). Use the companion book: Understanding cryptography textbook for students by Christof Paar to do exercises (do within the week of)

Harvard intensive course: [https://intensecrypto.org/public/index.html](https://intensecrypto.org/public/index.html) For each topic, understand the theoretical concept to be able to explain it, solve simple exercises. (read every day)
### 1. foundational learning
- Encryption and decryption [x]
- Symmetric Key Cryptography (2 days)
    - Block ciphers (focus on e.g., AES)
    - Stream ciphers
    - Modes of operation (ECB, CBC, CTR, GCM)
- Public Key Cryptography (2 days)
    - RSA algorithm
    - Elliptic Curve Cryptography (ECC)
    - Diffie-Hellman key exchange
- Hash Functions (1 day)
    - Properties (collision resistance, preimage resistance)
    - Common algorithms (SHA-2, SHA-3)
- Message Authentication Codes (MACs) and Digital Signatures (1 day)
    - HMAC
    - RSA and ECDSA signatures
- Random Number Generation (1 day)
    - True random vs. pseudorandom number generators
    - Cryptographically secure PRNGs
- Key Management (1 day)
    - Key generation, distribution, and storage
    - Public Key Infrastructure (PKI)
- Cryptographic Protocols (2 days)
    - TLS/SSL
- Basic Cryptanalysis (1 day)
    - Common attack vectors (e.g., man-in-the-middle, replay attacks)
    - Principles of secure system design
- Information Theory Basics (1 day)
    - Entropy
    - Perfect secrecy and one-time pads
- Zero-Knowledge Proofs (1 day)
    - Basic concepts and applications
### 2. emerging cryptographic techniques

For each topic, you should skim the relevant chapter here for a quick intro. [https://cdn.governance.ai/Garfinkel_Tour_Of_Emerging_Cryptographic_Technologies.pdf](https://cdn.governance.ai/Garfinkel_Tour_Of_Emerging_Cryptographic_Technologies.pdf) Go through this content: [https://intensecrypto.org/public/lec_17_SFE.html](https://intensecrypto.org/public/lec_17_SFE.html) Cryptography boot camp from simons institute as extra.

- Homomorphic encryption
- Zero-knowledge proofs
- Secure multi-party computation
- Post-quantum cryptography

### 3. Signal processing. Mathematics intro: 

Sources: [https://introtcs.org/public/lec_00_1_math_background.htmlhttps://www.khanacademy.org/computing/computer-science/cryptography](https://introtcs.org/public/lec_00_1_math_background.htmlhttps://www.khanacademy.org/computing/computer-science/cryptography) read the parts of modular arithmetic Aim to get a conceptual understanding for the concepts below with several small examples

- Number theory: Modular arithmetic + Prime numbers and factorization, Euler's totient function
- Abstract algebra: Finite fields, group theory, elliptic curves
    - Intro to Galois fields: [https://youtu.be/x1v2tX4_dkQ?si=F8LE78fnRXpXgBg5](https://youtu.be/x1v2tX4_dkQ?si=F8LE78fnRXpXgBg5)
- Probability/statistics: information theory, statistical tests for randomness.
    - [https://www.khanacademy.org/computing/computer-science/informationtheory](https://www.khanacademy.org/computing/computer-science/informationtheory) Focus on modern information theory, learn mental models and be able to give a few examples
- Linear algebra: Matrix operations, vector spaces, eigenvalues and eigenvectors
- Complexity theory: NP-completeness, quantum complexity theory
- Discrete Mathematics: graph theory, combinatorics
- Signal processing: fourier transform, wavelet analysis