from datetime import date, datetime, timedelta

from pathlib import Path

print(Path(__file__).resolve().parent)


d = date(2020, 7, 3)

dt = datetime(2020, 7, 3, 00, 1, 2, 45)

d_today = date.today()

dt_today = datetime.today()

delta = timedelta(days=5)

date_final = d_today - delta

date_str = d.strftime("%a %d %b %Y")

dictionnaire = {'CAD': [1.5476, 168], 'CHF': [1.0819, 78], 'USD': [1.183, 40]}

if __name__ == '__main__':
    for key, value in dictionnaire.items():
        print(key, value)