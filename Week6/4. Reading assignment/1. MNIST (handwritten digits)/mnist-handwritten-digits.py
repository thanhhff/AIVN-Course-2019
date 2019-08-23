import numpy as np
import gzip
import os
import matplotlib.pyplot as plt

# Doc file .gz va xu ly du lieu

def load_handwritten_mnist(path, kind='train'):
    # Load Handwritten_MNIST data from `path`
    labels_path = os.path.join(path, '%s-labels-idx1-ubyte.gz' % kind)
    images_path = os.path.join(path, '%s-images-idx3-ubyte.gz' % kind)

    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784)

    return images, labels

X_train, y_train = load_handwritten_mnist('data/')
print(X_train.shape)

# Lay ngau nhien 100 phan tu trong X_train
indices = list(np.random.randint(X_train.shape[0], size=100))

fig = plt.figure(figsize=(9, 9))
columns = 10
rows = 10

for i in range(1, columns*rows + 1):
    img = X_train[indices[i-1]].reshape(28, 28)
    fig.add_subplot(rows, columns, i)
    plt.axis('off')
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)

plt.show()