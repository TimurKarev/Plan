from plan_loader import *
from reformatter import *
import plotly.express as px

plan_loader = PlanLoader('план.xlsx')
plan_loader.delete_rows_ready()

ref = PlanReformatter(plan_loader.df)

i=0
l = []
while i < len(ColumnNames)-2:
    l.append(ColumnNames[i][:-4])
    i+=2

data = ref.get_df_for_gantt(20)

#TODO придумать, как показывать наложившиеся друг на бруга бары
fig = px.timeline(data, x_start="Start", x_end="Finish", y="Task", color='zakaz', category_orders={'Task':l})
#fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.update_xaxes(
    dtick='D1',
    )
fig.show()