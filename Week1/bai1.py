#Chuyen goc tu do sang radian

import math

degree = float(input("Input Degree: "))

#tinh goc theo radian
radian = degree * math.pi / 180

print("Radian: ", radian)

#Chuyen goc tu radian -> do

radian_change = float(input("Input Radian: "))

degree_change = radian * 180 / math.pi

print("Degree: ", degree_change)
