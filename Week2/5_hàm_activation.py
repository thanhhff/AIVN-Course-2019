import math

# Hàm sigmoid (logistic)
def sigmoid_function(data):
    result = []
    for d in data:
        result.append(1 / (1 + math.exp(-d)))
    return result

# Hàm tanh 
def tanh_function(data):
    result = []
    for d in data:
        result.append(2 / (1 + math.exp(-2*d)) -1)
    return result

# Hàm ReLU
def ReLU_function(data):
    result = []
    for d in data:
        if d < 0:
            result.append(0)
        else:
            result.append(d)
    return result

# Hàm PReLU
def PReLU_function(data, alpha):
    result = []
    for d in data:
        if d < 0:
            result.append(d*alpha)
        else:
            result.append(d)
    return result

# ELU
def ELU_function(data, alpha):
    result = []
    for d in data:
        if d < 0:
            result.append(alpha * (math.exp(d) - 1))
        else:
            result.append(d)
    return result

# Hàm Softplus
def Softplus_function(data):
    result = []
    for d in data:
        result.append(math.log(1 + math.exp(d)))
    return result

data = [1, 5, -4, 3, -2]
result = sigmoid_function(data)
print('Sigmoid:\n',result)

result = tanh_function(data)
print('Tanh:\n', result)

result = ReLU_function(data)
print('ReLU:\n', result)

result = PReLU_function(data, 0.1)
print('PReLU:\n', result)

result = ELU_function(data, 0.1)
print('ELU:\n', result)

result = Softplus_function(data)
print('Softplus:\n', result)
