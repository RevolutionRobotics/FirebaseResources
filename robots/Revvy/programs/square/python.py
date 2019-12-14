for count in range(4):
  robot.drive(direction=Motor.DIRECTION_FWD, rotation=2, unit_rotation=Motor.UNIT_SEC, speed=75, unit_speed=Motor.UNIT_SPEED_RPM)
  robot.turn(direction=Motor.DIRECTION_LEFT, rotation=90, unit_rotation=Motor.UNIT_TURN_ANGLE, speed=75, unit_speed=Motor.UNIT_SPEED_RPM)