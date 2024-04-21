import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# generate random data for the starting points
n = 10
data = np.random.rand(n, 2)
df = pd.DataFrame(data, columns=['x', 'y'])

# generate random vectors (directions and magnitudes)
vector_data = np.random.rand(n, 2) - 0.5  # Subtract 0.5 to allow for negative directions
df['u'] = vector_data[:, 0]
df['v'] = vector_data[:, 1]

# plot the data with vectors
fig, ax = plt.subplots()
# The arguments are x positions, y positions, x components, y components
ax.quiver(df['x'], df['y'], df['u'], df['v'], angles='xy', scale_units='xy', scale=1, color='r')
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title('Vector Field Representation')
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.grid(True)  # Optional, but helps to visualize scales and positions
plt.show()
