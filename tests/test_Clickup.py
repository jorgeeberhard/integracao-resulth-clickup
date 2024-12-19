import unittest
from src.models.clickup.Clickup import Clickup

class TestClickup(unittest.TestCase):

    def test_post_task(self):
        clickup = Clickup()

        task_object = {
            "name": "nome_teste",
            "description": "Descrição de teste",
            "tags": ["ganesa"]
        }

        response = clickup.post_task(task_object)


        self.assertEqual(response.status_code, 200)

    