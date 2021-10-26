import math
from typing import List, Dict
# for diagrams
from matplotlib import pyplot as plt
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = -1


# file choice
choice = 0
while True:
    print("Bring in the number of dataset:\n1. birch1\n2. birch2\n3. birch3\n4. s1\n")
    choice = int(input())
    # choice = 4
    if choice >= 1 & choice <= 4:
        break
    print("You brought in a wrong value\n")
filename = 0
if choice == 1:
    filename = "birch1.txt"
elif choice == 2:
    filename = "birch2.txt"
elif choice == 3:
    filename = "birch3.txt"
elif choice == 4:
    filename = "s1.txt"
# reading from file
file_content = open(filename, 'r')
points = []
for line in file_content:
    temp = line.strip().split(" ")
    points.append(Point(int(temp[0]), int(temp[len(temp) - 1])))
file_content.close()

# taking the number of clusters
number_of_clusters = 0
while True:
    print(f"Bring in the number of clusters (from 1 to {len(points)}): ")
    number_of_clusters = int(input())
    # number_of_clusters = 4
    if 1 <= number_of_clusters <= len(points):
        break
    print("You brought in a wrong value\n")


# changes the points' coordinates and returns list of clusters like points
def k_means_method(_points: List[Point], _number_of_clusters) -> (List[Point], List[List[Point]]):
    # creating clusters with random coordinates
    x_coord = [point.x for point in _points]
    y_coord = [point.y for point in _points]
    # List[Point]
    _clusters = get_points_with_random_coordinates(_number_of_clusters, min(x_coord), max(x_coord),
                                                  min(y_coord), max(y_coord))
    _clusters_points = []
    is_final_distribution = False
    while not is_final_distribution:
        # assigning points to clusters
        # List[List[Point]]
        _clusters_points = assign_points_to_clusters(_points, _clusters)
        # center clusters
        is_final_distribution = center_clusters(_clusters, _clusters_points)
        # build_graphic(_clusters, _clusters_points, plt)
    return _clusters, _clusters_points


def get_points_with_random_coordinates(number_of_points: int, x_min: int, x_max: int, y_min: int, y_max: int) \
        -> List[Point]:
    _clusters = []
    x = []
    y = []
    for i in range(number_of_points):
        temp_x = random.randint(x_min, x_max)
        temp_y = random.randint(y_min, y_max)
        while True:
            if temp_x not in x:
                break
            temp_x = random.randint(x_min, x_max)
        while True:
            if temp_y not in y:
                break
            temp_y = random.randint(y_min, y_max)
        x.append(temp_x)
        y.append(temp_y)
        _clusters.append(Point(temp_x, temp_y))
    return _clusters


# assigning points to clusters
def assign_points_to_clusters(_points: List[Point], _clusters: List[Point]) -> List[list]:
    _clusters_points = []
    for i in range(len(_clusters)):
        _clusters_points.append([])

    if len(_clusters) == 1:
        for point in _points:
            point.cluster = 0
            _clusters_points[0].append(point)
        return _clusters_points

    for point in _points:
        cluster_number = 0
        distance = math.sqrt((point.x - _clusters[0].x)**2 + (point.y - _clusters[0].y)**2)
        for i in range(len(_clusters)):
            new_distance = math.sqrt((point.x - _clusters[i].x)**2 + (point.y - _clusters[i].y)**2)
            if new_distance < distance:
                cluster_number = i
                distance = new_distance
        point.cluster = cluster_number
        _clusters_points[cluster_number].append(point)
    return _clusters_points


def center_clusters(_clusters: List[Point], _clusters_points) -> bool:
    is_coordinates_not_changed = True
    for i in range(len(_clusters)):
        x_sum = 0
        y_sum = 0
        for point in _clusters_points[i]:
            x_sum += point.x
            y_sum += point.y
        divisor = len(_clusters_points[i])
        if divisor == 0:
            divisor = 1
        if _clusters[i].x != x_sum/divisor or _clusters[i].y != y_sum/divisor:
            is_coordinates_not_changed = False
        _clusters[i].x = x_sum / divisor
        _clusters[i].y = y_sum / divisor
    return is_coordinates_not_changed


def build_graphic(_clusters: List[Point], _clusters_points: List[List[Point]], _plt):
    for i in range(len(_clusters)):
        _points_x = [point.x for point in _clusters_points[i]]
        _points_y = [point.y for point in _clusters_points[i]]
        plt.scatter(_points_x, _points_y)
    _clusters_x = [point.x for point in _clusters]
    _clusters_y = [point.y for point in _clusters]
    plt.scatter(_clusters_x, _clusters_y, c="red")
    # plt.show()


def standard_deviation(_clusters: List[Point], _clusters_points: List[List[Point]]) -> int:
    _deviation = 0
    for i in range(len(_clusters)):
        for _point in _clusters_points[i]:
            _deviation += (_point.x - _clusters[i].x) ** 2
            _deviation += (_point.y - _clusters[i].y) ** 2
    return _deviation


clusters = []
clusters_points = []
standard_deviations = {}
for i in range(1, number_of_clusters+1):
    clusters, clusters_points = k_means_method(points, i)
    deviation = standard_deviation(clusters, clusters_points)
    standard_deviations[i] = deviation
    print(f"{i} clusters")

build_graphic(clusters, clusters_points, plt)
plt.show()

plt.plot(standard_deviations.keys(), standard_deviations.values())
plt.show()



