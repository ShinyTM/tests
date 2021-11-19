import unittest
import pandas as pd

class TestEmployeeMissingInPayrun(unittest.TestCase):
    def test_employee_missing_in_payrun(self):
        gtn = pd.read_excel('GTN.xlsx', sheet_name='1')
        payrun = pd.read_excel('Payrun.xlsx') 
        employees_payrun = set(payrun['Employee ID'])
        gtn['Match'] = gtn['employee_id'].isin(employees_payrun).astype(int)
        gtn = gtn.dropna(subset = ['employee_id'])
        # error message in case if test case got failed
        message = "Employees are present in the GTN but missing in the Payrun File!"
        # assertEqual() to check equality of first & second value
        self.assertEqual(len(gtn['Match'].value_counts()), 1, message)