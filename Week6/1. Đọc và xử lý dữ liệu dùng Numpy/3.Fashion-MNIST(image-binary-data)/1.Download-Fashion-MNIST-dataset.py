import numpy as np
from urllib import request
import gzip
import pickle

filename = [
    ["training_images", "train-images-idx3-ubyte.gz"],
    ["test_images", "train-labels-idx1-ubyte.gz"],
    ["training_labels", "t10k-images-idx3-ubyte.gz"],
    ["test_labels", "t10k-labels-idx1-ubyte.gz"]
]


def download_fashion_mnist(folder):
    base_url = "http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/"
    for name in filename:
        print("Downloading " + name[1] + "...")

        # lưu vào folder data_fashion_mnist
        request.urlretrieve(base_url + name[1], folder + name[1])
    print("Download complete.")


# download dataset và lưu vào folder 'data_fashion_mnist/'
folder = 'data_fashion_mnist/'
download_fashion_mnist(folder)
