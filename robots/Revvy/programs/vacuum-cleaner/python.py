while True:
  if (robot.sensors["distance"].read()) < 15:
    robot.drive(direction=Motor.DIRECTION_BACK, rotation=1, unit_rotation=Motor.UNIT_SEC, speed=100, unit_speed=Motor.UNIT_SPEED_RPM)
    robot.turn(direction=Motor.DIRECTION_RIGHT, rotation=22.5, unit_rotation=Motor.UNIT_TURN_ANGLE, speed=75, unit_speed=Motor.UNIT_SPEED_RPM)
  else:
    robot.drivetrain.set_speeds(direction=Motor.DIRECTION_FWD, speed=40, unit_speed=Motor.UNIT_SPEED_RPM)
  time.sleep(0.05)  # allow other threads to run