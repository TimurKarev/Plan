import plotly.graph_objects as go
from gantt_bar import *
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import timedelta

class ViewManager:
    def __init__(self, height=700):
        self.fig = go.Figure()
        self.bar = GanttBar()
        self.height = height

    def get_fig(self, data, column_names):

        for i in range(data.shape[0]):
            self.fig.add_trace(self.bar.get_bar(data['Start'][i], data['Finish'][i],
                            column_names.index(data['Task'][i]), group=int(data['zakaz'][i])))

        self.fig.update_layout(
            yaxis = dict(
                tickmode = 'array',
                tickvals = [n for n in range(len(column_names))],
                ticktext = column_names
            ),
            height = self.height
        )

        self.fig.update_xaxes(
            dtick='D1',
            range=[dt.today() - timedelta(days=7),
                dt.today() + timedelta(days=30)],
            tickangle = 90,
            )

        return self.fig