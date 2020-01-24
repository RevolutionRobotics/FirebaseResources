import time

robot.motors["gripper"].move(direction=Motor.DIRECTION_BACK, amount=90, unit_amount=Motor.UNIT_DEG, limit=20, unit_limit=Motor.UNIT_SPEED_RPM)
time.sleep(1)