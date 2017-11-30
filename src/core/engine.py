from pprint import pprint

from src.core.interfaces import Environment
from src.core.samples import Population


def main(env: Environment, nbr_individu: int, nbr_generations: int, muta_prob: float, elected_prop: float, log=False):
    pop = Population(nbr_individu, env)
    pop.generate()
    for _ in range(nbr_generations):
        pop.generate()
        pop.mutate(muta_prob)
        pop.select(elected_prop)
        if log:
            print(f"Mutation : {format(muta_prob, '.2f')},\tconservé : {elected_prop}%,\t"
                  f"moyenne : {format(pop.mean, '.3f')},\tbest : {round(pop.environment.get_grade(pop.best), 3)}")
        if round(pop.environment.get_grade(pop.best), 3) == 0:
            print(_)
            break


if __name__ == '__main__':
    from src.environnments.shortest_path import CustomEnv, Map
    rep = []
    mapa = Map(9, 100)
    for i in range(1):
        main(CustomEnv(mapa), 100, 1000, 1, 90, True)
        # main(CustomEnv(mapa), 300, 100, 0.1, 74)
