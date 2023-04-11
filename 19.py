
'''

Equality of 3 Values

Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.

Notes:

Your function must return 0, 2 or 3.

'''

def equal(a, b, c):
    num = 0
    if a == b == c:
        num = 3
    elif a == b or a == c or b == c:
        num = 2
    else:
        num = 0
    return num
