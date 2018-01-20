import unittest

from gengine.demonstrations.shortest_path.shortest_path import Map


class TestMap(unittest.TestCase):
    def test_get_random_path(self):
        mapa = Map(9, 20)
        print(mapa)
        rp = mapa.get_random_path()
        print(rp.get_path_length())
