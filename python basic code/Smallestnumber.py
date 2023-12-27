
numbers = [2,10,36,8,9,16]
min = numbers[0]
for number in numbers:
    if number < min:
        min = numbers
print(min)

numbers = [2,10,36,8,9,16]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)