import unittest
from src.models.database import DataBase

class TestDataBase(unittest.TestCase):

    def test_query(self):
        database = DataBase()

        query_object = {
            "sql": "SELECT 1"
        }

        query_results = database.query(query_object)
        self.assertEqual(query_results[0].get("1"), 1)
