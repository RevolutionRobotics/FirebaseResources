while True:
  while robot.sensors["button"].read():
    time.sleep(0.05)  # allow other threads to run
  while not robot.sensors["button"].read():
    time.sleep(0.05)  # allow other threads to run
  robot.motors["left"].spin(direction=Motor.DIRECTION_FWD, rotation=150, unit_rotation=Motor.UNIT_SPEED_RPM)
  robot.motors["right"].spin(direction=Motor.DIRECTION_BACK, rotation=150, unit_rotation=Motor.UNIT_SPEED_RPM)
  while robot.sensors["button"].read():
    time.sleep(0.05)  # allow other threads to run
  while not robot.sensors["button"].read():
    time.sleep(0.05)  # allow other threads to run
  for motor in robot.motors:
    motor.stop(action=Motor.ACTION_RELEASE)
  time.sleep(0.05)  # allow other threads to run