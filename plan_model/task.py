from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as dd

class Task:
    
    PR_MV = 0
    PR_ERR = 1
    PR_IGN = 2
    
    DUR_USUAL = 8
    DUR_OVER = 10
    
    def __init__(self, order=None, name=None, start=None, end=None, duration=None,
                comment=None, overjob = False, mercenary = False):

        self.order : int = order
        self.name : str = name
        self.comment : str = comment

        self.start : dt = start
        self.end : dt = end

        self.duration = duration

        self.overjob : bool = overjob
        self.mercenary : bool = mercenary

        self.predecessors = []  #предшественники
        self.followers = [] #последователи
        
        self.decomp_parent = [] #корневые задачи
        self.decomp_child = [] #дочерние задачи
        
        self.time_before = None
        self.time_after = None

    def __str__(self):
        rs =    'Name - ' + str(self.name)
        rs += '\nDur  - ' + str(self.duration)
        pred = [p.name for p in self.predecessors]
        rs += '\nPre  - ' + str(pred)
        fol = [f.name for f in self.followers]
        rs += '\nFol  - ' + str(fol)

        return rs
    
    
    def __repr__(self):
        return self.__str__()

'''
    def set_end_by_start(self,
                        duration = None,
                        start = None,
                        err_prop = PR_IGN,
                        overjob = False,
                        mercenary = False):

        if duration is not None:
            self.duration = duration
        if start is not None:
            self.start = start
        if err_prop is not None:
            err_prop = err_prop
        if overjob is not None:
            self.overjob = overjob
        if mercenary is not None:
            self.mercenary = mercenary

        #TODO сделать проверку start на пересечение с предшественниками

        cur_dur = self.duration
        cur_time = self.start
        day_dur = DUR_USUAL if self.overjob is False else DUR_OVER
        while cur_dur <= self.__get
'''