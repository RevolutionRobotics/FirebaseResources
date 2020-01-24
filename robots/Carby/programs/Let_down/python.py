import time

robot.motors["lift"].move(direction=Motor.DIRECTION_FWD, amount=370, unit_amount=Motor.UNIT_DEG, limit=20, unit_limit=Motor.UNIT_SPEED_PWR)
time.sleep(1)