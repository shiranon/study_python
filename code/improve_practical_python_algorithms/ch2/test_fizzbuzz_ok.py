def get_fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def test_get_fizzbuzz():
    assert get_fizzbuzz(3) == "Fizz"
    assert get_fizzbuzz(5) == "Buzz"
    assert get_fizzbuzz(7) == "7"
    assert get_fizzbuzz(15) == "FizzBuzz"
