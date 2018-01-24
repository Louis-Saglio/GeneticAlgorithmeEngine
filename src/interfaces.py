class Environment:
    def get_initial_chromosomes(self):
        raise NotImplementedError

    def get_grade(self, chromosomes) -> float:
        raise NotImplementedError

    def mate(self, chromosome_1, chromosome_2):
        raise NotImplementedError

    def mutate(self, chromosomes):
        raise NotImplementedError
