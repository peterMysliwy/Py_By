# import importlib
# from importlib import import_module
#
# importlib.find_loader()
# moduleName = "os"
# globals()[moduleName] = import_module(moduleName)
# print('The module name is :', moduleName)

# to dynamcially load 'ClassA' from the 'foo' module

import importlib
foo = importlib.import_module('foo')
foo_classA = getattr(foo, 'ClassA')

# is equivalent to
#  from foo import ClassA as foo_ClassA