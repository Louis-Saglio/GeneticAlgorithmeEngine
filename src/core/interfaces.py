import typing

import src.core.samples as samples


class Environment:
    def get_initial_chromosomes(self):
        raise NotImplementedError

    def get_grade(self, individu: samples.Individu) -> float:
        raise NotImplementedError

    def choose_mate(self, individu: samples.Individu, population: typing.List[samples.Individu]) -> samples.Individu:
        raise NotImplementedError

    def mate(self, chromosome_1, chromosome_2):
        raise NotImplementedError

    def mutate(self, chromosomes):
        raise NotImplementedError
