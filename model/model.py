from model.plan_loader import *
from model.reformatter import *

class Model:
    def __init__(self, filename):
        self.num_zakaz = 25
        self.ign_zakaz = 0
        
        pl = PlanLoader('план.xlsx')
        pl.delete_rows_ready()
        self.__pr = PlanReformatter(pl.df)
        self.current_df = self.__pr.get_df_for_gantt(self.num_zakaz,
                                              self.ign_zakaz)

    def set_zakaz_intervals(self, num, ignore=None):
        self.num_zakaz = num
        self.ign_zakaz = ignore
        self.current_df = self.__pr.get_df_for_gantt(self.num_zakaz,
                                              self.ign_zakaz)


    def get_list_of_jobs(self, reverse):
        return self.__pr.get_jobs_names(reverse)
