import numpy as np

def generate_random_bits(n_bits: int, p: float = 0.5) -> np.ndarray:
   return np.random.binomial(size=n_bits, n=1, p=p).astype(np.uint8) 
