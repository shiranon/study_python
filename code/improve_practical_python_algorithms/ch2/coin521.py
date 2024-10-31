# 手元に、1円、5円、10円、50円、100円、500円の硬貨が無数にある。
# この硬貨を組み合わせて521円を用意する。組み合わせは何通りあるか
AMOUNT = 521
pattern = 0
for c1 in range(0, AMOUNT + 1):
    for c5 in range(0, AMOUNT // 5 + 1):
        for c10 in range(0, AMOUNT // 10 + 1):
            for c50 in range(0, AMOUNT // 50 + 1):
                for c100 in range(0, AMOUNT // 100 + 1):
                    for c500 in range(0, AMOUNT // 500 + 1):
                        total = (
                            c1 + c5 * 5 + c10 * 10 + c50 * 50 + c100 * 100 + c500 * 500
                        )
                        if total == AMOUNT:
                            pattern += 1
                            if pattern % 10 == 9:
                                print("(経過) 組み合わせ数=", pattern)
print("(結果) 組み合わせ数=", pattern)
