# this is just a rough python script for my testing 

import lzma
from torch import cuda

if cuda.is_available():
    print("yes")
else:
    print("no")

#since my laptop has intel it does not support cuda