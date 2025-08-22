
from time import sleep
import sys

TEMPERATURE_LOW_THRESHOLD = 95
TEMPERATURE_HIGH_THRESHOLD = 102
PULSE_RATE_LOW_THRESHOLD = 60
PULSE_RATE_HIGH_THRESHOLD = 100
OXY_SAT_LOW_THRESHOLD = 90

checks = [
  (temperature < TEMPERATURE_LOW_THRESHOLD, "Temperature critical!"),
  (temperature > TEMPERATURE_HIGH_THRESHOLD, "Temperature critical!"),
  (pulseRate < PULSE_RATE_LOW_THRESHOLD, "Pulse Rate is out of range!"),
  (pulseRate > PULSE_RATE_HIGH_THRESHOLD, "Pulse Rate is out of range!"),
  (spo2 < OXY_SAT_LOW_THRESHOLD, "Oxygen Saturation out of range!"),
]

def vitalsOutofRange(error_messages):
  for message in error_messages:
    output(message)
    for i in range(6):
      print('\r* ', end='')
      sys.stdout.flush()
      sleep(1)
      print('\r *', end='')
      sys.stdout.flush()
      sleep(1)

def check_vitals(temperature, pulseRate, spo2):

return [msg for cond, msg in checks if cond]

def vitals_ok(temperature, pulseRate, spo2):
  error_messages = check_vitals(temperature, pulseRate, spo2)
  if error_messages:
    vitalsOutofRange(error_message)
    return False
  return True
