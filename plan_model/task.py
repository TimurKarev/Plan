from datetime import datetime as dt
from dateutil.relativedelta import relativedelta as dd


class Task:
    
    PR_MV = 0
    PR_ERR = 1
    PR_IGN = 2
    
    DUR_USUAL = 8
    DUR_OVER = 10
    
    def __init__(self):
        self.order : int
        self.name : str
        self.comment : str
        
        self.start : dt
        self.end : dt
        self.duration : dd

        self.overjob : bool
        self.mercenary : bool
        
        self.predecessors : list  #предшественники
        self.followers : list #последователи


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