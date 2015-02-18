#!/usr/bin/env python

try:
    import IPython
    print("IPython version should be at least 2.4, it is:",
          IPython.__version__)
except ImportError:
    print("Please install IPython")

try:
    import matplotlib
    print("matplotlib version should be at least 1.4, it is:",
          matplotlib.__version__)
except ImportError:
    print("Please install matplotlib")

try:
    import numba
    print("Numba version should be at least 0.16.0, it is:", numba.__version__)
except ImportError:
    print("Please install numba")

try:
    import pandas
    print("Pandas version should be at least 0.15.0, it is:",
          pandas.__version__)
except ImportError:
    print("Please install pandas")
