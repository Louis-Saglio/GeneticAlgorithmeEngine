import gengine.src.interfaces as interfaces
import gengine.src.samples as samples


# noinspection PyMethodMayBeStatic,PyUnusedLocal
class Engine:

    def __init__(self):
        self.environment: interfaces.Environment = None
        self.population: samples.Population = None
        self.population_size: int = None
        self.mutation_probability: float = None
        self.retained_pct: float = None
        self.generation_nbr: int = None
        self.begining_stop_condition = lambda i, result_set: False
        self.end_stop_condition = lambda i, result_set: False

    def make_population(self):
        assert self.population_size >= 0
        self.population = samples.Population(self.population_size, self.environment)

    def run(self):
        result_set = None
        for i in range(self.generation_nbr):
            if self.begining_stop_condition(i, result_set):
                break
            self.population.generate()
            self.population.mutate(self.mutation_probability)
            self.population.select(self.retained_pct)
            result_set = samples.ResultSet(**self.__dict__, mean=self.population.mean,
                                           best=self.environment.get_grade(self.population.best.chromosomes), generation_num=i)
            print(result_set)
            # print(self.environment.get_grade(self.population.best))
            if self.end_stop_condition(i, result_set):
                break
