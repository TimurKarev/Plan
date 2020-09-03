from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

def get_two_dates(string, cur_year = 2020):
    ss = string.split('-')
    d1 = dt.strptime(ss[0],'%d')
    d2 = dt.strptime(ss[1],'%d.%m')

    d1 = d1.replace(month = d2.month)
    
    if d1.day > d2.day:
        d1 = d1 - relativedelta(months=1)
    
    d1 = d1.replace(year = dt.today().year)

    if d1.month > d2.month:
        d2 = d2.replace(year = d1.year+1)


    return (d1,d2)