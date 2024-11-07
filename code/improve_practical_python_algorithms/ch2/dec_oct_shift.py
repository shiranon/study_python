# 論理演算とシフトで8進数変換


def dec_to_oct(n):
    result = ""
    if n == 0:
        return "0"
    while n > 0:
        m = n & 0b111
        n = n >> 3
        result = str(m) + result
    return result


def oct_to_dec(oct_str):
    result = 0
    length = len(oct_str)
    for i, c in enumerate(oct_str):
        result += int(c)
        result = result << (3 * (length - i - 1))
    return result


def test_oct_dec():
    assert dec_to_oct(8) == "10"
    assert dec_to_oct(10) == "12"
    assert oct_to_dec("10") == 8
    assert oct_to_dec("12") == 10


if __name__ == "__main__":
    print("oct_to_dec('12')", oct_to_dec("12"))
