import uesugi_table as table

COLS = "いろはにほへと"
ROWS = "ちりぬるをわか"


def encrypt(src):
    result = ""
    for c in src:
        if c in table.CONV_DIC:
            c = table.CONV_DIC[c]
        result += COLS[c[0]] + COLS[c[1]]
    return result
