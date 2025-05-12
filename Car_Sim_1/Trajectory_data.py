### This data contains trajectory path of and it is stored

import pandas as pd

# Store Trajectory data
trajectory_df = pd.DataFrame(trajectory, columns=['x', 'y'])
trajectory_df.to_csv('trajectory.csv', index = False)

# Load and visualise the traj data
loaded_trajectory = pd.read_csv('trajectory.csv').values

plt.plot(loaded_trajectory[:, 0], loaded_trajectory[:, 1], 'g-', label= 'loaded_trajectory')
plt.legend()
plt.show()


##############
# Further Comments(Shortcut to make comments "Ctrl = /")