import random

MARKS = ["♥", "♦", "♠", "♣"]
NUMS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]


def get_label(no):
    mark = no // 13
    num = no % 13
    return MARKS[mark] + NUMS[num]


def shuffle(arr):
    n = len(arr)
    # n-1まで繰り返す
    for i in reversed(range(1, n)):
        k = random.randint(0, i)
        arr[i], arr[k] = arr[k], arr[i]


if __name__ == "__main__":
    cards = list(range(0, 52))
    shuffle(cards)
    print([get_label(no) for no in cards[0:7]])
