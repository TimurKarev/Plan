import pandas as pd
import pyparsing as pp


class PlanLoader:
    df = pd.DataFrame()

    def __init__(self, exel_name, key_word = '№ з/з', header = None):
        
        self.key_word = key_word

        self.df = pd.read_excel(exel_name, sheet_name='2020')
        self.key_word = key_word
        self.create_indexes()
        self.create_columns()
        self.delete_rows()
        
        self.df.fillna('нет', inplace=True)
    
    #TODO make loading able without first empty string
    def create_indexes(self):
        icn = list((self.df == '№ з/з').sum(axis=0)).index(True)
        self.df = self.df.set_index(self.df.iloc[:,icn].name)
        self.df.index.name = None


    def create_columns(self):
        #make row with key word as column names
        crn = list(self.df.index).index(self.key_word)
        self.df.columns = self.df.iloc[crn]
        self.df = self.df.drop(labels=self.key_word, axis='index')

        #rename colums with empty names
        cn = self.df.columns
        rv = cn.isnull()
        l = list(cn)
        for i in range(1, len(l)):
            if rv[i]:
                l[i] = l[i-1] + '_1'
        self.df.columns = l

    def delete_rows(self):
        self.df.index = self.df.index.fillna('delete')

        for i in self.df.index.values:
            try:
                pp.Word(pp.nums).parseString(str(i))
            except pp.ParseException:
                #print(i)
                self.df = self.df.drop([i])
        