from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plotly.express import colors

def get_color(color):
    while color >= 23:
        color = color - 23
    return color

class GanttBar:
    
    def __init__(self):
        self.was_group = set()

    def get_bar(self, st, fn, val, task, group, working_hour, delta=0.4):
        c = get_color(group)
        c = colors.qualitative.Dark24[c]
        self.line = go.scatter.Line(color=c, shape = 'hv', width=2.5)
        self.marker = go.scatter.Marker(opacity=0)

        self.bar = go.Scatter(
                    y=[val+delta, val, val, val-delta], 
                    x=[st,st,fn,fn],
                    line=self.line,
                    marker=self.marker,
                    opacity=0.5,
                    legendgroup=group,
                    showlegend=(group not in self.was_group),
                    name=group,
                    hovertemplate = '<b>{}</b> - {}'.format(group, task) + \
                                    '<br>' + '{}'.format(st.strftime('%d-%m')) + \
                                    '<br>' + '{}'.format(fn.strftime('%d-%m')) + \
                                    '<br>' + 'часы - {}'.format(working_hour) + \
                                    '<extra></extra>'
        )

        self.was_group.add(group)
        
        #self.bar = go.Scatter(x=[1,2], y=[1,1])
        return self.bar
