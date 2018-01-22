import typing

import gengine


class Environment:
    def get_initial_chromosomes(self):
        raise NotImplementedError

    def get_grade(self, individu: gengine._Individu) -> float:
        raise NotImplementedError

    def choose_mate(self, individu: gengine._Individu, population: typing.List[gengine._Individu]) -> gengine._Individu:
        raise NotImplementedError

    def mate(self, chromosome_1, chromosome_2):
        raise NotImplementedError

    def mutate(self, chromosomes):
        raise NotImplementedError
