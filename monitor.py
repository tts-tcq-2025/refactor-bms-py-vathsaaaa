
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

def vitals_ok(temperature, pulseRate, spo2):
  checks = [
      (temperature > 102 or temperature < 95, "Temperature critical!"),
      (pulseRate < 60 or pulseRate > 100, "Pulse Rate is out of range!"),
      (spo2 < 90, "Oxygen Saturation out of range!"),
  ]
  
  for condition, message in checks:
      if condition:
          print(message)
          vitalsOutofRange()
          return False
  return True
