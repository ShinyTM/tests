import unittest
import pandas as pd

class TestEmployeeMissingInGtn(unittest.TestCase):
    def test_employee_missing_in_gtn(self):
        gtn = pd.read_excel('GTN.xlsx', sheet_name='1')
        payrun = pd.read_excel('Payrun.xlsx')
        employees_gtn = set(gtn['employee_id'])
        # checking if every employee is in the other table
        payrun['Match'] = payrun['Employee ID'].isin(employees_gtn).astype(int)
        payrun = payrun.dropna(subset = ['Employee ID'])
        # error message in case if test case got failed
        message = "Employees are present in the Payrun but missing in the GTN File!"
        # assertEqual() to check if there is an employee with no match in the other table
        self.assertEqual(len(payrun['Match'].value_counts()), 1, message)