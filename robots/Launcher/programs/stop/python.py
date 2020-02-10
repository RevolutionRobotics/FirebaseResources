import time


for motor in robot.motors:
  motor.stop(action=Motor.ACTION_RELEASE)
time.sleep(2)