class Horse:
    def __init__(self):
        self.x_distance = 0  # Пройденный путь
        self.sound = 'Frrr'  # Звуки, которые издает лошадь

    def run(self, dx):
        self.x_distance += dx  # Увеличиваем пройденный путь


class Eagle:
    def __init__(self):
        self.y_distance = 0  # Высота полета
        self.sound = 'I train, eat, sleep, and repeat'  # Звук, который издает орел

    def fly(self, dy):
        self.y_distance += dy  # Увеличиваем высоту полета


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()  # Вызов конструктора родительских классов - первого родителя Horse
        Eagle.__init__(self)  # Вызов конструктора класса - второго родителя Eagle

    def move(self, dx, dy):
        self.run(dx)  # метод run
        self.fly(dy)  # метод fly

    def get_pos(self):
        return (self.x_distance, self.y_distance)  # Возвращаем текущее положение

    def voice(self):
        print(self.sound)  # Печатаем звук


# Пример использования
p1 = Pegasus()

print(p1.get_pos())  # (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # (5, 35)

p1.voice()  # "Frrr"
