import random
from copy import copy


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
            self.population.append(copy(random.choice(self.population)))

    def select(self, percent_to_retain: float):
        nbr = self._get_item_number_by_percent(percent_to_retain)
        self.population = sorted(
            self.population,
            key=lambda individu: self.environment.get_grade(individu)
        )[:nbr]
        self._complete_size()

    def generate(self):
        new_pop = []
        for individu in self.population:
            new_pop.append(
                Individu(self.environment.mate(individu.chromosomes, self._choose_mate(individu).chromosomes))
            )
        self.population = new_pop

    def _choose_mate(self, individu: Individu) -> Individu:
        return self.environment.choose_mate(individu, self.population)

    @property
    def mean(self):
        return sum([self.environment.get_grade(individu) for individu in self.population]) / len(self.population)

    @property
    def best(self):
        return sorted(
            self.population,
            key=lambda individu: self.environment.get_grade(individu)
        )[0]

    def __repr__(self):
        return f"Population{self.population}"


class ResultSet:
        def __init__(self, mutation_probability, conserved_pct, mean, best, population_size, generation_nbr):
            self.pop = population_size
            self.best = best
            self.moyenne = mean
            self.conserve = conserved_pct
            self.mutation = mutation_probability
            self.nbr_gen = generation_nbr