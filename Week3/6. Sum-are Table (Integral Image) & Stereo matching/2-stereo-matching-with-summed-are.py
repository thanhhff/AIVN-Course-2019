import numpy as np
from PIL import Image


def stereo_matching_ssd(left_img, right_img, kernel_size, disparity_range):
    # doc anh trai, doc anh phai roi chuyen sang anh grayscale
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)

    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)

    # Lay chieu rong va chieu cao cua anh
    height, width = left.shape

    # tao disparity map
    depth = np.zeros((height, width), np.uint8)

    kernel_half = int((kernel_size - 1) / 2)
    scale = 255 / disparity_range

    # build sum-area table for each disparity
    memory = np.ones((disparity_range, height, width))
    # print(memory.shape)

    for j in range(disparity_range):
        print('.', end=' ')

        data = np.ones((height, width))
        for y in range(kernel_half, height - kernel_half):
            for x in range(kernel_half, width - kernel_half):
                if x - j >= 0:
                    data[y, x] = abs(int(left[y, x]) - int(right[y, x - j])) / 255.0

        memory[j, 0, 0] = data[0, 0]
        memory[j] = data.cumsum(axis=0).cumsum(axis=1)
        # print(memory.cumsum(axis=0).cumsum(axis=1))

    for y in range(kernel_half + 1, height - kernel_half):
        for x in range(kernel_half + 1, width - kernel_half):

            x0 = x - kernel_half
            x1 = x + kernel_half
            y0 = y - kernel_half
            y1 = y + kernel_half

            # Tim j tai do cost co gia tri min
            disparity = 0
            cost_min = 1000000  # a large number

            for j in range(disparity_range):
                a = memory[j, y0 - 1, x0 - 1]
                b = memory[j, y1, x0 - 1]
                c = memory[j, y0 - 1, x1]
                d = memory[j, y1, x1]
                ssd = d - b - c + a

                if ssd < cost_min:
                    cost_min = ssd
                    disparity = j

            # gan j cho cost min vao diparity map
            depth[y, x] = int(disparity * scale)

    # Chuyen du lieu tu ndarray sang kieu Image va luu xuong file
    Image.fromarray(depth).save('disparity_map_ssd_table.png')


disparity_range = 16  # Cho cap anh Tsukuba
kernel_size = 9
stereo_matching_ssd('left.png', 'right.png', kernel_size, disparity_range)
