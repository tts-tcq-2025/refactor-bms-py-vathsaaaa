import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    Temperature_Valid = 98.1
    Temperature_Above_Threshold = 102.1
    Temperature_Below_Threshold = 94.9
    PulseRate_Valid = 70
    PulseRate_Above_Threshold = 101
    PulseRate_Below_Threshold = 59
    OxygenSat_Valid = 98
    OxygenSat_BelowThreshold = 89
    def test_not_ok_when_any_vital_out_of_range(self):
        self.assertTrue(vitals_ok(Temperature_Valid, PulseRate_Valid, OxygenSat_Valid))
        self.assertFalse(vitals_ok(Temperature_Above_Threshold, PulseRate_Valid, OxygenSat_Valid))
        self.assertFalse(vitals_ok(Temperature_Valid, Temperature_Below_Threshold, OxygenSat_Valid))
        self.assertFalse(vitals_ok(Temperature_Valid, PulseRate_Above_Threshold, OxygenSat_Valid))
        self.assertFalse(vitals_ok(Temperature_Valid, PulseRate_Valid, PulseRate_Below_Threshold))
        self.assertFalse(vitals_ok(Temperature_Valid, PulseRate_Valid, OxygenSat_BelowThreshold))

if __name__ == '__main__':
  unittest.main()



