# 🧠 NeuralHash: Cryptographic Neural Dynamics

NeuralHash is an experimental cryptographic hashing algorithm that utilizes the non-linear, chaotic properties of untrained Deep Neural Networks to generate secure, one-way file fingerprints.

## 🚀 The Concept: Deterministic Chaos
NeuralHash explores the use of **Mathematical Chaos** in continuous space as a substitute for traditional discrete bitwise operations used in algorithms like SHA-256.

### 🛠️ Key Technical Features
- **Deep Architecture:** Utilizes a 5-layer fully connected network built from scratch in NumPy. The network is never "trained"—the weights are fixed upon initialization.
- **Irreducible Random Projections:** By passing data through a high-dimensional space of random weights, the algorithm creates a "scrambling" effect that is computationally irreducible.
- **The Avalanche Effect:** Optimized to ensure high **Entropy**. A single bit change in the input causes a chaotic cascade, resulting in a completely different 256-bit fingerprint.
- **Zero-Library Neural Logic:** Implements matrix calculus, weights, and non-linear activation functions (ReLU/Sigmoid) manually, without the help of PyTorch or TensorFlow.
- **Xavier Initialization:** Uses deterministic seeding to ensure that the "chaos" is identical across different machines, maintaining the core requirement of a hashing function.

## 📊 Results
In empirical testing, NeuralHash demonstrates extreme sensitivity to initial conditions (The Butterfly Effect), making it an effective tool for detecting even the smallest data modifications.

---
*Part of the MIT Maker Portfolio 2026. Bridging the gap between Machine Learning and Information Security.* 🧠🔐
