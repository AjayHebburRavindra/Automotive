###This Project is to analyse the simulation of two car models to exactly match the travel time between them.
###1.Car 1 is travelling in Clockwise Direction and path trajectory is plotted and translation and rotations vectors are stored in Some file (Will name it later)
###2. Car 2 is travelling in exactly opposite direction by taking the data of path trajectory from car 1 which has travelled.
### Calculate the exact speed a car 2 has to travel if it starts after car 1 is completed the path 5 times to actually beat the car 1 before The number of laps end(Which is 10)
### Plot the trajectory of car 1 only, Plot the difference in speed vs time of both cars as graph. 

###(Further Update: I think of extracting the data find the actual difference if I try to a function called Nitros similarly as in real cars to control speed in secondary wa

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pybullet as p
import pybullet_data
import time

# Car class definition
class Car:
    def __init__(self, position, velocity,turn):
        self.position = position
        self.velocity = velocity
        self.turn = turn

    def move(self, time_step):
        self.position += self.velocity * time_step
        self.turn += self.position

# Define the path (same as in car_sim.py)
path = np.array([[0, 0], [1, 1], [2, 4], [3, 9], [4, 16]])

# Create car instance and simulate movement
car = Car(position=np.array([0, 0]), velocity=np.array([1, 1]), turn=np.array([1,1]))
trajectory = []

for point in path:
    car.move(time_step=1)
    trajectory.append(car.position.copy())

trajectory = np.array(trajectory)

# Plot the trajectory (optional, for visualization)
plt.plot(path[:, 0], path[:, 1], 'r--', label='Desired Path')
plt.plot(trajectory[:, 0], trajectory[:, 1], 'b-', label='Car Trajectory')
plt.legend()
plt.show()

# Store trajectory data
trajectory_df = pd.DataFrame(trajectory, columns=['x', 'y'])
trajectory_df.to_csv('trajectory.csv', index=False)

# Load trajectory data (for further use, optional)
loaded_trajectory = pd.read_csv('trajectory.csv').values

# Reverse the trajectory
reverse_trajectory = loaded_trajectory[::-1]

# Create second car instance and simulate movement
second_car = Car(position=reverse_trajectory[0], velocity=np.array([-1, -1]), turn=np.array([1, 1]))
second_trajectory = []

for point in reverse_trajectory:
    second_car.move(time_step=1)
    second_trajectory.append(second_car.position.copy())

second_trajectory = np.array(second_trajectory)

# Plot the reverse trajectory (optional, for visualization)
plt.plot(reverse_trajectory[:, 0], reverse_trajectory[:, 1], 'r--', label='Reverse Path')
plt.plot(second_trajectory[:, 0], second_trajectory[:, 1], 'b-', label='Second Car Trajectory')
plt.legend()
plt.show()

# Connect to PyBullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load plane and car URDF
plane_id = p.loadURDF('plane.urdf')
car_id = p.loadURDF("racecar/racecar.urdf", [0, 0, 0])

# Run the simulation
try:
    for _ in range(10000):  # Increase the range for a longer simulation
        p.stepSimulation()
        time.sleep(1./240.)  # Adjust the sleep time to match the desired simulation speed
finally:
    # Disconnect from PyBullet
    p.disconnect()