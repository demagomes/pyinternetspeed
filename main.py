# This is the speedtest library that we need to install
# refer to readme for info on how to do so
import speedtest


import inspect

s = speedtest.Speedtest()
print('This is our internet speed test....')

for method in inspect.getmembers(s, predicate=inspect.ismethod):
    print(method[0])

