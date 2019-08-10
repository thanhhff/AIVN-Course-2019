import random
import matplotlib.pyplot as plt

def generate_vectors(n = 10, m = 8):
    vectors = [[0]*n for _ in range(m)]
    # print(vectors)
    #
    for i in range(m):
        for j in range(n):
            if random.random() >= 0.5:
                vectors[i][j] = 1

    return vectors

vectors = generate_vectors(10, 8)
print(vectors)

