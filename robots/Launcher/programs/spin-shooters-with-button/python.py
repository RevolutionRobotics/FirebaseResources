import time

spinning = None
lastPressed = None


spinning = False
lastPressed = robot.time()
while True:
  if (robot.sensors["bumper"].read()) and ((robot.time()) - lastPressed > 1):
    lastPressed = robot.time()
    spinning = not spinning
    if spinning:
      robot.motors["left"].spin(direction=Motor.DIRECTION_FWD, rotation=150, unit_rotation=Motor.UNIT_SPEED_RPM)
      robot.motors["right"].spin(direction=Motor.DIRECTION_BACK, rotation=150, unit_rotation=Motor.UNIT_SPEED_RPM)
    else:
      robot.stop_all_motors(action=Motor.ACTION_RELEASE)
  time.sleep(0.05)  # allow other threads to run