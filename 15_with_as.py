try:
     with open("data/sql.py", "r") as file :
         print(file.read())
except FileNotFoundError :
    print("файл не знайдено")