#!/usr/bin/env python

import subprocess
import os

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

try:
    import cython
    print("Cython version should be at least 0.20, it is:",
          cython.__version__)
except ImportError:
    print("Please install pandas")

try:
    print("Checking for gcc compiler:")
    print("-"*80)
    subprocess.call(["gcc", "--version"])
    print("-"*80)
    print("success")
    print("-"*80)
except OSError as e:
    if e.errno == os.errno.ENOENT:
        # handle file not found error.
        print("Cannot find the gcc compiler")
    else:
        # Something else went wrong while trying to run `wget`
        print("`gcc --version` failed for some reason: ", e)
