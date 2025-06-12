import numpy as np

from signal_io.bitstream import generate_random_bits
from config import *

# 1. Generate bits
bits = generate_random_bits(int(10e6))

# 2. Pass through transmitter
# 3. Pass through channel
# 4. Pass through receiver
# 5. BER calculation
