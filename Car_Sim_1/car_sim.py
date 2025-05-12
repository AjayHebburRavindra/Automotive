###This Project is to analyse the simulation of two car models to exactly match the travel time between them.
###1.Car 1 is travelling in Clockwise Direction and path trajectory is plotted and translation and rotations vectors are stored in Some file (Will name it later)
###2. Car 2 is travelling in exactly opposite direction by taking the data of path trajectory from car 1 which has travelled.
### Calculate the exact speed a car 2 has to travel if it starts after car 1 is completed the path 5 times to actually beat the car 1 before The number of laps end(Which is 10)
### Plot the trajectory of car 1 only, Plot the difference in speed vs time of both cars as graph. 

###(Further Update: I think of extracting the data find the actual difference if I try to a function called Nitros similarly as in real cars to control speed in secondary way)



# Creating of Car Class and Simulate Movement
class car:
    def __init__(self, position, velocity):      #Error 1 = (FIRST MAJOR ERROR was def__init__ , Sol =  def __init__ - space should be added after def)
        self.position = position
        self.velocity = velocity
        
    def move(self, time_step):
        self.position += self.velocity * time_step
        
        
# Importing the necessary libraries
import numpy as np 
import matplotlib.pyplot as plt

# Defining the path
path = np.array([[0,0],[1,1],[2,4],[3,9],[4,16]]) # This is just an example path which I have created for more intriguing path need to use better (Update will be added here)

# creation of the car instance
car = car(position = np.array([0,0]), velocity = np.array([1,1]))

#Simulate the car movement
trajectory = []

for point in path:
    car.move(time_step = 1)
    trajectory.append(car.position.copy())
    
trajectory = np.array(trajectory)

# Plot the trajectory
plt.plot(path[:,0], path[:,1], 'r--', label='Desired Path')
plt.plot(trajectory[:,0],trajectory[:,1],'b-', label='Car trajectory')
plt.legend()
plt.show()

# This is the simulation of the car 2


# reverse the trajectory
reverse_trajectory = loaded_trajectory[::,-1]

# Create second Car instance
second_car = car(position =  reverse_trajectory[0], velocity = np.array([-1, -1]))

# Simulate the second Car movement
second_trajectory = []

for point in reverse_trajecotry:
    second_car.move(time_step=1)
    second_trajectory.append(second_car.position.copy())
    
second_trajectory = np.array(second_trajectory)


# Plot the reverse trajectory
plt.plot(reverse_trajectory[:, 0], reverse_trajectory[:, 1], 'r-' , label = 'Reverse Path')
plt.plot(second_trajectory[:,0], second_trajectory[:, 1], 'b-' , label = 'Second Car Trajectory')
plt.legend()
plt.show()
