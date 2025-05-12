# This file contains the Advanced 3D Simulation of the Car using pybullet

import pybullet as p
import pybullet_data

# connection to pybullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())


# Load Plane and Car URDF
# URDF = (URDF stands for Unified Robot Description Format. It is an XML format used to describe all elements of a robot in a structured manner. 
        # URDF files define the physical and visual properties of a robot, including its geometry, kinematics, dynamics, and other relevant attributes.)

plane_id = p.loadURDF('plane.urdf')
car_id = p.loadURDF("racecar/racecar.urdf", [0, 0, 0])

# run the simulation
for _ in range(1000):
    p.stepSimulation()
    p.setRealTimeSimulation(1) # Enables Real-Time Simulation


# Disconnection
p.disconnect()