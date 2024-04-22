# Import required modules
import numpy as np
import matplotlib.pyplot as plt

# Meshgrid
resolution = 20  # Increased resolution for a finer grid
x, y = np.meshgrid(np.linspace(-5, 5, resolution), np.linspace(-5, 5, resolution))

# Avoid division by zero by adding a small constant in the denominator
epsilon = 1e-6  # Small constant to avoid division by zero
magnitude = np.sqrt(x**2 + y**2) + epsilon

# Directional vectors normalized for better visualization
u = -y / magnitude
v = x / (magnitude**2)

# Plotting Vector Field with QUIVER
plt.quiver(x, y, u, v, color='g', scale=20, width=0.003)

# Setting the title
plt.title('Vector Field')

# Setting x, y boundary limits based on the linspace values
plt.xlim(-6, 6)
plt.ylim(-6, 6)

# Show plot with grid
plt.grid(True)
plt.show()
