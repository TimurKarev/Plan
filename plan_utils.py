from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import pandas as pd

# get string from exel cell format dd-dd.mm
# and return tuple of two strings
def get_two_dates(string):
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

# reformat dataframe for visualisation and working
def reformat_dataframe(row):
       
    
    return pd.Series([1, 2], index=['foo', 'bar'])




    