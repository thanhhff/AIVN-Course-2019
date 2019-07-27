# Phuong phap 1: dua vao pixel (SM1)
import numpy as np
from PIL import Image


def stereo_matching(left_img, right_img, disparity_range):

    # doc anh trai va anh phai -> roi chuyen sang grayscale
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)

    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)

    # cho truoc chieu rong va chieu cao cua anh
    height = 288
    width = 384

    # tao disparity map
    depth = np.zeros((height, width), np.uint8)
    scale = 255 / disparity_range

    for y in range(height):
        for x in range(width):
            # tim j tai do cost co gia tri min
            disparity = 0
            cost_min = (int(left[y, x]) - int(right[y, x]))**2

            for j in range(1, disparity_range):
                cost = (int(left[y, x]) - int(right[y, x - j]))**2
                if cost < cost_min:
                    cost_min = cost
                    disparity = j

                # da tim duoc j (luu o bien disparity) de cost min
                # gan j do vao disaprity map
                # nhan cho scale de nhin thay ro rang (khong can scale cung duoc)
                depth[y, x] = disparity * scale

    # Chuyen du lieu tu ndarray sang kieu image va luu xuong file
    Image.fromarray(depth).save('disparity_map.png')


if __name__ == '__main__':
    disparity_range = 16  # cho cap anh Tsukuba
    stereo_matching("left.png", "right.png", disparity_range)
