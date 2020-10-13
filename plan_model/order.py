from plan_model.task import Task

class Order:
    def __init__(self, df, num_order):
        self.name = num_order
        self.tasks = []
        self.order_df = df[df.zakaz==num_order]

        for _, row in self.order_df.iterrows():
            t = Task(
                    order=row.zakaz,
                    name=row.Task,
                    start=row.Start,
                    end=row.Finish,
                    duration=row.Hours,
                )
            self.tasks.append(t)
        
        self.set_dependence('ЗаливкаНМ', '')

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
        return str(self.name) + ' ' + str(len(self.tasks)) + ' -tasks'