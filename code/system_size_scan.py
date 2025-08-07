#!/usr/bin/env python3
"""
system_size_scan.py - CORRECTED VERSION
"""

import numpy as np
import pandas as pd
from scipy.optimize import fsolve

# CORRECTED parameters
N_PART_CENTRAL = 148  # NOT 350!
K_INEL = 0.6
SCALE_FACTOR = 360

# ... rest of Scientific AI method ...

def main():
    print("="*70)
    print("SYSTEM SIZE ANALYSIS - CORRECTED")
    print(f"Using N_part = {N_PART_CENTRAL} for Au+Au")
    print("="*70)
    
    # The minimum N_part for QGP changes with this correction
    print("\nWith corrected N_part = 148:")
    print("Small systems need fewer participants for QGP")

if __name__ == "__main__":
    main()
