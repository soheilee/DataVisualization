import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.randn(100, 4)

# Create a boxplot
plt.boxplot(data)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Boxplot Example')

# Show the plot
plt.show()
