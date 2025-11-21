# 8.1
n = int(input())
i = 1
while i*i <= n:
    print(i*i)
    i += 1

# 8.2
n = int(input())
i = 1
while i*i <= n:
    i += 1
print(i*i)

# 8.3
a = float(input())
znam = 1
while 1/znam >= a:
    print(1/znam)
    znam += 1

# 8.4
a = float(input())
znam = 1
while 1/znam >= a:
    znam += 1
print(1/znam)

# 8.5
a = float(input())
n = 2
while 1 + 1/n >= a:
    print(1 + 1/n)
    n += 1

# 8.6
a = float(input())
n = 2
while 1 + 1/n >= a:
    print(1 + 1/n)
    n += 1

# 8.7
a = float(input())
n = 2
while 1 + 1/n >= a:
    n += 1
print(1 + 1/n)

# 8.8
a = float(input())
n = 2
while 1 + 1/n >= a:
    print(n)
    n += 1

# 8.9
a = float(input())
n = 2
while 1 + 1/n >= a:
    n += 1
print(n)

# 8.10
a = float(input())
n = 1
current = 1
while current < a:
    print(current)
    n += 1
    current = 1 + 1/n

# 8.11
n_input = float(input())
n = 1
current = 1
while current <= n_input:
    n += 1
    current = 1 + 1/n
print(current)

# 8.12
a = float(input())
n = 1
total = 0
while total <= a:
    total += 1/n
    if total > a:
        print(n)
    n += 1

# 8.13
a = float(input())
n = 1
total = 0
while total <= a:
    total += 1/n
    n += 1
print(n-1)

# 8.14
a = float(input())
n = 1
while 1/n >= a:
    n += 1
print(1/n)

# 8.15
m = float(input())
x = 1
while x <= 100:
    y = (x*x + 100)/(x + 200)
    if y < m:
        print(y)
    x += 1

# 8.16
m = float(input())
n = 1
while n/(n+1) < m:
    print(n/(n+1))
    n += 1

# 8.17
num1, num2 = 1, 1
den1, den2 = 1, 1
while True:
    num3 = num1 + num2
    den3 = den1 + den2
    fraction = num3/den3
    prev_fraction = num2/den2
    if abs(fraction - prev_fraction) <= 0.001:
        print(fraction)
        break
    num1, num2 = num2, num3
    den1, den2 = den2, den3

# 8.18
a = float(input())
x = float(input())
epsilon = float(input())
y_prev = a
y_curr = 0.5 * (y_prev + x/(y_prev - 1))
while abs(y_curr**2 - y_prev**2) >= epsilon:
    y_prev = y_curr
    y_curr = 0.5 * (y_prev + x/(y_prev - 1))
print(y_curr)

# 8.19a
fib1, fib2 = 1, 1
total = 0
while fib1 <= 1000:
    total += fib1
    fib1, fib2 = fib2, fib1 + fib2
print(total)

# 8.19b
n = int(input())
fib1, fib2 = 1, 1
while fib1 <= n:
    fib1, fib2 = fib2, fib1 + fib2
print(fib1)
