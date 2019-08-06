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

# Dữ liệu
weights = [1, 2, 5, 7, 10, 12, 15, 23, 32, 33, 35, 37]  # Cân nặng đồ vật
prices = [1, 3, 6, 7, 12, 15, 25, 32, 44, 45, 47, 50]  # Giá trị của các đồ vật tương ứng


def generate_random_value():
    return random.randint(0, 1)


def create_individual():
    return [generate_random_value() for _ in range(n)]


def compute_weight(individual):
    return sum(c * x for x, c in zip(weights, individual))


def compute_fitness(individual):
    fitness = sum(c * x for x, c in zip(prices, individual))
    if compute_weight(individual) > max_weight:
        fitness /= 1000
    return fitness


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
        print(gen, '- BEST:', compute_fitness(sorted_population[m - 1]))

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


population = [create_individual() for _ in range(m)]

for i in range(n_generations):
    population = create_new_population(population, 2, i)

plt.plot(fitnesses[:n_generations])
plt.show()

sorted_population = sorted(population, key=compute_fitness)
individual_best = sorted_population[-1]

print(individual_best)
print('Tong trong luong: ', np.dot(weights, individual_best))
print('Gia tri: ', np.dot(prices, individual_best))
