
- Đây là những kiến thức mình học từ hướng dẫn của anh [Bá Ngọc](https://www.facebook.com/ngbangoc1706) (Google Developer Group Hanoi - GDG HaNoi Founder and Community Manager)
- Liên kết tới bài học [tại đây](https://github.com/bangoc123/learn-machine-learning-in-two-months/blob/master/python-tutorials/integer-float-boolean.ipynb) 
- Trong bài này mình sử dụng Python 3.7

### I. Integer và Float 

#### 1. Integer 


```python
x = 2
type(x)
```




    int




```python
# Phép cộng
x + 2
```




    4




```python
# Phép nhân 
x * 5
```




    10




```python
# Integer là dạng bất biến (immutable). Khi thực hiện các phép tón trên dạng biến này, một ô nhớ khác được tạo ra và chứa kết quả, giá trị biến ban đầu được bảo toàn

x
```




    2




```python
# Giá trị x chỉ thay đổi khi được gán bởi một giá trị mới 
x = x * 2
print(x)
```

    4



```python
x
```




    4



#### 2. Float


```python
# Tương tự Float cũng là dạng bất biến (immutable)
y = 2.5
```


```python
type(y)
```




    float




```python
# Phép cộng 
y + 3.5
```




    6.0




```python
# Phép chia 
y / 2
```




    1.25




```python
# Bình phương 
y**2
```




    6.25




```python
# Tính bất biến 
y
```




    2.5




```python
y = y / 8
```


```python
y
```




    0.3125



### II. Boolean 

Tham khảo thêm tại [Notes about booleans and logical operators](http://thomas-cokelaer.info/tutorials/python/boolean.html)

#### 1. Khai báo biến 


```python
right = True 
wrong = False 

type(right)
```




    bool



#### 2. Giá trị Boolean?
< Cần nắm chắc để tránh mắc lỗi trong quá trình lập trình Python >


```python
0 == False 
```




    True




```python
1 == True 
```




    True



#### 3. Phép toán so sánh

#### a. Lớn hơn 


```python
10 > 3
```




    True



#### b. Lớn hơn hoặc bằng 


```python
5 >= 5
```




    True



#### c. Nhỏ hơn 


```python
1 < 5
```




    True



#### d. Nhỏ hơn hoặc bằng 


```python
4 <= 4
```




    True



#### e. Bằng 


```python
2 == 2
```




    True



#### f. Không bằng 


```python
3 != 4
```




    True



#### g. Chuỗi so sánh 


```python
z = 20
1 < z > 0
```




    True




```python
20 == z < 60
```




    True




```python
70 > z <= 50
```




    True



#### 4. Phép toán logic

#### a. and 
Cả 2 biểu thức True -> Kết quả: True 


```python
True and True
```




    True




```python
True and False
```




    False




```python
False and True
```




    False




```python
False and False 
```




    False



#### b. or 
Một trong 2 biểu thức True -> Kết quả: True


```python
True or False 
```




    True




```python
False or False
```




    False



#### c. not
Biểu thức phủ định


```python
not True
```




    False




```python
not False
```




    True



#### d.Mức độ ưu tiên


```python
# Thực hiện từ trái qua phải, tương đương với (True and False) or True 

True and False or True
```




    True



#### 5. Phép toán thành viên (Membership Operators)

#### a. in


```python
'i' in 'string'
```




    True




```python
1 in [20, 40, 3]
```




    False



#### b. not in


```python
1 not in [20, 40, 3]
```




    True


