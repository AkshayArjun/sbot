import pybullet as p
import pybullet_data

# Initialize the simulation
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
snakeId = p.loadURDF("/home/akshay/snake_ws/src/sbot/description/snake_servo.urdf" , [0, 0, 0] , p.getQuaternionFromEuler([0, 0, 0]))

p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)
# Simulation loop

while True:
    # Step the simulation 
    p.stepSimulation()
    p.getCameraImage(320, 200)

# Disconnect from the simulation
p.disconnect()

