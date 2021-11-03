""" Bài 1 """
print('Bài 1')
print('Hello, world!')
print('Hello', end = ' ' )
print('world', end = '!')

print('Hello', 'Word', sep = ' ')

""" Bài 2 """
print('Bài 2')
num1 = 1.5
num2 = 6.3

sum = num1 + num2

print ('Tổng = ', sum)

""" Bài 3 """
print('Bài 3')
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

sum = num1 + num2

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

num = 8
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))

import cmath
num = 1+2j
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

""" Bài 4 """
a = float(input("Nhập giá trị cho cạnh a :"))
b = float(input("Nhập giá trị cho cạnh b :"))
c = float(input("Nhập giá trị cho cạnh c :"))

if (a+b >= c) and (a+c >=b) and (c+b>=a):
     s = float((a+b+c)/2)
     area = s*(s-a)*(s-b)*(s-c)**0.5
     print('The area of the triangle is %0.2f' %area)
else :
     print('Nhập dữ liệu chưa đúng ')


""" Bài 5  """
a = float(input("Nhập giá trị cho a :"))
b = float(input("Nhập giá trị cho b :"))
c = float(input("Nhập giá trị cho c :"))

if (a == 0):
        if (b == 0):
               if (c == 0 ):
                    print ("Phương trình vô số nghiệm!")
               else :
                    print ("Phương trình vô nghiệm!")
        else:
             x = -c / b
             print ("Phương trình có một nghiệm: x = ",x)
else:
     d = b * b - 4 * a * c
     import math
     if (d > 0):
          sol1  = (float)((-b + math.sqrt(d)) / (2 * a))
          sol2 = (float)((-b - math.sqrt(d)) / (2 * a))
          print ("Phương trình có 2 nghiệm là: sol1  = ", sol1 , " và sol2 = ", sol2)
     elif (d == 0):
          sol1  = (-b / (2 * a))
          print("Phương trình có nghiệm kép: sol1  = sol2 = ", sol1 )
     else:
          print("Phương trình vô nghiệm!")

""" Bài 6 """
print('Bài 6')
x = int(input('Enter value of x: '))
y = int(input('Enter value of y: '))

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

""" Bài 7 """
print('Bài 7')
import random

print(random.randint(0,9))

""" Bài 8  """
print('Bài 8')
kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

""" Bài 9 """
print('Bài 9')
print('Bài 9')
Tc = float(input("Nhập nhiệt độ bạn cần đổi từ °C qua °F : "))

Tf = Tc * 1.8 + 32

print('Nhiệt độ bạn nhập {0} T(°F) = {1}'.format(Tc,Tf))