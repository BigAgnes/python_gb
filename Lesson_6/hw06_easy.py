
#Задача-1: Написать класс, например, Worker, который должен содержать информацию
#о работнике (ФИО, оклад, надбавка за напряженность).
#Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
#оклад и надбавки). Оклад и надбавку передать в виде строки.
#На основе строки создать атрибут income, который реализовать в виде словаря
#и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
#Применить к экземпляру
#класса метод __dict__ и проверить какой будет результат применения этого метода.
#А комментариях к заданию написать тип результата на русском языке.


class Worker():
    def __init__(self, name, surname, position, salary, allowance):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"salary:" : salary,
        "allowance:" : allowance}
    def get_full_name(self):
        return self.surname + ' ' + self.name

work = Worker("Петр", "Алексеев", "Водитель", 20000, 2000)
work.get_full_name()
print(work.get_full_name(), work._income)
print(work.__dict__)

#В результате применения метода __dict__, образовался словарь. Он содержит
#пары: название и значение всех атрибутов класса.



#Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
#Position (реализовать наследование). Добавить классу уникальный атрибут -
#% премии к зарплате (от суммы оклада).
#Создать метод расчета зарплаты с учетом только премии.
#Реализовать обращение к этому атриубуту, как к свойству.
#Проверить работу всей структуры на реальных данных, вывести результаты.

class Position(Worker):
    def __init__(self, name, surname, position, salary, allowance, bonus):
        Worker.__init__(self, name, surname, position, salary, allowance)
        self.bonus = bonus
    @property
    def salarys_bonus(self):
        salary_bonus = (self._income["salary:"]*self.bonus)/100 + self._income["salary:"]
        return salary_bonus

working = Position("Альберт", "Грибов", "Повар", 30000, 3000, 20)
print(working.salarys_bonus)


#Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
#использования знака + в методах 1) вывода полного имени работника и возраста
#2) вычисления общего дохода работника с учетом надбавки .
#Проверить работу всей структуры на реальных данных, вывести результаты.

class Position(Worker):
    def __init__(self, name, surname, position, age, salary, allowance, bonus):
        Worker.__init__(self, name, surname, position, salary, allowance)
        self.allowance = allowance
        self.bonus = bonus
        self.age = age
    @property
    def salarys_bonus(self):
        salary_bonus = (self._income["salary:"]*self.bonus)/100 + self._income["salary:"]
        return salary_bonus
    @property
    def get_full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.age
    @property
    def get_full_salarys(self):
        full_salarys = self.allowance + self.salarys_bonus
        return full_salarys


positions = Position("Олег", "Пупкин", "Садовник", "30", 30000, 3000, 20)
print(positions.get_full_name)
print(positions.get_full_salarys)
