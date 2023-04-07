
'''
Add, Subtract, Multiply or Divide?

Write a function that takes two numbers and returns if they should be added, subtracted, multiplied or divided to get 24.
If none of the operations can give 24, return None.

Notes:

Only integers are used as test input.
Numbers should be added, subtracted, divided or multiplied in the order they appear in the parameters.
The function should return either "added", "subtracted", "divided", "multiplied" or None.

'''

def operation(num1, num2):
    if num1 + num2 == 24:
        return 'added'
    elif num1 - num2 == 24 or num2 - num1 == 24:
        return 'subtracted'
    elif num1 / num2 == 24 or num2 / num1 == 24:
        return 'dicided'
    elif num1 * num2 == 24:
        return 'multiplied'
    else:
        return None
