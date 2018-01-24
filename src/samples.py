import random
import copy

import gengine.src.utils as utils


class Individu:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes

    def __repr__(self):
        return f"Individu_{self.chromosomes.__repr__()}"


class Population:
    def __init__(self, nbr: int, environment):
        """
        :type environment: src.core.interfaces.Environment
        """
        self.nbr = nbr
        self.environment = environment
        self.population = [Individu(self.environment.get_initial_chromosomes()) for _ in range(nbr)]

    def mutate(self, proba: float):
        assert 0 < proba <= 1, f"{proba} doit être compris entre 0 et 1"
        for individu in self.population:
            if random.random() < proba:
                individu.chromosomes = self.environment.mutate(individu.chromosomes)

    def _get_item_number_by_percent(self, percent: float) -> int:
        return int((len(self.population) * percent) / 100)

    def _complete_size(self):
        while len(self.population) != self.nbr:
            self.population.append(copy.copy(random.choice(self.population)))

    def select(self, percent_to_retain: float, best_is: bool):
        nbr = self._get_item_number_by_percent(percent_to_retain)
        self.population = sorted(
            self.population,
            key=lambda individu: self.environment.get_grade(individu.chromosomes),
            reverse=best_is
        )[:nbr]
        self._complete_size()

    def generate(self):
        new_pop = []
        for individu in self.population:
            new_pop.append(
                Individu(self.environment.mate(individu.chromosomes, self._choose_mate().chromosomes))
            )
        self.population = new_pop

    def _choose_mate(self) -> Individu:
        return random.choice(self.population)

    @property
    def mean(self):
        return sum([self.environment.get_grade(individu.chromosomes) for individu in self.population]) / len(self.population)

    @property
    def best(self):
        return sorted(
            self.population,
            key=lambda individu: self.environment.get_grade(individu.chromosomes)
        )[0]

    def __repr__(self):
        return f"Population{self.population}"


class ResultSet:
    header = ("population_size", "best", "mean", "retained_pct", "mutation_probability", "generation_nbr", "generation_num", "answer")
    column_size = 25

    def __init__(self, **kwargs):
        for key in self.header:
            self.__dict__[key] = kwargs[key]

    @staticmethod
    def get_header():
        return ''.join(key.ljust(ResultSet.column_size)[:ResultSet.column_size] for key in ResultSet.header)

    def __repr__(self):
        return ''.join(str(getattr(self, key)).ljust(ResultSet.column_size)[:ResultSet.column_size] for key in ResultSet.header)
