import pandas as pd
import unittest

file = 'GTN.xlsx'

class TestTypeExcel(unittest.TestCase):
    def test_type_excel(self):
      
        # error message in case if test case got failed
        message = "Excel file format cannot be determined, you must specify an engine manually."
        gtn = pd.ExcelFile(file)
        self.assertTrue(gtn, message)