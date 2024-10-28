# 引数nが素数かどうか調べる関数(未)
def is_prime(n):
    # 2未満は素数ではない
    if n < 2:
        return False
    # 2からn-1まで繰り返す
    for i in range(2, n):
        # 割り切れたら素数ではない
        if n % i == 0:
            return False
    return True


# 関数is_primeをテストする
def test_is_prime():
    assert is_prime(3)
    assert not is_prime(8)
    assert is_prime(89)
