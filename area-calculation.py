# 这一行调用了 print() 函数。
# 引号里的内容是一个字符串，
# print() 会把它显示在终端中。
print("hello!")
print("never mind")

# 这一行创建了一个叫 width 的变量。
# 等号 (=) 把 15 赋值给这个变量。
width = 15

# 这一行创建了一个叫 height 的变量。
# 等号 (=) 把 4 赋值给这个变量。
height = 4

# 这一行计算 width * height。
# 等号把计算结果存放到 area 变量里。
# 星号 * 在 Python 里表示乘法运算符。
area = width * height

# 这一行再次调用 print() 函数。
# 这里使用了 f-string，
# 所以 Python 会把变量的值插入到字符串中。
print(f"The area of a rectangle with width {width} and height {height} is {area}.")

# 这一行再次调用 print() 函数。
# 它单独显示 area 里保存的数字值。
# area 没有加引号，因为它是数字，不是文字。
print(area)