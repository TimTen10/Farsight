import numpy as np


class GeoMap:

    def __init__(self, shape, distance, terrain_function):
        self.shape = shape
        self.distance = distance
        self.terrain_function = terrain_function
        self.height_map =\
            np.array([[self.terrain_function(dim1, dim2) for dim1 in range(shape[1])] for dim2 in range(shape[0])])
