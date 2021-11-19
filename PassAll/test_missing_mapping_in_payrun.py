import unittest
import pandas as pd
import json

with open('mapping.json') as f:
    data = json.load(f)

payrun = pd.read_excel('Payrun.xlsx', header=[0, 1])

payrun_mappings = []
gtn_mappings = []

for m in data['mappings']:
    payrun_mappings += [m]
    
for m in payrun_mappings:
    gtn_mappings.append(data['mappings'][m]['vendor'])
    
no_missed_mappings = True

for x in payrun_mappings:
    if not payrun.filter(regex=".*" + x + "*").bool:
        no_missed_mappings = False
        break

for x in payrun_mappings:
    if x not in payrun.columns:
        no_missed_mappings = False
        break
     
class TestMissingMappingInPayrun(unittest.TestCase):
    def test_missing_mapping_in_payrun(self):
        message = "Pay Elements in the GTN file do not have a mapping in the Payrun File!"
        self.assertTrue(no_missed_mappings, message)