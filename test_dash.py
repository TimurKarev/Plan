import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from plotly.subplots import make_subplots
import plotly.graph_objects as go

from controller import * 

from reformatter import *
from plan_loader import *

from view import *

#TODO переставить отметки времени наверх
#cacidi.pythonanywhere.com
#/home/cacidi/mysite/flask_app.py

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


ctrl = Controller('план.xlsx')
fig = ctrl.get_fig(10)

app.layout = html.Div([
    #TODO create validation system for input  max, min properties
    #TODO make input areas smaller
    dbc.Row([
        dbc.Label("Количество заказов для вывода:  "),
        dbc.Input(name='num_zakaz',type="number", inputMode='numeric', value=10),
        dbc.Label("Не включать последние "),
        dbc.Input(name='ign_zakaz', type="number", inputMode='numeric', value=0),
        dbc.Label("заказов"),
    ]),

    dcc.Graph(
        id='graph_plan',
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