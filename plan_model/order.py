from plan_model.task import Task

class Order:
    def __init__(self):
        self.order_name = None
        self.tasks = []
        self.order_df = None

    def get_task_by_name(self, name):
        task = None
        
        for t in self.tasks:
            if t.name == name:
                task = t
                break
        
        return task

    def set_dependence(self, name1, name2):

        task1 = self.get_task_by_name(name1)
        if task1 is None:
            return False

        task2 = self.get_task_by_name(name2)
        if task2 is None:
            return False

        task1.followers.append(task2)
        task2.predecessors.append(task1)

        return True

    def __str__(self):
        return str(self.order_name) + ' ' + str(len(self.tasks)) + ' -tasks'
    
    def __repr__(self):
        return self.__str__()