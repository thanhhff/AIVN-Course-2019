import numpy as np
import os
from random import shuffle
from tqdm import tqdm
from PIL import Image

TRAIN_DIR = 'dogs-vs-cats/train'
TEST_DIR = 'dogs-vs-cats/test1'
IMG_SIZE = 50


def label_img(img):
    word_label = img.split('.')[0]
    if word_label == 'cat':
        return 0
    elif word_label == 'dog':
        return 1


def create_train_data():
    X_list = []
    y_list = []
    # modul tqdm duoc su dung de hien thi tien trinh hoan thanh cua chuong trinh
    for img in tqdm(os.listdir(TRAIN_DIR)):
        label = label_img(img)
        path = os.path.join(TRAIN_DIR, img)

        img = Image.open(path)
        img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
        img = np.asarray(img)

        X_list.append(img)
        y_list.append(label)

    X = np.array(X_list)
    y = np.array(y_list)

    np.save('dogs-vs-cats/X.npy', X)
    np.save('dogs-vs-cats/y.npy', y)

    return X, y


X, y = create_train_data()
print(X.shape)
print(y.shape)


def create_test_data():
    X_test_list = []
    for img in tqdm(os.listdir(TEST_DIR)):
        path = os.path.join(TEST_DIR, img)

        img = Image.open(path)
        img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
        img = np.asarray(img)

        X_test_list.append(img)

    X_test = np.array(X_test_list)
    np.save('dogs-vs-cats/X_test.npy', X_test)

    return X_test


X_test = create_test_data()
print(X_test.shape)
