# 21/05/2019 STAGE DAY 2
# ULB LISA, BRUXELLES, BELGIQUE
# OBJET:
# LEARN THE GRAMMER OF THE PYTHON


print("test0**************************")
print('Hello Word!!')


print("test1**************************")
# Fibonacci series: (the last number is the sum of the two numbers before)
# the sum of two elements defines the next

a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b

print("test2**************************")
i = 256**2
print('the value of i is', i)

print("test2**************************")
a, b = 0, 1
while b < 10:
    print(b, end=",")
    a, b = b, a+b

print("test3: IF bloc**************************")
# x = int(input("Please enter an integer: "))
x = 0;
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    
    print('zero')
elif x == 1:
    print('Single')
else:
    print('More')

print("test4: FOR bloc**************************")
words = ['cat', 'elephant', 'dog', 'bird']
for w in words:
    print(w, len(w))


print("test5: FOR bloc, using the Cutting logo**************************")
words = ['cat', 'elephant', 'dog', 'bird']
wordss = []
for w in words[:]:
    if len(w) > 3:
        print(w, len(w))
        wordss.insert(0, w)  # 插入到列表首位

print(wordss)

print("test6: FOR bloc, Using the function range()**************************")
words = ['cat', 'elephant', 'dog', 'bird']
for i in range(len(words)):
    print((i+1), words[i], len(words[i]))

print("test7: FOR bloc, Using break**************************")
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else: # 与第二个for循环同级，与第二个for循环组合使用，同包含于第一个循环。 在的二个循环未出现break时执行
        print(n, 'is a prime number')

print("test8: FOR bloc, Using continue**************************")
for n in range(2, 15):
    if n % 3 == 0:
        print('Found an %3 number', n)
        continue # 结束本次循环，之后的代码不执行； 并重新开始下一个循环
    print('Found a number', n)


print("test9: DEFINE A FUNCTION, Using while bloc**************************")


def fib(nn):
    """Print a Fibonacci series up to n"""
    aa, bb = 0, 1
    while aa < nn:
        print(aa, end=',')
        aa, bb = bb, aa+bb
    print()


fib(2000)
f = fib
f(100)
print(f(100))

print("test10: DEFINE A FUNCTION, with return **************************")


def fibr(nn):
    """Return a list containing th Fibonacci series uo to n."""
    result = []
    aa, bb = 0, 1
    while aa < nn:
        result.append(aa)
        aa, bb = bb, aa + bb
    return result


f100 = fibr(100)
print(f100)


print("test10: DEFINE A FUNCTION, with initialisation **************************")


def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        # ok = input(prompt)
        ok = 'yes'
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)


print(ask_ok('Do you really want to quit?', 2, 'only yes or no'))


print("test11: DEFINE A FUNCTION, with default effect **************************")
i = 5 # 作为默认值出现


def f(arg=i):
    print(arg)


i = 6
f()
f(i)

print("test12: DEFINE A FUNCTION, example, for store the old values **************************")
L = []


def f1(a, L=[]):
    L.append(a)
    return L


print(f1(1))
print(f1(2))
print(f1(3))

print("test13: DEFINE A FUNCTION, example, if don't want to store the old values **************************")
L = []


def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


print(f2(1))
print(f2(2))
print(f2(3))

print("test14: DEFINE A FUNCTION,use of keyword **************************")


def parrot(voltage, state='a stiff', action='voom', type='Nrwegian Blue'): # 后三个参数为可选参数
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)
print('-----------')
parrot(voltage=1000)
print('-----------')
parrot(voltage=1000000, action='VOOOOOOM')
print('-----------')
parrot(action='VOOOOOOM', voltage=1000000)
print('-----------')
parrot('a million', 'bereft of life', 'jump')
print('-----------')

print("test15: DEFINE A FUNCTION, use *name and **name **************************")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm very sorry, we're all out of", kind)

    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limurger",
           "It's very runny,sir.",
           "It's really very, very runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="CHeese Shop Sketch")


print("test16: DEFINE A FUNCTION, use Arbitrry Argument Lists 可变参数列表 **************************")


def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

print("test17:  参数列表的拆分 **************************")

print(list(range(3, 6)))
args = [3, 10, 2] # 列表， 内部元素仅有3 和 10 和2（指定为start，stop 和 step）
print(list(range(*args))) # * 符号可以拆分列表


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d) # **符可以拆分关键字参数为词典

print("test18: lambda 函数*************************")


def make_incrementor(nn):
    return lambda xx: xx+nn


f = make_incrementor(5)
print(f(0))
print(f(1))
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


def example_Doc_String():
    """Just an example

    the second line don't contain anything
    """
    pass


print(example_Doc_String.__doc__)

