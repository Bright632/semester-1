# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    print("Error: no numbers provided", file=sys.stderr)
    sys.exit(1)

minimum = min(numbers)
maximum = max(numbers)
mean = sum(numbers) / len(numbers)

numbers.sort()
middle = len(numbers) // 2

if len(numbers) % 2 == 1:
    median = numbers[middle]
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2

print("Minimum =", minimum)
print("Maximum =", maximum)
print("Mean =", mean)
print("Median =", median)
