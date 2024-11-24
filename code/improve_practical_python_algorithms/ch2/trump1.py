import random

# トランプ生成のための定数
MARKS = ["♥", "♦", "♠", "♣"]
NUMS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# カードを生成
card = []

for i in range(0, 4):  # 絵柄
    for n in range(0, 13):  # 数字
        mark = MARKS[i]
        num = NUMS[n]
        card.append(mark + num)

# カードをシャッフル
random.shuffle(card)

# カードを表示
print(card[0:7])
