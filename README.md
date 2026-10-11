# Python Programs

## 1. Find Numbers Divisible by 7 but Not a Multiple of 3

### Problem Statement
Write a program to find all numbers between 2000 and 3200 that are divisible by 7 but are not multiples of 3. Print the output as a comma-separated sequence.

### Program
```python
numbers = []

for i in range(2000, 3201):
    if i % 7 == 0 and i % 3 != 0:
        numbers.append(str(i))

print(",".join(numbers))
```

### Explanation
- `range(2000, 3201)` generates numbers from 2000 to 3200.
- `i % 7 == 0` checks whether a number is divisible by 7.
- `i % 3 != 0` checks whether a number is not divisible by 3.
- `numbers.append(str(i))` adds each valid number to the list as a string.
- `",".join(numbers)` prints the numbers separated by commas.

### Output
The program prints all numbers between 2000 and 3200 that satisfy both conditions, separated by commas.

---

## 2. Convert a List of Characters into a String

### Problem Statement
Given a list of characters, write a program to convert the list into a single string.

### Program
```python
characters = ['C', 'O', 'D', 'I', 'N', 'G']

result = ''.join(characters)

print(result)
```

### Explanation
- `characters` stores the list of characters.
- `''.join(characters)` combines all the characters into a single string without spaces.
- `print(result)` displays the resulting string.

### Output
```text
CODING
```

---

## 3. Generate a Dictionary Containing (i, i*i)

### Problem Statement
Given an integer `n`, write a program to generate a dictionary containing numbers from 1 to `n` as keys and their squares as values.

### Program
```python
n = int(input("Enter a number: "))

result = {}

for i in range(1, n + 1):
    result[i] = i * i

print(result)
```

### Explanation
- `input()` accepts an integer from the user.
- `result = {}` creates an empty dictionary.
- `range(1, n + 1)` generates numbers from 1 to `n`.
- `result[i] = i * i` stores each number and its square in the dictionary.
- `print(result)` displays the dictionary.

### Output
```text
Enter a number: 5
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## Conclusion

These programs demonstrate basic Python concepts, including loops, conditional statements, lists, strings, dictionaries, and arithmetic operations.# MDC-WORK-
