import numpy as np
import scipy as sp
import assignment5 as a5

def enum(**enums):
    return type('Enum', (), enums)

Directions = enum(X=1, Y=0)

def getAvgDerivativeKernel(direction):
    if direction == Directions.X:
        return np.array([[0, 0, 0],
                         [-0.5, 0, 0.5],
                         [0, 0, 0]])
    elif direction == Directions.Y:
        return np.array([[0, -0.5, 0],
                        [0, 0, 0],
                        [0, 0.5, 0]])
    else:
        return None

def getPrewittKernel(direction):
    if direction == Directions.X:
        return np.array([[-1, 0, 1],
                         [-1, 0, 1],
                         [-1, 0, 1]])
    elif direction == Directions.Y:
        return np.array([[-1, -1, -1],
                         [0, 0, 0],
                         [1, 1, 1]])

    else:
        return None

def getSobelKernel(direction):
    if direction == Directions.X:
        return np.array([[-1, 0, 1],
                         [-2, 0, 2],
                         [-1, 0, 1]])
    elif direction == Directions.Y:
        return np.array([[-1, -2, -1],
                         [0, 0, 0],
                         [1, 2, 1]])
    else:
        return None

def getGaussianDerivativeKernel(direction, gaussian):
    if direction == Directions.X:
        return a5.imageGradientX(gaussian)
    elif direction == Directions.Y:
        return a5.imageGradientY(gaussian)
    else:
        return None

