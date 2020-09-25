from view import *
from model.model import *

class Controller:
    def __init__(self, filename):
        self.model = Model(filename)
        jobs = self.model.get_list_of_jobs(True)
        self.view = ViewManager(jobs, jobs, V.Fig_hight)
        self.num = V.Zakaz_intervals[0]
        self.ign = V.Zakaz_intervals[1]

    def get_fig(self):
        return self.view.get_fig(self.model.current_df) 

    #TODO make value chekings (???)
    def set_zakaz_intervals(self, num, ignore=None):
        self.num = num
        self.ign = ignore
        self.model.set_zakaz_intervals(self.num, self.ign)

    def get_job_checklist_list(self,):
        l = self.model.get_list_of_jobs(False)
        options = []
        value = []
        for i in range(len(l)):
            d = {}
            d['label'] = l[i]
            d['value'] = l[i]
            options.append(d)
            value.append(l[i])
        return (options, value)

    def set_fig_exclude_jobs_list(self, exclude_list):
        self.view.exclude_jobs = exclude_list
        
    def set_fig_hight(self, hight):
        self.view.hight = hight