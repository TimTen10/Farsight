import numpy as np


class GeoMap:

    def __init__(self, shape, distance):
        self.shape = shape
        self.distance = distance

        # TODO: still kind of hard coded, needs change
        # later on this is going to be a real map anyway
        self.terrain_function = lambda x, y: abs(x - 500 + y - 500)
        self.height_map =\
            np.array([[self.terrain_function(dim1, dim2) for dim1 in range(shape[1])] for dim2 in range(shape[0])])
