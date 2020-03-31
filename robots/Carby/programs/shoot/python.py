import time


robot.motors["shooter"].move(direction=Motor.DIRECTION_BACK, amount=0.1, unit_amount=Motor.UNIT_SEC, limit=100, unit_limit=Motor.UNIT_SPEED_PWR)
time.sleep(1)
robot.motors["shooter"].move(direction=Motor.DIRECTION_FWD, amount=1, unit_amount=Motor.UNIT_SEC, limit=20, unit_limit=Motor.UNIT_SPEED_PWR)
time.sleep(1)