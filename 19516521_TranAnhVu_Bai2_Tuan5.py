import numpy as np
import matplotlib.pyplot as plt

# ========================= VẼ ĐỒ THỊ ĐƠN GIẢN =============================

plt.style.use("ggplot")
plt.plot([1, 2, 4, 7, 5, 4])
plt.show() 

plt.plot([-3, -2, 0, 5], [1, 3, 2, 10],color='red')
plt.xlim(-5, 7)
plt.ylim(None, 12)
plt.show()

x = np.linspace(-2, 2, 500)
y = x**2
plt.title('Hàm bình phương')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, y, color='blue')
plt.show()

# ========================= THAY ĐỔI KÍCH THƯỚC ĐỒ THỊ =============================
x = np.linspace(-2, 2, 500)
y = x**2
plt.subplots(figsize=(12, 4))

plt.plot(x, y, color='blue')
plt.title('Hàm bình phương')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(False)    #Thử thay đổi sang giá trị False để xem kết quả
plt.show()

# ========================= ĐỊNH DẠNG ĐƯỜNG THẲNG VÀ MÀU SẮC =============================
x = np.linspace(-2, 2, 500)
y = x**2
plt.plot(x, y, 'b--')
plt.title('Hàm bình phương')
plt.xlabel('x')
plt.ylabel('y = x**2')

plt.show()

x = np.linspace(-1.4, 1.4, 30)
plt.plot(x, x, 'g--')
plt.plot(x, x**2, 'r:')
plt.plot(x, x**3, 'b^')

plt.show()

# ========================= VẼ ĐỒ THỊ CON =============================
x = np.linspace(-1.4, 1.4, 30)
plt.subplot(2, 2, 1)
plt.plot(x, x)         # ma trận đồ thị con 2 dòng, 2 cột, đồ thị thứ nhất trái trên
  
plt.subplot(2, 2, 2)
plt.plot(x, x**2)      # ma trận đồ thị con 2 dòng, 2 cột, đồ thị thứ hai phải trên

plt.subplot(2, 2, 3)   # ma trận đồ thị con 2 dòng, 2 cột, đồ thị thứ ba trái dưới
plt.plot(x, x**3)

plt.subplot(2, 2, 4)
plt.plot(x, x**4)      # ma trận đồ thị con 2 dòng, 2 cột, đồ thị thứ tư phải dưới

plt.show()

x = np.linspace(-1.4, 1.4, 30)
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot = top left
plt.plot(x, x)

plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd subplot = top right
plt.plot(x, x**2)

plt.subplot(2, 1, 2)  # 2 rows, *1* column, 2nd subplot = bottom
plt.plot(x, x**3)
plt.show()

# ========================= THÊM CHỮ VÀ CHÚ THÍCH =============================
x = np.linspace(-1.5, 1.5, 30)
px = 0.8
py = px**2

plt.plot(x, x**2, "b-", px, py, "ro")

plt.text(0, 1.5, "Hàm số \n$y = x^2$", fontsize=15, color='blue', horizontalalignment="center")
plt.text(px, py, "x = %0.2f\ny = %0.2f"%(px, py), rotation=10, color='gray')

plt.show()

# ========================= HISTOGRAMS =============================
data = [1, 1.1, 1.8, 2, 2.1, 3.2, 3, 3, 3, 3]
plt.subplot(2,1,1)
plt.hist(data, bins = 10, rwidth=0.8)

plt.subplot(2,1,2)
plt.hist(data, bins = [1, 1.5, 2, 2.5, 3], rwidth=0.8)

plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

data1 = np.random.randn(100)
data2 = np.random.randn(100) + 3
data3 = np.random.randn(100) + 6

plt.hist(data1, bins=5, color='g', alpha=0.75, label='bar hist') # default histtype='bar'
plt.hist(data2, color='b', alpha=0.65, histtype='stepfilled', label='stepfilled hist')
plt.hist(data3, color='r', label='bar hist')

plt.legend()
plt.show()

# ========================= SCATTER PLOTS =============================
x, y = np.random.rand(2, 10)
plt.scatter(x, y)
plt.show()

scale = np.random.rand(10)
scale = 500 * scale ** 2
plt.scatter(x, y, s=scale)
plt.show()

for color in ['red', 'green', 'blue']:
    n = 10
    x, y = np.random.rand(2, n)
    scale = 500.0 * np.random.rand(n) ** 2
    plt.scatter(x, y, s=scale, c=color, alpha=0.3)

plt.show()

# ========================= BOXPLOTS =============================
data1 = np.random.rand(10)*2 + 5
plt.boxplot(x=data1)
plt.title("Boxplot")
plt.show()


# ========================= LƯU HÌNH VẼ =============================
x = np.linspace(-1.4, 1.4, 30)
plt.plot(x, x**2)
# plt.savefig("my_square_function.png", transparent=True);
plt.savefig("test.jpg")
plt.show()
