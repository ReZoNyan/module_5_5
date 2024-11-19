class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        for i in args:
            if isinstance(i, str):
                cls.houses_history.append(i)
        cls.args = args
        return super().__new__(cls)

    def __init__(self, name, number_or_floors):
        self.name = name
        self.number_of_floors = number_or_floors

    def __del__(self):
        print(f'{self.name} снесен, но навсегда останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
