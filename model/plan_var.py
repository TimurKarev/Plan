Zakaz_intervals = (25,0)
Fig_hight = 600

Not_date = ['None', 'unknown', 'word']

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

DoubleCoulums = {7 : ['StShinaUvr', 'FnShinaUvr', 'StShinaTr', 'FnShinaTr'],
                 12: ['StInst04', 'FnInst04', 'StInst10', 'FnInst10']}

# create list of final colum names from list and dict where dict indexes must be skiped from list
# def get_FinalFinalColumnNames():
#   rl = list()
#   l = ColumnNames
#   d = DoubleCoulums

#   k = 0
#   i = 0
#   while i < len(l):
#     if (i == 14) | (i == 24):
#       for j in d[list(d.keys())[k]]:
#         rl.append(j)
#       i+=2
#       k+=1
#     else:
#       rl.append(l[i])
#       i+=1
  
#   return rl

  #FinalColumnNames = get_FinalFinalColumnNames(ColumnNames, DoubleCoulums)