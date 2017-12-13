from src.core.interfaces import Environment
from src.core.samples import Population


# noinspection PyMethodMayBeStatic,PyUnusedLocal
class Engine:

    def __init__(self):
        self.environment: Environment = None
        self.population: Population = None
        self.nbr_individu: int = None
        self.mutation_probability: float = None
        self.retained_pct: float = None
        self.generation_nbr: int = None

    def run(self):
        for i in range(self.generation_nbr):
            if self.begining_stop_condition(i):
                break
            self.population.generate()
            self.population.mutate(self.mutation_probability)
            self.population.select(self.retained_pct)
            if self.end_stop_condition(i):
                break

    def begining_stop_condition(self, index: int) -> bool:
        return False

    def end_stop_condition(self, index: int) -> bool:
        return False
