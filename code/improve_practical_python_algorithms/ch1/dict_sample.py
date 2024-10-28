# 辞書型を初期化
fruits = {
    "Orange": 300,
    "Banana": 500,
    "Mango": 700,
}

# 値を参照する
print(fruits["Banana"])
fruits["Banana"] = 530
print(fruits["Banana"])

if "Apple" in fruits:
    print("Appleが存在する")
else:
    print("Appleが存在しない")
