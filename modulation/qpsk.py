import numpy as np
import numpy.typing as npt

def qpsk_mod(bits: npt.ArrayLike) -> np.ndarray[np.complex64]:
    
    # Pair up bits
    bits = bits.reshape(-1, 2)

    # Map bits to symbols
    mapping = {
        (0, 0):  1 + 1j,
        (0, 1):  1 - 1j,
        (1, 1): -1 - 1j,
        (1, 0): -1 + 1j,
    }
    symbols = [mapping[tuple(pair)] for pair in bits]

    return symbols

