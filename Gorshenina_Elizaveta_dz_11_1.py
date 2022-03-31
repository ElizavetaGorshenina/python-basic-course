class Date:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def extract_date(cls, date_str):
        return [int(_) for _ in date_str.split('-')]

    @staticmethod
    def date_validation(date_int_list):
        the_day, the_month, the_year = date_int_list
        if str(the_year).isdigit() and 1900 <= the_year <= 2100:
            if the_month in [1, 3, 5, 7, 8, 10, 12] and the_day in range(32)[1:]:
                res = 'The date is valid'
            elif the_month in [4, 6, 9, 11] and the_day in range(31)[1:]:
                res = 'The date is valid'
            elif the_month == 2 and the_year % 4 != 0 and the_day in range(29)[1:]:
                res = 'The date is valid'
            elif the_month == 2 and the_year % 4 == 0 and the_day in range(30)[1:]:
                res = 'The date is valid'
            else:
                res = 'The date is invalid'
        else:
            res = 'The date is invalid'
        return res


print(Date.extract_date('29-03-2022'))
date_1 = Date('29-03-2022')
print(Date.extract_date(date_1.date_str))
print(Date.date_validation(Date.extract_date(date_1.date_str)))
print(Date.date_validation(Date.extract_date('29-02-2022')))
