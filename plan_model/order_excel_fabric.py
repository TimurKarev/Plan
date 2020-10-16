from plan_model.order import Order
from plan_model.task import Task

class OrderExcelFabric:
    def create_order(self, df, num_order, type):
        self.order = Order()
        self.order.order_df =  df[df.zakaz==num_order]

        for _, row in self.order.order_df.iterrows():
            t = Task(
                    order=row.zakaz,
                    name=row.Task,
                    start=row.Start,
                    end=row.Finish,
                    duration=row.Hours,
                )
            self.order.tasks.append(t)

