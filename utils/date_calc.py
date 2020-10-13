from datetime import datetime
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
import holidays

class DateCalc:
    work_beg = (8,20)
    work_end = (17,20)
    fri_end = (16,20)
    work_over = 2
    fri_over = 3
    hol_over = 8
    ru_hol = holidays.RU()

    @staticmethod
    def add_hour(start : datetime, hour : tuple, 
                work_over : bool = False,
                sat_over : bool = False, sun_over : bool = False, 
                hol_over: bool = False):
        pass


def is_working_time(cur_date : datetime,
                work_over : bool = False,
                sat_over : bool = False, sun_over : bool = False,
                hol_over : bool = False) -> bool:

    #date_day = cur_date.replace(hour=0, minute=0, second=0, microsecond=0)

    fin_time : tuple = (17,20) # конец рабочего дня

    if (cur_date in DateCalc.ru_hol) and (hol_over is False):
        return False

    if (cur_date.weekday() == 5) and (sat_over is False):
        return False

    if (cur_date.weekday() == 6) and (sun_over is False):
        return False

    if (cur_date.weekday()  == 4):
        if (work_over is False):
            fin_time = DateCalc.fri_end
        else:
            fin_time = (DateCalc.fri_end[0] + DateCalc.fri_over, 20)

    if (cur_date.weekday()  in [0,1,2,3]):
        if (work_over is False):
            fin_time = DateCalc.work_end
        else:
            fin_time = (DateCalc.work_end[0] + DateCalc.work_over, 20)

    if (cur_date.hour < DateCalc.work_beg[0]) \
        or (cur_date.hour > fin_time[0]):
            return False

    if (cur_date.hour == DateCalc.work_beg[0]) \
        and (cur_date.minute < DateCalc.work_beg[1]):
            return False
    
    if (cur_date.hour == fin_time[0]) \
        and (cur_date.minute > fin_time[1]):
            return False
    
    return True

