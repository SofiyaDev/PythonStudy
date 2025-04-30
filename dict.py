chelovek = {"name" : "sofia", "age" : 15, "mama" : 33}
print(chelovek.get("name"))

#print(chelovek.items()) #виводить все так як написано
chelovek.popitem() #видаляє останній елемент
chelovek.pop("name") #видаляє окремий елемент

for i, s in chelovek.items():
    print(i, s, sep=" - ")

for d in chelovek.keys(): # лише ключи
    print(d)

print("\n")

for g in chelovek.values(): # виключно значення
    print(g)

dops = {"papa" : 42, "mama" : 33}
dops["bio"] = "rop" #додає новий елемент
print(dops.get("papa")) #виводить якесь окреме значення

for i, p in dops.items():
    print(i, p, sep=" - ")

player = {
    "player_1" : {
        "name" : "roma",
        "age" : 42,
        "country" : ("France", "paris", 345),
        "sports" : {"voleyball" : "four years", "football" : "five years"}
    },
    "player_2" : {
        "name" : "uliana",
        "age" : 22,
        "country" : ("Britan", "London"),
        "grades" : {"english" : 4, "math" : 3}
    }
}
print(player)