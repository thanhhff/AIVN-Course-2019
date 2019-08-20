from PIL import Image
import numpy as np

X_train = np.load('dogs-vs-cats/X.npy')
y_train = np.load('dogs-vs-cats/y.npy')

# Test: 12.500 data
m_test = 12500
X_test = np.load('dogs-vs-cats/X_test.npy')

# Training - 25.000 data
# -> Set: training: 20.000 and Validation: 5.000 data

m_train = 20000
m_validation = 5000

# mask: m_train 20.000 -> 24.999
mask = list(range(m_train, m_train + m_validation))

# Creat validation 5.000 data
X_val = X_train[mask]
y_val = y_train[mask]

# Creat train 20.000 data
# mask: 0 -> 19.999
mask = list(range(m_train))
X_train = X_train[mask]
y_train = y_train[mask]

print("X_train shape: ", X_train.shape)
print("y_train shape: ", y_train.shape)
print("X_val shape: ", X_val.shape)
print("y_val shape: ", y_val.shape)
print("X_test shape: ", X_test.shape)
