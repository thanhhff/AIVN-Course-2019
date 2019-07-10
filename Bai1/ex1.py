# #tao bien number_of_day co gia tri 10
# # number_of_day = 10
# #
# # distance = 10.5
# #
# # gretting = "Hello"
# #
# # is_student = True
# #
# # print(number_of_day)
# # print(distance)
# # print(gretting)
# # print(is_student)
# #
# # print(type(number_of_day))
# # print(type(distance))
# # print(type(gretting))
# # print(type(is_student))

#yeu cau nhap du lieu tu ban phim
input_data = input("Nhap ten cua ban: ")

data_type_input_data = type(input_data)

print("----------------------------")
print(data_type_input_data)
print(input_data)

print("----------------------------")
input_data_age = input("Nhap tuoi cua ban: ")
data_type_input_data_2 = type(input_data)

print("----------------------------")
print(data_type_input_data_2)
print(input_data_age)

print("----------------------------")
#Ep kieu
input_data_age_int = int(input_data_age)
print(type(input_data_age_int))
print("Tuoi cua ban: ", input_data_age_int)
