import random
import matplotlib.pyplot as plt

n = 5  # so luong thanh pho
m = 400  # so luong ca the trong quan the
n_generations = 1000  # so vong doi
losses = []  # de ve bieu de losses


# load data
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


map = load_data()
print('load_data')
print(map)


# tao individual
def create_individual():
    # list cac thanh pho    
    return [random.randint(1, n) for _ in range(n)]


# tinh loss
def compute_loss(individual):
    i = 0
    price = 0
    while i < n - 1:
        a = individual[i] - 1
        b = individual[i + 1] - 1
        price += map[a][b]
        i += 1
    # cong voi quang duong tp cuoi ve tp dau
    start = individual[0] - 1
    finish = individual[n - 1] - 1
    price += map[finish][start]

    # Kiem tra xem individual co chua het thanh pho khong
    s = set(individual)
    # print(s)
    price += ((n - len(s)) * 1000)

    return price


# tinh fitness
def compute_fitness(individual):
    loss = compute_loss(individual)
    return 1 / (1 + loss)


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
            individual_m[i] = random.randint(1, n)

    return individual_m


# tao quan the moi
def create_new_population(soted_old_population):
    # luu vao losses
    losses.append(compute_loss(sorted_old_population[-1]))

    # in cac gia tri tot nhat qua tung doi
    # print(losses[-1])

    new_population = []
    while len(new_population) < m - 2:
        # chon loc
        individual1 = selection(sorted_old_population)
        individual2 = selection(sorted_old_population)

        # lai ghep
        individual_c1, individual_c2 = crossover(individual1, individual2)

        # dot bien
        individual_m1 = mutate(individual_c1)
        individual_m2 = mutate(individual_c2)

        # cho vao quan the moi
        new_population.append(individual_m1)
        new_population.append(individual_m2)

    # cho 2 con dep nhat cua quan the cu vao quan the moi
    new_population.append(sorted_old_population[-1])
    new_population.append(sorted_old_population[-2])

    return new_population


# tao quan the ban dau
population = [create_individual() for _ in range(m)]

for _ in range(n_generations):
    sorted_old_population = sorted(population, key=compute_fitness)
    population = create_new_population(sorted_old_population)

# hien thi tuyen duong ngan nhat
route_min = sorted_old_population[-1]
route_min.append(sorted_old_population[-1][0])
print('duong di ngan nhat: ', route_min, 'chi phi: ', losses[-1])

plt.plot(losses[:n_generations])
plt.show()
