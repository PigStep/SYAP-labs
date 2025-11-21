class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def greet(self):
        print(f"Привет! Меня зовут {self.name}, мне {self.age} лет.")

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def get_total_instances(cls):
        return cls.count


# Демонстрация работы
p1 = Person("Алексей", 20)
p2 = Person("Мария", 17)

p1.greet()
p2.greet()

print("Алексей взрослый?", Person.is_adult(p1.age))
print("Мария взрослая?", Person.is_adult(p2.age))
print("Всего объектов Person:", Person.get_total_instances())
