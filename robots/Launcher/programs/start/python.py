robot.motors["left"].spin(direction=Motor.DIRECTION_FWD, rotation=150, unit_rotation=Motor.UNIT_SPEED_RPM)
robot.motors["right"].spin(direction=Motor.DIRECTION_BACK, rotation=150, unit_rotation=Motor.UNIT_SPEED_RPM)
time.sleep(2)