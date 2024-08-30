import pybullet as p
import pybullet_data

# Initialize the simulation
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
planeId = p.loadURDF("plane.urdf")
snakeId = p.loadURDF("/home/akshay/snake_ws/src/sbot/sbot/snake.urdf" , [0, 0, 0] , p.getQuaternionFromEuler([0, 0, 0]))


# Simulation loop
while True:
    # Step the simulation
    p.stepSimulation()

    p.getCameraImage(320, 200)

# Disconnect from the simulation
p.disconnect()

