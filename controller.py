from plan_loader import *
from reformatter import *
from view import *

class Controller:
    def __init__(self, filename):
        self.view = ViewManager()

        pl = PlanLoader('план.xlsx')
        pl.delete_rows_ready()
        self.model = PlanReformatter(pl.df)

    def get_fig(self, num, ignore=None):
        column_names = self.model.get_column_names(True)

        return self.view.get_fig(self.model.get_df_for_gantt(num, ignore), column_names)
