# Hệ số tương quan
# Công thức tính: http://quantri.vn/dict/details/9178-cac-phuong-phap-du-bao

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
