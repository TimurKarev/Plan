import unittest

from plan_model.order import Order
from plan_model.task import Task
from plan_model.order_xml_fabric import OrderXmlFabric

class TestXMLFabric(unittest.TestCase):
    def test_set_dependencies(self):
        f = OrderXmlFabric()
        order = f.create_order()
        order.get_task_by_name('Заливка_ВМ')