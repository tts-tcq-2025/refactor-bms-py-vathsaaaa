import unittest, pytest
from monitor import vitals_ok, check_vitals


class MonitorTest(unittest.TestCase):
    Temperature_Valid = 98.1
    Temperature_Above_Threshold = 102.1
    Temperature_Below_Threshold = 94.9
    PulseRate_Valid = 70
    PulseRate_Above_Threshold = 101
    PulseRate_Below_Threshold = 59
    OxygenSat_Valid = 98
    OxygenSat_BelowThreshold = 89
    logs = []

    def test_ok_when_vitals_in_range(self):
        self.assert check_vitals(self.Temperature_Valid, self.PulseRate_Valid, self.OxygenSat_Valid) == []
    def test_not_ok_lowTemp(self):
        self.assert check_vitals(self.Temperature_Below_Threshold, self.PulseRate_Valid, self.OxygenSat_Valid) == ["Temperature critical!"]
    def test_not_ok_highTemp(self):
        self.assert check_vitals(self.Temperature_Above_Threshold, self.PulseRate_Valid, self.OxygenSat_Valid) == ["Temperature critical!"]
    def test_not_ok_lowPulseRate(self):
        self.assert check_vitals(self.Temperature_Valid, self.PulseRate_Below_Threshold, self.OxygenSat_Valid) == ["Pulse Rate is out of range!"]
    def test_not_ok_hightPulseRate(self):
        self.assert check_vitals(self.Temperature_Valid, self.PulseRate_Above_Threshold, self.OxygenSat_Valid) == ["Pulse Rate is out of range!"]
    def test_not_ok_lowOxySat(self):
        self.assert check_vitals(self.Temperature_Valid, self.PulseRate_Valid, self.OxygenSat_BelowThreshold) == ["Oxygen Saturation out of range!"]
    def test_not_ok_multiple(self):
        errors = check_vitals(self.Temperature_Above_Threshold, self.PulseRate_Above_Threshold, self.OxygenSat_BelowThreshold)
        self.assert "Temperature critical!" in errors
        self.assert "Pulse Rate is out of range!" in errors
        self.assert "Oxygen Saturation out of range!" in errors
        assert len(errors) == 3
    
    def test_vitals_ok_all_ok():
        logs = []
        result = vitals_ok(self.Temperature_Valid, self.PulseRate_Valid, self.OxygenSat_Valid, output=logs.append)
        assert result is True
        assert logs == []

    def test_vitals_ok_with_errors():
        logs = []
        result = vitals_ok(self.Temperature_Above_Threshold, self.PulseRate_Above_Threshold, self.OxygenSat_BelowThreshold, output=logs.append)
        assert result is False
        assert "Temperature critical!" in logs
        assert "Pulse Rate is out of range!" in logs
        assert "Oxygen Saturation out of range!" in logs

if __name__ == '__main__':
  unittest.main()






