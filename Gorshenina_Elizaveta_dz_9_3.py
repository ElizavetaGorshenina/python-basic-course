class Worker:

    def __init__(self, name, surname, position, wage=2000, bonus=1000):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


employee_1 = Position('Maria', 'van Heveren', 'Head of HR Department', wage=2000, bonus=2000)
employee_2 = Position('Jason', 'White', 'Senior Lawyer', wage=2500, bonus=1000)
print(employee_1.name)
print(employee_1.surname)
print(employee_1.position)
print(employee_2.get_full_name())
print(employee_2.get_total_income())
