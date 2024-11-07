# 10進数から8進数に変換する関数
def dec_to_oct(n):
    # 8進数で文字は使わないのでlabelは必要ない
    # label = "01234567"
    result = ""
    if n == 0:
        return "0"
    while n > 0:
        m = n % 8
        n = n // 8
        # result =  label[m] + result
        result = str(m) + result
    return result


# 8進数から10進数に変換する関数
def oct_to_dec(oct):
    result = 0
    for c in oct:
        result *= 8
        result += int(c) if c in "01234567" else 0
    return result


def test_oct_dec():
    assert dec_to_oct(8) == "10"
    assert dec_to_oct(10) == "12"
    assert oct_to_dec("10") == 8
    assert oct_to_dec("12") == 10


if __name__ == "__main__":
    print("dec_to_oct(0) =>", dec_to_oct(0))
