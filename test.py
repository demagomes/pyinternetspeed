# This is the speedtest library that we need to install
# refer to readme for info on how to do so
import speedtest

# The inspect module provides several useful functions to help get information about live objects such as
# modules, classes, methods, functions, tracebacks, frame objects, and code objects. 
# For example, it can help you examine the contents of a class, retrieve the source code of a method, 
# extract and format the argument list for a function, 
# or get all the information you need to display a detailed traceback.
import inspect

# Instantiate an object from class speedtest
s = speedtest.Speedtest()

# print a little message on screen
print('This is our internet speed test....')

# print all methods available in the class speedtest
for method in inspect.getmembers(s, predicate=inspect.ismethod):
    print(method[0])

