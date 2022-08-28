class OfficeEquipmentStorage:

    EQUIPMENT_LIST = ['printer', 'scanner', 'copier']

    def __init__(self):
        self.available_equipment = {}
        self.equipment_in_use = {}

    def accept(self, name, quantity):
        if OfficeEquipmentStorage.data_validation(name, quantity) == 'valid':
            if name.lower() in self.available_equipment.keys():
                self.available_equipment[name.lower()] += quantity
            else:
                self.available_equipment.update({name.lower(): quantity})

    def handover(self, name=None, quantity=None, department=None, items=[]):
        if OfficeEquipmentStorage.data_validation(name, quantity, dept_check=department, items_check=items) == 'valid':
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

    @staticmethod
    def data_validation(name_check, q_check, dept_check=None, items_check=[]):
        validation_flag = 'valid'
        if name_check.lower() not in OfficeEquipmentStorage.EQUIPMENT_LIST:
            print('The equipment is unknown. Please extend the equipment list')
            validation_flag = 'invalid'
        if not isinstance(q_check, int):
            print('The quantity value is of the wrong type. Please check the number of items')
            validation_flag = 'invalid'
        if isinstance(q_check, int) and q_check <= 0:
            print('The quantity value is of the wrong value. Please check the number of items')
            validation_flag = 'invalid'
        if dept_check is not None and not isinstance(dept_check, str):
            print('The department name is of the wrong type. Please check the name of the department')
            validation_flag = 'invalid'
        if len(items_check) != 0:
            for item_check in items_check:
                if item_check.__class__ not in ['Scanner', 'Printer', 'Copier']:
                    print('The items are not proper. Please check the items list')
                    validation_flag += 'invalid'
        return validation_flag


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
storage_1.accept('Scanner', -3)
storage_1.accept('Scanner', '3')
storage_1.handover(name='shredder', quantity=5, department='Audit')
storage_1.handover(name='printer', quantity='5', department='Audit')
scanner_1 = OfficeEquipment()
storage_1.handover(name='scanner', quantity=4, department='Audit', items=[scanner_1])
