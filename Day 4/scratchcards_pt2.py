
def score(line):
    first, second = line.split(":")[1].split("|")
    winners = set({int(x) for x in first.split()})
    guesses = set({int(x) for x in second.split()})
    return len(winners.intersection(guesses))


f = open("Day 4/input.txt", "r")
a = f.readlines()
lines = []
multiples = []

for line in a:
    lines.append(line)
    multiples.append(1)
for idz, line in enumerate(lines):
    win_count = score(line)
    if win_count > 0:
        for i in range(1, win_count+1):
            multiples[idz+i] += multiples[idz]
total = sum(multiples)
print(total)


