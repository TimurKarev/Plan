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
        
class TestGetEndOfWorkDay(unittest.TestCase):
    def test_hole_func(self):
        # будни без переработка
        answer = datetime(2020, 10, 1, 17, 20)
        d = answer.replace(hour= 12, minute= 0)
        self.assertEqual(answer, dc.get_end_of_workday(d))
        # будни переработка
        answer = datetime(2020, 10, 1, 19, 20)
        d = answer.replace(hour= 12, minute= 0)
        self.assertEqual(answer, dc.get_end_of_workday(d, True))

        # пятница без переработка
        answer = datetime(2020, 10, 2, 16, 20)
        d = answer.replace(hour= 12, minute= 0)
        self.assertEqual(answer, dc.get_end_of_workday(d))
        # пятница переработка
        answer = datetime(2020, 10, 2, 19, 20)
        d = answer.replace(hour= 12, minute= 0)
        self.assertEqual(answer, dc.get_end_of_workday(d, True))

        # суббота без переработка
        answer = datetime(2020, 10, 3, 17, 20)
        d = answer.replace(hour= 12, minute= 0)
        self.assertEqual(answer, dc.get_end_of_workday(d))
        # суббота переработка
        answer = datetime(2020, 10, 3, 17, 20)
        d = answer.replace(hour= 12, minute= 0)
        self.assertEqual(answer, dc.get_end_of_workday(d, True))

        # вс без переработка
        answer = datetime(2020, 10, 4, 17, 20)
        d = answer.replace(hour= 12, minute= 0)
        self.assertEqual(answer, dc.get_end_of_workday(d))
        # вс переработка
        answer = datetime(2020, 10, 4, 17, 20)
        d = answer.replace(hour= 12, minute= 0)
        self.assertEqual(answer, dc.get_end_of_workday(d, True))

        # праздник без переработка
        answer = datetime(2020, 11, 4, 17, 20)
        d = answer.replace(hour= 12, minute= 0)
        self.assertEqual(answer, dc.get_end_of_workday(d))
        # праздник переработка
        self.assertEqual(answer, dc.get_end_of_workday(d, True))
        
class TestGetNextWorkDay(unittest.TestCase):
    def test_hole_func(self):
    #пятница без переработка
        d = datetime(2020, 10, 2)
        answer = datetime(2020, 10, 5, 8, 20, 0, 0)
        d = dc.DateCalc.get_next_workday(d, work_over = True, hol_over = True)
        self.assertEqual(answer, d)
    #пятница переработка в субботу
        d = datetime(2020, 10, 2)
        answer = datetime(2020, 10, 3, 8, 20, 0, 0)
        d = dc.DateCalc.get_next_workday(d, work_over = True, hol_over = True, sat_over = True, sun_over = True)
        self.assertEqual(answer, d)
    #пятница переработка в воскресенье
        d = datetime(2020, 10, 2)
        answer = datetime(2020, 10, 4, 8, 20, 0, 0)
        d = dc.DateCalc.get_next_workday(d, work_over = True, hol_over = True, sun_over = True)
        self.assertEqual(answer, d)
    #пятница обратн без переработка
        d = datetime(2020, 10, 2)
        answer = datetime(2020, 10, 1, 17, 20)
        d = dc.DateCalc.get_next_workday(d, reverse=True, work_over = False, hol_over = True, sat_over = True, sun_over = True)
        self.assertEqual(answer, d)
    #пятница обратн переработка
        d = datetime(2020, 10, 2)
        answer = datetime(2020, 10, 1, 19, 20)
        d = dc.DateCalc.get_next_workday(d, reverse=True, work_over = True)
        self.assertEqual(answer, d)
    #пн переработка
        d = datetime(2020, 10, 5)
        answer = datetime(2020, 10, 6, 8, 20, 0, 0)
        d = dc.DateCalc.get_next_workday(d, work_over = True)
        self.assertEqual(answer, d)
    #пн обратн без переработка
        d = datetime(2020, 10, 5)
        answer = datetime(2020, 10, 2, 16, 20)
        d = dc.DateCalc.get_next_workday(d, reverse = True)
        self.assertEqual(answer, d)
    #пн обратн переработка в рабочее время
        d = datetime(2020, 10, 5)
        answer = datetime(2020, 10, 2, 19, 20)
        d = dc.DateCalc.get_next_workday(d, reverse = True, work_over = True)
        self.assertEqual(answer, d)
    #пн обратнт переработка в субботу
        d = datetime(2020, 10, 5)
        answer = datetime(2020, 10, 3, 17, 20)
        d = dc.DateCalc.get_next_workday(d, reverse = True, work_over = True, hol_over = True, sun_over = False, sat_over = True)
        self.assertEqual(answer, d)
    #пн обратн переработка в воскресенье
        d = datetime(2020, 10, 5)
        answer = datetime(2020, 10, 4, 17, 20)
        d = dc.DateCalc.get_next_workday(d, reverse = True, work_over = True, hol_over = True, sun_over = True, sat_over = True)
        self.assertEqual(answer, d)
    #предпразн без переработка
        d = datetime(2020, 11, 3)
        answer = datetime(2020, 11, 5, 8, 20, 0, 0)
        d = dc.DateCalc.get_next_workday(d, reverse = False, work_over = True, hol_over = False, sun_over = True, sat_over = True)
        self.assertEqual(answer, d)
    #предпразн переработка
        d = datetime(2020, 11, 3)
        answer = datetime(2020, 11, 4, 8, 20, 0, 0)
        d = dc.DateCalc.get_next_workday(d, reverse = False, work_over = True, hol_over = True, sun_over = True, sat_over = True)
        self.assertEqual(answer, d)
    #постпразн обратн без переработка
        d = datetime(2020, 11, 5)
        answer = datetime(2020, 11, 3, 17, 20)
        d = dc.DateCalc.get_next_workday(d, reverse = True, sun_over = True, sat_over = True)
        self.assertEqual(answer, d)
    #постпразн обратн переработка
        d = datetime(2020, 11, 5)
        answer = datetime(2020, 11, 4, 17, 20)
        d = dc.DateCalc.get_next_workday(d, reverse = True, sun_over = True, sat_over = True, hol_over = True)
        self.assertEqual(answer, d)

class TestEqualsMethods(unittest.TestCase):
    def test_is_bigger(self):
        self.assertEqual(None, dc.DateCalc.is_bigger())
        self.assertEqual(None, dc.DateCalc.is_bigger(s_date = datetime.now(), s_time=(12,30)))
        self.assertEqual(None, dc.DateCalc.is_bigger(f_date = datetime.now(), f_time=(12,30)))
        d = datetime.now()
        self.assertFalse(dc.DateCalc.is_bigger(f_date = d.replace(hour=12, minute=30), 
                                                s_date = d.replace(hour=13, minute=30)))
        self.assertFalse(dc.DateCalc.is_bigger(f_date = d.replace(hour=13, minute=30), 
                                                s_date = d.replace(hour=13, minute=35)))
        self.assertTrue(dc.DateCalc.is_bigger(f_date = d.replace(hour=14, minute=30), 
                                                s_date = d.replace(hour=13, minute=30)))
        self.assertTrue(dc.DateCalc.is_bigger(f_date = d.replace(hour=13, minute=37), 
                                                s_date = d.replace(hour=13, minute=35)))
        self.assertTrue(dc.DateCalc.is_bigger(f_date = d.replace(hour=13, minute=37), 
                                                s_time = (13,35)))
        self.assertFalse(dc.DateCalc.is_bigger(f_date = d.replace(hour=13, minute=30), 
                                                s_time = (13,35)))

    def test_is_smaller(self):
        self.assertEqual(None, dc.DateCalc.is_smaller())
        self.assertEqual(None, dc.DateCalc.is_smaller(s_date = datetime.now(), s_time=(12,30)))
        self.assertEqual(None, dc.DateCalc.is_bigger(f_date = datetime.now(), f_time=(12,30)))
        d = datetime.now()
        self.assertTrue(dc.DateCalc.is_smaller(f_date = d.replace(hour=12, minute=30), 
                                                s_date = d.replace(hour=13, minute=30)))
        self.assertTrue(dc.DateCalc.is_smaller(f_date = d.replace(hour=13, minute=30), 
                                                s_date = d.replace(hour=13, minute=35)))
        self.assertFalse(dc.DateCalc.is_smaller(f_date = d.replace(hour=14, minute=30), 
                                                s_date = d.replace(hour=13, minute=30)))
        self.assertFalse(dc.DateCalc.is_smaller(f_date = d.replace(hour=13, minute=37), 
                                                s_date = d.replace(hour=13, minute=35)))
        self.assertFalse(dc.DateCalc.is_smaller(f_date = d.replace(hour=13, minute=37), 
                                                s_time = (13,35)))
        self.assertTrue(dc.DateCalc.is_smaller(f_date = d.replace(hour=13, minute=30), 
                                                s_time = (13,35)))



class TestGetTimeRest(unittest.TestCase):
    def test_hole_func(self):
        # Прямой после обеда не переработок
        d = datetime(2020, 10, 1, 13, 0)
        d = dc.get_day_time_rest(d, reverse = False, work_over = False)
        answer = 15600
        self.assertEqual(answer, d)
        # Прямой до обеда переработка
        d = datetime(2020, 10, 1, 13, 0)
        d = dc.get_day_time_rest(d, reverse = False, work_over = True)
        answer = 22800
        self.assertEqual(answer, d)
        # Прямой до обеда не переработок
        d = datetime(2020, 10, 1, 10, 20)
        d = dc.get_day_time_rest(d, reverse = False, work_over = False)
        answer = 22320
        self.assertEqual(answer, d)
        # Прямой до обеда переработок
        d = datetime(2020, 10, 1, 10, 20)
        d = dc.get_day_time_rest(d, reverse = False, work_over = True)
        answer = 29520
        self.assertEqual(answer, d)
        # Прямой пятница после обеда не переработок
        d = datetime(2020, 10, 2, 15, 20)
        d = dc.get_day_time_rest(d, reverse = False, work_over = False)
        answer = 3600
        self.assertEqual(answer, d)
        # Прямой пятница после обеда переработка
        d = datetime(2020, 10, 2, 15, 20)
        d = dc.get_day_time_rest(d, reverse = False, work_over = True)
        answer = 14400
        self.assertEqual(answer, d)
        # Прямой пятница до обеда не переработок
        d = datetime(2020, 10, 2, 10, 20)
        d = dc.get_day_time_rest(d, reverse = False, work_over = False)
        answer = 18720
        self.assertEqual(answer, d)
        # Прямой пятница до обеда переработок
        d = datetime(2020, 10, 2, 10, 20)
        d = dc.get_day_time_rest(d, reverse = False, work_over = True)
        answer = 29520
        self.assertEqual(answer, d)

        # Обратный до обеда не переработок
        d = datetime(2020, 10, 1, 10, 20)
        d = dc.get_day_time_rest(d, reverse = True, work_over = False)
        answer = 7200
        self.assertEqual(answer, d)
        # Обратный после обеда переработка
        d = datetime(2020, 10, 1, 15, 20)
        d = dc.get_day_time_rest(d, reverse = True, work_over = False)
        answer = 22320
        self.assertEqual(answer, d)
        # Обратный пятница до обеда переработока
        d = datetime(2020, 10, 2, 10, 20)
        d = dc.get_day_time_rest(d, reverse = True, work_over = False)
        answer = 7200
        # Обратный пятница после обеда не переработока
        d = datetime(2020, 10, 2, 15, 20)
        d = dc.get_day_time_rest(d, reverse = True, work_over = False)
        answer = 22320
        self.assertEqual(answer, d)

class TestAddIntradays(unittest.TestCase):
    def test_hole_func(self):
        #No dinner forward
        d = datetime(2020, 10, 1, 10, 0)
        a = dc.add_time_intraday(d, 3600, False)
        b = datetime(2020, 10, 1, 11, 0)
        self.assertEqual(a,b)

        #No dinner reverse
        d = datetime(2020, 10, 1, 10, 0)
        a = dc.add_time_intraday(d, 3600, True)
        b = datetime(2020, 10, 1, 9, 0)
        self.assertEqual(a,b)

        #Dinner forward outside
        d = datetime(2020, 10, 1, 10, 0)
        a = dc.add_time_intraday(d, 2*3600, False)
        b = datetime(2020, 10, 1, 12, 48)
        self.assertEqual(a,b)

        #Dinner reverse outside
        d = datetime(2020, 10, 1, 13, 0)
        a = dc.add_time_intraday(d, 3*3600, True)
        b = datetime(2020, 10, 1, 9, 12)
        self.assertEqual(a,b)

        #Dinner forward outside
        d = datetime(2020, 10, 1, 12, 0)
        a = dc.add_time_intraday(d, 1*3600, False)
        b = datetime(2020, 10, 1, 13, 48)
        self.assertEqual(a,b)

        #Dinner reverse outside
        d = datetime(2020, 10, 1, 12, 0)
        a = dc.add_time_intraday(d, 1*3600, True)
        b = datetime(2020, 10, 1, 10, 12)
        self.assertEqual(a,b)

class TestMoveTime(unittest.TestCase):
    def test_intraday_(self):
        # рабочий день без переработок
        d = datetime(2020, 10, 5, 12, 0)
        d = dc.DateCalc.move_time(d, (1,20), reverse = False, work_over = True, hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 5, 14, 8)
        self.assertEqual(answer, d)
        # рабочий день переработка
        d = datetime(2020, 10, 5, 12, 0)
        d = dc.DateCalc.move_time(d, (6,20), reverse = False, work_over = True, hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 5, 19, 8)
        self.assertEqual(answer, d)

        # рабочий  обратн день без переработок
        d =      datetime(2020, 10, 5, 12, 0)
        d = dc.DateCalc.move_time(d, (0,40), reverse = True, work_over = True, hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 5, 10, 32)
        self.assertEqual(answer, d)
        
        # рабочий  обратн день c переработок
        d =      datetime(2020, 10, 5, 19, 0)
        d = dc.DateCalc.move_time(d, (5,40), reverse = True, work_over = True, hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 5, 13, 20)
        self.assertEqual(answer, d)

    def test_overday_one_day_forwards(self):
        # (рабочий день - рабочий день)  без переработок
        d = datetime(2020, 10, 5, 8, 20)
        d = dc.DateCalc.move_time(d, (10,0), reverse = False, work_over = False, hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 6, 10, 8)
        self.assertEqual(answer, d)

        # (рабочий день - рабочий день)  без переработок задача на полный день
        d = datetime(2020, 10, 5, 8, 20)
        d = dc.DateCalc.move_time(d, (8,12), reverse = False, work_over = False, hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 5, 17, 20)
        self.assertEqual(answer, d)

        # (рабочий день - рабочий день)  переработока
        d = datetime(2020, 10, 5, 8, 20)
        d = dc.DateCalc.move_time(d, (14,0), reverse = False, work_over = True, hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 6, 12, 56)
        self.assertEqual(answer, d)

        # обратн (рабочий день - рабочий день)  без переработок
        d = datetime(2020, 10, 6, 10, 8)
        d = dc.DateCalc.move_time(d, (10,0), reverse = True, work_over = False, hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 5, 8, 20)
        self.assertEqual(answer, d)

        # (рабочий день - рабочий день)  переработока
        d = datetime(2020, 10, 5, 8, 20)
        d = dc.DateCalc.move_time(d, (14,0), reverse = False, work_over = True, hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 6, 12, 56)
        self.assertEqual(answer, d)

        # обратн (рабочий день - выходные)  без переработок
        d = datetime(2020, 10, 6, 10, 8)
        d = dc.DateCalc.move_time(d, (11,0), reverse = True, work_over = False,
                                hol_over = True, sun_over = False, sat_over = False)
        answer = datetime(2020, 10, 2, 15, 20)
        self.assertEqual(answer, d)

        # обратн (рабочий день - выходные)  вс раб
        d = datetime(2020, 10, 6, 10, 8)
        d = dc.DateCalc.move_time(d, (11,0), reverse = True, work_over = False,
                                hol_over = True, sun_over = True, sat_over = True)
        answer = datetime(2020, 10, 4, 16, 20)
        self.assertEqual(answer, d)
