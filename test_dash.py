import dash
import dash_core_components as dcc
import dash_html_components as html

from plotly.subplots import make_subplots
import plotly.graph_objects as go

import pandas as pd
from reformatter import *
from plan_loader import PlanLoader
from gantt_bar import *

#cacidi.pythonanywhere.com
#/home/cacidi/mysite/flask_app.py

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

plan_loader = PlanLoader('план.xlsx')
plan_loader.delete_rows_ready()
ref = PlanReformatter(plan_loader.df)

gantt_df  = ref.get_df_for_gantt(15)

l = ref.get_column_names(True)
fig = go.Figure()
b = GanttBar()

data = ref.get_df_for_gantt(25)
for i in range(data.shape[0]):
    fig.add_trace(b.get_bar(data['Start'][i], data['Finish'][i],
                    l.index(data['Task'][i]), group=int(data['zakaz'][i])))
    
fig.update_layout(
    yaxis = dict(
        tickmode = 'array',
        tickvals = [n for n in range(len(l))],
        ticktext = l
    ),
    height = 800
)

fig.update_xaxes(
    dtick='D1',
    range=[dt.today() - timedelta(days=7),
          dt.today() + timedelta(days=30)],
    tickangle = 90,
    )

app.layout = html.Div([
    dcc.Graph(
        id='graph-with-slider',
        figure=fig,
    ),

])

'''
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", 
                     size="pop", color="continent", hover_name="country", 
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig
'''

if __name__ == '__main__':
    app.run_server(debug=True)