# phát biểu: có n = 12 vật có giá trị và cân nặng có trước
# hãy để n vật này vào một cái túi có sức chứa tối đa max_weight = 70kg
# sao cho giá trị trong chiếc túi là lớn nhất.

import random
import matplotlib.pyplot as plt
import numpy as np

n = 12  # Số lượng vật
m = 1000  # Số lượng cá thể trong quần thể
n_generations = 500  # Số đời
fitnesses = []  # Để vẽ đồ thị fitnesses
max_weight = 70  # Khối lượng tối đa cái túi có thể đựng được

CROSS_RATE = 0.9
MUTATION_RATE = 0.05

# Dữ liệu
weights = np.array([1, 2, 5, 7, 10, 12, 15, 23, 32, 33, 35, 37])  # Cân nặng đồ vật
prices = [1, 3, 6, 7, 12, 15, 25, 32, 44, 45, 47, 50]  # Giá trị của các đồ vật tương ứng


def create_pop():
    return np.random.randint(2, size=(m, n))


def compute_weight(pop):
    return np.dot(pop, weights)


def compute_fitness(pop):
    fitness = np.dot(pop, prices)

    w = compute_weight(pop) > max_weight
    fitness[w] = fitness[w] / 100

    return fitness


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


pop = create_pop()

for i in range(n_generations):
    pop = create_new_population(pop, i)

plt.plot(fitnesses[:])
plt.show()
