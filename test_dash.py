import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from plotly.subplots import make_subplots
import plotly.graph_objects as go

from controller import * 
# from view import *
# from model.model import *

#TODO Сделать интерактивную ширину экрана
#TODO Make start intervals from global variables
#cacidi.pythonanywhere.com
#/home/cacidi/mysite/flask_app.py

external_stylesheets = [dbc.themes.CERULEAN]#['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


ctrl = Controller('план.xlsx')
fig = ctrl.get_fig()

(cl_options, cl_value) = ctrl.get_job_checklist_list()

app.layout = html.Div([
    #TODO create validation system for input  max, min properties
    #TODO make input areas smaller
    dbc.Row([
        dbc.Col(dbc.Label("Количество заказов для вывода:  "), width={'size':2}),
        dbc.Col(dbc.Input(id='num_zakaz',type="number", inputMode='numeric', value=10), width={'size':1}),
        dbc.Col(dbc.Label("Не включать последние "), width={'size':2}),
        dbc.Col(dbc.Input(id='ign_zakaz', type="number", inputMode='numeric', value=0), width={'size':1}),
        dbc.Col(dbc.Label("заказов")),
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Graph(
                    id='graph_plan',
                    figure=fig,
            ), width={'size': 11, 'order':'last'}
        ),

        dbc.Col(
            [
                html.Label('Показывать работы'),
                dbc.Checklist(
                    id='jobs_checklist',
                    options=cl_options,
                    value=cl_value
                )
            ], width={'size': 1, 'order':'first'}
        ),
    ])
])


@app.callback(Output('graph_plan', 'figure'),
    [Input('num_zakaz', 'value'), 
     Input('ign_zakaz', 'value'),
     Input('jobs_checklist', 'value')])
def update_figure(num, ign, job_list):
    ctx = dash.callback_context
    trig = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if trig in ['num_zalaz', 'ign_zakaz']:
        ctrl.set_zakaz_intervals(num, ign)
    elif trig == 'jobs_checklist':
        ctrl.set_fig_exclude_jobs_list(job_list)
        

    fig = ctrl.get_fig()
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)