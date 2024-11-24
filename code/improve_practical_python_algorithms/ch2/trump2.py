import random

# トランプ生成のための定数
MARKS = ["♥", "♦", "♠", "♣"]
NUMS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


# カード番号から絵柄と番号の文字列を返す
def get_label(no):
    mark = no // 13
    num = no % 13
    return MARKS[mark] + NUMS[num]


# カード番号を生成
cards = list(range(0, 52))
random.shuffle(cards)

# カードを表示
print(list(map(get_label, cards[0:7])))
