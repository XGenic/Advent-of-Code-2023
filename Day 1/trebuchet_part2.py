f = open('Day 1/input.txt', 'r')
a = f.readlines()
real = []

translation = {'zero': 'z0o', 'one': 'o1e', 'two': 't2o', 'three': 't3e', 'four': 'f4r', 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

for line in a: 
    for key, value in translation.items(): 
        line = line.replace(key, value) 
    nums = [int(j) for j in [*line] if j.isdigit()] 
    real.append(int(''.join([str(nums[0]), str(nums[-1])]))) 
code = sum(real)

print(code)