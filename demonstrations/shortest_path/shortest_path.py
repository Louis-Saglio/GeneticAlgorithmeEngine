import random
import typing

from gengine import Environment


class Point:

    @staticmethod
    def get_distances_between(a: typing.Tuple[float, float], b: typing.Tuple[float, float]):
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1/2)

    def __init__(self, position: typing.Tuple[float, float]):
        self.position = position

    def __repr__(self):
        return f"Point{self.position.__repr__()}"

    def get_distance_with(self, other: "Point"):
        return Point.get_distances_between(self.position, other.position)


class Path(list):

    def __repr__(self):
        return f"Path_{round(self.get_path_length(), 3)}"

    def get_path_length(self) -> float:
        total = 0
        for i, point in enumerate(self[:-1]):
            total += point.get_distance_with(self[i+1])
        return total


class Map(set):

    def __init__(self, maxi: int, nbr_points: int):
        super().__init__()
        for _ in range(nbr_points):
            self.add(Point((random.random() * maxi, random.random() * maxi)))

    def get_random_path(self) -> "Path":
        return Path(random.sample(self, len(self)))


class ShortestPathEnv(Environment):

    def __init__(self, map_: Map):
        self.map = map_

    def get_grade(self, chromosomes) -> float:
        return chromosomes.get_path_length()

    def get_initial_chromosomes(self):
        return self.map.get_random_path()

    def mutate(self, chromosomes):
        random.shuffle(chromosomes)
        return chromosomes

    def mate(self, chromosome_1, chromosome_2):
        assert len(chromosome_1) == len(chromosome_2)
        assert len(chromosome_1) % 2 == 0, len(chromosome_1)
        return Path(chromosome_1[:int(len(chromosome_1) / 2)] + chromosome_2[:int(len(chromosome_2) / 2)])
