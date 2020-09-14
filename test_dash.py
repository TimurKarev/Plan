import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from reformatter import *
from plan_loader import PlanLoader

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

plan_loader = PlanLoader('план.xlsx')
plan_loader.delete_rows_ready()
ref = PlanReformatter(plan_loader.df)

gantt_df  = ref.get_df_for_gantt(5)

i=0
l = []
while i < len(ColumnNames)-2:
    l.append(ColumnNames[i][:-4])
    i+=2

fig = px.timeline(gantt_df, x_start="Start", x_end="Finish", y="Task", color='Task', category_orders={'Task':l}, facet_row="zakaz",
                  width=1800, height=900)
#fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.update_yaxes(matches=None)
fig.update_xaxes(dtick='D1')


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