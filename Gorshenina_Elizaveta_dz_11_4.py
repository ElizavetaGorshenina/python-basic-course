class OfficeEquipmentStorage:

    EQUIPMENT_LIST = ['printer', 'scanner', 'copier']


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
print(copier_1.name)
print(copier_1.facility)
print(copier_1.condition)
print(copier_1.department)
storage_1 = OfficeEquipmentStorage()
print(storage_1.EQUIPMENT_LIST)
