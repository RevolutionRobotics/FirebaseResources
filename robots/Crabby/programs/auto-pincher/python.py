import time


while True:
  if (robot.sensors["distance"].read()) < 50:
    robot.motors["motor3"].spin(direction=Motor.DIRECTION_FWD, rotation=50, unit_rotation=Motor.UNIT_SPEED_RPM)
    robot.motors["motor6"].spin(direction=Motor.DIRECTION_FWD, rotation=50, unit_rotation=Motor.UNIT_SPEED_RPM)
    time.sleep(5)
    robot.motors["motor3"].stop(action=Motor.ACTION_RELEASE)
    robot.motors["motor6"].stop(action=Motor.ACTION_RELEASE)
  time.sleep(0.05)  # allow other threads to run