class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __str__(self):
        return f"{self.name} {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def __add__(self, other):
        return self.salary + other.salary + self.bonus

    def give_task_to_engineer(self, engineer):
        engineer.task = "Do something!"

    def __str__(self):
        return f"{self.name} {self.salary} {self.bonus}"


class Engineer(Employee):
    def __init__(self, name, salary, bonus, task):
        super().__init__(name, salary)
        self.bonus = bonus
        self.task = task

    def __add__(self, other):
        return self.salary + other.salary + self.bonus

    def __str__(self):
        return f"{self.name} {self.salary} {self.bonus} {self.task}"

    def do_task(self):
        print(self.task)


class Salesperson(Employee):
    def __init__(self, name, salary, bonus, sales):
        super().__init__(name, salary)
        self.bonus = bonus
        self.sales = sales

    def __add__(self, other):
        return self.salary + other.salary + self.bonus

    def __str__(self):
        return f"{self.name} {self.salary} {self.bonus} {self.sales}"

    def sell(self):
        self.sales += 1


def main():
    employee = Employee("Ion", 1000)
    print(employee)

    manager = Manager("Gheorghe", 2000, 500)
    print(manager)

    engineer = Engineer("Vasile", 1500, 100, "Do something!")
    print(engineer)

    salesperson = Salesperson("Mihai", 1500, 100, 10)
    print(salesperson)

    print(employee + manager)
    print(manager + engineer)
    print(engineer + salesperson)

    manager.give_task_to_engineer(engineer)
    engineer.do_task()

    salesperson.sell()
    print(salesperson)


main()