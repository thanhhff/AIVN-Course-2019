import numpy as np
import matplotlib.pyplot as plt

n = 10  # Chromosome length
m = 100  # population size
n_generations = 200

CROSS_RATE = 0.9
MUTATION_RATE = 0.05
BOUND = 100


# function that needs to be optimized
def sphere_function(x):
    return np.sum(x * x, axis=1)


# find non-zero fitness for selection
def compute_fitness(pred):
    return 1 / (pred + 1)


# nature selection wrt pop's fitness
def select(pop, fitness):
    # binary selection
    idx = np.random.choice(np.arange(m), size=m, replace=True, p=fitness / fitness.sum())
    return pop[idx]


# mating process (genes crossover)
def crossover(s1, s2):
    crossover_prob = np.random.rand(n)
    # crossover_mask trẻ về kết quả True khi thoả mãn điều kiện < CROSS_RATE
    crossover_mask = crossover_prob < CROSS_RATE

    # save s1
    buffer = s1.copy()

    # mating and produce one child
    s1[crossover_mask] = s2[crossover_mask]
    s2[crossover_mask] = buffer[crossover_mask]

    return s1, s2


def mutate(child):
    mutate_vector = (np.random.random(size=n) - 0.5) * BOUND

    mutate_prob = np.random.rand(n)
    mutate_mask = mutate_prob < MUTATION_RATE
    child[mutate_mask] = mutate_vector[mutate_mask]
    return child


# initialize the population
pop = (np.random.random(size=(m, n)) - 0.5) * BOUND

# to print losses
losses = []

# evolution
for g in range(n_generations):
    # compute function value
    cost_values = sphere_function(pop)

    # compute fitness
    fitness = compute_fitness(cost_values)
    if g % 1 == 0:
        print(g, '- Cost: ', np.min(cost_values))
        losses.append(np.min(cost_values))

    pop = select(pop, fitness)
    parent_pop = pop.copy()

    for i in range(m // 2 - 2):
        k1 = np.random.randint(0, m, size=1)
        k2 = np.random.randint(0, m, size=1)

        # Lựa chọn mảng 1 chiều [0]
        s1 = parent_pop[k1].copy()[0]
        s2 = parent_pop[k2].copy()[0]

        s1, s2 = crossover(s1, s2)

        s1 = mutate(s1)
        s2 = mutate(s2)

        # parent is replaced by its child
        pop[2 * i][:] = s1
        pop[2 * i + 1][:] = s2

    # elitism
    two_best = fitness.argsort()[-2:]
    pop[m - 2][:] = parent_pop[two_best[0]].copy()[0]
    pop[m - 1][:] = parent_pop[two_best[1]].copy()[0]

# Plot losses
plt.plot(losses)
plt.xlabel('Generations')
plt.ylabel('losses')
plt.show()
