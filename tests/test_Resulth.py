import unittest
from src.models.resulth import Resulth

class TestResulth(unittest.TestCase):

    def test_get_os(self):
        resulth = Resulth()
        response = resulth.get_os(140000)

        self.assertEqual(response.status_code, 200)

    def test_get_ocorrencia(self):
        resulth = Resulth()
        response = resulth.get_ocorrencia(140000)

        self.assertEqual(response.status_code, 200)

    def test_get_log(self):
        resulth = Resulth()
        response = resulth.get_log(6000)

        self.assertEqual(response.status_code, 200)

    def test_get_causa(self):
        resulth = Resulth()
        response = resulth.get_causa(140000)

        self.assertEqual(response.status_code, 200)

    def test_get_defeito(self):
        resulth = Resulth()
        response = resulth.get_defeito(140000)

        self.assertEqual(response.status_code, 200)

    def test_get_equipamento(self):
        resulth = Resulth()
        response = resulth.get_equipamento(153000)

        self.assertEqual(response.status_code, 200)