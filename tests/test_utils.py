from datetime import datetime
from datetime import timedelta, date
import unittest

from utils import date_calc as dc

class TestIsWorkingTime(unittest.TestCase):


    def test_holiday(self):
        # Праздник 
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=4)))
        # Праздник переработка в праздники рабочее время
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=4, hour=12),
                                            hol_over = True))
        # Праздник переработка в праздники НЕ рабочее время
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=4, hour=7),
                                            hol_over = True))
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=4, hour=18),
                                            hol_over = True))
        # Праздник НЕ переработка в праздники рабочее время
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=4, hour=12),
                                            sun_over = True,
                                            sat_over = True,
                                            work_over = True))
        # Праздник переработка в праздники НЕ рабочее время пограничниы значения
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=4, hour=8, minute=19),
                                            hol_over = True))
        # Праздник переработка в праздники рабочее время пограничниы значения
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=4, hour=8, minute=20),
                                            hol_over = True))
        # Праздник переработка в праздники НЕ рабочее время пограничниы значения
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=4, hour=17, minute=21),
                                            hol_over = True))
        # Праздник переработка в праздники рабочее время пограничниы значения
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=4, hour=17, minute=20),
                                            hol_over = True))


    def test_sunday(self):
        # ВС 
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=4)))
        #  ВС переработка в праздники рабочее время
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=11, hour=12),
                                            sun_over = True))
        # BC переработка в праздники НЕ рабочее время
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=18, hour=7),
                                            sun_over = True))
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=4, hour=18),
                                            sun_over = True))
        # BC НЕ переработка в ВС
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=4, hour=12),
                                            sun_over = False,
                                            sat_over = True,
                                            work_over = True,
                                            hol_over = True))
        # BC переработка в BC НЕ рабочее время пограничниы значения
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=25, hour=8, minute=19),
                                            sun_over = True))
        # ВС переработка в праздники рабочее время пограничниы значения
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=18, hour=8, minute=20),
                                            sun_over = True))
        # ВС переработка в ВС НЕ рабочее время пограничниы значения
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=4, hour=17, minute=21),
                                            sun_over = True))
        # ВС переработка в ВС рабочее время пограничниы значения
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=11, hour=17, minute=20),
                                            sun_over = True))


    def test_sataday(self):
        # Сб 
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=3)))
        #  Сб переработка в праздники рабочее время
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=10, hour=12),
                                            sat_over = True))
        # Cб переработка в праздники НЕ рабочее время
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=17, hour=7),
                                            sat_over = True))
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=3, hour=18),
                                            sat_over = True))
        # Cб НЕ переработка в Сб
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=3, hour=12),
                                            sun_over = True,
                                            sat_over = False,
                                            work_over = True,
                                            hol_over = True))
        # Cб переработка в Cб НЕ рабочее время пограничниы значения
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=24, hour=8, minute=19),
                                            sat_over = True))
        # Сб переработка в праздники рабочее время пограничниы значения
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=17, hour=8, minute=20),
                                            sat_over = True))
        # Сб переработка в Сб НЕ рабочее время пограничниы значения
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=3, hour=17, minute=21),
                                            sat_over = True))
        # Сб переработка в Сб рабочее время пограничниы значения
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=10, hour=17, minute=20),
                                            sat_over = True))


    def test_friday(self):
        #Пятница нерабочее время утро
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=2,
                                                                hour=7)))
        #Пятница рабочее время
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=2,
                                                                hour=9)))
        #Пятница нерабочее время утро пограничное значение
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=9,
                                                                hour=8, minute=19)))
        #Пятница нерабочее время вечер
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=16,
                                                                hour=17, minute=19)))
        #Пятница нерабочее время вечер пограничное значение
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=23,
                                                                hour=16, minute=21)))
        #Пятница рабочее время вечер пограничное значение
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=23,
                                                                hour=16, minute=20)))
        #Пятница рабочая переработка
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=23,
                                                                hour=18, minute=21),
                                            work_over = True))
        #Пятница рабочая переработка пограничное значение
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=30,
                                                                hour=19, minute=20),
                                                                work_over = True))
        #Пятница нерабочее время вечер есть переработка
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=6,
                                                                hour=21, minute=20),
                                                                work_over = True))
        #Пятница нерабочее время вечер есть переработка пограничное значение
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=13,
                                                                hour=19, minute=21),
                                                                work_over = True))
        #Пятница рабочее время вечер есть переработка пограничное значение
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=13,
                                                                hour=19, minute=20),
                                                                work_over = True))
        #Пятница нерабочее время есть все переработки кроме рабочей 
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=20,
                                                                hour=23, minute=21),
                                                                work_over = False,
                                                                hol_over = True,
                                                                sat_over = True,
                                                                sun_over = True))

    def test_workday(self):
        #нерабочее время утро
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=1,
                                                                hour=7)))
        #рабочее время
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=5,
                                                                hour=9)))
        #нерабочее время утро пограничное значение
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=6,
                                                                hour=8, minute=19)))
        #нерабочее время вечер
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=7,
                                                                hour=18, minute=19)))
        #нерабочее время вечер пограничное значение
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=8,
                                                                hour=17, minute=21)))
        #рабочее время вечер пограничное значение
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=12,
                                                                hour=17, minute=20)))
        #рабочая переработка
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=13,
                                                                hour=18, minute=21),
                                                                work_over = True))
        #рабочая переработка пограничное значение
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=14,
                                                                hour=19, minute=20),
                                                                work_over = True))
        #Пятница нерабочее время вечер есть переработка
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=11, day=15,
                                                                hour=21, minute=20),
                                                                work_over = True))
        #Пятница нерабочее время вечер есть переработка пограничное значение
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=19,
                                                                hour=19, minute=21),
                                                                work_over = True))
        #Пятница рабочее время вечер есть переработка пограничное значение
        self.assertTrue(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=20,
                                                                hour=19, minute=20),
                                                                work_over = True))
        #Пятница нерабочее время есть все переработки кроме рабочей 
        self.assertFalse(dc.is_working_time(cur_date = datetime(year=2020, month=10, day=21,
                                                                hour=23, minute=21),
                                                                work_over = False,
                                                                hol_over = True,
                                                                sat_over = True,
                                                                sun_over = True))

class TestIsWorkingDay(unittest.TestCase):
    def test_hole_func(self):
        # рабочий день
        self.assertTrue(dc.is_working_day(datetime(2020,10,13)))
        
        # суббота
        self.assertFalse(dc.is_working_day(datetime(2020,10,10), sat_over=False, sun_over=True, hol_over=True))
        self.assertTrue(dc.is_working_day(datetime(2020,10,10), sat_over=True))
        
        self.assertFalse(dc.is_working_day(datetime(2020,10,11), sat_over=True, sun_over=False, hol_over=True))
        self.assertTrue(dc.is_working_day(datetime(2020,10,11), sun_over=True))
        
        self.assertFalse(dc.is_working_day(datetime(2020,11,4), sat_over=True, sun_over=True, hol_over=False))
        self.assertTrue(dc.is_working_day(datetime(2020,11,4), hol_over=True))