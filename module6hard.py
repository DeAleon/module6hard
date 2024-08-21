class Figure:
    sides_count = 0

    def __init__(self, rgb, len_, filled=False):
        self.__sides = len_
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]
        self.__color = (self.r, self.g, self.b)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                self.__color = (r, g, b)
                self.filled = True

    def set_color(self, r, g, b):
        Figure.__is_valid_color(self, r, g, b)

    def __is_valid_sides(self, sides):
        for i in sides:
            if i % 1 != 0 or i < 1:
                return False
        return True

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides) and len(self.__sides) == self.sides_count:
            self.__sides = sides

    def get_sides(self):
        if len(self.__sides) == 1:
            return [*self.__sides] * self.sides_count


class Circle(Figure):
    sides_count = 1

    def __init__(self, rgb, *len_, filled=True):
        super().__init__(rgb, len_, filled)
        if len(len_) != self.sides_count:
            self.__sides = 1
        self.__radius = len_[0] / (2 * 3.14)

    def get_square(self):
        square = (self.__radius ** 2) * 3.14
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, rgb, *len_, filled=True):
        super().__init__(rgb, len_, filled)
        if len(len_) != self.sides_count and len(len_) != 1:
            self.len_ = [1] * self.sides_count
        elif len(len_) == 1:
            self.len_ = [*len_] * self.sides_count
        else:
            self.len_ = [*len_]
        self.s = (sum(self.len_) / 2)

    def get_square(self):
        square = (self.s * (self.s - self.len_[0]) * (self.s - self.len_[1]) * (self.s - self.len_[2])) ** 0.5
        return round(square, 2)


class Cube(Figure):
    sides_count = 12

    def __init__(self, rgb, *len_, filled=True):
        super().__init__(rgb, len_, filled)
        if len(len_) != self.sides_count and len(len_) != 1:
            self.len_ = [1] * self.sides_count
        elif len(len_) == 1:
            self.len_ = [*len_] * self.sides_count
        else:
            self.len_ = [*len_]

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Дополнительная проверка
triangle1 = Triangle((222, 35, 130), 8)
triangle1.set_color(200, 70, 75)  # Не изменится
print(triangle1.get_color())
print(triangle1.get_square())
print(len(triangle1))
print(len(cube1))
