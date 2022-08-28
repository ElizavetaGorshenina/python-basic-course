class OfficeEquipmentStorage:

    EQUIPMENT_LIST = ['printer', 'scanner', 'copier']

    def __init__(self):
        self.available_equipment = {}
        self.equipment_in_use = {}

    def accept(self, name, quantity):
        if name.lower() in self.available_equipment.keys():
            self.available_equipment[name.lower()] += quantity
        else:
            self.available_equipment.update({name.lower(): quantity})

    def handover(self, name=None, quantity=None, department=None, items=[]):
        if self.available_equipment[name.lower()] >= quantity:
            self.available_equipment[name.lower()] -= quantity
            if name.lower() in self.equipment_in_use.keys():
                self.equipment_in_use[name.lower()]['quantity'] += quantity
                self.equipment_in_use[name.lower()]['departments'].extend([(quantity, department)])
            else:
                self.equipment_in_use.update({name.lower(): {'quantity': quantity, 'departments': [(quantity, department)]}})
            for item in items:
                item.condition = 'in use'
                item.department = department
        else:
            print('The required quantity is not available')


class OfficeEquipment:

    condition = 'new'
    department = 'none'


class Printer(OfficeEquipment):

    name = 'printer'
    facility = 'print'


class Scanner(OfficeEquipment):

    name = 'scanner'
    facility = 'scan'


class Copier(OfficeEquipment):

    name = 'copier'
    facility = 'copy'


copier_1 = Copier()
print(copier_1.condition)
print(copier_1.facility)
storage_1 = OfficeEquipmentStorage()
storage_1.accept('Printer', 10)
print(storage_1.available_equipment)
storage_1.accept('Copier', 5)
print(storage_1.available_equipment)
print(storage_1.equipment_in_use)
storage_1.handover(name='Copier', quantity=3, department='Backoffice', items=[copier_1])
print(storage_1.available_equipment)
print(storage_1.equipment_in_use)
print(copier_1.name)
print(copier_1.department)
print(copier_1.condition)
copier_2 = Copier()
copier_3 = Copier()
storage_1.handover(name='copier', quantity=2, department='International Law', items=[copier_2, copier_3])
print(storage_1.equipment_in_use)
storage_1.accept('Copier', 10)
storage_1.accept('Scanner', 12)
storage_1.handover(name='Scanner', quantity=2, department='Backoffice')
storage_1.handover(name='copier', quantity=4, department='Russian Law')
print(storage_1.available_equipment)
print(storage_1.equipment_in_use)
scanner_1 = Scanner()
storage_1.handover(name='Scanner', quantity=1, department='Russian Law', items=[scanner_1])
print(storage_1.available_equipment)
print(storage_1.equipment_in_use)
print(scanner_1.name)
print(scanner_1.department)
print(scanner_1.condition)
