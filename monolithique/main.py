from src.core.engine import Engine
import src.environnments.shortest_path as sp


engine = Engine()
engine.environment = sp.ShortestPathEnv(sp.Map(9, 80))
engine.population_size = 300
engine.make_population()
engine.retained_pct = 75
engine.generation_nbr = 1000
engine.mutation_probability = 0.8
engine.run()

# todo améliorer l'environnement
# corriger les problèmes anodins
# corriger les paramètres (proba muatation ...) en cours d'engine
