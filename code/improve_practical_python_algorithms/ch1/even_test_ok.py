def is_even(num):
    """

    >>> is_even(2)
    True

    >>> is_even(3)
    False
    """
    return num % 2 == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
