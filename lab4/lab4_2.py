class Employee:
    def __init__(self, fio, stazh, hourly_wage, hours_worked):
        self.fio = fio
        self.stazh = stazh
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
        self.salary = self.calculate_salary()
        self.bonus = self.calculate_bonus()

    def calculate_salary(self):
        return self.hourly_wage * self.hours_worked

    def calculate_bonus(self):
        if self.stazh < 1:
            rate = 0.01
        elif self.stazh < 3:
            rate = 0.05
        elif self.stazh < 5:
            rate = 0.08
        else:
            rate = 0.15
        return self.salary * rate

    def __str__(self):
        return (
            "======================\n"
            f"ФИО: {self.fio}\n"
            f"Стаж: {self.stazh} года(ов)\n"
            f"Часовая ставка: {self.hourly_wage}\n"
            f"Отработанные часы: {self.hours_worked}\n"
            f"Заработная плата: {self.salary:.2f}\n"
            f"Премия: {self.bonus:.2f}\n"
            "======================\n"
        )


employees = []
num = int(input("Введите количество сотрудников: "))
for i in range(num):
    print(f"\nСотрудник {i+1}:")
    fio = input("ФИО: ")
    stazh = int(input("Стаж (года): "))
    hourly_wage = float(input("Часовая ставка: "))
    hours_worked = float(input("Отработанные часы: "))
    emp = Employee(fio, stazh, hourly_wage, hours_worked)
    employees.append(emp)

# Print all employees
for emp in employees:
    print(emp)
