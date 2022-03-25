import matplotlib.pyplot as plt

from geomap import GeoMap


def main(shape, distance):
    gm = GeoMap(shape, distance)
    return gm.height_map


def compute_bresenham_predecessor(height_map):
    # returns np.array of shape height_map.shape with predecessor
    pass


def visualize(height_map):
    plt.imshow(height_map, cmap="terrain")  # alternative: cmap="gist_earth"
    # plt.imshow(height_map, cmap="tab20c", alpha=0.5)
    plt.show()


def neighbors(height_map, i, j):
    pass


def determine_visible(x, y):
    pass


if __name__ == "__main__":
    t = main((1001, 1001), 5)
    visualize(t)
