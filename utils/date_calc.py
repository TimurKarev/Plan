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
    ru_hol = holidays.RU() #TODO сделать более широкую функцию выхи + праздники
    dinner_beg = (11,30)
    dinner_end = (12,18)

    @staticmethod
    def move_time(start : datetime, time : tuple, reverse = False, 
                work_over : bool = False,
                sat_over : bool = False, sun_over : bool = False, 
                hol_over: bool = False):

        time_sec = time[0] * 3600 + time[1] * 60
        
        cur_time = start
        if not is_working_time(cur_time, work_over):
            cur_time = get_next_workday(cur_time, reverse, work_over, sat_over, sun_over, hol_over)

        day_time_rest = None
        while True:

            if reverse is False:
                day_time_rest = get_day_time_rest(cur_time, reverse, work_over)
            else:
                day_time_rest = get_day_time_rest(cur_time, reverse, work_over)
        
            if day_time_rest > time_sec:
                break
            
            cur_time = get_next_workday(cur_time, False, work_over, sat_over, sun_over, hol_over)
            time_sec -= day_time_rest
        
        #k = 1 if reverse is False else -1
        
        return add_time_intraday(cur_time, time_sec, reverse)


    @staticmethod
    def is_bigger(f_date : datetime = None, s_date : datetime = None,
                    f_time : tuple = None, s_time : tuple = None):
        
        ret = DateCalc.__format_time(f_date, s_date, f_time, s_time)
        if ret is None:
            return None
        
        f_time = ret[0]
        s_time = ret[1]
        
        if f_time[0] > s_time[0]:
            return True
        
        if (f_time[0] == s_time[0]) and (f_time[1] >= s_time[1]):
            return True
        
        return False

    @staticmethod
    def is_smaller(f_date : datetime = None, s_date : datetime = None,
                    f_time : tuple = None, s_time : tuple = None):
        
        ret = DateCalc.__format_time(f_date, s_date, f_time, s_time)
        if ret is None:
            return None
        
        f_time = ret[0]
        s_time = ret[1]
        
        if f_time[0] < s_time[0]:
            return True
        
        if (f_time[0] == s_time[0]) and (f_time[1] <= s_time[1]):
            return True
        
        return False

    @staticmethod
    def __format_time(f_date : datetime = None, s_date : datetime = None,
                f_time : tuple = None, s_time : tuple = None):

        if (f_date is None) and (s_date is None) and (f_time is None) and (s_time is None):
            return None
        
        if (f_date is None) and (f_time is None):
            return None

        if (s_date is None) and (s_time is None):
            return None

        if f_date is not None:
            f_time = (f_date.hour, f_date.minute)

        if s_date is not None:
            s_time = (s_date.hour, s_date.minute)
    
        return (f_time, s_time)

# TODO Придумать как быть, потому что может перевалить за день (как вариант вызвать еще раз def move_time)
def add_time_intraday(cur_time, sec, reverse = False):
    pass


# Возвращает остаток рабочего дня
def get_day_time_rest(cur_time, reverse = False, work_over = False):
    day_time_rest = None
    if reverse is False:
        day_time_rest = (get_end_of_workday(cur_time, work_over) - cur_time).total_seconds()
        if DateCalc.is_smaller(f_date=cur_time, s_time= DateCalc.dinner_beg):
            day_time_rest -= 48 * 60
    else:
        day_time_rest = (cur_time - cur_time.replace(hour=8, minute=20, second=0, microsecond=0)).total_seconds()
        if DateCalc.is_bigger(f_date=cur_time, s_time= DateCalc.dinner_end):
            day_time_rest -= 48 * 60

    return day_time_rest


def is_working_day(cur_date: datetime,
                    sat_over : bool = False,
                    sun_over : bool = False,
                    hol_over : bool = False) -> bool:
    
    if (cur_date in DateCalc.ru_hol) and (hol_over is False):
        return False

    if (cur_date.weekday() == 5) and (sat_over is False):
        return False

    if (cur_date.weekday() == 6) and (sun_over is False):
        return False
    
    return True


def is_working_time(cur_date : datetime,
                work_over : bool = False,
                sat_over : bool = False, sun_over : bool = False,
                hol_over : bool = False) -> bool:

    if is_working_day(cur_date, sat_over, sun_over, hol_over) is False:
        return False

    fin_time : tuple = (17,20) # конец рабочего дня

    #TODO использовать расширинную функцию get_end_of_workday
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

def get_next_workday(cur_date : datetime, reverse = False, 
                    work_over = False, sat_over = False,
                    sun_over = False, hol_over = False) -> datetime:

    k = 1 if reverse is False else -1
    
    c = cur_date + timedelta(days=1) * k
    while not is_working_day(c, sat_over = sat_over, sun_over = sun_over, hol_over = hol_over):
        c = c + k * timedelta(days=1)
    
    pass
    if reverse is False:
        c = c.replace(hour=DateCalc.work_beg[0], minute=DateCalc.work_beg[1], second=0, microsecond=0)
    else:
        c = get_end_of_workday(c, work_over)  #TODO сделать функцию с упором на производственный календарь, через функцию
    
    return c


    # Функция возвращает конец рабочего дня который ей передали ОНА не проверяет рабочий ли день ей передали
def get_end_of_workday(cur_date : datetime, work_over = False):  #TODO сделать проверку является ли переданный день рабочим и кинать ексепшн  (а может и не надо)
    c = None
    if (cur_date in DateCalc.ru_hol):
        c = cur_date.replace(hour=DateCalc.work_end[0], minute=DateCalc.work_end[1], second=0, microsecond=0)
        return c
    
    weekday = cur_date.weekday()
    
    if weekday == 4:
        if work_over == False:
            c = cur_date.replace(hour=DateCalc.fri_end[0], minute=DateCalc.fri_end[1], second=0, microsecond=0)
        else:
            c = cur_date.replace(hour=DateCalc.fri_end[0] + DateCalc.fri_over, minute=DateCalc.fri_end[1], second=0, microsecond=0)
    elif weekday in [0,1,2,3]:
        if work_over == False:
            c = cur_date.replace(hour=DateCalc.work_end[0], minute=DateCalc.work_end[1], second=0, microsecond=0)
        else:
            c = cur_date.replace(hour=DateCalc.work_end[0] + DateCalc.work_over, minute=DateCalc.work_end[1], second=0, microsecond=0)
    elif weekday in [5,6]:
        c = cur_date.replace(hour=DateCalc.work_end[0], minute=DateCalc.work_end[1], second=0, microsecond=0)

    return c

