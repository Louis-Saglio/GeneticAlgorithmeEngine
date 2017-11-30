from typing import List

from src.core.samples import Individu


class Environment:
    def get_initial_chromosomes(self):
        raise NotImplementedError

    def get_grade(self, individu: Individu) -> float:
        raise NotImplementedError

    def choose_mate(self, individu: Individu, population: List[Individu]) -> Individu:
        raise NotImplementedError

    def mate(self, chromosome_1, chromosome_2):
        raise NotImplementedError

    def mutate(self, chromosomes):
        raise NotImplementedError
