import time


robot.motors["gripper"].move(direction=Motor.DIRECTION_FWD, amount=2, unit_amount=Motor.UNIT_SEC, limit=35, unit_limit=Motor.UNIT_SPEED_PWR)
time.sleep(1)