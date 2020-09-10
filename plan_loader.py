import pandas as pd


class PlanLoader:
    df = pd.DataFrame()

    def __init__(self, exel_name):
        self.df = pd.read_excel(exel_name, sheet_name='2020')

