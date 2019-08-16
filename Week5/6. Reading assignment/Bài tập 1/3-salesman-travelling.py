import random
import numpy as np
import matplotlib.pyplot as plt

n = 5  # số lượng thành phố
m = 400  # số lượng cá thể trong quần thể
n_generations = 1000  # số vòng đời
losses = []  # để vẽ biểu đồ

CROSS_RATE = 0.9
MUTATION_RATE = 0.05
BOUND = 100


def load_data():
    map = []
    file = open('data_route.txt', 'r')
    lines = file.readlines()

    # bo header
    for i in range(1, len(lines)):
        strings = lines[i].split(',')

        # bo cot dau tien
        prices = [int(s.strip()) for s in strings[1:]]
        map.append(prices)
    file.close()
    return map


def create_pop():
    return np.random.randint(1, n + 1, size=(m, n))


def compute_loss(pop):
    price = np.array([])
    for individual in pop:
        i = 0
        total = 0
        while i < n - 1:
            a = individual[i] - 1
            b = individual[i + 1] - 1
            total += map[a][b]
            i += 1
        # Cộng với quãng đường thành phố cuối về thành phố đầu
        start = individual[0] - 1
        finish = individual[n - 1] - 1
        total += map[finish][start]

        # Kiểm tra xem có chứa hết thành phố không
        s = set(individual)
        # print(s)
        total += ((n - len(s)) * 100000)
        price = np.append(price, total)

    return price


def compute_fitness(individual):
    loss = compute_loss(individual)
    return 1 / (1 + loss)


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
    mutate_vector = np.random.randint(1, n + 1, size=n)

    mutate_prob = np.random.rand(n)
    mutate_mask = mutate_prob < MUTATION_RATE
    child[mutate_mask] = mutate_vector[mutate_mask]
    return child


def create_new_population(pop, gen=1):
    cost_values = compute_loss(pop)
    fitness = compute_fitness(pop)

    if gen % 10 == 0:
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
    map = load_data()
    print('load_data')
    print(map)

    pop = create_pop()

    for i in range(n_generations):
        pop = create_new_population(pop, i)

    plt.plot(losses[:])
    plt.show()