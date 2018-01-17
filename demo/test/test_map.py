from unittest import TestCase

import src.environnement as env


class TestMap(TestCase):
    def test_get_random_path(self):
        mapa = env.Map(9, 20)
        print(mapa)
        rp = mapa.get_random_path()
        print(rp.get_path_length())
