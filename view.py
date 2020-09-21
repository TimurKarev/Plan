import plotly.graph_objects as go
from gantt_bar import *
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
from datetime import timedelta

class ViewManager:
    def __init__(self, jobs_names, exclude_jobs, height=600,):
        self.fig = go.Figure()
        self.bar = GanttBar()
        self.height = height
        self.jobs_names = jobs_names
        self.exclude_jobs = exclude_jobs

    def get_fig(self, data):
        self.fig.data = []
        self.bar = GanttBar()
        column_names = self.jobs_names
        for i in range(data.shape[0]):
            if data['Task'][i] in self.exclude_jobs:
                self.fig.add_trace(self.bar.get_bar(data['Start'][i], data['Finish'][i],
                                column_names.index(data['Task'][i]), group=int(data['zakaz'][i])))

        #TODO move to separate block
        self.fig.add_trace(go.Scatter(x=[dt.today(), dt.today()], y=[-2,22], showlegend=False, opacity=.4))
        #self.fig.add_trace(go.Bar(x=[dt.today()], y=[23]))

        self.fig.update_layout(
            yaxis = dict(
                tickmode = 'array',
                tickvals = [n for n in range(len(column_names))],
                ticktext = column_names,
                range=[-1,18]
            ),
            shapes=[
                dict(
                    type="rect",
                    xref="x",
                    yref="y",
                    x0="2020-09-19",
                    y0="-1",
                    x1="2020-09-21",
                    y1="21",
                    fillcolor="lightgray",
                    opacity=0.4,
                    line_width=0,
                    layer="below"
                ),
            ],
            height = self.height
        )

        self.fig.update_xaxes(
            dtick='D1',
            range=[dt.today() - timedelta(days=7),
                dt.today() + timedelta(days=30)],
            )

        return self.fig

