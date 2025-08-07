# QCD Entropy-QGP Formation: Universal Threshold for Phase Transition

**DOI** [10.5281/zenodo.16762323](https://doi.org/10.5281/zenodo.16762323) **License:** MIT

## Abstract

Universal entropy-mass relation predicts quark-gluon plasma formation from first principles - completing the QCD entropy trilogy. The universal entropy budget |ΔS_RG| = 9.81 kB fundamentally constrains the hadronic to QGP phase transition.

## Key Results

- ✅ **QGP transition predicted at √s_NN = 17-19 GeV** (observed: 17-20 GeV at RHIC)
- ✅ **Zero empirical QGP parameters** - pure first-principles prediction
- ✅ **148 Au+Au collision energies analyzed** systematically
- ✅ **23 exotic hadron melting temperatures** calculated
- ✅ **Minimum system sizes** determined for all energies
- ✅ **Small system predictions** validated (p+Au, d+Au, O+O)
- ✅ **Critical fluctuation point** identified at √s_NN = 17.5 ± 0.5 GeV

## Repository Structure

```
qcd-entropy-qgp-2025/
├── code/                                   # Python analysis pipeline
│   ├── qgp_entropy_threshold.py           # Main QGP transition calculator
│   ├── hadron_melting.py                  # Exotic hadron melting sequence
│   ├── system_size_scan.py                # Minimum system size analysis
│   ├── validation_paper3.py               # Validation against RHIC data
│   └── README_code.md                     # Code documentation
├── data/                                   # CSV datasets
│   ├── table1_AuAu_results.csv           # Au+Au collision results
│   ├── table2_small_systems.csv          # Small system predictions
│   └── table3_melting_temps.csv          # 23 hadron melting temperatures
├── figures/                                # Publication figures
│   ├── figure1_entropy_ratio.png         # S/N_part vs beam energy
│   ├── figure2_phase_diagram.png         # QCD phase diagram
│   ├── figure3_melting_sequence.png      # Exotic hadron melting
│   └── figure4_min_system_size.png       # Minimum N_part vs energy
├── latex/                                  # Paper source
│   ├── main.tex                          # LaTeX source
│   └── Universal_Entropy_Threshold_for_Quark_Gluon_Plasma_Formation.pdf
└── LICENSE                                # MIT License
```

## Quick Start

### Run Analysis
```bash
# Calculate QGP transition for Au+Au collisions
python3 code/qgp_entropy_threshold.py

# Generate exotic hadron melting sequence  
python3 code/hadron_melting.py

# Analyze minimum system sizes
python3 code/system_size_scan.py

# Validate against RHIC data
python3 code/validation_paper3.py
```

## Core Discovery

### QGP Formation Criterion
When entropy per participant exceeds the universal threshold:
```
S_total/N_part > ΔS_RG = 9.81 kB  →  Quark-Gluon Plasma forms
```

### Transition Results (Au+Au Central Collisions)
| √s_NN (GeV) | T₀ (MeV) | S/N_part (×9.81 kB) | Phase |
|-------------|----------|---------------------|--------|
| 7.7         | 153      | 0.91               | Hadronic |
| 11.5        | 155      | 0.94               | Hadronic |
| 14.5        | 157      | 0.97               | Hadronic |
| **19.6**    | **159**  | **1.02**           | **QGP** |
| 27.0        | 163      | 1.10               | QGP |
| 39.0        | 169      | 1.23               | QGP |
| 62.4        | 182      | 1.51               | QGP |
| 200         | 253      | 4.10               | QGP |

## Five Falsifiable Predictions

1. **No QGP in p+p at 13 TeV** - system size below threshold
2. **Marginal QGP in p+Au at 200 GeV** - only in 0-5% central collisions
3. **X(6900) melts at T = 155 MeV** - precisely at QGP transition
4. **Critical fluctuations peak at √s_NN = 17.5 ± 0.5 GeV** - searchable in BES
5. **Minimum N_part = 164 at 7.7 GeV, 36 at 200 GeV** - testable at RHIC

## Scientific Impact

This work completes the QCD entropy trilogy:

1. **[Paper 1](https://zenodo.org/records/16743904)**: Light hadron masses (100 MeV scale)
2. **[Paper 2](https://zenodo.org/records/16752674)**: Exotic hadrons (1-10 GeV scale)  
3. **Paper 3**: QGP formation (10-100 GeV scale) - This work

**One universal constant (9.81 kB) governs three orders of magnitude in QCD physics**

## Citation

```bibtex
@article{tupay2025qgp,
  author = {Tupay, Johann Anton Michael},
  title = {Universal Entropy Threshold for Quark-Gluon Plasma Formation: 
           Third in a Series on QCD Entropy Constraints},
  year = {2025},
  month = aug,
  publisher = {Zenodo},
  version = {v1.0.0},
  doi = {10.5281/zenodo.16762323},  
  url = {https://github.com/JAMTUPAY/qcd-entropy-qgp-2025}
}
```

## Original Work

Based on: [Universal Entropy-Mass Relation in QCD](https://zenodo.org/records/16743904)

## Previous Papers in Series

- **Paper 1**: [QCD Entropy-Mass Relation](https://github.com/JAMTUPAY/qcd-entropy-mass)
- **Paper 2**: [Entropy-Forbidden Exotic Hadrons](https://github.com/JAMTUPAY/qcd-entropy-forbidden-states)

## Author

**Johann Anton Michael Tupay**  
Contact: jamtupay@icloud.com  
ORCID: 0009-0008-7661-8698

## License

MIT License - See LICENSE file

## Acknowledgments

Special thanks to the RHIC collaborations (STAR, PHENIX, BRAHMS, PHOBOS) and LHC collaborations (ALICE, CMS, ATLAS) for experimental data validating these theoretical predictions. The author acknowledges the importance of open scientific discourse and independent research in advancing fundamental physics.
