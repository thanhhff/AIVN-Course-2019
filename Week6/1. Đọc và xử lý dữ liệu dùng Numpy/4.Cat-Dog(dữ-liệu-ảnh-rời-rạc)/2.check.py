from PIL import Image
import numpy as np

# Check training 25.000 data
indices = list(np.random.randint(25000, size=10))
X = np.load('dogs-vs-cats/X.npy')

for i in range(10):
    im = Image.fromarray(X[indices[i]].reshape(50, 50, 3))
    im.save('dogs-vs-cats/image_' + str(i) + '.jpg')

# Check test 12.500 data
indices = list(np.random.randint(12500, size=5))
X_test = np.load('dogs-vs-cats/X_test.npy')
print(X_test.shape)
for i in range(5):
    im = Image.fromarray(X_test[indices[i]].reshape(50, 50, 3))
    im.save('dogs-vs-cats/image_test_' + str(i) + '.jpg')
