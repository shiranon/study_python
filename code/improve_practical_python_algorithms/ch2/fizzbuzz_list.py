# 実行結果を保持する数値リストを作成
result = [str(i) for i in range(100 + 1)]
# 3の倍数の要素にFizzを代入
for i in range(1, 100 // 3 + 1):
    result[i * 3] = "Fizz"
for i in range(1, 100 // 5 + 1):
    result[i * 5] = "Buzz"
for i in range(1, 100 // 15 + 1):
    result[i * 15] = "FizzBuzz"

print("\n".join(result[1:101]))
