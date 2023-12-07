#USED FOR BOTH PART 1 AND 2#

n = 45977295
y = 305106211101695

total = 0

for i in range (1, n-1):
    d = (n-i)*i
    if d > y:
       total += 1

print(total)
