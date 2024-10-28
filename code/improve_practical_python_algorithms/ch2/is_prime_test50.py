# 関数is_primeを網羅的にテストする関数
def test_is_prime_all():
    answer = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    prime_list = []
    for i in range(1, 51):
        if is_prime(i):
            prime_list.append(i)
    assert prime_list == answer


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
