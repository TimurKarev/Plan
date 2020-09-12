Not_date = ['None', 'unknown', 'word']

# ColumnNames = [ 'StBuildBot', 'FnBuildBot',
#                 'StBuildTop', 'FnBuildTop',
#                 'StMetBot', 'FnMetBot',
#                 'StMetTop', 'FnMetTop',
#                 'StEmu', 'FnEmu',
#                 'StShit', 'FnShit',
#                 'StSn', 'FnSn',
#                 'StShina', 'FnShina',
#                 'St04', 'Fn04',
#                 'StSec04', 'FnSec04',
#                 'St10', 'Fn10',
#                 'StSec10', 'FnSec10',
#                 'StInst', 'FnInst',
#                 'StRm', 'FnRm',
#                 'StMain', 'FnMain',
#                 'StCompl', 'FnCompl',
#                 'Fin', 'NewFin',
#               ]

DoubleCoulums = {7 : ['StShinaUvr', 'FnShinaUvr', 'StShinaTr', 'FnShinaTr'],
                 12: ['StInst04', 'FnInst04', 'StInst10', 'FnInst10']}

# create list of final colum names from list and dict where dict indexes must be skiped from list
def get_FinalFinalColumnNames():
  rl = list()
  l = ColumnNames
  d = DoubleCoulums

  k = 0
  i = 0
  while i < len(l):
    if (i == 14) | (i == 24):
      for j in d[list(d.keys())[k]]:
        rl.append(j)
      i+=2
      k+=1
    else:
      rl.append(l[i])
      i+=1
  
  return rl

  #FinalColumnNames = get_FinalFinalColumnNames(ColumnNames, DoubleCoulums)