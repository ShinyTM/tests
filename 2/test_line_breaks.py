import unittest
import pandas as pd

file = 'GTN.xlsx'

class TestTypeExcel(unittest.TestCase):
    def test_type_excel(self):
        gtn = pd.read_excel(file, sheet_name='1')
        # clearing the empty lines
        gtn_wo_breaks = gtn.dropna(axis = 0, how='all')
        # error message in case if test case got failed
        message = "There are line breaks in the GTN File!"
        # assertEqual() to check equality of first & second value
        self.assertEqual(len(gtn_wo_breaks.index), len(gtn.index), message)