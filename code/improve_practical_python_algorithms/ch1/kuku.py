for n in range(1, 9 + 1):
    line = "|"
    for m in range(1, 9 + 1):
        value = n * m
        line += f"{value:3d} |"
    print(line)
