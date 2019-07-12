list_goc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_moi = list(filter(lambda a: (a % 2 == 0), list_goc))

print(list_moi)
