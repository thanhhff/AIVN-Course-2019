import random
import matplotlib.pyplot as plt

n = 20  # Số gen của một cá thể (chromosome)
m = 10  # Số cá thể
n_generations = 40  # number of generations

# Để vẽ biểu đồ quá trình tối ưu
fitnesses = []


def generate_random_value():
    return random.randint(0, 1)


def create_individual():
    return [generate_random_value() for _ in range(n)]


def compute_fitness(individual):
    return sum(gen for gen in individual)


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
    sorted_population = sorted(old_population, key=compute_fitness)

    if gen % 1 == 0:
        fitnesses.append(compute_fitness(sorted_population[m - 1]))
        print('BEST:', compute_fitness(sorted_population[m - 1]))

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
        # print(ind.copy())
        new_population.append(ind.copy())

    return new_population


# With m = 10
population = [create_individual() for _ in range(m)]
# print('Old Population')
# for i in population:
#     print(i)

# Thực hiện tối ưu hoá n_generations = 40 lần
for i in range(n_generations):
    population = create_new_population(population, 2, i)

# print('New population')
# for i in population:
#     print(i)


y = [i for i in range(n_generations)]
plt.plot(y, fitnesses)
plt.show()
