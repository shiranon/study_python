# 1から50までの数を出力するプログラムを書いてください
# ただし、3の倍数のときと、3が付く数字の時は、
# 数字の代わりに「A」を表示してください
# pytestを利用したテストも書き加えること


def get_nabeatu(num):
    # 3の倍数の時 'A'を返す
    if num % 3 == 0:
        return "A"
    # '3'が含まれる時 'A'を返す
    if "3" in str(num):
        return "A"
    # それ以外の時 数字を文字で返す
    return str(num)


def test_get_nabeatu():
    # 3の倍数の時
    assert get_nabeatu(3) == "A"
    assert get_nabeatu(9) == "A"
    # 3が含まれる時
    assert get_nabeatu(32) == "A"
    assert get_nabeatu(130) == "A"
    # 3の倍数ではなく、3も含まれない
    assert get_nabeatu(1) == "1"
    assert get_nabeatu(17) == "17"


if __name__ == "__main__":
    for n in range(1, 51):
        print(get_nabeatu(n))
