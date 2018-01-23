class Environment:
    def get_initial_chromosomes(self):
        raise NotImplementedError

    def get_grade(self, individu) -> float:
        raise NotImplementedError

    def choose_mate(self, individu, population):
        raise NotImplementedError

    def mate(self, chromosome_1, chromosome_2):
        raise NotImplementedError

    def mutate(self, chromosomes):
        raise NotImplementedError
