import plotly.graph_objects as go
from gantt_bar import *
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import timedelta, date
import holidays
from model import plan_var as V

class ViewManager:
    def __init__(self, jobs_names, exclude_jobs, hight=600,):
        self.fig = go.Figure()
        self.bar = GanttBar()
        self.hight = hight
        self.jobs_names = jobs_names
        self.exclude_jobs = exclude_jobs

    def get_fig(self, _data):
        self.fig.data = []
        self.bar = GanttBar()
        column_names = self.__get_column_names()
        data = _data.copy()
        data = data[data['Task'].isin(column_names)]
        #print("col", column_names, data.shape, _data.shape)

        try:
            for _, i in data.iterrows():
                #print(i)
                ind = column_names.index(i['Task'])
                #print(ind)
                self.fig.add_trace(self.bar.get_bar(i['Start'], i['Finish'],
                                ind, i['Task'], group=int(i['zakaz']), working_hour=i['Hours']))
        except Exception as e:
            print('exeption', e)

        #TODO move to separate block
        self.fig.add_trace(go.Scatter(x=[dt.today(), dt.today()], y=[-2,22], showlegend=False, opacity=.4))
        #self.fig.add_trace(go.Bar(x=[dt.today()], y=[23]))

        self.fig.update_layout(
            yaxis = dict(
                tickmode = 'array',
                tickvals = [n for n in range(len(column_names))],
                ticktext = column_names,
                range=[-1,len(column_names)+.5]
            ),
            shapes=self.__get_weekend_shapes(),
            height = self.hight,
            hoverlabel = dict(
                font_size = 20
            )
        )

        self.fig.update_xaxes(
            dtick='D1',
            range=[dt.today() - timedelta(days=7),
                dt.today() + timedelta(days=30)],
            tickangle = 90,
            side = 'top',
            )

        return self.fig


    def __get_column_names(self):
        col = self.jobs_names.copy()
        i=0
        while i < len(col):
            if col[i] not in self.exclude_jobs:
                col.pop(i)
            else:
                i+=1
        return col

    def __get_weekend_shapes(self):
        shapes=[]
        ru_holiday = holidays.RU()
        b_dct = {
            'type': "rect",
            'xref': 'x',
            'yref': "y",
            'y0' : "-1",
            'y1' : "21",
            'fillcolor' : "lightgray",
            'opacity' : 0.4,
            'line_width' : 0,
            'layer' : "below",
        }

        d = dt.today() - relativedelta(days=45)
        d = d.replace(hour=0,minute=0,second=0, microsecond=0)

        for i in range(154):
            if date(d.year, d.month, d.day) in V.get_not_working_days():
                dct = b_dct.copy()
                dct['x0'] =  d
                dct['x1'] = d + relativedelta(days=1)
                shapes.append(dct)
            d = d + relativedelta(days=1)

        return shapes


