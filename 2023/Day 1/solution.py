input = open("input.txt", "r")
sum = 0
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
empty = [[], []]

for line in input:
    numbers = empty
    for c in line:
        if c.isdigit():
            numbers[0].append(int(c))
            numbers[1].append(line.index(c))
    print(numbers)
    for word in words:
        if word in line:
            numbers[0].append(words.index(word) + 1)
            numbers[1].append(line.index(word))
    if numbers != empty:
        first = numbers[1].index(min(numbers[1]))
        last = numbers[1].index(max(numbers[1]))
        number = numbers[0][first] * 10 + numbers[0][last]
        sum += number


print(sum)

