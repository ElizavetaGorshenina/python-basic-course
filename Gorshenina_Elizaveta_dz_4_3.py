import requests
from decimal import *
from datetime import datetime, date
import datetime


def currency_rates(cur):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.text
    rate = Decimal('1000.000001')
    for el in content.split('<CharCode>'):
        if cur.lower() == el[0:3].lower():
            val = (el.split('<Value>')[1]).split('</Value>')[0]
            nominal = (el.split('<Nominal>')[1]).split('</Nominal>')[0]
            val = Decimal(val.replace(',', '.'))
            nominal = Decimal(nominal)
            rate = (val / nominal).quantize(Decimal('1000.000001'), rounding=ROUND_HALF_EVEN)
            break
        else:
            rate = None
    cur_date = (content.split('Date="')[1]).split('"')[0]
    cur_date = (datetime.datetime.strptime(cur_date, "%d.%m.%Y")).date()
    return rate, cur_date


for currency in 'USD', 'eur':
    rate_now, date_now = currency_rates(currency)
    print(f'Курс {currency.upper()} на дату {date_now} по отношению к RUB: {rate_now}')
