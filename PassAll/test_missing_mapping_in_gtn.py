import unittest
import pandas as pd
import json

with open('mapping.json') as f:
    data = json.load(f)

gtn = pd.read_excel('GTN.xlsx', sheet_name='1')

payrun_mappings = []
gtn_mappings = []

for m in data['mappings']:
    payrun_mappings += [m]
    
for m in payrun_mappings:
    gtn_mappings.append(data['mappings'][m]['vendor'])
    
no_missed_mappings = True

for x in gtn_mappings:
    if x not in gtn.columns:
        no_missed_mappings = False
        break

class TestMissingMappingInGtn(unittest.TestCase):
    def test_missing_mapping_in_gtn(self):
        message = "Pay Elements in the Payrun file do not have a mapping in the GTN File!"
        self.assertTrue(no_missed_mappings, message)