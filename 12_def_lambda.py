def new_fank():
    for i in range(1, 101):
        print(i, end=" ---  ")
        print("ba", "ba", sep="-", end="-")
        print("dooooook")



new_fank()

ug = [1, 2, 33, 4, 55, 22, 76, 4, 55, 22, 7]

def minus_one(list):
    ret_val = []
    if len(list) > 10:
        for element in list:
            ret_val.append(element - 1)
    else:
        for element in list:
            ret_val.append(element + 10)

    return ret_val


print(minus_one(ug))



def say_hello(name):
    print("Привіт,", name)

say_hello("Олексій")  # Виведе: Привіт, Олексій
say_hello("Марія")

def add(a, b):
    return a + b

result = add(3, 5)
print(result)



def minimal(l):
    min1 = l[0]
    for i in l:
       if i < min1:
           min1 = i

    return min1


nums2 = [-32, 33, 2, 7, -32]
res2 = (nums2)

nums1 = [4, 5, 23, 54, 55, 2]
res1 = (nums1)

if len(res1) > len(res2):
    print("nona")
else :
    print("sopd")