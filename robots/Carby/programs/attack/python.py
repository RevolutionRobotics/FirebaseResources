import time


while True:
  if (robot.sensors["distance"].read()) < 20:
    for count in range(3):
      robot.motors["gripper"].move(direction=Motor.DIRECTION_FWD, amount=2, unit_amount=Motor.UNIT_SEC, limit=35, unit_limit=Motor.UNIT_SPEED_PWR)
      time.sleep(0.1)
      robot.motors["gripper"].move(direction=Motor.DIRECTION_BACK, amount=90, unit_amount=Motor.UNIT_DEG, limit=20, unit_limit=Motor.UNIT_SPEED_RPM)
      time.sleep(0.1)
  time.sleep(0.05)  # allow other threads to run