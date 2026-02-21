#mock data
import numpy as np

# Mock illumination values
X = np.array([
    [820, 420, 790, 400],  # strong left
    [410, 850, 390, 830],  # strong right
    [900, 920, 400, 420],  # strong top
    [400, 420, 900, 910],  # strong bottom
    [750, 760, 740, 755],  # balanced
])

# Target outputs (steps to rotate)
Y = np.array([
    [-15,  5],   # rotate left, small up
    [ 20,  5],   # rotate right, small up
    [  0, 25],   # tilt up
    [  0,-20],   # tilt down
    [  0,  0],   # stable
])