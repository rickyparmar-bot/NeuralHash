# 🧠 NeuralHash: Cryptographic Neural Dynamics

![Task](https://img.shields.io/badge/Task-Cryptographic%20Hashing-blue) ![Engine](https://img.shields.io/badge/Engine-Manual%20NumPy-orange) ![Security](https://img.shields.io/badge/Security-One--Way%20Function-lightgrey)

NeuralHash is an experimental cryptographic hashing algorithm that utilizes the non-linear, chaotic properties of untrained Deep Neural Networks to generate secure fingerprints.

## 🚀 The Core Hypothesis
Traditional hashing relies on bitwise shuffling. NeuralHash relies on **High-Dimensional Random Projections**. By projecting data through a deep architecture of fixed weights, we create an irreducible one-way function.

### 🛠️ Technical Specs
- **Architecture:** 5-Layer Deep Feed-Forward Network.
- **Weights:** Xavier-Initialized (Deterministic Seed).
- **Avalanche Effect:** Optimized activation functions ensure that a single-bit input change leads to a >50% variance in the resulting hash.
- **Zero-Library:** No PyTorch/TensorFlow. Pure linear algebra implemented in NumPy.

---

## 💻 Benchmarking & Usage
### Calculate a Hash
```bash
python3 hasher.py "MIT 2026 Maker Portfolio"
```

### Run Collision Test
Test the sensitivity of the algorithm to small data changes.
```bash
python3 hasher.py --test-avalanche
```

---

## 📂 Project Structure
```text
NeuralHash/
├── hasher.py       # Main algorithm and CLI interface
├── activation.py   # Manual implementation of ReLU/Sigmoid
├── benchmarking/   # Entropy and collision statistics
└── README.md       # Surface documentation
```

## 🗺️ Roadmap
- [ ] **Proof of Work:** Implementing a blockchain using NeuralHash as the puzzle.
- [ ] **Hardware Acceleration:** Writing a CUDA kernel for high-speed batch hashing.
- [ ] **Entropy Mapping:** Mathematical proof of collision resistance.

---
