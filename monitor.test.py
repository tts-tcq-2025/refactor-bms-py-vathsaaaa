import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_any_vital_out_of_range(self):
        self.assertTrue(vitals_ok(98.1, 70, 98))
        self.assertFalse(vitals_ok(102.1, 70, 98))
        self.assertFalse(vitals_ok(94.9, 70, 98))
        self.assertFalse(vitals_ok(98.1, 59, 98))
        self.assertFalse(vitals_ok(98.1, 101, 98))
        self.assertFalse(vitals_ok(98.1, 70, 89))


if __name__ == '__main__':
  unittest.main()


