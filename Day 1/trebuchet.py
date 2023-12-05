# Function to extract and process numbers from a string
def process_string(s):
    numbers = [int(char) for char in s if char.isdigit()]  # Extract all digits from the string
    if len(numbers) >= 2:
        return int(str(numbers[0]) + str(numbers[-1]))  # Concatenate the first and last digit
    elif len(numbers) == 1:
        return int(str(numbers[0]) + str(numbers[0])) # Only one digit, return it
    else:
        return 0  # No digits in the string

translate = { 'zero': 'z0e', 'one': 'o1e', 'two': 't2o', 'three': 't3r', 'four': 'f4o', 'five': 'f5e', 'six': 's6e', 'seven': 's7e', 'eight': 'e8t', 'nine': 'n9n'}

# Read the text file
file_path = "Day 1/input.txt"
total_sum = 0

with open(file_path, 'r') as file:
    for line in file:
        line_sum = process_string(line)
        total_sum += line_sum

print(f"Total sum of processed numbers: {total_sum}")

