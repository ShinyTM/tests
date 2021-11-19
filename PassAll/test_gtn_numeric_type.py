import pandas as pd
import unittest

gtn = pd.read_excel('GTN.xlsx', sheet_name='1')

gtn = gtn.drop(['employee_id', 'tax_id', 'firstname', 'lastname'], axis=1)

numeric = True;

dtypes = gtn.dtypes.to_dict()

for col_name, typ in dtypes.items():
    if (typ != 'float64' and typ != 'int64'):
        numeric = False
        break
        
class TestGtnNumericType(unittest.TestCase):
    def test_gtn_numeric_type(self):
        message = "The values in GTN file's Pay Elements have non-numeric type"
        # assertEqual() to check equality of first & second value
        self.assertTrue(numeric, message)
    
