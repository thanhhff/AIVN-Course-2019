# https://aivietnam.ai/courses/aisummer2019/lessons/reading-assignment-va-bai-tap-lap-trinh/
import math
e = math.e

# Identity f(x) = x
def identity(x):
    y = 1
    return y

# Logistic f(x) = 1 / (1 + e^-x)
def logistic(x):
    y = math.e**(-x) / (1 + math.e**(-x))**2 
    return y

# Tanh f(x)

def tanh(x):
    y = 4 * e**(-2*x) / (1 + e**(-2*x))**2
    return y

# ReLU
def reLU(x):
    y = 0
    if x < 0:
        return y
    else:
        y = 1
        return y

# PReLU
def pReLU(alpha, x):
    if x < 0:
        return alpha
    else:
        return 1

# ELU
def eLU(alpha, x):
    if x < 0:
        return alpha * (e**x)
    else:
        return 1

# SoftPlus
def softPlus(x):
    y = e**x / (1 + e**x)
    return y


x = float(input("Input x: "))
alpha = float(input("Input alpha: "))

print("Identity: ", identity(x))
print("Logistic: ", logistic(x))
print("Tanh: ", tanh(x))
print("ReLU: ", reLU(x))
print("PReLU: ", pReLU(alpha, x))
print("ELU: ", eLU(alpha, x))
print("SoftPlus: ", softPlus(x))

