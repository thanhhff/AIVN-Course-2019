import random
import matplotlib.pyplot as plt

# Tìm min hàm sphere: f(x) = x1^2 + x2^2 + ... + x6^2
n = 6  # Số gen của 1 cả thể là 6 trong chromosome
m = 50  # Số chromosome
n_generations = 100  # 100 lần lặp

# Để vẽ biểu đồ quá trình tối ưu
losses = []


def generate_random_value(bound=20):
    return (random.random() * 2 - 1) * bound


def compute_loss(individual):
    # Bài toán tìm min
    return sum(gen * gen for gen in individual)


def compute_fitness(individual):
    # Bài toán tìm max
    loss = compute_loss(individual)
    fitness = 1 / (loss + 1)
    return fitness


def create_individual():
    return [generate_random_value() for _ in range(n)]


def crossover(individual1, individual2, crossover_rate=0.9):
    # Lai ghép giữa 2 cá thể
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()

    for i in range(n):
        if random.random() < crossover_rate:
            # Trong trường hợp True sẽ hoán đổi 2 gen của 2 cá thể với nhau
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]

    return individual1_new, individual2_new


def mutate(individual, mutation_rate=0.05):
    # Đột biến
    individual_m = individual.copy()

    for i in range(n):
        if random.random() < mutation_rate:
            # Trong trường hợp True sẽ đột biến gen đó
            # Đột biến bằng việc random
            individual_m[i] = generate_random_value()

    return individual_m


def selection(sorted_old_population):
    index1 = random.randint(0, m - 1)
    while True:
        index2 = random.randint(0, m - 1)
        # Lựa chọn 2 gen khác nhau trong cá thể
        if index2 != index1:
            break

    # Lựa chọn individual_s trong sorted_population
    individual_s = sorted_old_population[index1]
    if index2 > index1:
        individual_s = sorted_old_population[index2]
    return individual_s


def create_new_population(old_population, elitism=2, gen=1):
    # key=compute_fitness -> Sắp xếp tăng dần
    sorted_population = sorted(old_population, key=compute_fitness)

    if gen % 1 == 0:
        losses.append(compute_loss(sorted_population[m - 1]))
        print('Best loss:', compute_loss(sorted_population[m - 1]))

    new_population = []
    while len(new_population) < m - elitism:
        # Selection
        individual_s1 = selection(sorted_population)
        individual_s2 = selection(sorted_population)

        # Crossover
        individual_c1, individual_c2 = crossover(individual_s1, individual_s2)

        # Mutation
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        new_population.append(individual_m1)
        new_population.append(individual_m2)

    for ind in sorted_population[m - elitism:]:
        new_population.append(ind.copy())

    return new_population


population = [create_individual() for _ in range(m)]

print('Old Population')
for i in population:
    print(i)

for i in range(n_generations):
    population = create_new_population(population, 2, i)

print('New Population')
for i in population:
    print(i)

y = [i for i in range(n_generations)]
plt.plot(y, losses)
plt.show()
