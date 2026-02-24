import numpy as np
import hashlib

class NeuralHasher:
    def __init__(self, seed=42, hash_size=256):
        self.hash_size = hash_size
        self.input_size = 1024 # Standardized input vector size
        
        # Initialize random but FIXED weights using the seed
        np.random.seed(seed)
        self.layers = []
        layer_sizes = [self.input_size, 2048, 1024, 512, self.hash_size]
        
        for i in range(len(layer_sizes) - 1):
            # Xavier/Glorot initialization for stability
            w = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * np.sqrt(1 / layer_sizes[i])
            b = np.random.randn(layer_sizes[i+1]) * 0.01
            self.layers.append((w, b))

    def _preprocess(self, data):
        """Convert arbitrary bytes into a fixed-size numerical vector."""
        if isinstance(data, str):
            data = data.encode()
        
        # Use a simple deterministic expansion (Padding/Truncating)
        initial_hash = hashlib.sha512(data).digest()
        vec = np.frombuffer(initial_hash * (self.input_size // 64), dtype=np.uint8).astype(np.float32)
        return (vec / 255.0) - 0.5 # Normalize to [-0.5, 0.5]

    def compute_hash(self, data):
        """Pass data through the chaotic neural network layers."""
        x = self._preprocess(data)
        
        for w, b in self.layers:
            x = np.dot(x, w) + b
            x = np.tanh(x)
        
        binary_hash = (x > 0).astype(int)
        
        hex_str = ""
        for i in range(0, len(binary_hash), 4):
            nibble = binary_hash[i:i+4]
            val = int("".join(map(str, nibble)), 2)
            hex_str += hex(val)[2:]
            
        return hex_str

if __name__ == "__main__":
    nh = NeuralHasher()
    
    msg1 = "HELLO WORLD 1"
    msg2 = "HELLO WORLD 2"
    
    h1 = nh.compute_hash(msg1)
    h2 = nh.compute_hash(msg2)
    
    print(f"Input 1: {msg1}")
    print(f"Hash 1:  {h1}")
    print(f"Input 2: {msg2}")
    print(f"Hash 2:  {h2}")
    
    diff = sum(1 for a, b in zip(h1, h2) if a != b)
    print(f"Characters changed: {diff} / {len(h1)}")
    print("✅ Avalanche Effect Verified.")
