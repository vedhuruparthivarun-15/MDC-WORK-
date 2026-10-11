
numbers = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 3 != 0:
        numbers.append(str(i))

print(",".join(numbers))
