""" 1.1 Viết chương trình kiểm tra một số là số dương, số âm hay bằng không không """
""" Dạng 1 if ... elif ... else """
num = float(input("Nhập vào một số: "))
if num > 0:
    print("Số dương")
elif num == 0:
    print("Số 0")
else:
    print("Số âm")

"""  Dạng 2: Nested if """
num = float(input("Nhập vào một số: "))

if num > 0 :
    if num == 0 :
        print('Số 0')
    else : 
        print('Số dương')
else :
    print('Số âm')
""" 1.2. Viết chương trình kiểm tra một năm có phải năm nhuận không. """
year = int(input("Nhập năm: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} là năm nhuận".format(year))
        else:
            print("{0} không phải là năm nhuận".format(year))
    else:
        print("{0} là năm nhuận".format(year))
else:
    print("{0} không phải là năm nhuận".format(year))

""" # Sử dụng lệnh if ... elif ... else """
year = int(input("Nhập năm: "))

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print("{0} là năm nhuận".format(year))
else:
    print("{0} không phải là năm nhuận".format(year))

""" 1.3. Viết chương trình kiểm tra một số nguyên có phải số nguyên tố không. Nếu không phải là số nguyên tố in ra lý do. """

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print("{0} khong la so nguyen to!".format(num))
            break
        else:
            print(num," là số nguyên tố")
            break
else:
    print(num,"không phải là số nguyên tố")

""" 1.4. Viết chương trình in ra tất cả các số nguyên tố trong khoảng (a,b)"""

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:    
        for j in range(2, num):
            if num % j == 0:
                break
        else:
            print(num, end=' ')

""" 1.5. Viết chương trình in ra 5 số Armstrong bé nhất. """
count = 0
num = 1

while count < 5:
    temp = num
    sum = 0
    order = len(str(num))

    while temp>0:                                                
        digit = temp%10                                              
        sum = sum + (digit**order)                                        
        temp = temp//10
        print(temp)                                             
        if num == sum:                                                
            print(num) 
            count += 1
    num += 1

""" 2.1. Viết hàm nhận vào một số nguyên, trả về giá trị True nếu nó là số nguyên tố, và False nếu nó không phải là số nguyên tố """
def prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
                break
            else:
                return True
                break
    else:
        return False

n = int(input("Nhập vào một số:"))

if prime(n):
    print(n, 'là số nguyên tố')
else:
    print(n, 'không phải là số nguyên tố')

""" 2.2. Viết hàm nhận vào một số nguyên, trả về giá trị True nếu nó là số Armstrong, và False nếu nó không phải là số Armstrong. """
def armstrong(n):
    s = 0                                                     
    k = n                                                     
    while k>0:                                                
        d = k%10                                              
        s = s + (d**3)                                        
        k = k//10                                             
    if n == s:                                                
        return True      
    else:                                                       
        return False

n = 1

if armstrong(n):
    print(n, 'là số armstrong')
else:
    print(n, 'không phải là số armstrong')