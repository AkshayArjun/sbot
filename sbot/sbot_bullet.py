import pybullet as p
import pybullet_data
import math
import time

# Initialize the simulation
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
snakeId = p.loadURDF("/home/akshay/snake_ws/src/sbot/description/snake.urdf" , [0, 0, 12] , p.getQuaternionFromEuler([0, 0, 0]))

p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)
# Simulation loop
print =("------- Simulation started -------")
while True:
    # Get the joint info of the snake
    num_joints = p.getNumJoints(snakeId)
    joint_indices = range(num_joints)

    # Set the joint positions to create a snake-like movement
    for i, joint_index in enumerate(joint_indices):
        joint_info = p.getJointInfo(snakeId, joint_index)
        joint_name = joint_info[1].decode("utf-8")
        joint_type = joint_info[2]

        if joint_type == p.JOINT_REVOLUTE:
            joint_position = 0.8 * math.sin(1* i *time.time())
            p.setJointMotorControl2(snakeId, joint_index, p.POSITION_CONTROL, targetPosition=joint_position)

    # Sleep for a small amount of time to control the simulation speed
    time.sleep(0.0001)
    p.stepSimulation()
   
print("------- Simulation ended -------")
# Disconnect from the simulation
p.disconnect()

