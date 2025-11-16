# 6.52
num = 12345
digits = str(num)
print(f"а) Есть цифра 3: {'3' in digits}")
print(f"б) Есть цифры 2 и 5: {'2' in digits and '5' in digits}")

# 6.53
num = 12345
a, b, k = 3, 6, 1
digits = str(num)
print(f"а) Есть цифра {a}: {str(a) in digits}")
print(f"б) Нет цифры {b}: {str(b) not in digits}")
print(f"в) Цифра {a} встречается >{k} раз: {digits.count(str(a)) > k}")
print(f"г) Есть цифры {a} и {b}: {str(a) in digits and str(b) in digits}")

# 6.54
num = 120099
digits = str(num)
count_0 = digits.count('0')
count_9 = digits.count('9')
if count_0 > count_9:
    print("0 встречается чаще")
elif count_9 > count_0:
    print("9 встречается чаще")
else:
    print("0 и 9 встречаются одинаково")

# 6.55
num = 12345
a, b = 2, 3
digits = str(num)
count_a = digits.count(str(a))
count_b = digits.count(str(b))
print(f"Цифра {a} встречается реже, чем {b}: {count_a < count_b}")

# 6.56
num = 12525
digits = str(num)
pos_2 = digits.find('2')
pos_5 = digits.find('5')
if pos_2 != -1 and pos_5 != -1:
    if pos_2 < pos_5:
        print("Цифра 2 левее")
    else:
        print("Цифра 5 левее")

# 6.57
num = 12525
a, b = 2, 5
digits = str(num)
pos_a = digits.rfind(str(a))
pos_b = digits.rfind(str(b))
if pos_a != -1 and pos_b != -1:
    if pos_a > pos_b:
        print(f"Цифра {a} правее")
    else:
        print(f"Цифра {b} правее")

# 6.58
num = 132233
digits = [int(d) for d in str(num)]
max_digit = max(digits)
count = digits.count(max_digit)
print(f"Способ 1: {count}")

count = 0
max_digit = 0
for d in digits:
    if d > max_digit:
        max_digit = d
        count = 1
    elif d == max_digit:
        count += 1
print(f"Способ 2: {count}")

# 6.59
num = 102200
digits = [int(d) for d in str(num)]
min_digit = min(digits)
count = digits.count(min_digit)
print(f"Способ 1: {count}")

count = 0
min_digit = 9
for d in digits:
    if d < min_digit:
        min_digit = d
        count = 1
    elif d == min_digit:
        count += 1
print(f"Способ 2: {count}")

# 6.60
num = 123459
digits = [int(d) for d in str(num)]
sorted_digits = sorted(set(digits), reverse=True)
print(f"а) Максимальные цифры: {sorted_digits[0]}, {sorted_digits[1]}")
sorted_digits = sorted(set(digits))
print(f"б) Минимальные цифры: {sorted_digits[0]}, {sorted_digits[1]}")

# 6.61
num = 123459
digits = [int(d) for d in str(num)]
max1, max2 = -1, -1
pos1, pos2 = -1, -1
for i, d in enumerate(digits):
    if d > max1:
        max2, max1 = max1, d
        pos2, pos1 = pos1, i
    elif d > max2:
        max2 = d
        pos2 = i
print(f"а) Максимальные: с конца {len(digits)-pos1}, {len(digits)-pos2}; с начала {pos1+1}, {pos2+1}")

min1, min2 = 10, 10
pos1, pos2 = -1, -1
for i, d in enumerate(digits):
    if d < min1:
        min2, min1 = min1, d
        pos2, pos1 = pos1, i
    elif d < min2:
        min2 = d
        pos2 = i
print(f"б) Минимальные: с конца {len(digits)-pos1}, {len(digits)-pos2}; с начала {pos1+1}, {pos2+1}")

# 6.62
num = 12345
print(f"а) {int(str(num)[::-1])}")
print(f"б) {int('2' + str(num) + '2')}")
a = 3
print(f"в) {int(str(num).replace(str(a), ''))}")
digits = list(str(num))
digits[0], digits[-1] = digits[-1], digits[0]
print(f"г) {int(''.join(digits))}")
print(f"д) {int(str(num) + str(num))}")

# 6.63
num = 12321
print(str(num) == str(num)[::-1])

# 6.64
n = 100
denominations = [64, 32, 16, 8, 4, 2, 1]
result = {}
for d in denominations:
    count = n // d
    if count > 0:
        result[d] = count
        n %= d
print(result)

# 6.65
a, b = 48, 18
while b:
    a, b = b, a % b
print(a)

# 6.66
a, b, c = 48, 18, 12
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
result = gcd(gcd(a, b), c)
print(result)

# 6.67
a, b = 12, 18
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
lcm = a * b // gcd(a, b)
print(lcm)

# 6.68
a, b = 12, 18
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
divisor = gcd(a, b)
p = a // divisor
q = b // divisor
print(f"{p}/{q}")

# 6.69
a, b = 425, 131
result = {}
while a > 0 and b > 0:
    if a >= b:
        count = a // b
        result[b] = count
        a %= b
    else:
        count = b // a
        result[a] = count
        b %= a
print(result)

# 6.70
a, b = 425, 131
result = {}
while a > 0 and b > 0:
    if a >= b:
        count = a // b
        result[b] = count
        a %= b
    else:
        count = b // a
        result[a] = count
        b %= a
print(result)

# 6.71
n = 21
a, b = 1, 1
while a < n:
    a, b = b, a + b
print(a == n)

# 6.72
n, f, s = 15, 3, 4
print((n - f) % s == 0 and n >= f)

# 6.73
m, g, z = 16, 1, 2
if z == 1:
    print(m == g)
else:
    temp = m / g
    while temp > 1 and temp % z == 0:
        temp /= z
    print(temp == 1)

# 6.74
n = 81
temp = n
while temp % 3 == 0:
    temp //= 3
print(f"а) Степень 3: {temp == 1}")

temp = n
while temp % 5 == 0:
    temp //= 5
print(f"б) Степень 5: {temp == 1}")

# 6.75
def f1(x):
    return x**4 + 2*x**3 - x - 1

def f2(x):
    return x**3 - 0.2*x**2 - 0.2*x - 1.2

a, b = 0, 1
while b - a > 0.001:
    mid = (a + b) / 2
    if f1(a) * f1(mid) < 0:
        b = mid
    else:
        a = mid
print(f"а) Корень: {(a + b) / 2:.3f}")

a, b = 1, 1.5
while b - a > 0.001:
    mid = (a + b) / 2
    if f2(a) * f2(mid) < 0:
        b = mid
    else:
        a = mid
print(f"б) Корень: {(a + b) / 2:.3f}")

# 6.76
a, b = 4, 6
fence_length = 0
while a > 0 and b > 0:
    if a >= b:
        fence_length += b
        a -= 1
    else:
        fence_length += a
        b -= 1
print(fence_length)

# 6.77
num = 666
digits = str(num)
print(f"а) Все цифры одинаковы: {len(set(digits)) == 1}")

has_duplicate = False
for i in range(len(digits)-1):
    if digits[i] == digits[i+1]:
        has_duplicate = True
        break
print(f"б) Есть одинаковые соседние: {has_duplicate}")

# 6.78
num = 5321
digits = [int(d) for d in str(num)]
is_ordered = True
for i in range(len(digits)-1):
    if digits[i] <= digits[i+1]:
        is_ordered = False
        break
print(is_ordered)

# 6.79
num = 9663
digits = [int(d) for d in str(num)]
is_ordered = True
for i in range(len(digits)-1):
    if digits[i] < digits[i+1]:
        is_ordered = False
        break
print(is_ordered)

# 6.80
num = 1478
digits = [int(d) for d in str(num)]
is_ordered = True
for i in range(len(digits)-1):
    if digits[i] >= digits[i+1]:
        is_ordered = False
        break
print(is_ordered)

# 6.81
num = 13579
digits = [int(d) for d in str(num)]
is_increasing = True
for i in range(len(digits)-1):
    if digits[i] >= digits[i+1]:
        is_increasing = False
        break
print(is_increasing)

# 6.82
num = 1669
digits = [int(d) for d in str(num)]
is_non_decreasing = True
for i in range(len(digits)-1):
    if digits[i] > digits[i+1]:
        is_non_decreasing = False
        break
print(is_non_decreasing)

# 6.83
num = 76520
digits = [int(d) for d in str(num)]
is_increasing = True
is_decreasing = True
for i in range(len(digits)-1):
    if digits[i] >= digits[i+1]:
        is_increasing = False
    if digits[i] <= digits[i+1]:
        is_decreasing = False
print(is_increasing or is_decreasing)
