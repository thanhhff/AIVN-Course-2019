# Phep cong 2 vector

def add_vectors(vector1, vector2):
    return [v1 + v2 for v1, v2 in zip(vector1, vector2)]

vector1 = [10, 5]
vector2 = [10, 6]

print(add_vectors(vector1, vector2))

