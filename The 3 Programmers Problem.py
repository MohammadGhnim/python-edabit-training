
'''

The 3 Programmers Problem

You hired three programmers and you (hopefully) pay them.
Create a function that takes three numbers (the hourly wages of each programmer) and returns the difference between the highest-paid programmer and the lowest-paid.


Notes:

- Don't forget to return the result.
- If you get stuck on a challenge, find help in the Resources tab.
- If you're really stuck, unlock solutions in the Solutions tab.

'''

def programers(one, two, three):
    highest = 0
    lowest = 0
    if one > two and one > three:
        highest = one
    elif two > one and two > three:
        highest = two
    else:
        highest = three
    if one < two and one < three:
        lowest = one
    elif two < one and two < three:
        lowest = two
    else:
        lowest = three
    difference = highest - lowest
    return difference
