# NeuralHash: Cryptography via Deep Learning 🧠🔐

NeuralHash is an experimental cryptographic hashing algorithm that utilizes the non-linear, chaotic properties of an untrained Deep Neural Network to generate secure file fingerprints.

## 🚀 Concept
Traditional hashing algorithms (like SHA-256) are built on discrete mathematics and bitwise operations. NeuralHash explores a different path: **Mathematical Chaos in Continuous Space.**

By passing data through a deep architecture of fixed, random weights, we create a high-dimensional "scrambling" effect. Because the network is initialized with a deterministic seed, it remains a pure function—the same input always produces the same output—but the relationship between the two is computationally irreducible.

### Key Features:
*   **Deep Architecture:** 5-layer fully connected network built from scratch in NumPy.
*   **Avalanche Effect:** Optimized to ensure that a single bit change in input results in a complete cascade of changes in the output hash.
*   **Zero-Library Dependencies:** Implements all matrix calculus and activations manually, proving the fundamental principles of AI.
*   **Deterministic Weights:** Uses Xavier initialization with a fixed seed to ensure cross-platform consistency.

## 🧪 Results
In empirical testing, changing 1 byte of a string resulted in a **100% change** in the hex fingerprint, demonstrating extreme sensitivity to initial conditions (The Butterfly Effect).

## 🛠️ Tech Stack
*   **Language:** Python 3.x
*   **Engine:** NumPy (Manual Matrix Calculus)
*   **Theory:** Deep Random Projections, Non-linear Dynamics.

---
*Developed for the MIT Maker Portfolio 2026. Bridging the gap between Machine Learning and Information Security.*
