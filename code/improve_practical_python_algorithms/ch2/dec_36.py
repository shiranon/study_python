# アルファベットを全て使った36進数の変換をする
def dec_to_t36(n):
    label = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    if n == 0:
        return "0"
    while n > 0:
        m = n % 36
        n = n // 36
        result = label[m] + result

    return result


def t36_to_dec(t36_str):
    result = 0
    for c in t36_str:
        result *= 36
        v = 0
        if c in "0123456789":
            v = ord(c) - ord("0")
        elif c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            v = ord(c) - ord("A") + 10
        elif c in "abcdefghijklmnopqrstuvwxyz":
            v = ord(c) - ord("a") + 10
        result += v
    return result


def test_dec_hex():
    assert dec_to_t36(35) == "Z"
    assert dec_to_t36(36) == "10"
    assert dec_to_t36(1295) == "ZZ"

    assert t36_to_dec("z") == 35
    assert t36_to_dec("10") == 36
    assert t36_to_dec("ZZ") == 1295
