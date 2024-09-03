class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)


class Car:
    def __init__(self, model, vin, numbers):

        self.model = model
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.__vin = vin
            self.__numbers = numbers
            print(f'{self.model} успешно создан')
        else:
            pass

    def __is_valid_vin(self, vin_number):
        try:
            if isinstance(vin_number, float):
                raise IncorrectVinNumber('Некорректный тип vin номерa')
            if not 1000000 <= vin_number <= 9999999:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        except IncorrectVinNumber:
            pass
        else:
            return True


    def __is_valid_numbers(self, numbers):
        try:
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
        except IncorrectCarNumbers:
            pass
        else:
            return True


car1 = Car('Mod1', 5555555, 'r222op')
car2 = Car('Mod2', 3333, 'r222op')
car3 = Car('Mod3', 5555555.7, 'r222op')
car4 = Car('Mod4', 5555555, 'r222op5')
car5 = Car('Mod5', 5555555, 77)
car6 = Car('Mod6', 1234567, 'q999iu')

