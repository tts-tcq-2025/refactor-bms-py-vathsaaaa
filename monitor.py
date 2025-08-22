
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
  if temperature > 102 or temperature < 95:
      return "Temperature critical!"
  if pulseRate < 60 or pulseRate > 100:
      return "Pulse Rate is out of range!"
  if spo2 < 90:
      return "Oxygen Saturation out of range!"
  return None

def vitals_ok(temperature, pulseRate, spo2):
  error_message = check_vitals(temperature, pulseRate, spo2)
  if error_message:
      print(error_message)
      blink_alert()
      return False
  return True
