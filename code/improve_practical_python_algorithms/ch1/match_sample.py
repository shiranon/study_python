def match_test(num):
    match num:
        case 1:
            print(f"{num}は1です")
        case 2:
            print(f"{num}は2です")
        case 3:
            print(f"{num}は3です")
        case _:
            print(f"{num}は1~3以外です")


for i in range(1, 5 + 1):
    match_test(i)
