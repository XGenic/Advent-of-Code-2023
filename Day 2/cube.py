import re

f = open("day 2/input.txt", "r")
a = f.readlines()
ans = []

for line in a:
    match = re.search(r"(([1-9][4-9]\s+green|[2-9][0-9]\s+green)|([1-9][3-9]\s+red|[2-9][0-9]\s+red)|([1-9][5-9]\s+blue|[2-9][0-9]\s+blue))", line)
    if match:
        continue
    else:
        game_number = int(re.search(r'Game (\d+):', line).group(1))
        ans.append(game_number)


print(sum(ans))


#([1-9][2-9]|[2-9][0-9]|\d{3,})#