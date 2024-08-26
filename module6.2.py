class Vehicle:
    __COLOR_VARIANTS = ["white", "black", "blue", "green", "yellow"]

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__color = color.lower()
        self.__engine_power = engine_power


    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"мощность: {self.__engine_power}"

    def get_color(self):
        return f"Цвет модели: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        new_color = new_color.lower()
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color.upper()
        else:
            print(f'Невозможно покрасить в {new_color.capitalize()}')



class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)



vehicle1 = Sedan('TIKHON', 'Toyota Mark II', 'blue', "500")


vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'ANDREY'


vehicle1.print_info()