# R-32 Selectivity, S<sub>R32</sub> Prediction for a Given Ionic Liquid

This repository provides a minimal script to load a pretrained artificial neural network (ANN) and a fitted scaler to predict the R-32 selectivity **S<sub>R32</sub>** from **50 molecular features** (e.g., sigma-profile descriptors) of a given ionic liquid. An example input corresponding to the ionic liquid **[EMIM][PF₆]** is included.

> **Expected result for the provided `[EMIM][PF6]` example**  
> **ML-predicted `S_R32`**: `6.595544815063477`  
> **COSMO-predicted (reference)**: `6.550745304`

---

## Repository contents

```
.
├── main.py                         # Loads model + scaler and predicts S from 50 features
├── S-ANN-340K_model.weights.h5     # Keras model weights (HDF5)
├── scaler_S.pkl                    # Fitted scikit-learn scaler (joblib)
└── input_IL.txt                    # Example 50-D feature vector for [EMIM][PF6]
```

> **Note:** `input_IL.txt` is **tab-separated**. 

---

## Quick start

### 1) Clone

```bash
git clone https://github.com/aiftakher/HFC-IL-ActivityCoefficient.git
cd HFC-IL-ActivityCoefficient
```

### 2) Create a Python environment

> **Recommended Python:** 3.10

Using `venv`:

```bash
python3.10 -m venv .venv
# macOS/Linux:
source .venv/bin/activate
```

### 3) Install dependencies

Create `requirements.txt` with:

```txt
numpy>=1.22,<2.0
tensorflow<2.16
keras<3.0
scikit-learn>=1.2,<1.5
joblib>=1.3,<2.0
```

Then install:

```bash
pip install -r requirements.txt
```

### 4) Run the example

```bash
> python main.py
```

**Expected console output:**

```
> Predicted S_R32: 6.595544815063477
```

This reproduces the ML prediction for the included `[EMIM][PF6]` example. For comparison, the COSMO prediction is `6.550745304`.

---

## How it works

- The script defines a Keras `Sequential` model with two hidden layers (64 units, ReLU).  
- It loads pretrained weights from `S-ANN-340K_model.weights.h5`.  
- A scikit-learn scaler (`scaler_S.pkl`) standardizes raw 50-D feature vector before inference.  
- The network outputs **log(S_R32)**; the script exponentiates it to return **S_R32**.

---

## Use your own features

1. Prepare a single line containing **exactly 50 numeric features**, **tab-separated**.  
2. Save it as `input_IL.txt` (or change the filename in `main.py`).  
3. Run:
   ```bash
   python main.py
   ```

## License

This project is released under the **MIT License**. See `LICENSE`.

---

## Citation

If you use this repository or model in academic work, please cite the paper:
```
@article{Iftakher2025_HFCIL_Solubility,
  author  = {Iftakher, Ashfaq and Hasan, M. M. Faruque},
  title   = {Design Space Exploration and Machine Learning Prediction of Hydrofluorocarbon Solubility in Ionic Liquids for Refrigerant Separation},
  journal = {Journal of Chemical Information and Modeling},
  year    = {2025},
  note    = {Accepted}
}
```

---

## Contact

Questions or issues? Please open a GitHub Issue in this repository or email iftakher@tamu.edu.
