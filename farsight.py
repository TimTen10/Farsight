import itertools

import matplotlib.pyplot as plt
import numpy as np

from geomap import GeoMap
from util.linealgo import bresenham
from util.functions import euclidean_distance


def compute_bresenham_predecessor(height_map):
    """
    Not working as intended.

    :param height_map:
    :return:
    """
    shape = height_map.shape
    predecessors = np.empty(shape)
    # top and bottom row
    for i, j in itertools.product([0, shape[1] - 1], range(shape[1])):
        current_predecessor_list = bresenham(0, 0, i, j)
        for index, point in enumerate(current_predecessor_list[1:]):
            x, y = point
            predecessors[x][y] = current_predecessor_list[index - 1][0]
    # left and right outer column (without top / bottom most element)
    for i, j in itertools.product(range(1, shape[0] - 1), [0, shape[0] - 1]):
        current_predecessor_list = bresenham(0, 0, i, j)
        for index, point in enumerate(current_predecessor_list[1:]):
            x, y = point
            predecessors[x][y] = current_predecessor_list[index - 1][0]
    return predecessors.astype(int)


def visualize(height_map, visibility_map):
    plt.imshow(height_map, cmap="terrain")  # alternative: cmap="gist_earth"
    plt.imshow(visibility_map, cmap="YlOrBr", alpha=0.5)
    plt.show()


def visibility_single_point(geomap, viewpoint, point_in_question):
    # TODO: Note - It would be great, if the bresenham function could add distance, view_angle, etc. while iterating
    # TODO: Looks like recursion, as visibility of a point is dependent on all predecessor points
    # TODO: Along predecessor view_angle seems like something that should be saved in/with a point
    line_of_sight = bresenham(*viewpoint, *point_in_question)
    height_difference = geomap.height_map - (geomap.height_map[viewpoint] + 2)  # ~human height
    distances = np.zeros(geomap.height_map.shape)
    for index, value in np.ndenumerate(height_difference):
        distances[index] = euclidean_distance(viewpoint, index) * geomap.distance
    view_angle = np.arctan2(height_difference, distances)
    view_angle = np.rad2deg(np.nan_to_num(view_angle, copy=False))

    output = np.zeros(geomap.height_map.shape)
    output[viewpoint] = 1
    for index, point in enumerate(line_of_sight[1:]):
        if any([view_angle[i] >= view_angle[point] for i in line_of_sight[:index]]):
            output[point] = 0
        else:
            output[point] = 1

    return output


def neighbors(height_map, i, j):
    pass


def main():
    terrain_function = lambda x, y: 10 * np.sin(0.1 * x) + 10 * np.cos(0.1 * y)
    gm = GeoMap(shape=(1001, 1001), distance=5, terrain_function=terrain_function)
    visibility_map = visibility_single_point(gm, (0, 0), (740, 980))
    visualize(gm.height_map, visibility_map)


if __name__ == "__main__":
    # t = main((1001, 1001), 5)
    # visualize(t)

    # x = np.zeros((10, 10))
    # preds = compute_bresenham_predecessor(x)
    # print(preds)

    main()
