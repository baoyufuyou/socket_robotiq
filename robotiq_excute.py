from Robotiq.robotiq85 import Robotiq85
import time

SOCKET_HOST = "10.3.15.94"
SOCKET_PORT = 30003
SOCKET_NAME = "gripper_socket"

gripper = Robotiq85(socket_host=SOCKET_HOST, socket_port=SOCKET_PORT)

# gripper.current_pose_mm()
# time.sleep(2)


gripper.rq_open_and_wait()
# time.sleep(2)

gripper.rq_close_and_wait()
# time.sleep(2)
# gripper.move_to_mm(128)
# time.sleep(2)
# gripper.rq_move_mm(85)
gripper.rq_move_mm(0.04)
# time.sleep(1)
gripper.motion()
gripper.close_socket()