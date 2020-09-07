from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import pandas as pd
import plan_var as V

# get string from exel cell format dd-dd.mm
# and return tuple of two strings
#TODO there is a cells dd/dd.mm
def get_two_dates(string):
    ss = string.split('-')

    if len(ss) == 1:
        ss.append(ss[0])
        d1 = dt.strptime(ss[0],'%d.%m')
        d2 = d1
    else:
        s = ss[0].split('.')
        if len(s) == 2:
            d1 = dt.strptime(ss[0],'%d.%m')
        else:
            d1 = dt.strptime(ss[0],'%d')    

        ss[1] = ss[1].split(' ', 1)[0]
        d2 = dt.strptime(ss[1],'%d.%m')
        if d1.day > d2.day:
            day = d1.day
            d1 = d2 - relativedelta(months=1)
            d1 = d1.replace(day=day)
        else:
            d1 = d1.replace(month=d2.month)
    
    d1 = d1.replace(year = dt.today().year)
    d2 = d2.replace(year = dt.today().year)

    if d1.month > d2.month:
        d2 = d2.replace(year = d2.year+1)


    return [d1,d2]

# delete rows if it is not about zz
def delete_rows(df):
    dropIndexes = list()
    for i in df.index.values.tolist():
        if type(i) != int:
            dropIndexes.append(i)
    
    return df.drop(dropIndexes)

# reformat dataframe for visualisation and working
def reformat_dataframe(row):
    
    i = 0
    while type(row[i]) != dt:     
        row = row.append(get_two_coulums(row,i))
        i += 1
    
    return row

# get cell and return two Series coulum with Start and Finish datetime dates
def get_two_coulums(row, ind):
    s = pd.Series()

    if is_date(row[ind]):
        s = pd.Series(get_two_dates(row[ind]))
    else:
        s = pd.Series([row[ind], row[ind]])
    s = s.rename({0: V.ColumnNames[ind*2], 1 : V.ColumnNames[ind*2+1]})
    
    return s


# checks if cell is date or not
def is_date(cell):
    if (cell == 'нет') | (cell == 'готов'):
        return False
    return True




    