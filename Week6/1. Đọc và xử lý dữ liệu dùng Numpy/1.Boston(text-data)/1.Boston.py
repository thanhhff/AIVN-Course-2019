import numpy as np

# Use skip_header if csv_file have header
data = np.genfromtxt('boston.csv', dtype='float', delimiter=',', skip_header=1)
print(data.shape)

# Read from col 2 to col -1
# Col1 is ID
X = data[:, 1:-1]
y = data[:, -1]

print(X.shape)
print(X)
print(y.shape)
