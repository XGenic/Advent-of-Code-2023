
def score(line):
    first, second = line.split(":")[1].split("|")
    winners = set({int(x) for x in first.split()})
    guesses = set({int(x) for x in second.split()})
    return len(winners.intersection(guesses))


f = open("Day 4/input.txt", "r")
a = f.readlines()
total = 0
for line in a:
    win_count = score(line)
    if win_count > 0:
        total += 2**(win_count - 1)
print(total)
    
