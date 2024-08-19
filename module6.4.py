class Figure:
    SILENT_MODE = True

    def __init__(self, sides_count, rgb_tuple, *sides):
        if not Figure.SILENT_MODE:
            print(f'Figure.__init__: Длина списка сторон на входе {len(sides)}')
            print(f'Figure.__init__: Список сторон на входе = {sides}')
        self.sides_count = sides_count
        self.__sides = [1 for _ in range(sides_count)]
        self.set_sides(*sides)
        self.__color = (0, 0, 0)
        r, g, b = rgb_tuple
        self.set_color(r, g, b)
        self.filled = True
        if not Figure.SILENT_MODE:
            print(f'Figure.__init__: Финальная длина списка сторон {len(self.__sides)}')
            print(f'Figure.__init__: Финальный список сторон = {self.__sides}')

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for c in [r, g, b]:
            if type(c) != int:
                if not Figure.SILENT_MODE:
                    print('__is_valid_color: ошибка типа одного из каналов цвета')
                return False
            if c < 0 or c > 255:
                if not Figure.SILENT_MODE:
                    print('__is_valid_color: ошибка значения цветового канала')
                return False

        return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        elif not Figure.SILENT_MODE:
            print(f'Figure: Цвет ({r}, {g}, {b}) не может быть установлен.')

    def __is_valid_sides(self, *sides_int_list):
        if len(sides_int_list) != self.sides_count:
            if not Figure.SILENT_MODE:
                print(f'__is_valid_sides: Длина списка сторон {len(sides_int_list)} и количество сторон {self.sides_count} фигуры не равны.')
                print(f'__is_valid_sides: Список сторон на входе функции = {sides_int_list}')
            return False
        for side in sides_int_list:
            if isinstance(side, int):
                if side < 0:
                    return False
            else:
                return False

        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perimetr = 0
        for side in self.__sides:
            perimetr += side
        return perimetr

    def set_sides(self, *new_sides):
        if not Figure.SILENT_MODE:
            print(f'set_sides: Длина списка сторон на входе {len(new_sides)}')
            print(f'set_sides: Список сторон на входе = {new_sides}')
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __str__(self):
        info = f'\nFigure:\n - sides_count = {self.sides_count}'
        info += f'\n - sides = {self.__sides}\n - color = {self.__color}\n - filled = {self.filled}'
        info += f'\n - P = len() = {len(self)}'
        return info


class Circle(Figure):

    PI_CONST = 3.141592653589793

    def __init__(self, rgb_tuple, *sides):
        super().__init__(1, rgb_tuple, *sides)
        self.__radius = self.get_radius()

    def get_radius(self):
        R = len(self) / (2.0 * Circle.PI_CONST)

        self.__radius = R
        return R

    def get_square(self):
        return Circle.PI_CONST * self.__radius ** 2

    def __str__(self):
        info = super().__str__()
        info += f'\n   Circle:'
        info += f'\n    - radius = {self.get_radius()}'
        info += f'\n    - area = {self.get_square()}'
        return info

class Triangle(Figure):

    def __init__(self, rgb_tuple, *sides):
        super().__init__(3, rgb_tuple, *sides)
        self.__height = self.get_heights()

    def get_square(self):

        half_P = 0.5 * len(self)
        p = half_P
        for side in self.get_sides():
            p *= (half_P - side)
        return p ** 0.5

    def get_heights(self):

        area = self.get_square()
        heights = []
        for side in self.get_sides():
            heights.append(2 * area / side)

        self.__height = heights
        return heights

    def __str__(self):
        info = super().__str__()
        info += f'\n   Triangle:'
        info += f'\n    - heights = {self.get_heights()}'
        info += f'\n    - area = {self.get_square()}'
        return info

class Cube(Figure):


    SILENT_MODE = True

    def __init__(self, rgb_tuple, *one_side):
        if len(one_side) == 1:
            value = one_side[0]
        else:
            value = 1
        self.__sides = [value for _ in range(12)]
        if not Cube.SILENT_MODE:
            print(f'Cube: len(one_side) = {len(one_side)}, one_side[0] = {one_side[0]}')
            print(f'Cube: self.__sides = {self.__sides}')
        super().__init__(12, rgb_tuple, *self.__sides)

    def get_volume(self):
        return self.__sides[0] ** 3



def geometry_test():
    print('Geometry test:')
    rectangle = Figure(4, (255, 255, 255), 5, 7, 5, 7)
    print(len(rectangle))
    print(rectangle)

    circle = Circle((127, 127, 127), 1000)
    print(circle)

    triangle = Triangle((64, 64, 64), 3, 4, 5)
    print(triangle)

def main():
    print('\nКод для проверки:')
    circle1 = Circle((200, 200, 100), 10)
    cube1 = Cube((222, 35, 130), 6)


    circle1.set_color(55, 66, 77)
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)
    print(cube1.get_color())


    cube1.set_sides(5, 3, 12, 4, 5)
    print(cube1.get_sides())
    circle1.set_sides(15)
    print(circle1.get_sides())


    print(len(circle1))


    print(cube1.get_volume())

if __name__ == '__main__':
    geometry_test()
    main()

'''
Выходные данные (консоль):
[55, 66, 77]
[222, 35, 130]
[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
[15]
15
216'''