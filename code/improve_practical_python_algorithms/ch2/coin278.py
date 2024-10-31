# 財布の中に、1円玉が18枚、5円玉が20枚、10円玉が30枚ある
# 硬貨を組み合わせてちょうど278円を用意したい
# 組み合わせが何通りあるか
# 一番少ない硬貨の組み合わせは何か
# 手元の小銭を少なくするため、一番多い硬貨で用意する組み合わせは何か

AMOUNT = 278
coin1, coin5, coin10 = 18, 20, 30
coin_pattern = 0
min_count = 9999
min_combo = []
max_count = 0
max_combo = []

for c1 in range(coin1 + 1):
    for c5 in range(coin5 + 1):
        for c10 in range(coin10 + 1):
            total = c1 + c5 * 5 + c10 * 10
            if total == AMOUNT:
                coin_pattern += 1
                coin_count = c1 + c5 + c10
                if coin_count < min_count:
                    min_count = coin_count
                    min_combo = [c1, c5, c10]
                if coin_count > max_count:
                    max_count = coin_count
                    max_combo = [c1, c5, c10]
print(f"組み合わせ数:{coin_pattern}")
min1, min5, min10 = min_combo
print(f"最小の組み合わせ:1円:{min1}枚、5円:{min5}枚、10円:{min10}枚")
max1, max5, max10 = max_combo
print(f"最大の組み合わせ:1円:{max1}枚、5円:{max5}枚、10円:{max10}枚")
