import unittest
from src.models.database import DataBase

class TestDataBase(unittest.TestCase):

    def test_select(self):
        database = DataBase()

        query = {
            "sql": "SELECT (?)",
            "params": ["1"]
        }

        query_results = database.query(query)
        self.assertEqual(query_results[0].get("1"), 1)
