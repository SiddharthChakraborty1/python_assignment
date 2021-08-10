input_str = input("Enter the string: ")
letter_count = 0
digit_count = 0
for char in input_str:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print(f'Letters: {letter_count}')
print(f'Digits: {digit_count}')

