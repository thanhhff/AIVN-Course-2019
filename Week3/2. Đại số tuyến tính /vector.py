import math
# Phep cong 2 vector
def add_vectors(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

def minus_vectors(vector1, vector2):
    return [v1 - v2 for v1, v2 in zip(vector1, vector2)]

def dot_product(vector1, vector2):
    return sum([v1 * v2 for v1, v2 in zip(vector1, vector2)])

def Hadamard_product(vector1, vector2):
    return [v1 * v2 for v1, v2 in zip(vector1, vector2)]

def cosine_similarity(vector1, vector2):
    sumxy = sum([v1*v2 for v1, v2 in zip(vector1, vector2)])
    sumxx = sum([v1*v2 for v1, v2 in zip(vector1, vector1)])
    sumyy = sum([v1*v2 for v1, v2 in zip(vector2, vector2)])

    return sumxy / math.sqrt(sumxx*sumxy)

vector1 = [10, 5]
vector2 = [10, 6]

print('Plus 2 vectors:')
print(add_vectors(vector1, vector2))

print('Minus 2 vectors:')
print(minus_vectors(vector1, vector2))

print('Dot product:')
print(dot_product(vector1, vector2))

print('Hadamard product (Nhân giữa hai ma trận):')
print(Hadamard_product(vector1, vector2))

result = cosine_similarity(vector1, vector2)
print('Cos: ', result)
