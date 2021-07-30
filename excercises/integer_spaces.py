"""
Teaching
- for loop
- python numerical operators
- range
"""


number = int(input("Enter an integer: "))
digits = len(str(number)) - 1

for digit in range(digits, -1, -1):
    divisor = 10 ** digit
    each = number // divisor
    number %= divisor
    print(each, end=" ")