import pandas as pd
import plan_utils as pu
import plan_var as V
from datetime import datetime as dt
from datetime import timedelta
from dateutil.relativedelta import relativedelta

ColumnNames = [
    'Заливка_НМ_Нач', 'Заливка_НМ_Кон',
    'Заливка_ВМ_Нач', 'Заливка_ВМ_Кон',
    'Навеска_НМ_Нач', 'Навеска_НМ_Кон',
    'Навеска_ВМ_Нач', 'Навеска_ВМ_Кон',
    'ЭМУ_Нач',        'ЭМУ_Кон',
    'СборкаЩитов_Нач','СборкаЩитов_Кон',
    'Монтаж_СН_Нач',  'Монтаж_СН_Кон',
    'ШинаУВР_Нач',    'ШинаУВР_Кон',
    'Шина_ТР_Нач',    'Шина_ТР_Кон',
    'СборкаНН_Нач',   'СборкаНН_Кон',
    'ВторНН_Нач',     'ВторНН_Кон',
    'СборкаВВ_Нач',   'СборкаВВ_Кон',
    'ВторВВ_Нач',     'ВторВВ_Кон',
    'УсткаНН_Нач',    'УсткаНН_Кон',
    'УсткаВВ_Нач',    'УсткаВВ_Кон',
    'УсткаRM_Нач',    'УсткаRM_Кон',
    'Наладка_Нач',    'Наладка_Кон',
    'Комплект_Нач',   'Комплект_Кон',
    'ОТГРУЗКА_Зап',   'ОТГРУЗКА_Нов']


def get_dates_from_tuple(tup, year=2020):

    d = list()

    fr, st = tup
    
    if fr in V.Not_date:
        return st

    if fr == 'dd-dd.mm':
        d.append(dt.strptime(st[0]+'.'+st[2], '%d.%m'))
        d.append(dt.strptime(st[1]+'.'+st[2], '%d.%m'))
        if d[0].day > d[1].day:
            d[0] = d[0] - relativedelta(months=1)


    if fr == 'dd.mm-dd.mm':
        d.append(dt.strptime(st[0]+'.'+st[1], '%d.%m'))
        d.append(dt.strptime(st[2]+'.'+st[3], '%d.%m'))

    if fr == 'dd.mm/dd.mm':
        d.append(dt.strptime(st[0]+'.'+st[1], '%d.%m'))
        d.append(dt.strptime(st[2]+'.'+st[3], '%d.%m'))

    if fr == 'dd/dd.mm':
        d.append(dt.strptime(st[0]+'.'+st[2], '%d.%m'))
        d.append(dt.strptime(st[1]+'.'+st[2], '%d.%m'))
        #if d[0].day > d[1].day:
            #d[0] = d[0] - relativedelta(months=1)
        #print(d, len(d), st)

    if fr == 'dd.mm':
        d.append(dt.strptime(st[0]+'.'+st[1], '%d.%m'))
    
    #TODO create wright year calculation
    for i in range(len(d)):
        d[i] = d[i].replace(year=year)

    return d


class PlanReformatter:
    
    def __init__(self, dataframe, magic_rows=[7,12]):
        self.df = dataframe
        self.magic_rows = magic_rows
        self.r_df = self.df.apply(lambda row: self.get_series_with_dates(row), axis=1)

    def get_series_with_dates(self, row):

        l = []
        for i in range(len(row)-2):
            t = pu.get_cell_format(row[i])
            try:
                d = get_dates_from_tuple(t, row[-2].year)
            except ValueError:
                print("В зз {} столбец {} имеет неверное значение".format(row.name, row.index[i]))
            
            if i in self.magic_rows:
                if len(d) == 1:
                    l.extend([d[0],d[0],d[0],d[0]])
                if len(d) == 2:
                    l.extend([d[0],d[0],d[1],d[1]])
                if len(d) == 4:
                    l.extend(d)
            else:
                if len(d) == 1:
                    l.extend([d[0], d[0]])
                if len(d) == 2:
                    l.extend(d)

        ser = pd.Series(l)
        
        l = [i for i in range(len(ColumnNames))]
        dic = dict(zip(l, ColumnNames))

        ser = ser.rename(dic)
        return ser.append(pd.Series(row[-2:]))

    def get_df_for_gantt(self, num=10):
        self.gant_df = pd.DataFrame()
        dd = self.r_df.iloc[num*-1:]
        for ser in dd.iloc:
            i = 0
            while i < len(ser) - 2:
                if type(ser[i]) == dt:
                    self.gant_df = self.gant_df.append(pd.DataFrame([dict(Task=ser.index[i][:-4],
                                                        Start=ser[i] + timedelta(hours=8, minutes=20),
                                                        Finish=ser[i+1] + timedelta(hours=16, minutes=20),
                                                        zakaz=str(ser.name) if type(ser.name)==int else str(ser.name[:4]))]), ignore_index=True)
                    i+=1
                i+=1
        return self.gant_df

    def get_column_names(self, reverse=False):
        i=0
        l = []
        while i < len(ColumnNames)-2:
            l.append(ColumnNames[i][:-4])
            i+=2
        if reverse:
            l = l[::-1]
        return l