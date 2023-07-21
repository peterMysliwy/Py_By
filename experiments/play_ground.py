import sys
class Foobar:
    pass
def str_to_class(str):
    return getattr(sys.modules[__name__], str)
print(str_to_class("Foobar"))
print(type(Foobar))




"""
# Python code to demonstrate dictionary
# comprehension

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

# but this line shows dict comprehension here
myDict = { k:v for (k,v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print (myDict)"""
