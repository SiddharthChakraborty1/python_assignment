from math import sqrt

C = 50
H = 30


def calculate_value(D):
    Q = int(sqrt((2 * C * D) / H))
    return Q


D_List = [int(x) for x in input("Enter comma separated values of D: ").split(',')]

for D in D_List:
    print(f'{calculate_value(D) }')
