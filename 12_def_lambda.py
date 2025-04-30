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