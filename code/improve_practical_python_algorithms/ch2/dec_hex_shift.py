# ビットシフトで10進数を16進数に変換する関数
def dec_to_hex(n):
    label = "0123456789ABCDEF"
    result = ""
    if n == 0:
        return "0"
    while n > 0:
        m = n & 0b1111  # 論理演算で最下位4bitから今回の桁を求める
        n = n >> 4  # 右に4bitシフトして次の値にする
        result = label[m] + result
    return result


def test_dec_to_hex():
    assert dec_to_hex(255) == "FF"
    assert dec_to_hex(256) == "100"
    assert dec_to_hex(0) == "0"


if __name__ == "__main__":
    print("dec_to_hex(255)=>", dec_to_hex(255))
