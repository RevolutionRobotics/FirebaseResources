import time


robot.play_tune('robot')
robot.motors["gripper"].move(direction=Motor.DIRECTION_FWD, amount=2, unit_amount=Motor.UNIT_SEC, limit=35, unit_limit=Motor.UNIT_SPEED_PWR)
robot.play_tune('robot')
robot.motors["lift"].move(direction=Motor.DIRECTION_BACK, amount=370, unit_amount=Motor.UNIT_DEG, limit=20, unit_limit=Motor.UNIT_SPEED_RPM)
robot.play_tune('robot')
robot.motors["gripper"].move(direction=Motor.DIRECTION_BACK, amount=90, unit_amount=Motor.UNIT_DEG, limit=20, unit_limit=Motor.UNIT_SPEED_RPM)
robot.play_tune('robot')
robot.motors["lift"].move(direction=Motor.DIRECTION_FWD, amount=370, unit_amount=Motor.UNIT_DEG, limit=20, unit_limit=Motor.UNIT_SPEED_PWR)
robot.play_tune('robot2')
robot.motors["shooter"].move(direction=Motor.DIRECTION_BACK, amount=0.1, unit_amount=Motor.UNIT_SEC, limit=100, unit_limit=Motor.UNIT_SPEED_PWR)
time.sleep(1)
robot.play_tune('yee_haw')
robot.motors["shooter"].move(direction=Motor.DIRECTION_FWD, amount=1, unit_amount=Motor.UNIT_SEC, limit=15, unit_limit=Motor.UNIT_SPEED_PWR)