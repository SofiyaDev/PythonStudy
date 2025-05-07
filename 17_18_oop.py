class Dog:
    name = None
    age = None
    Birthday = None
    isHappy = None

    def __init__(self, name = "dopa", age = 77, Birthday = "13.07.3465", isHappy = True):
         self.set_data(name, age, Birthday, isHappy)
         self.get_data()

    def set_data(self, name, age, Birthday, isHappy = True):
        self.name = name
        self.age = age
        self.Birthday = Birthday
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, "Birthday:", self.Birthday, ". Happy", self.isHappy)


dog1 = Dog("bobby", 6, True)
dog1.set_data("alex", 22, 45)
dog2 = Dog("slavik", 2, "02 03 2023", False)
