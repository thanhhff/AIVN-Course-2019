import numpy as np
from PIL import Image


def stereo_matching_sad(left_img, right_img, kernel_size, disparity_range):
    # đọc ảnh trái và phải, rồi chuyển sang ảnh grayscale
    left_img = Image.open(left_img).convert('L')
    left = np.asarray(left_img)

    right_img = Image.open(right_img).convert('L')
    right = np.asarray(right_img)

    # Lấy chiều rộng và chiều cao của ảnh
    height, width = left.shape
    # print(left)

    # Tạo disparity map
    depth = np.zeros((height, width), np.uint8)

    kernel_half = int((kernel_size - 1) / 2)
    scale = 255 / disparity_range

    # Xây dựng bảng tổng độ lệch
    memory = np.ones((disparity_range, height, width))

    for j in range(disparity_range):
        print('.', end=' ')

        data = np.ones((height, width))
        for y in range(kernel_half, height - kernel_half):
            for x in range(kernel_half, width - kernel_half):
                if x - j >= 0:
                    data[y, x] = abs(int(left[y, x]) - int(right[y, x - j])) / 255.0

        # Tính sum-area table
        memory[j] = data.cumsum(axis=0).cumsum(axis=1)

    for y in range(kernel_half + 1, height - kernel_half):
        for x in range(kernel_half + 1, width - kernel_half):
            # add constraint for x0=y0=0
            x0 = x - kernel_half
            x1 = x + kernel_half
            y0 = y - kernel_half
            y1 = y + kernel_half

            # Tìm j tại đó cost có giá trị min
            disparity = 0
            cost_min = 1000000  # a large number

            for j in range(disparity_range):
                a = memory[j, y0 - 1, x0 - 1]
                b = memory[j, y1, x0 - 1]
                c = memory[j, y0 - 1, x1]
                d = memory[j, y1, x1]

                sad = d - b - c + a

                if sad < cost_min:
                    cost_min = sad
                    disparity = j

            # Gán j cho cost_min vào disaprity map
            depth[y, x] = int(disparity * scale)

    # Chuyển dữ liệu từ ndarray sang kiểu Imgae và lưu xuống file
    Image.fromarray(depth).save('disparity_map_sad.png')


kernel_size = 9
# stereo_matching_sad('left.png', 'right.png', kernel_size, 16)

stereo_matching_sad('Aloe_left_1.png', 'Aloe_right_1.png', kernel_size, 64)
