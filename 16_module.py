import cowsay
import my_module
import time
import datetime
import sys
import os, platform
from math import sqrt, ceil as c

print(c(sqrt(144)))

time.sleep(2)
print(datetime.datetime.now().time())
print(sys.path)
print(os.name)
print(platform.system())


my_module.hi()
print(my_module.name)

cowsay.cow("FREDYA")

