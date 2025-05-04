#data = input("Hobby: ")

file = open("data/my.file.text", "r")

#print(file.read())
#file.write(data + "\n")
#file.write("\n\n\n")
#file.write("!!!")

for line in file:
    print(line)

file.close()

# w - відкривається лише існуючий файл
# + - якщо такого файлу немає, він стрворюється автоматично
# a - кожен раз додається новий текст
# r - читання файлу