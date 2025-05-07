#спадкування
#поліморфізм
#інкапсуляція

class build:
    year = None
    city = None

    def __init__(self, year, city):
        self.year =  year
        self.city = city


    def get_info(self):
        print("year: ", self.year, ". city:", self.city)


class school(build):
    pupils = None

    def __init__(self, year, city, pupils=507):
        super(school, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super().get_info()
        print("pupils: ", self.pupils)


class house(build):
    pass


class shop(build):
    pass


school = school(1990, "kharkov")
school.get_info()
house =  house(2010, "svetlik")
house.get_info()
shop =  shop(2022, "new york")