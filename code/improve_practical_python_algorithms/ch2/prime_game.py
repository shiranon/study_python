# 素数化どうかを判定する関数
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_prime_game(max_value):
    res = ""
    for n in range(1, max_value + 1):
        # 素数ならPを、素数でなければ数値を返す
        if is_prime(n):
            v = "P"
        else:
            v = n
        res += "{:>4}".format(v)

        # 値をカンマで縊り10個ずつ改行を出力(1から数えて10)
        if (n - 1) % 10 == 9:
            res += "\n"
        else:
            res += ","
    return res


if __name__ == "__main__":
    # 1から200までの値を出力
    print(get_prime_game(200))
