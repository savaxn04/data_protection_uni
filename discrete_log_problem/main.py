import math

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x1, y1 = egcd(b, a % b)
    return (g, y1, x1 - (a // b) * y1)

def invmod(a, m):
    a %= m
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("inverse does not exist")
    return x % m

def discrete_log_bsgs(g, h, q):
    g %= q
    h %= q
    if q <= 1 or math.gcd(g, q) != 1 or math.gcd(h, q) != 1:
        return None
    if h == 1:
        return 0
    if g == 1:
        return 0 if h == 1 else None

    N = q - 1
    m = math.isqrt(N) + 1
    table = {}
    e = 1
    for j in range(m):
        if e not in table:
            table[e] = j
        e = (e * g) % q
    g_inv = invmod(g, q)
    factor = pow(g_inv, m, q)
    gamma = h
    for i in range(m + 1):
        if gamma in table:
            x = i * m + table[gamma]
            if pow(g, x, q) == h:
                return x
        gamma = (gamma * factor) % q
    return None

if __name__ == "__main__":
    G = int(input("G: "))
    H = int(input("H: "))
    Q = int(input("Q: "))
    x = discrete_log_bsgs(G, H, Q)
    print(x if x is not None else "No solution")
