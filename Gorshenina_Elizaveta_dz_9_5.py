class Stationery:
    title = 'Письменная принадлежность'

    @staticmethod
    def draw():
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Ручка'

    @staticmethod
    def draw():
        print('Запуск записи информации')


class Pencil(Stationery):
    title = 'Карандаш'

    @staticmethod
    def draw():
        print('Запуск создания рисунка')


class Handle(Stationery):
    title = 'Маркер'

    @staticmethod
    def draw():
        print('Запуск выделения текста')


stationery = Stationery()
print(stationery.title)
stationery.draw()
pen = Pen()
print(pen.title)
pen.draw()
pencil = Pencil()
print(pencil.title)
pencil.draw()
handle = Handle()
print(handle.title)
handle.draw()
