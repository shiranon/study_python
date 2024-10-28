# FizzBuzz問題の結果を返す関数(テストのみ)
# FizzBuzzの結果を返す関数


def get_fizzbuzz(num):
    return "FizzBuzz"


def test_fizzbuzz():
    assert get_fizzbuzz(1) == "1"
    assert get_fizzbuzz(3) == "Fizz"
    assert get_fizzbuzz(5) == "Buzz"
    assert get_fizzbuzz(15) == "FizzBuzz"
