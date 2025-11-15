# 5.64
num = 1234567
reversed_num = 0
temp = num
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10
print(reversed_num)

# 5.65
n = 6
square = 0
for i in range(1, 2*n, 2):
    square += i
print(square)

# 5.66
total = 0
for n in range(1, 13):
    square = 0
    for i in range(1, 2*n, 2):
        square += i
    total += square
print(total)

# 5.67
n = 5
start = n * (n - 1) + 1
total = 0
for i in range(n):
    total += start + 2*i
print(total)

# 5.68
n = 5
total = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += factorial
print(total)

# 5.69
n = 5
total = 1
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += 1 / factorial
print(total)

# 5.70
n = 5
x = 2
total = 1
factorial = 1
power = 1
for i in range(1, n + 1):
    factorial *= i
    power *= x
    total += power / factorial
print(total)

# 5.71
import math
result = math.sqrt(50)
for i in range(49, 0, -1):
    result = math.sqrt(i + result)
print(result)

# 5.72
import math
n = 5

total_a = 0
sin_sum = 0
for i in range(1, n + 1):
    sin_sum += math.sin(i)
    total_a += 1 / sin_sum
print(f"a) {total_a}")

result_b = math.sqrt(2)
for i in range(2, n + 1):
    result_b = math.sqrt(2 + result_b)
print(f"b) {result_b}")

total_c = 0
cos_sum = 0
for i in range(1, n + 1):
    cos_sum += math.cos(i)
    total_c += cos_sum
print(f"c) {total_c}")

total_d = 0
sin_sum = 0
for i in range(1, 2*n + 1):
    sin_sum += math.sin(i)
    total_d += sin_sum
print(f"d) {total_d}")

result_e = math.sqrt(3*n)
for i in range(n-1, 0, -1):
    result_e = math.sqrt(3*i + result_e)
print(f"e) {result_e}")

# 5.73
import math
length = 4.5
distance = 3
while distance > 0:
    angle = math.degrees(math.acos(distance / length))
    print(f"Расстояние: {distance:.1f} м, Угол: {angle:.1f}°")
    distance -= 0.2

# 5.74
print("Вариант 1:")
for i in range(10, 101):
    if i % 2 != 0:
        print(i)

print("Вариант 2:")
for i in range(11, 101, 2):
    print(i)

# 5.75
for i in range(100, 201):
    if i % 3 == 0:
        print(i)

# 5.76
a, b, c = 10, 50, 7
for i in range(a, b + 1):
    if i % c == 0:
        print(i)

# 5.77
for i in range(10, 100):
    if i % 2 != 0 and (i % 10 == 3 or i % 10 == 7):
        print(i)

# 5.78
for i in range(100, 1000):
    if i % 47 == 43 and i % 43 == 45:
        print(i)

# 5.79
for i in range(1000, 10000):
    if i % 133 == 125 and i % 134 == 111:
        print(i)

# 5.80
n = 3
for i in range(10, 100):
    if i % n == 0 or str(n) in str(i):
        print(i)

# 5.81
print("a):")
for i in range(100, 1000):
    if i**2 % 1000 == i:
        print(i)

print("б):")
for i in range(100, 1000):
    if i % 7 == 0:
        digit_sum = sum(int(d) for d in str(i))
        if digit_sum % 7 == 0:
            print(i)

# 5.82
print("a):")
for i in range(10, 100):
    digits = [int(d) for d in str(i)]
    if (digits[0]**2 + digits[1]**2) % 13 == 0:
        print(i)

print("б):")
for i in range(10, 100):
    digit_sum = sum(int(d) for d in str(i))
    if digit_sum + digit_sum**2 == i:
        print(i)

# 5.83
total = 0
for i in range(1, 50, 2):
    total += i
print(total)

# 5.84
total = 0
for i in range(100, 1000, 2):
    total += i
print(total)

# 5.85
a, b = 10, 50
total = 0
for i in range(a, b + 1):
    if i % 4 == 0:
        total += i
print(total)

# 5.86
total = 0
for i in range(31, 100):
    if i % 3 == 0 and i % 10 in [2, 4, 8]:
        total += i
print(total)

# 5.87
count = 0
for i in range(100, 501):
    digit_sum = sum(int(d) for d in str(i))
    if digit_sum == 15:
        count += 1
print(count)

# 5.88
s = 15
count = 0
for i in range(100, 1000):
    digit_sum = sum(int(d) for d in str(i))
    if digit_sum == s:
        count += 1
print(count)

# 5.89
count = 0
for i in range(100, 1000):
    if i % 7 == 0:
        digit_sum = sum(int(d) for d in str(i))
        if digit_sum % 7 == 0:
            count += 1
print(count)

# 5.90
n = 10
fib = [1, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
total = sum(fib[:n])
print(total % 2 == 0)

# 5.91
num = 28
print("a) Делители:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)

print("б) Сумма делителей:")
div_sum = sum(i for i in range(1, num + 1) if num % i == 0)
print(div_sum)

print("в) Сумма четных делителей:")
even_div_sum = sum(i for i in range(1, num + 1) if num % i == 0 and i % 2 == 0)
print(even_div_sum)

print("г) Количество делителей:")
div_count = sum(1 for i in range(1, num + 1) if num % i == 0)
print(div_count)

print("д) Количество нечетных делителей:")
odd_div_count = sum(1 for i in range(1, num + 1) if num % i == 0 and i % 2 != 0)
print(odd_div_count)

print("е) Четных делителей:")
even_count = sum(1 for i in range(1, num + 1) if num % i == 0 and i % 2 == 0)
print(even_count)

print("ж) Делителей больше d:")
d = 10
greater_count = sum(1 for i in range(1, num + 1) if num % i == 0 and i > d)
print(greater_count)

# 5.92
num = 17
is_prime = True
for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break
print(is_prime)

# 5.93
num = 28
div_sum = sum(i for i in range(1, num) if num % i == 0)
print(div_sum == num)

# 5.94
n = 100
i = 1
while i*i <= n:
    print(i)
    i += 1
