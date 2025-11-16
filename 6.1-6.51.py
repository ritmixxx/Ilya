# 6.1
a, b = 17, 5
quotient = 0
temp = a
while temp >= b:
    temp -= b
    quotient += 1
print(f"Целая часть: {quotient}")
print(f"Остаток: {temp}")

# 6.2
n = 15
i = 1
while i <= n:
    print(i)
    i += 1

# 6.3
i = 10
while i <= 100:
    if i % 2 != 0:
        print(i)
    i += 1

# 6.4
num = 191
while num % 17 != 0:
    num += 1
print(num)

# 6.5
num = 5000
while num % 139 != 0:
    num -= 1
print(num)

# 6.6
factorial = 120
n = 1
product = 1
while product < factorial:
    n += 1
    product *= n
print(n)

# 6.7
n = 100
i = 1
while i*i <= n:
    print(i)
    i += 1

# 6.8
n = 50
i = 1
while i*i <= n:
    i += 1
print(i)

# 6.9
while True:
    num = int(input("Введите четное число: "))
    if num % 2 == 0:
        break
    print("Ошибка! Число должно быть четным.")

# 6.10
password = 1234
while True:
    user_input = int(input("Введите пароль: "))
    if user_input == password:
        print("Добро пожаловать!")
        break
    print("Неверный пароль!")

# 6.11
for i in range(10):
    num = int(input("Введите число: "))
    if num == 0:
        break

# 6.12
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    print(f"Вы ввели число: {num}")

# 6.13
print("а) Цикл с предусловием:")
i = 10
while i <= 30:
    print(i)
    i += 1

print("б) Цикл с постусловием:")
i = 10
while True:
    print(i)
    i += 1
    if i > 30:
        break

# 6.14
i = 100
while i >= 80:
    print(i)
    i -= 1

# 6.15
for n in range(21, 152, 10):
    print(2 * n)

# 6.16
n = 2
while n <= 12:
    print(n)
    n += 0.5

# 6.17
num = 1.0
while num <= 13.5:
    print(num)
    num += 0.5

# 6.18
import math
a, b = 10, 5
print("а) Цикл с предусловием:")
i = a
while i >= b:
    print(math.sqrt(i))
    i -= 1

print("б) Цикл с постусловием:")
i = a
while True:
    print(math.sqrt(i))
    i -= 1
    if i < b:
        break

# 6.19
num = 12345
for digit in str(num):
    print(digit)

# 6.20
num = 12345
digits = [int(d) for d in str(num)]
print(f"а) Сумма цифр: {sum(digits)}")
print(f"б) Количество цифр: {len(digits)}")
print(f"в) Произведение цифр: {1}")
product = 1
for d in digits:
    product *= d
print(f"в) Произведение цифр: {product}")

print(f"г) Среднее арифметическое: {sum(digits)/len(digits)}")
print(f"д) Сумма квадратов: {sum(d*d for d in digits)}")
print(f"е) Сумма кубов: {sum(d**3 for d in digits)}")
print(f"ж) Первая цифра: {digits[0]}")
print(f"з) Сумма первой и последней: {digits[0] + digits[-1]}")

# 6.21
n = 12345
print(int(str(n)[1]))

# 6.22
n = 12345
print(int(str(n)[2]))

# 6.23
n = 12345
m = 3
last_digits = int(str(n)[-m:])
total = 0
for d in str(last_digits):
    total += int(d)
print(total)

# 6.24
n = 12345
digits = [int(d) for d in str(n)]
sum_a = 0
sign = 1
for d in digits:
    sum_a += sign * d
    sign = -sign
print(f"а) {sum_a}")

sum_b = 0
sign = 1
for d in reversed(digits):
    sum_b += sign * d
    sign = -sign
print(f"б) {sum_b}")

# 6.25
n = 49
for i in range(2, n+1):
    if n % i == 0:
        print(i)
        break

# 6.26
print("а) Без условия:")
for i in range(13, 100, 13):
    print(i)

print("б) С условием:")
i = 13
while i < 100:
    print(i)
    i += 13

# 6.27
count = 0
num = 100
while count < 15:
    if num % 19 == 0:
        print(num)
        count += 1
    num += 1

# 6.28
count = 0
num = 500
while count < 20:
    if num % 13 == 0 or num % 17 == 0:
        print(num)
        count += 1
    num += 1

# 6.29
count = 0
num = 100
while count < 10:
    if num % 9 == 0 and num % 10 == 7:
        print(num)
        count += 1
    num += 1

# 6.30
a, b = 7, 25
quotient = 0
temp = abs(b)
while temp >= abs(a):
    temp -= abs(a)
    quotient += 1
if (a < 0 and b > 0) or (a > 0 and b < 0):
    quotient = -quotient
print(f"а) Целая часть: {quotient}")
print(f"б) Остаток: {b - quotient * a}")

# 6.31
deposit = 1000
month = 1
while True:
    increase = deposit * 0.02
    if increase > 30:
        print(f"а) Месяц {month}")
        break
    deposit += increase
    month += 1

deposit = 1000
month = 1
while deposit <= 1200:
    deposit *= 1.02
    month += 1
    print(f"б) Месяц {month}")

# 6.32
distance = 10
day = 1
while distance <= 20:
    day += 1
    distance *= 1.1
print(f"а) День {day}")

total = 10
distance = 10
day = 1
while total <= 100:
    day += 1
    distance *= 1.1
    total += distance
print(f"б) День {day}")

# 6.33
area = 100
yield_per_ha = 20
year = 1
while yield_per_ha <= 22:
    year += 1
    yield_per_ha *= 1.02
print(f"а) Год {year}")

area = 100
year = 1
while area <= 120:
    year += 1
    area *= 1.05
print(f"б) Год {year}")

area = 100
yield_per_ha = 20
total_yield = 0
year = 1
while total_yield <= 800:
    total_yield += area * yield_per_ha
    area *= 1.05
    yield_per_ha *= 1.02
    year += 1
print(f"в) Год {year}")

# 6.34
m, n = 3, 5
for i in range(1, m*n + 1):
    if i % m == 0 or i % n == 0:
        print(i)

# 6.35
num = 133353
digits = [int(d) for d in str(num)]
print(f"а) Цифр 3: {digits.count(3)}")
print(f"б) Последняя цифра встречается: {digits.count(digits[-1])}")
print(f"в) Четных цифр: {sum(1 for d in digits if d % 2 == 0)}")
print(f"г) Сумма цифр >5: {sum(d for d in digits if d > 5)}")
print(f"д) Произведение цифр >7: {1}")
product = 1
for d in digits:
    if d > 7:
        product *= d
print(f"д) Произведение цифр >7: {product}")
print(f"е) Цифр 0 и 5: {digits.count(0) + digits.count(5)}")

# 6.36
num = 123456
a = 3
digits = [int(d) for d in str(num)]
print(f"а) Цифра {a} встречается: {digits.count(a)}")
print(f"б) Сумма цифр >{a}: {sum(d for d in digits if d > a)}")
print(f"в) Сумма четных цифр: {sum(d for d in digits if d % 2 == 0)}")
x, y = 2, 4
print(f"г) Цифры {x} и {y} встречаются: {digits.count(x) + digits.count(y)}")

# 6.37
num = 128438
digits = [int(d) for d in str(num)]
position = 0
for i in range(len(digits)-1, -1, -1):
    if digits[i] == 8:
        position = len(digits) - i
        break
print(position)

# 6.38
num = 133353
digits = [int(d) for d in str(num)]
position = 0
for i in range(len(digits)):
    if digits[i] == 3:
        position = len(digits) - i
print(position)

# 6.39
num = 12345
for digit in str(num):
    print(digit)

# 6.40
num = 123415
first_digit = int(str(num)[0])
count = sum(1 for d in str(num) if int(d) == first_digit)
print(count)

# 6.41
num = 123459
digits = [int(d) for d in str(num)]
print(f"а) Максимальная цифра: {max(digits)}")
print(f"б) Минимальная цифра: {min(digits)}")

# 6.42
num = 123459
digits = [int(d) for d in str(num)]
max_digit = max(digits)
min_digit = min(digits)
print(f"а) Максимальная: {max_digit}, Минимальная: {min_digit}")
print(f"б) Разница: {max_digit - min_digit}")
print(f"в) Сумма: {max_digit + min_digit}")

# 6.43
num = 123459
a = 8
digits = [int(d) for d in str(num)]
sum_extreme = max(digits) + min(digits)
print(sum_extreme % a == 0)

# 6.44
num = 123459
digits = [int(d) for d in str(num)]
diff = max(digits) - min(digits)
print(diff % 2 == 0)

# 6.45
num = 123459
digits = [int(d) for d in str(num)]
max_digit = max(digits)
min_digit = min(digits)
max_pos_from_end = len(digits) - digits.index(max_digit)
max_pos_from_start = digits.index(max_digit) + 1
min_pos_from_end = len(digits) - digits.index(min_digit)
min_pos_from_start = digits.index(min_digit) + 1
print(f"а) Максимальная цифра: с конца {max_pos_from_end}, с начала {max_pos_from_start}")
print(f"б) Минимальная цифра: с конца {min_pos_from_end}, с начала {min_pos_from_start}")

# 6.46
num = 123459
digits = [int(d) for d in str(num)]
max_digit = max(digits)
min_digit = min(digits)
max_pos_from_end = len(digits) - digits.index(max_digit)
max_pos_from_start = digits.index(max_digit) + 1
min_pos_from_end = len(digits) - digits.index(min_digit)
min_pos_from_start = digits.index(min_digit) + 1
print(f"а) Максимальная: с конца {max_pos_from_end}, с начала {max_pos_from_start}")
print(f"б) Минимальная: с конца {min_pos_from_end}, с начала {min_pos_from_start}")

# 6.47
num = 123459
digits = [int(d) for d in str(num)]
max_pos = digits.index(max(digits))
min_pos = digits.index(min(digits))
if max_pos < min_pos:
    print("Максимальная цифра левее")
else:
    print("Минимальная цифра левее")

# 6.48
num = 123459
digits = [int(d) for d in str(num)]
odd_digits = [d for d in digits if d % 2 != 0]
print(f"а) Максимальная нечетная: {max(odd_digits) if odd_digits else 'нет'}")
min_digit = min(digits)
min_pos = digits.index(min_digit) + 1
print(f"б) Позиция минимальной: {min_pos}")

# 6.49
num = 1234
digits = [int(d) for d in str(num)]
print(f"а) Сумма >10: {sum(digits) > 10}")

product = 1
for d in digits:
    product *= d
print(f"б) Произведение <50: {product < 50}")

print(f"в) Четное количество цифр: {len(digits) % 2 == 0}")
print(f"г) Четырехзначное: {len(digits) == 4}")
print(f"д) Первая цифра <=6: {digits[0] <= 6}")
print(f"е) Начинается и заканчивается одинаково: {digits[0] == digits[-1]}")
print(f"ж) Первая цифра больше последней: {digits[0] > digits[-1]}")

# 6.50
num = 1234
a, b, k, m = 8, 20, 4, 2
digits = [int(d) for d in str(num)]
print(f"а) Сумма <{a}: {sum(digits) < a}")

product = 1
for d in digits:
    product *= d
print(f"б) Произведение >{b}: {product > b}")

print(f"в) {k}-значное: {len(digits) == k}")
print(f"г) Первая цифра >{m}: {digits[0] > m}")

# 6.51
num = 1234
k, b, x, y, a, b2, m, n = 5, 2000, 1, 4, 50, 2, 8, 3
digits = [int(d) for d in str(num)]
sum_digits = sum(digits)
product = 1
for d in digits:
    product *= d
print(f"а) Сумма >{k} и четное: {sum_digits > k and num % 2 == 0}")
print(f"б) Четное количество и число <{b}: {len(digits) % 2 == 0 and num <= b}")
print(f"г) Начинается на {x} и заканчивается на {y}: {digits[0] == x and digits[-1] == y}")
print(f"д) Произведение <{a} и делится на {b2}: {product < a and num % b2 == 0}")
print(f"е) Сумма >{m} и делится на {n}: {sum_digits > m and num % n == 0}")
