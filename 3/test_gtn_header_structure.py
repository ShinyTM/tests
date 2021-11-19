import pandas as pd
import unittest


gtn = pd.read_excel('GTN.xlsx', sheet_name='1', header = 0)

print(gtn.head())

shape = gtn.shape
print('Number of columns :', shape[1])

##TODO

        
class TestGtnHeaderStructure(unittest.TestCase):
    def test_gtn_header_structure(self):
        
        self.assertTrue(numeric, message)
    
