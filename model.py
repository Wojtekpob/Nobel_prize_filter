class Laureat:
    def __init__(self, name, surname, born, died, born_country, born_city, gender, prizes):
        self.name = name
        self.surname = surname
        self.born = born
        self.died = died
        self.born_country = born_country
        self.born_city = born_city
        self.gender = gender
        self.prizes = prizes


class Prize:
    def __init__(self, year, category, motivation):
        self.year = year
        self.category = category
        self.motivation = motivation
