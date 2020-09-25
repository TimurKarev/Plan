import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from plotly.subplots import make_subplots
import plotly.graph_objects as go

from controller import * 
# from view import *
# from model.model import *


#TODO Сделать сохранение статусов после перезагрузки экрана

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
        dbc.Col(dbc.Label("Количество заказов для вывода:  "), width={'size':3}),
        dbc.Col(dbc.Input(id='num_zakaz',type="number", inputMode='numeric', value=ctrl.num), width={'size':1}),
        dbc.Col(dbc.Label("Не включать последние "), width={'size':2}),
        dbc.Col(dbc.Input(id='ign_zakaz', type="number", inputMode='numeric', value=ctrl.ign), width={'size':1}),
        dbc.Col(dbc.Label("заказов"), width={'size': 1}),
        dbc.Col(dbc.Label("Высота графика"), width = {'size':2, 'offset': 1}),
        dbc.Col(dbc.Input(id='fig_hight', type="number", inputMode='numeric', value=V.Fig_hight), width={'size':1}),
    ]),

    dbc.Row([
        dbc.Col(
            dcc.Graph(
                    id='graph_plan',
                    figure=fig,
            ), width={'size': 11, 'order':'first'}
        ),

        dbc.Col(
            [
                html.Label('Показывать работы'),
                dbc.Checklist(
                    id='jobs_sel_all',
                    options=[{'label':' ','value':'True'}],
                    value=['True']
                ),
                dbc.Checklist(
                    id='jobs_checklist',
                    options=cl_options,
                    value=cl_value
                )
            ], width={'size': 1, 'order':'last'}
        ),
    ]),

    dbc.Row([
        dbc.Col(
            [dbc.Button("Применить фильтры", id='reload_button', n_clicks=0)], width={'size': 11}
        )
    ])
])


@app.callback(Output('jobs_checklist', 'value'),
            [Input('jobs_sel_all', 'value')], 
            [State('jobs_checklist', 'value')])
def update_joblis(value, lst):
    l = []
    if len(value):
        _, l = ctrl.get_job_checklist_list()

    return l


@app.callback(Output('graph_plan', 'figure'),
            [Input('reload_button', 'n_clicks')],
            [State('num_zakaz','value'),
            State('ign_zakaz', 'value'),
            State('jobs_checklist', 'value'), 
            State('fig_hight', 'value')])
def update_output(n_clicks, num_zakaz, ign_zakaz, job_list, hight):
    ctrl.set_zakaz_intervals(num_zakaz, ign_zakaz)
    ctrl.set_fig_exclude_jobs_list(job_list)
    ctrl.set_fig_hight(hight)
    fig = ctrl.get_fig()
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)