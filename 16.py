'''
Let's Feul up!

A vehicle needs 10 times the amount of fuel than the distance
it travels.
However , it must always carry a minimum of 100 fuel before stting off. 

create a function which calculate the amount of fuel it needs, given the distance.

Notes:

1- distance will be a number greater than zero.
2- Return 100 if the calculated fuel turns out to be less than 100.

'''

def calculate_fuel(n):
    fuel = n * 10
    if fuel > 100:
        return fuel
    else:
        return 100
