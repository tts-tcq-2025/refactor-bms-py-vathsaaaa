
from time import sleep
import sys

def vitalsOutofRange():
  for i in range(6):
    print('\r* ', end='')
    sys.stdout.flush()
    sleep(1)
    print('\r *', end='')
    sys.stdout.flush()
    sleep(1)

def check_vitals(temperature, pulseRate, spo2):
  checks = [
      (temperature < 95, "Temperature critical!"),
      (temperature > 102, "Temperature critical!"),
      (pulseRate < 60, "Pulse Rate is out of range!"),
      (pulseRate > 100, "Pulse Rate is out of range!"),
      (spo2 < 90, "Oxygen Saturation out of range!"),
  ]

  # Return first failing message, or None
  for cond, msg in checks:
      if cond:
          return msg
  return None

def vitals_ok(temperature, pulseRate, spo2):
  error_message = check_vitals(temperature, pulseRate, spo2)
  if error_message:
      print(error_message)
      vitalsOutofRange()
      return False
  return True
