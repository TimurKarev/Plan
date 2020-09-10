from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import pandas as pd
import plan_var as V

# get string from exel cell format dd-dd.mm
# and return tuple of two strings
#TODO there is a cells dd/dd.mm
def get_two_dates(string):
    print(string)
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
        if i in V.DoubleCoulums:
            row = row.append(get_four_coulums(row,i))
        else:
            row = row.append(get_two_coulums(row,i))
        i += 1
    
    row = row.append(pd.Series([row[i], row[i+1]], V.ColumnNames[-2:]))
    
    return row

#get cell and return four Series coulum with Start and Finish datatime dates
def get_four_coulums(row,ind):
    s = pd.Series()
    s = s.append(get_two_coulums(row, ind=ind, dic=True, dict_index=0))
    s = s.append(get_two_coulums(row, ind=ind, dic=True, dict_index=2))
    return s


# get cell and return two Series coulum with Start and Finish datetime dates
def get_two_coulums(row, ind = 0, dic = False, dict_index = 0):
    s = pd.Series()
    string = ' '

    if not dic:
        string = row[ind]
    else:
        if '/' in row[ind]:
            ss = row[ind].split('/')
            string = ss[int(dict_index/2)]
            print(string)
        else:
            string = row[ind]

    if is_date(string):
        s = pd.Series(get_two_dates(string))
    else:
        s = pd.Series([string, string])

    if not dic:
        s = s.rename({0: V.ColumnNames[ind*2], 1 : V.ColumnNames[ind*2+1]})
    else:
        s = s.rename({0: V.DoubleCoulums[ind][dict_index], 1 : V.DoubleCoulums[ind][dict_index+1]})
    
    return s


# checks if cell is date or not
def is_date(cell):
    if (cell == 'нет') | (cell == 'готов'):
        return False
    return True




    