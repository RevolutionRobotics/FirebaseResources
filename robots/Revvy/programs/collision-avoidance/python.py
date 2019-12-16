while True:
  if (robot.sensors["distance"].read()) < 10:
    robot.drive(direction=Motor.DIRECTION_BACK, rotation=1, unit_rotation=Motor.UNIT_SEC, speed=75, unit_speed=Motor.UNIT_SPEED_RPM)
  time.sleep(0.05)  # allow other threads to run