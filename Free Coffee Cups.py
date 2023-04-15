

'''

Free Coffee Cups:

For each of the 6 coffee cups i buy, i get a 7th cup free.
In total, I get 7 cups.
Create a function that takes n cups bought and return the total number of cups I would get.

Notes:

- Number of cups I bought + number of cups I got for free.
- Only valid inputs will be given.

'''


def total_cups(n):
    free = int(n/6)
    string = str(free)
    total = free + n
    return total
