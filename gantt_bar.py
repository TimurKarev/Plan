from plotly.subplots import make_subplots
import plotly.graph_objects as go

class GanttBar:
    
    def __init__(self):
        pass
    
    def get_bar(self, st, fn, val, delta=0.15):
        self.line = go.scatter.Line(color='rgba(255,25,255,0.5)', shape = 'hv', width=2.5)
    
        self.bar = go.Scatter(
                    y=[val+delta, val, val, val-delta], 
                    x=[st,st,fn,fn],
                    line=self.line)
        
        #self.bar = go.Scatter(x=[1,2], y=[1,1])
        return self.bar
