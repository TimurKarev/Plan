from datetime import timedelta, date

from plan_model.order import Order
from plan_model.task import Task

from utils.date_calc import DateCalc

from xml.etree import ElementTree as ET

class OrderXmlFabric:
    def create_order(self, num_order = 0, df = None, type = None):
        
        self.order = Order()
        
        self.order.order_name = num_order

        #TODO сделать обработку исключений и path
        tasks = ET.parse('plan_model/structure.xml').getroot()
        

        for task in tasks:
            name = task.get("name")
            d = task.find("duration").get('days')
            h = task.find("duration").get('hours')
            m = task.find("duration").get('minutes')
            self.order.tasks.append(Task(order=num_order, name = name, duration = (d,h,m)))
        
        for task in tasks:
            name = task.get("name")
            followers = task.findall('follower')
            for f in followers:
                self.order.set_dependence(name, f.attrib['fol'])
        
        self.__set_time_order(date.today())

        return self.order


    def __set_time_order(self, time):
        queue = [self.order.tasks[0].name]
        
        self.order.tasks[0].start = DateCalc.get_next_workday(time)
        self.order.tasks[0].end = self.order.tasks[0].start 

        while len(queue) > 0:
            task = self.order.get_task_by_name(queue[0])
            
        
    def __set_time_task(self, time, task : Task):
        task.start = DateCalc.get_next_workday(time)
        task.end = self.__add_time(task.start, time)
    
    
    def __add_time(self, time, time_to_add):
        ret_time = time

        for _ in range(time_to_add[0]):
            ret_time = DateCalc.get_next_workday(ret_time)
        
        ret_time = DateCalc.move_time(ret_time, (time_to_add[1], time_to_add[2]))
        
        return ret_time