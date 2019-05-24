from HelloWordTest1 import fib
import sys
import HelloWordTest1

print("test0  列表推导式**************************")

# 用for语句实现功能，但变量x在结束后仍然存在
squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

# 方法二
squaress = list(map(lambda x: x**2, range(10)))
print(squaress)

# 方法三

squaresss = [x**2 for x in range(10)]
print(squaresss)

k = [(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x != y]
print(k)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(vec[1][2])
t_vec = [num for elem in vec for num in elem]   #   **num**   **for elem in vec**   **for num in elem**
# 第一个for产生elem， 其元素为长度为3的列表； 第二个for产生num， 将前面的elem分开， 输出到num上
print(t_vec)

print("test1  嵌套的列表推导式**************************")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 求矩阵的转置
matrix_p = [[row[i] for row in matrix] for i in range(4)] # 每个 **row** 都是长度为4的列表，row[i] 是取其第i位组成一个新的列表
print(matrix_p)

matrix_pp = list(zip(*matrix))

print(matrix_pp)


string1, string2, string3 = '', 'tomads', 'hae deef'

notnule = string2 and string3
print(notnule)

fib(500)

print(sys.path)
print(dir(HelloWordTest1))



