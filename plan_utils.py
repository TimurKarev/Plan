from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import pandas as pd

# get string from exel cell format dd-dd.mm
# and return tuple of two strings
def get_two_dates(string):
    ss = string.split('-')

    if len(ss) == 1:
        ss.append(ss[0])
        d1 = dt.strptime(ss[0],'%d.%m')
    else:
        d1 = dt.strptime(ss[0],'%d')

    d2 = dt.strptime(ss[1],'%d.%m')

    d1 = d1.replace(month = d2.month)
    
    if d1.day > d2.day:
        d1 = d1 - relativedelta(months=1)
    
    d1 = d1.replace(year = dt.today().year)
    d2 = d2.replace(year = dt.today().year)

    if d1.month > d2.month:
        d2 = d2.replace(year = d2.year+1)


    return [d1,d2]

def delete_rows(df):
    dropIndexes = list()
    for i in df.index.values.tolist():
        if type(i) != int:
            dropIndexes.append(i)
    
    return df.drop(dropIndexes)

# reformat dataframe for visualisation and working
def reformat_dataframe(row):
    s = pd.Series()#[row[0], row[0]], index=['StartBuildingBot', 'StartBuildingBot'])
    
    if is_date(row[0]):
        s = s.append(pd.Series(get_two_dates(row[0]), index=['j','k']))
    else:
        s = s.append(pd.Series([row[0], row[0]], index=['j','k']))
    
    return row.append(s)


def is_date(cell):
    if (cell == 'нет') | (cell == 'готов'):
        return False
    return True




    