import math
from numbers import Number
import time

dist = None
i = None


while True:
  dist = round((robot.sensors["distance"].read()) / 3)
  if dist > 12:
    dist = 12
  i = 0
  for count in range(int(dist)):
    i = (i if isinstance(i, Number) else 0) + 1
    if i <= 2:
      robot.led.set(led_index=i, color='#ff0000')
    else:
      if i <= 9:
        robot.led.set(led_index=i, color='#ffcc00')
      else:
        robot.led.set(led_index=i, color='#009900')
  for count2 in range(int(12 - dist)):
    i = (i if isinstance(i, Number) else 0) + 1
    robot.led.set(led_index=i, color='#000000')
  time.sleep(0.05)  # allow other threads to run