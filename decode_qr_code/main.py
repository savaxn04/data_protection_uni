def scanner(qrcode):
    n = len(qrcode)
    func = [[False] * n for _ in range(n)]
    def mark_finder(r0, c0):
        for r in range(r0, r0 + 7):
            for c in range(c0, c0 + 7):
                func[r][c] = True

    mark_finder(0, 0)
    mark_finder(0, n - 7)
    mark_finder(n - 7, 0)
    for c in range(0, 8): func[7][c] = True
    for r in range(0, 8): func[r][7] = True

    for c in range(n - 7 - 1, n): func[7][c] = True
    for r in range(0, 8): func[r][n - 7 - 1] = True

    for c in range(0, 8): func[n - 7 - 1][c] = True
    for r in range(n - 7, n): func[r][7] = True
    for c in range(8, n - 8): func[6][c] = True
    for r in range(8, n - 8): func[r][6] = True
    func[13][8] = True
    for c in range(0, 6): func[8][c] = True
    func[8][7] = True
    func[8][8] = True
    for r in range(0, 6): func[r][8] = True
    func[7][8] = True
    for c in range(n - 8, n): func[8][c] = True
    for r in range(n - 8, n): func[r][8] = True
    bits = []
    upward = True
    col = n - 1
    while col > 0:
        if col == 6:
            col -= 1
        cols = [col, col - 1]
        rows = range(n - 1, -1, -1) if upward else range(0, n)
        for r in rows:
            for c in cols:
                if not func[r][c]:
                    val = qrcode[r][c]
                    if (r + c) % 2 == 0:
                        val ^= 1
                    bits.append(val)
                    if len(bits) == 76:
                        mode = int(''.join(map(str, bits[:4])), 2)
                        length = int(''.join(map(str, bits[4:12])), 2)
                        data_bits = bits[12:12 + 8 * length]
                        msg = ''.join(
                            chr(int(''.join(map(str, data_bits[i:i + 8])), 2))
                            for i in range(0, 8 * length, 8)
                        )
                        return msg
        upward = not upward
        col -= 2
    if len(bits) >= 12:
        length = int(''.join(map(str, bits[4:12])), 2)
        data_bits = bits[12:12 + 8 * length]
        msg = ''.join(
            chr(int(''.join(map(str, data_bits[i:i + 8])), 2))
            for i in range(0, 8 * length, 8)
        )
        return msg
    return ""