import random
import matplotlib.pyplot as plt
import numpy as np

n = 500  # Số gen của một cá thể (chromosome)
m = 100  # Số cá thể
n_generations = 1000  # number of generations

# Để vẽ biểu đồ quá trình tối ưu
fitnesses = []

CROSS_RATE = 0.9
MUTATION_RATE = 0.05


def create_population():
    # np.random.randint(low, high=None, size=None, dtype='l')
    return np.random.randint(2, size=(m, n))


def compute_fitness(pop):
    return np.sum(pop, axis=1)


def select(pop, fitness):
    # binary selection
    idx = np.random.choice(np.arange(m), size=m, replace=True, p=fitness / fitness.sum())
    return pop[idx]


def crossover(s1, s2):
    crossover_prob = np.random.rand(n)
    # crossover_mask trẻ về kết quả True khi thoả mãn điều kiện < CROSS_RATE
    crossover_mask = crossover_prob < CROSS_RATE  # CROSS_RATE = 0.9

    # save s1
    buffer = s1.copy()

    # mating and produce one child
    s1[crossover_mask] = s2[crossover_mask]
    s2[crossover_mask] = buffer[crossover_mask]

    return s1, s2


def mutate(child):
    mutate_vector = np.random.randint(2, size=n)

    mutate_prob = np.random.rand(n)
    mutate_mask = mutate_prob < MUTATION_RATE
    child[mutate_mask] = mutate_vector[mutate_mask]
    return child


def create_new_population(pop, gen=1):
    fitness = compute_fitness(pop)

    if gen % 1 == 0:
        print(gen, '- Best: ', np.max(fitness))
        fitnesses.append(np.max(fitness))

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

    return pop


# Tạo population ban đầu
if __name__ == '__main__':
    pop = create_population()
    for g in range(n_generations):
        pop = create_new_population(pop, g)

    plt.plot(fitnesses[:])
    plt.show()
