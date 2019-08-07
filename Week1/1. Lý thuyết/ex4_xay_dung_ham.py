#Xay dung ham trong python

# def <ten_ham>(<Tham so tuy chon>):

def get_groceries():
    print("Milk")
    print("Flout")
    print("Sugar")
    print("Butter")

get_groceries()

# #Tao ham voi tham so
#
# def hello(name):
#     print("Hi " + name)
#
# name = input("Nhap ten cua ban: ")
# hello(name)

def add_three(value):
    result = value + 3
    print('The sum of', value, 'and 3 is:', result)

add_three(100)

def calculate_average(value1, value2, value3):
    result = (value1 + value2 + value3) / 3
    print('Average value is: ', result)

calculate_average(10, 20 , 30)

#Ham tra ve ket qua!

def add_three_return(value):
    result = value + 3
    return result

sum1 = add_three_return(10)

print('Ket qua:', sum1)