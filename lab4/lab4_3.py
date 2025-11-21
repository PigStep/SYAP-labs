class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки "


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return super().draw() + "ручкой"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return super().draw() + "карандашом"


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return super().draw() + "маркером"


pen = Pen("Мой")
pencil = Pencil("Мой")
handle = Handle("Мой")
print(pen.draw())
print(pencil.draw())
print(handle.draw())
