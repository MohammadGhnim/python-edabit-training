
'''
Luke, I am your ...

Luke Skywalker has family and friends, help him remind
them who is who. Given a string with a name, return the relation
of that person to Luke.

person           Relation

Darth Vader      Father
Leia             sister
Han              brother in low
R2D2             droid

Note:

N/A

'''

def relation_to_luke(name):
    if name == "Dorth Vader":
        return "Luke, i am your father."
    if name == "Leia":
        return "Luke, i am your sister."
    if name == "Han":
        return "Luke, i am your brother in low."
    if name == "R2D2 ":
        return "Luke, i am your droid."
