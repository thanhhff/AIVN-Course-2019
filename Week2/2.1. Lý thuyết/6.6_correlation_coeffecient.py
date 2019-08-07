# Hệ số tương quan
# Công thức tính: http://quantri.vn/dict/details/9178-cac-phuong-phap-du-bao

import numpy as np
from PIL import Image
from io import BytesIO
import requests

def find_corr_x_y(x, y):
    n = len(x)
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi * yi)

    sum_prod_x_y = sum(prod)

    sum_x = sum(x)
    sum_y = sum(y)

    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    x_square = []
    for xi in x:
        x_square.append(xi**2)
    x_square_sum = sum(x_square)

    y_square = []
    for yi in y:
        y_square.append(yi**2)
    y_square_sum = sum(y_square)

    numerator = n*sum_prod_x_y - sum_x * sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1 * denominator_term2) ** 0.5
    correlation = numerator / denominator
    return correlation

x = [7, 18, 29, 2, 10, 9, 9]
y = [1, 6, 12, 8, 6, 21, 10]

print('Hệ số tương quan tuyến tính giữa 2 biến x,y:', find_corr_x_y(x,y))

req1 = requests.get('https://www.dropbox.com/s/vfe090qo24t3v46/img1.png?raw=1')
req2 = requests.get('https://www.dropbox.com/s/vtz8ik7mb1e1is7/img2.png?raw=1')
req3 = requests.get('https://www.dropbox.com/s/auxezlf6ijoejwo/img3.png?raw=1')
req4 = requests.get('https://www.dropbox.com/s/w5oc29l57f77arp/img4.png?raw=1')

image1 = Image.open(BytesIO(req1.content))
image2 = Image.open(BytesIO(req2.content))
image3 = Image.open(BytesIO(req3.content))
image4 = Image.open(BytesIO(req4.content))

image1_list = np.asarray(image1).flatten().tolist()
image2_list = np.asarray(image2).flatten().tolist()
image3_list = np.asarray(image3).flatten().tolist()
image4_list = np.asarray(image4).flatten().tolist()

corr_1_2 = find_corr_x_y(image1_list, image2_list)
corr_1_3 = find_corr_x_y(image1_list, image3_list)
corr_1_4 = find_corr_x_y(image1_list, image4_list)

print('corr_1_2:', corr_1_2)
print('corr_1_3:', corr_1_3)
print('corr_1_4:', corr_1_4)


# Một tính chất quan trọng của hệ số tương quan là khả năng hoạt động tốt với linear transformation (dữ liệu thay đổi dạng tuyến tính). 

req5 = requests.get('https://www.dropbox.com/s/wdj080tsf92a0l0/img1_scale2.png?raw=1')
req6 = requests.get('https://www.dropbox.com/s/9fr6h5y9vejyl7h/img1_scale1.png?raw=1')

image5 = Image.open(BytesIO(req5.content))
image6 = Image.open(BytesIO(req6.content))

image5_list = np.asarray(image5).flatten().tolist()
image6_list = np.asarray(image6).flatten().tolist()


# tính correlation coefficient
corr_1_5 = find_corr_x_y(image1_list, image5_list)
corr_1_6 = find_corr_x_y(image1_list, image6_list)

print('corr_1_5:', corr_1_5)
print('corr_1_6:', corr_1_6)
