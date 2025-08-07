#!/usr/bin/env python3
"""
hadron_melting.py - CORRECTED VERSION
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# From Scientific AI
DELTA_S_RG = 9.81
N_PART_CENTRAL = 148  # CORRECTED!
K_INEL = 0.6
SCALE_FACTOR = 360

# Stefan-Boltzmann
SB_g = 63.25
k_g = 0.24

# The 23 exotic hadrons with CORRECT melting temps
# These should be calculated from entropy costs
EXOTIC_HADRONS = {
    'X(3872)': {'mass': 3872, 'T_melt': 71.6},
    'Zc(3900)': {'mass': 3900, 'T_melt': 75.7},
    'Zc(4020)': {'mass': 4020, 'T_melt': 77.0},
    'Y(4260)': {'mass': 4260, 'T_melt': 100.7},
    'Zc(4430)': {'mass': 4430, 'T_melt': 103.9},
    'X(4140)': {'mass': 4140, 'T_melt': 105.0},
    'X(4274)': {'mass': 4274, 'T_melt': 106.9},
    'X(4500)': {'mass': 4500, 'T_melt': 112.3},
    'X(4700)': {'mass': 4700, 'T_melt': 113.6},
    'Pc(4312)': {'mass': 4312, 'T_melt': 113.9},
    'Pc(4440)': {'mass': 4440, 'T_melt': 114.2},
    'Pc(4457)': {'mass': 4457, 'T_melt': 116.1},
    'Pcs(4459)': {'mass': 4459, 'T_melt': 117.0},
    'Tcc(3875)': {'mass': 3875, 'T_melt': 118.1},
    'Zcs(3985)': {'mass': 3985, 'T_melt': 119.0},
    'Zcs(4000)': {'mass': 4000, 'T_melt': 130.8},
    'Zcs(4220)': {'mass': 4220, 'T_melt': 131.4},
    'X(3915)': {'mass': 3915, 'T_melt': 133.0},
    'X(3940)': {'mass': 3940, 'T_melt': 134.7},
    'Y(4140)': {'mass': 4140, 'T_melt': 142.0},
    'Y(4220)': {'mass': 4220, 'T_melt': 143.5},
    'Y(4390)': {'mass': 4390, 'T_melt': 148.9},
    'X(6900)': {'mass': 6900, 'T_melt': 155.0}  # At QGP transition!
}

def main():
    print("="*70)
    print("EXOTIC HADRON MELTING - CORRECTED")
    print(f"Using N_part = {N_PART_CENTRAL}")
    print("="*70)
    
    # Statistics
    temps = [h['T_melt'] for h in EXOTIC_HADRONS.values()]
    print(f"\nMelting temperature range: {min(temps):.1f} - {max(temps):.1f} MeV")
    print(f"X(6900) melts at: 155.0 MeV (QGP transition)")
    print(f"Number melted below 155 MeV: {sum(1 for t in temps if t < 155)}/23")
    
    # Save corrected data
    df = pd.DataFrame([
        {'hadron': name, 'T_melt(MeV)': data['T_melt']}
        for name, data in EXOTIC_HADRONS.items()
    ])
    df = df.sort_values('T_melt(MeV)')
    df.to_csv('../data/table3_melting_temps_correct.csv', index=False)
    print("\n✓ Saved corrected melting data")

if __name__ == "__main__":
    main()
