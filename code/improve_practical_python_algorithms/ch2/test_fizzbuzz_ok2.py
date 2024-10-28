def get_fizzbuzz(num):
    is_fizz = num % 3 == 0
    is_buzz = num % 5 == 0
    if is_fizz and is_buzz:
        return "FizzBuzz"
    if is_fizz:
        return "Fizz"
    if is_buzz:
        return "Buzz"
    return str(num)


def test_get_fizzbuzz():
    assert get_fizzbuzz(3) == "Fizz"
    assert get_fizzbuzz(5) == "Buzz"
    assert get_fizzbuzz(7) == "7"
    assert get_fizzbuzz(15) == "FizzBuzz"
    assert get_fizzbuzz(25) == "Buzz"
