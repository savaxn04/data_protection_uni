# Classical Ciphers Toolkit

Small study repository with two modules:
- **Enigma-like encoder/decoder** (incremental Caesar + 3 fixed rotors)
- **Caesar shift cracker** using **letter-frequency analysis** (keeps case; non-letters unchanged)

> In the future you can add more methods (Vigenère, Playfair, etc.).

---

## Repository structure

```
.
├── enigma_machine/                # Enigma-like machine (incremental Caesar + 3 rotors)
│   └── main.py            # CLI-style script reading from stdin
├── frequency_based_decryption/        # Frequency analysis for Caesar (no key required)
│   └── main.py           # best_shift, decode_with_shift, helpers
└── README.md
```

## Requirements

- Python 3.11+
- Optional: virtual environment

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -U pip
```

---

## Enigma-like encoder/decoder

**Algorithm**
1. Incremental Caesar: for the *i*-th character use shift `start + i` (mod 26).
2. Apply three rotor substitutions sequentially (ROTOR1 → ROTOR2 → ROTOR3).
3. Decode does the inverse Caesar and traverses rotors in reverse with inverse mapping.

**Run (example)**

The script expects:
1) `ENCODE` or `DECODE`  
2) Start number (integer)  
3) `ROTOR1` (26-letter permutation, A–Z)  
4) `ROTOR2`  
5) `ROTOR3`  
6) Message (A–Z; adapt as needed)

```bash
python enigma/main.py << 'EOF'
ENCODE
2
BDFHJLCPRTXVZNYEIWGAKMUSQO
AJDKSIRUXBLHWTMCQGZNPYFVOE
EKMFLGDQVZNTOWYHXUSPAIBRCJ
DOG
EOF
# Expected: QGI
```

Swap to `DECODE` with the same parameters to recover plaintext.

---

## Caesar shift cracker (frequency analysis)

**Features**
- Finds the most likely shift (0–25) via χ² against English frequencies.
- Decodes while **preserving case** and **leaving non-letters unchanged**.

**Quick use in Python**

```python
from caesar_cracker.crack import best_shift, decode_with_shift

ct = "Gur Dhvpx Oebja Sbk Whzcf Bire Gur Ynml Qbt!"  # ROT13
s = best_shift(ct)            # -> 13
pt = decode_with_shift(ct, s) # preserves case, keeps punctuation
print(s, pt)
```

Uses these English letter frequencies (as provided):

```
A 8.08  B 1.67  C 3.18  D 3.99  E 12.56  F 2.17  G 1.80
H 5.27  I 7.24  J 0.14  K 0.63  L 4.04  M 2.60  N 7.38
O 7.47  P 1.91  Q 0.09  R 6.42  S 6.59  T 9.15  U 2.79
V 1.00  W 1.89  X 0.21  Y 1.65  Z 0.07
```
