# price = a*area + b
# First column is 'area' and next is 'price'
# Từ dữ liệu nhà đã cho, hãy dự đoán diện tích căn nhà 800 m^2

import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

n = 2  # size of indivudal (chromosome)
m = 100  # size of population
n_generations = 100  # number of generations
losses = []  # để vẽ biểu đồ quá trình tối ưu

CROSS_RATE = 0.9
MUTATION_RATE = 0.05
BOUND = 100

# Import data
dataframe = pd.read_csv('data.csv', header=None)

areas = np.asarray(dataframe.values[:, 0]).reshape(-1, 1)

prices = dataframe.values[:, 1].reshape(-1, 1)

ones = np.ones((len(areas), 1), dtype=int)
areas = np.concatenate((areas, ones), axis=1)


def plot_dataframe(areas, prices):
    fig = plt.figure('Show dataFrame')
    ax = fig.add_subplot(111)
    plt.xlabel('Diện tích nhà (x100m^2)')
    plt.ylabel('Giá nhà')
    plt.plot(areas, prices, 'o')
    plt.show()


def create_pop():
    return (np.random.random(size=(m, n))) * BOUND


def compute_loss(pop):
    z = abs(np.dot(areas, pop.T))
    losses = abs(z - prices)

    return np.sum(losses, axis=0)


def compute_fitness(pop):
    loss = compute_loss(pop)
    # loss + 1 dưới mẫu tránh trường hợp mẫu = 0
    fitness = 1 / (loss + 1)
    return fitness


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
    mutate_vector = (np.random.random(size=n)) * BOUND

    mutate_prob = np.random.rand(n)
    mutate_mask = mutate_prob < MUTATION_RATE
    child[mutate_mask] = mutate_vector[mutate_mask]
    return child


def create_new_population(pop, gen=1):
    cost_values = compute_loss(pop)
    fitness = compute_fitness(pop)

    if gen % 1 == 0:
        print(gen, '- Best loss: ', np.min(cost_values))
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

    return pop


if __name__ == '__main__':
    population = create_pop()

    for i in range(n_generations):
        population = create_new_population(population, i)

    plt.plot(losses[:])
    plt.show()

    # Du doan can nha 800 m^2
    # print(np.sort(population))
    population = np.sort(population)
    predict = population[-1, :]

    print('Gia tien can nha 800^2: ', 8*predict[0] + predict[1])
