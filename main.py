import numpy as np

from signal_io.bitstream import generate_random_bits
from modulation.qpsk import qpsk_mod
from config import *

# 1. Generate bits
bits = generate_random_bits(int(10e6))

test_bits = generate_random_bits(20)

# test qpsk modulation
print(test_bits)
print(qpsk_mod(test_bits))

# 2. Pass through transmitter
# 3. Pass through channel
# 4. Pass through receiver
# 5. BER calculation
