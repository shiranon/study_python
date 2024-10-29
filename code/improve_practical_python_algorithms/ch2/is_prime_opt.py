import math


# 最適化した試し割り法で素数科どうかを判定する関数
def is_prime(n):
    # 2未満の値は素数ではない
    if n < 2:
        return False
    # 2は素数である
    if n == 2:
        return True
    # 2の倍数は素数ではない
    if n % 2 == 0:
        return False
    sq = math.ceil(math.sqrt(n))
    # 3からsqまで偶数を飛ばして割り切れるかを試す
    for i in range(3, sq + 1, 2):
        if n % i == 0:
            return False
    return True


def test_is_prime_all():
    answer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    prime_list = list(filter(is_prime, range(1, 51)))
    assert prime_list == answer
