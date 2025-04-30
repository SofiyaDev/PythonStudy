#Set

ropa = {"gf", "gd", 14, "gf", "gd", 14}
ropa.pop() #видаляє останній елемент
#ropa.clear() #очищає все
ropa.add("dop") #додає елемент
ropa.update([14, 78, "42"]) #додає елементи яких ще немає
ropa.remove("42") #видаляє елемент з певним значенням
print(ropa)

lis = [42, 52, 1488, 1961, 42, 1488]
NewLis = set(lis)
print(NewLis)

for i in NewLis :
    print(i)

if len(NewLis) > 2025 :
    print("44")

else :
    print("43")

#Frozenset
#ми не можемо використовувати команди

ropa1 = frozenset(["gf", "gd", 14, "gf", "gd", 14])
print(ropa1)