import uesugi_table as table

COLS = "いろはにほへと"
ROWS = "ちりぬるをわか"


def encrypt(src):
    result = ""
    for c in src:
        if c in table.CONV_DIC:
            c = table.CONV_DIC[c]
        result += COLS[int(c[0]) - 1] + ROWS[int(c[1]) - 1]
    return result


def decrypt(src):
    result = ""
    n1 = -1
    for c in src:
        if c in COLS:
            n1 = COLS.index(c)
        elif c in ROWS:
            n2 = ROWS.index(c)
            if (0 <= n1 <= 6) and (0 <= n2 <= 6):
                result += table.CONV_TABLE[n1][n2]
        else:
            result += c
            n1 = -1
    return result


if __name__ == "__main__":
    enc = encrypt("おもてなしはおこのみやき")
    dec = decrypt(enc)
    print("暗号化", enc)
    print("復号化", dec)
