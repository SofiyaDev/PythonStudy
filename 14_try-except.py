#обрабка винятків
from logging import exception


try:
    a = int(input("enter num: "))
    b = int(input("enter num: "))
    с = int(input("enter num: "))
    print(a * b / с)
except Exception :
    print("помилка введення")

else:
    print("правильна відповідь")