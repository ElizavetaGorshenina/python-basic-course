import sys
import Gorshenina_Elizaveta_dz_4_5_utils

rate_now, date_now = Gorshenina_Elizaveta_dz_4_5_utils.currency_rates(sys.argv[1])
print(f'Курс {sys.argv[1].upper()} на дату {date_now} по отношению к RUB: {rate_now}')
