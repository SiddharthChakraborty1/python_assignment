
def factorial(num:int):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Enter the number whoes factorial is to be calculated: "))
print(f'The factorial of {num} is {factorial(num)}')