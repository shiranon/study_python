# 1から100までの数を順番に出力する・
# 3の倍数のときは数の代わりに「Fizz」、
# 5の倍数のときは数の代わりに「Buzz」、
# 3と5の倍数の時は代わりに「FizzBuzz」を表示

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
