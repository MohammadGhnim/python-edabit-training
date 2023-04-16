
'''

Is it True?

In this challenge you will be given a relation between two numbers, written as a string.
Write a function that determines if the relation is True or False.

Notes:

- Tests will only have three types of relations: =, >, and <
- Many approaches work here, but the eval() function is particularly useful!

'''

def is_it_true(relation):
    answer = eval(relation.replace("=", "=="))
