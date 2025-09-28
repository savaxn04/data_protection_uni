ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
EN_FREQ = [
    8.08, 1.67, 3.18, 3.99, 12.56, 2.17, 1.80, 5.27, 7.24, 0.14, 0.63, 4.04, 2.60,
    7.38, 7.47, 1.91, 0.09, 6.42, 6.59, 9.15, 2.79, 1.00, 1.89, 0.21, 1.65, 0.07
]
EN_FREQ = [x / 100.0 for x in EN_FREQ]

def letter_counts(text: str) -> list[int]:
    counts = [0] * 26
    for ch in text:
        if ch.isalpha():
            counts[ord(ch.upper()) - ord('A')] += 1
    return counts

def chi2_score(counts: list[int], total: int, shift: int) -> float:
    if total == 0:
        return float("inf")
    score = 0.0
    for i in range(26):
        expected = total * EN_FREQ[i]
        observed = counts[(i + shift) % 26]
        if expected > 0:
            diff = observed - expected
            score += (diff * diff) / expected
    return score

def best_shift(ciphertext: str) -> int:
    counts = letter_counts(ciphertext)
    total = sum(counts)
    scores = [(s, chi2_score(counts, total, s)) for s in range(26)]
    s_best, _ = min(scores, key=lambda t: t[1])
    return s_best

def decode_with_shift(ciphertext: str, shift: int) -> str:
    out = []
    for ch in ciphertext:
        if 'A' <= ch <= 'Z':
            base = ord('A')
            out.append(chr((ord(ch) - base - shift) % 26 + base))
        elif 'a' <= ch <= 'z':
            base = ord('a')
            out.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            out.append(ch)
    return "".join(out)


if __name__ == "__main__":
    message = input("message: ")
    shift = best_shift(ciphertext=message)
    result = decode_with_shift(ciphertext=message, shift=shift)
    print(result)