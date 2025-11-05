# 4.42 a)
x = float(input())
y = float(input())

if 0 < x < 1 and 0 < y < 2:
    print("Точка попадает в область I")
else:
    print("Точка не попадает в область I")
# 4.42 б)
x = float(input())
y = float(input())

if -2 < x < 0 and 0 < y < 4:
    print("Точка попадает в область I")
else:
    print("Точка не попадает в область I")
# 4.43
x = float(input())
y = float(input())

if 0 < x < 3 and 0 < y < 2:
    print("Точка попадает в область I")
else:
    print("Точка не попадает в область I")
# 4.44
x = float(input())
y = float(input())

if (x < -1 and y > 0) or (x > 0 and y < 0):
    print("Точка попадает в область I или III")
else:
    print("Точка не попадает в область I или III")
# 4.45
x = float(input())

if -2.4 <= x <= 5.7:
    f = x**2
else:
    f = 4

print(f)
# 4.46
import math

x = float(input())

if 0.2 <= x <= 0.9:
    f = math.sin(x)
else:
    f = 1

print(f)
# 4.47
a, b, c = map(float, input().split())
print(a < 6 < c)
print(b > a > c)

# 4.48
x, y = map(int, input().split())
print("да" if x % y == 0 or y % x == 0 else "нет")

# 4.49
num = int(input())
d1 = num // 10
d2 = num % 10
print("да" if 3 in [d1, d2] else "нет")
print("да" if d1 == int(input()) or d2 == int(input()) else "нет")  # В условии неясно, что под цифрой а — пропущено входное значение, допустим это цифра a
#a_digit = int(input())
#print("да" if a_digit in [d1, d2] else "нет")

# 4.50
num = int(input())
d1 = num // 10
d2 = num % 10
print("да" if 4 in [d1, d2] or 7 in [d1, d2] else "нет")
print("да" if any(d in [3, 6, 9] for d in [d1, d2]) else "нет")

# 4.51
num = int(input())
d1 = num // 100
d2 = (num // 10) % 10
d3 = num % 10
print("да" if 6 in [d1, d2, d3] else "нет")
print("да" if 6 in [d1, d2, d3] else "нет")  # совпадает с предыдущим, возможно опечатка

# 4.52
num = int(input())
digits = [num // 100, (num // 10) % 10, num % 10]
print("да" if 6 in digits else "нет")

# 4.53
num = int(input())
digits = [num // 100, (num // 10) % 10, num % 10]
print("да" if any(d in [4,7] for d in digits) else "нет")
print("да" if any(d in [3,6,9] for d in digits) else "нет")

# 4.54
num = int(input())
digits = [num // 1000, (num // 100) % 10, (num // 10) % 10, num % 10]
print("да" if 4 in digits else "нет")
b = int(input())
# В условии не указано, что такое b, предполагаю, что это цифра, которую нужно проверить
another_digit = b
print("да" if another_digit in digits else "нет")

# 4.55
num = int(input())
digits = [num // 1000, (num // 100) % 10, (num //10) % 10, num % 10]
print("да" if any(d in [2,7] for d in digits) else "нет")
print("да" if any(d in [3,6,9] for d in digits) else "нет")

# 4.56
num = int(input())
d1 = num // 1000
d2 = (num // 100) % 10
d3 = (num // 10) % 10
d4 = num % 10
print("да" if d1 == d4 and d2 == d3 else "нет")

# 4.57
a = int(input())
b = int(input())
c = int(input())
d = int(input())
r = int(input())
print("да" if a % b == r or a % b == c else "нет")

# 4.58
a, b, c = map(float, input().split())
print("да" if a == b or b == c or a == c else "нет")

# 4.59
a, b, c = map(float, input().split())
if a == b == c:
    print("равносторонний")
elif a == b or b == c or a == c:
    print("равнобедренный")
else:
    print("разносторонний")

# 4.60
h1 = float(input())
h2 = float(input())
h3 = float(input())
print("да" if h1 == h2 == h3 else "нет")

# 4.61
import math
a, b, c = map(float, input().split())
D = b**2 - 4 * a * c
# 4.62
a, b, c, d = map(float, input().split())
rect1_sides = sorted([a, b])
rect2_sides = sorted([c, d])
if (rect1_sides[0] <= rect2_sides[0] and rect1_sides[1] <= rect2_sides[1]) or \
   (rect1_sides[0] <= rect2_sides[1] and rect1_sides[1] <= rect2_sides[0]):
    print("да")
else:
    print("нет")

# 4.63
a, b, c, d = map(float, input().split())
if a + 2 >= c and b + 2 >= d:
    print("да")
else:
    print("нет")

# 4.64
a, b, c, d = map(float, input().split())
if c + 2 <= a and c + 2 <= b:
    print("да")
else:
    print("нет")

# 4.65
a, b, c, x, y = map(float, input().split())
diameter = c
for rot in [(a, b), (b, a)]:
    if (rot[0] + 1 <= x and rot[1] + 1 <= y) or (rot[0] + 1 <= y and rot[1] + 1 <= x):
        print("да")
        break
else:
    print("нет")

# 4.66
a1, a2, a3 = map(float, input().split())
b1, b2, b3 = map(float, input().split())
from itertools import permutations
max_count = 0
for perm in permutations([b1, b2, b3]):
    if all(perm[i] <= a1 if i == 0 else (a2 if i == 1 else a3)):
        max_count = 1
        break
print("да" if max_count else "нет")

# 4.67
num = input()
if len(num) == 6 and num.isdigit():
    first_three_sum = sum(int(d) for d in num[:3])
    last_three_sum = sum(int(d) for d in num[3:])
    print("да" if first_three_sum == last_three_sum else "нет")
else:
    print("нет")

# 4.68
year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("да")
else:
    print("нет")

# 4.69
a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
max_count = 0
# Генерируем все перестановки сторон костей и проверяем
from itertools import permutations
for sides in permutations([c, d, e], 3):
    for face in permutations([a, b], 2):
        if sides[0] <= face[0] and sides[1] <= face[1]:
            max_count = max(max_count, 1)
        elif sides[0] <= face[1] and sides[1] <= face[0]:
            max_count = max(max_count, 1)
print(max_count)
# 4.70
k = int(input())

if k % 7 == 6 or k % 7 == 0:
    print("Выходной")
else:
    print("Рабочий")
# 4.71
import math

alpha = float(input())
v0 = float(input())
R = float(input())
H = float(input())
P = float(input())
g = 9.8

t = R / (v0 * math.cos(math.radians(alpha)))
y = v0 * t * math.sin(math.radians(alpha)) - (g * t**2) / 2

if H <= y <= H + P:
    print("Снаряд поразит цель")
else:
    print("Снаряд не поразит цель")
# 4.72
x1, y1, w1, h1 = map(float, input().split())
x2, y2, w2, h2 = map(float, input().split())

x1_max, y1_max = x1 + w1, y1 + h1
x2_max, y2_max = x2 + w2, y2 + h2

a = (x1 >= x2 and y1 >= y2 and x1_max <= x2_max and y1_max <= y2_max)
b = (x1 >= x2 and x1_max <= x2_max and y1 >= y2 and y1_max <= y2_max) or \
    (x2 >= x1 and x2_max <= x1_max and y2 >= y1 and y2_max <= y1_max)
c = not (x1_max < x2 or x2_max < x1 or y1_max < y2 or y2_max < y1)

print("a)", "да" if a else "нет")
print("b)", "да" if b else "нет")
print("c)", "да" if c else "нет")

# 4.73
a_tens, a_ones = map(int, input().split())
b = int(input())

res = a_tens*10 + a_ones - b
tens = abs(res) // 10
ones = abs(res) % 10
if 10 <= abs(res) <= 99:
    print(tens, ones)
else:
    print("Результат не двузначное число")

# 4.74
a_units, a_tens = map(int, input().split())
b_units, b_tens = map(int, input().split())

num1 = a_tens * 10 + a_units
num2 = b_tens * 10 + b_units
diff = abs(num1 - num2)

if 10 <= diff <= 99:
    print(diff // 10, diff % 10)
else:
    print("Результат не двузначное число")
# 4.75
a_hundreds, a_units, b_tens, b_units = map(int, input().split())

sum_num = a_hundreds * 100 + a_units * 10 + b_tens * 10 + b_units
sum_hundreds = sum_num // 100
sum_tens = (sum_num // 10) % 10
sum_ones = sum_num % 10
print(sum_hundreds, sum_tens, sum_ones)

# 4.76
a, b, c, d = map(int, input().split())

# Проверка, находится ли фигура внутри доски 8x8
if not all(1 <= x <= 8 for x in [a, b, c, d]):
    print("Некорректные координаты")
else:
    # Ладья
    threat_rook = (a == c or b == d)

    # Слон
    threat_bishop = abs(a - c) == abs(b - d)

    # Король
    threat_king = max(abs(a - c), abs(b - d)) == 1

    # Ферзь
    threat_queen = threat_rook or threat_bishop

    # Белая пешка (с учетом что она идет вверх по доске отсчет снизу)
    threat_white_pawn = (a == c and b + 1 == d) or (abs(a - c) == 1 and b + 1 == d)

    # Черная пешка (она идет вниз по доске)
    threat_black_pawn = (a == c and b - 1 == d) or (abs(a - c) == 1 and b - 1 == d)

    # Конь
    threat_knight = (abs(a - c) == 2 and abs(b - d) == 1) or (abs(a - c) == 1 and abs(b - d) == 2)

    print("ладья", "да" if threat_rook else "нет")
    print("слон", "да" if threat_bishop else "нет")
    print("король", "да" if threat_king else "нет")
    print("ферзь", "да" if threat_queen else "нет")
    print("белая пешка", "да" if threat_white_pawn else "нет")
    print("черная пешка", "да" if threat_black_pawn else "нет")
    print("конь", "да" if threat_knight else "нет")
# 4.77
a, b, c, d, e, f = map(int, input().split())

def attacked_by(attacking_piece, target_x, target_y, threat_x, threat_y):
    if attacking_piece == 'rook':
        return target_x == threat_x or target_y == threat_y
    elif attacking_piece == 'queen':
        return target_x == threat_x or target_y == threat_y or abs(target_x - threat_x) == abs(target_y - threat_y)
    elif attacking_piece == 'knight':
        return (abs(target_x - threat_x) == 2 and abs(target_y - threat_y) == 1) or (abs(target_x - threat_x) == 1 and abs(target_y - threat_y) == 2)
    elif attacking_piece == 'bishop':
        return abs(target_x - threat_x) == abs(target_y - threat_y)
    elif attacking_piece == 'king':
        return max(abs(target_x - threat_x), abs(target_y - threat_y)) == 1
    elif attacking_piece == 'pawn_white':
        return target_x in [threat_x - 1, threat_x + 1] and target_y == threat_y + 1
    elif attacking_piece == 'pawn_black':
        return target_x in [threat_x - 1, threat_x + 1] and target_y == threat_y - 1
    return False

white_x, white_y = a, b
black_x, black_y = c, d
target_x, target_y = e, f

pieces = ['rook', 'queen', 'knight', 'bishop', 'queen', 'rook', 'king', 'bishop', 'knight', 'pawn_white', 'pawn_black']
# Варианты
# а) ладья и ладья
print("а)", not (attacked_by('rook', e, f, a, b) or attacked_by('rook', e, f, c, d)))
# б) ладья и ферзь
print("б)", not (attacked_by('rook', e, f, a, b) or attacked_by('queen', e, f, c, d)))
# в) ладья и конь
print("в)", not (attacked_by('rook', e, f, a, b) or attacked_by('knight', e, f, c, d)))
# г) ладья и слон
print("г)", not (attacked_by('rook', e, f, a, b) or attacked_by('bishop', e, f, c, d)))
# д) ферзь и ферзь
print("д)", not (attacked_by('queen', e, f, a, b) or attacked_by('queen', e, f, c, d)))
# е) ферзь и ладья
print("е)", not (attacked_by('queen', e, f, a, b) or attacked_by('rook', e, f, c, d)))
# ж) ферзь и конь
print("ж)", not (attacked_by('queen', e, f, a, b) or attacked_by('knight', e, f, c, d)))
# з) ферзь и слон
print("з)", not (attacked_by('queen', e, f, a, b) or attacked_by('bishop', e, f, c, d)))
# и) конь и конь
print("и)", not (attacked_by('knight', e, f, a, b) or attacked_by('knight', e, f, c, d)))
# к) конь и ладья
print("к)", not (attacked_by('knight', e, f, a, b) or attacked_by('rook', e, f, c, d)))
# л) конь и ферзь
print("л)", not (attacked_by('knight', e, f, a, b) or attacked_by('queen', e, f, c, d)))
# м) конь и слон
print("м)", not (attacked_by('knight', e, f, a, b) or attacked_by('bishop', e, f, c, d)))
# н) слон и слон
print("н)", not (attacked_by('bishop', e, f, a, b) or attacked_by('bishop', e, f, c, d)))
# о) слон и ферзь
print("о)", not (attacked_by('bishop', e, f, a, b) or attacked_by('queen', e, f, c, d)))
# п) слон и конь
print("п)", not (attacked_by('bishop', e, f, a, b) or attacked_by('knight', e, f, c, d)))
# р) слон и ладья
print("р)", not (attacked_by('bishop', e, f, a, b) or attacked_by('rook', e, f, c, d)))
# с) король и слон
print("с)", max(abs(a - c), abs(b - d)) == 1 or max(abs(a - c), abs(b - d)) == 1)
# т) король и ферзь
print("т)", max(abs(a - c), abs(b - d)) == 1)
# у) король и конь
print("у)", max(abs(a - c), abs(b - d)) == 1)
# ф) король и ладья
print("ф)", max(abs(a - c), abs(b - d)) == 1)
# 4.78
a, b, c, d = map(int, input().split())
print("да" if (a + b) % 2 == (c + d) % 2 else "нет")

# 4.79
import math
a, b, c = map(float, input().split())
sides_sum = a + b + c
max_side = max(a, b, c)
if 2 * max_side < sides_sum:
    print("да")
else:
    print("нет")

# 4.80
a, b, c = map(float, input().split())
if not (a + b > c and a + c > b and b + c > a):
    print("нет")
else:
    if math.isclose(a**2 + b**2, c**2) or math.isclose(a**2 + c**2, b**2) or math.isclose(b**2 + c**2, a**2):
        print("да")
    else:
        print("нет")
4.81
import math
a, b, c = map(float, input().split())
if a + b <= c or a + c <= b or b + c <= a:
    print("треугольник не существует")
else:
    if math.isclose(a**2 + b**2, c**2) or math.isclose(a**2 + c**2, b**2) or math.isclose(b**2 + c**2, a**2):
        print("прямоугольный", end=' ')
    elif a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2:
        print("остроугольный", end=' ')
    else:
        print("тупоугольный", end=' ')
    if a == b == c:
        print("равносторонний")
    elif a == b or b == c or a == c:
        print("равнобедренный")
    else:
        print("разносторонний")

# 4.82
p = int(input())
if p % 10 == 1 and p != 11:
    print(f"мне {p} лет")
elif 2 <= p % 10 <= 4 and not 12 <= p <= 14:
    print(f"мне {p} года")
else:
    print(f"мне {p} лет")

# 4.83
k = int(input())
if k % 10 == 1 and k % 100 != 11:
    print(f"мы нашли {k} гриб в лесу")
elif 2 <= k % 10 <= 4 and not 12 <= k % 100 <= 14:
    print(f"мы нашли {k} гриба в лесу")
else:
    print(f"мы нашли {k} грибов в лесу")

# 4.84
p = int(input())
rubles = p // 100
kopecks = p % 100
if rubles > 0 and kopecks > 0:
    print(f"{rubles} рубля{'и' if rubles>1 else ''} {kopecks} копейка{'и' if kopecks>1 else ''}")
elif rubles > 0:
    print(f"{rubles} рубль")
else:
    print(f"{kopecks} копейка{'и' if kopecks>1 else ''}")

# 4.85
p = int(input())
years = p // 12
months = p % 12
if years > 0 and months > 0:
    print(f"{years} год{'а' if years%10==1 and years%100!=11 else 'а'} {months} месяц{'а' if months%10==1 and months%100!=11 else 'а'}")
elif years > 0:
    print(f"{years} год{'а' if years%10==1 and years%100!=11 else 'а'}")
else:
    print(f"{months} месяц{'а' if months%10==1 and months%100!=11 else 'а'}")

# 4.86
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
age = y2 - y1
if m2 < m1 or (m2 == m1 and d2 < d1):
    age -= 1
print(age)

# 4.87
y1h, m1h, y2h, m2h = map(int, input().split())
age1 = y1h + (m1h > 0)
age2 = y2h + (m2h > 0)
if y1h < y2h or (y1h == y2h and m1h < m2h):
    print("Первый старше")
elif y1h > y2h or (y1h == y2h and m1h > m2h):
    print("Второй старше")
else:
    print("Они равны по возрасту")

# 4.88
by, bm, ny, nm = map(int, input().split())
full_years = ny - by
full_months = nm - bm
if full_months < 0:
    full_years -= 1
    full_months += 12
print(f"{full_years} лет {full_months} месяцев")

# 4.89
a, b, c, d, p, t = map(int, input().split())
arrival_time = a * 60 + b
departure_time = c * 60 + d
platform_time_start = arrival_time
platform_time_end = departure_time
contact_time = p * 60 + t
print("да" if contact_time >= platform_time_start and contact_time <= platform_time_end else "нет")

# 4.90
t, p = map(int, input().split())
# а) предыдущий день
if p == 1:
    prev_day = 31
    prev_month = t - 1
else:
    prev_day = p - 1
    prev_month = t
# б) следующий день
if p == 31:
    next_day = 1
    next_month = t + 1
else:
    next_day = p + 1
    next_month = t
print(f"{prev_day} {prev_month}")
print(f"{next_day} {next_month}")
4.91
import math
g, t, p = map(int, input().split())
def is_leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)
# а) без учета високосности
# предыдущий день
if p > 1:
    prev_p = p - 1
    prev_t = t
    prev_g = g
else:
    prev_p = 31 if t == 1 else None
    prev_t = t - 1 if t > 1 else None
    prev_g = g
    if t == 1:
        prev_t = 12
        prev_g -= 1

# следующий день
if p < 28:
    next_p = p + 1
    next_t = t
    next_g = g
elif p == 28:
    next_p = 29
    next_t = t
    next_g = g
elif p == 29:
    if not is_leap_year(g):
        next_p = 1
        next_t = t + 1
        next_g = g
    else:
        next_p = 30
        next_t = t
        next_g = g
elif p == 30:
    if t in [4,6,9,11]:
        next_p = 1
        next_t = t + 1
        next_g = g
    else:
        next_p = 31
        next_t = t
        next_g = g
elif p == 31:
    if t in [1,3,5,7,8,10,12]:
        next_p = 1
        next_t = t + 1
        next_g = g
    elif t == 12:
        next_p = 1
        next_t = 1
        next_g = g + 1

# б) с учетом високосности
def days_in_month(month, year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    if month in [4,6,9,11]:
        return 30
    return 29 if is_leap_year(year) else 28

# предыдущий день
if p > 1:
    prev_p = p - 1
    prev_t = t
    prev_g = g
else:
    prev_t = t - 1
    if prev_t < 1:
        prev_t = 12
        prev_g = g - 1
    else:
        prev_g = g
    prev_p = days_in_month(prev_t, prev_g)

# следующий день
if p < days_in_month(t, g):
    next_p = p + 1
    next_t = t
    next_g = g
else:
    next_p = 1
    next_t = t + 1
    next_g = g
    if next_t > 12:
        next_t = 1
        next_g += 1

print(prev_g, prev_t, prev_p)
print(next_g, next_t, next_p)

# 4.92
t = float(input())
t_mod = t * 60
phase_time = t_mod % 9
if phase_time < 3:
    print("зеленый")
elif phase_time < 4:
    print("желтый")
else:
    print("красный")

# 4.93
k = int(input())
d = int(input())
n = k
d_week = d
weekday_start = 1  # 1: понедельник
day_week = (n + weekday_start - 2) % 7 + 1
if day_week in [6,7]:
    print("выходной")
else:
    print("рабочий день")

# 4.94
k = int(input())
sequence = "10111213.9899"
digits = ""
for num in range(10, 151):
    digits += str(num)
if k <= len(digits):
    print(digits[k-1])
else:
    print()

# 4.95
sequence = "0123456789101112"  # пример, последовательность из условия
digits = ""
for i in range(1, 21):
    digits += str(i)
p = int(input())
print(digits[p-1])

# 4.96
k = int(input())
digits_sequence = ""
for num in range(50, 251):
    digits_sequence += str(num)
if k <= len(digits_sequence):
    print(digits_sequence[k-1])
else:
    print()

# 4.97
k = int(input())
digits_sequence = ""
for num in range(1, 111):
    digits_sequence += str(num)
if k <= len(digits_sequence):
    print(digits_sequence[k-1])
else:
    print()

# 4.98
a = int(input())
p = int(input())
total = 0
for num in range(a, a + p):
    total += num
print("да" if total % 2 == 0 else "нет")

# 4.99
x = float(input())
y = float(input())
a, b = 0, 0
if y > x:
    a = y
else:
    b = y
print(a if a > b else b)

# (термин "неполный оператор" я интерпретирую как использование логического выражения без полного условия)
# а) с использованием двух неполных условий
a = float(input())
b = float(input())
max_value = a if a > b else b
print(max_value)

# б) с одним неполным условием
a = float(input())
b = float(input())
max_value = a if a > b else b
print(max_value)
# 4.100
a, b = map(float, input().split())
less = a if a < b else b
more = a if a > b else b

# 4.101
a, b, c = map(float, input().split())
max_num = a if a > b and a > c else (b if b > c else c)
min_num = a if a < b and a < c else (b if b < c else c)

# 4.102
a, b, c, d = map(float, input().split())
max_num = a if a > b and a > c and a > d else (b if b > c and b > d else (c if c > d else d))
min_num = a if a < b and a < c and a < d else (b if b < c and b < d else (c if c < d else d))

# 4.103
x = float(input())
abs_x = x if x >= 0 else -x
print(abs_x)

# 4.104
a, b = map(float, input().split())
abs_a = a if a >= 0 else -a
abs_b = b if b >= 0 else -b
half_sum = (abs_a + abs_b) / 2
from math import sqrt
result = sqrt(abs_a * abs_b)

# 4.105
a, b = map(float, input().split())
if abs(a) > abs(b):
    a /= 2
print(a)

# 4.106
a, b = map(float, input().split())
from math import sqrt
if sqrt(b) < a:
    b *= 5
print(b)

# 4.107
a, b, c = map(int, input().split())
print(a if a % 2 == 0 else 0, b if b % 2 == 0 else 0, c if c % 2 == 0 else 0)

# 4.108
a, b, c = map(float, input().split())
a_squared = a ** 2 if a >= 0 else a
b_squared = b ** 2 if b >= 0 else b
c_squared = c ** 2 if c >= 0 else c
print(a_squared, b_squared, c_squared)

# 4.109
a, b, c = map(float, input().split())
print(a if 1.6 <= a <= 3.8 else "", end=' ')
print(b if 1.6 <= b <= 3.8 else "", end=' ')
print(c if 1.6 <= c <= 3.8 else "")

# 4.110
a, b, c, d = map(float, input().split())
count_neg = (1 if a < 0 else 0) + (1 if b < 0 else 0) + (1 if c < 0 else 0) + (1 if d < 0 else 0)
print(count_neg)

# 4.111
a, b, c, d = map(int, input().split())
count_even = (1 if a % 2 == 0 else 0) + (1 if b % 2 == 0 else 0) + (1 if c % 2 == 0 else 0) + (1 if d % 2 == 0 else 0)
print(count_even)

# 4.112
a, b, c = map(int, input().split())
sum_positive = (a if a > 0 else 0) + (b if b > 0 else 0) + (c if c > 0 else 0)
print(sum_positive)

# 4.113
a, b, c, d = map(float, input().split())
sum_gt_five = (a if a > 5 else 0) + (b if b > 5 else 0) + (c if c > 5 else 0) + (d if d > 5 else 0)
print(sum_gt_five)

# 4.114
a, b, c, d = map(int, input().split())
sum_div3 = (a if a % 3 == 0 else 0) + (b if b % 3 == 0 else 0) + (c if c % 3 == 0 else 0) + (d if d % 3 == 0 else 0)
print(sum_div3)

# 4.115
numbers = list(map(int, input().split()))
sum_positive = (numbers[0] if numbers[0] > 0 else 0) + (numbers[1] if numbers[1] > 0 else 0) + (numbers[2] if numbers[2] > 0 else 0) + (numbers[3] if numbers[3] > 0 else 0) + (numbers[4] if numbers[4] > 0 else 0) + (numbers[5] if numbers[5] > 0 else 0)
# 4.116
x = float(input())

if x < -1:
    y = -1
elif x > -1:
    y = x
else:
    y = 1

print(y)
# 4.117
a = float(input())

if a > 0:
    z = 1
elif a == 0:
    z = 0
else:
    z = -1

print(z)
# 4.118
x = float(input())

if x <= 0:
    f = 0
elif 0 < x <= 1:
    f = x
else:
    f = x**2

print(f)
# 4.119
y = float(input())

if y > 2:
    f = 2
elif 0 < y <= 2:
    f = 0
else:
    f = -3 * y

print(f)
# 4.120a
x = float(input())

if x < -1:
    y = 0
elif -1 <= x <= 1:
    y = 1
else:
    y = 0

print(y)
# 4.120b
x = float(input())

if x < -1:
    y = -1
elif -1 <= x <= 1:
    y = x
else:
    y = 1

print(y)
# 4.120c
x = float(input())

if x < -1:
    y = -1
elif -1 <= x <= 0:
    y = 0
elif 0 < x <= 1:
    y = 1
else:
    y = 2

print(y)
# 4.121
x = float(input())

if x < 0:
    print("I")
elif 0 <= x <= 1:
    print("II")
else:
    print("III")
# 4.122
x = float(input())
y = float(input())

if y > 5:
    print("I")
elif 2.5 < y <= 5:
    print("II")
else:
    print("III")
# 4.123
points = int(input())
result = "выигрыш" if points == 3 else "проигрыш" if points == 0 else "ничья"
print(result)

# 4.124
age_mitya, age_vasya = map(int, input().split())
result = "Митя старше" if age_mitya > age_vasya else "Вася старше" if age_mitya < age_vasya else "Они одного возраста"
print(result)

# 4.125
weight = float(input())
category = "легкий вес" if weight <= 60 else "первый полусредний вес" if weight <= 64 else "полусредний вес"
print(category)
# 4.126
a, b = map(int, input().split())
if b != 0 and a % b == 0:
    print("b является делителем а")
elif a != 0 and b % a == 0:
    print("а является делителем b")
else:
    print("Ни одно из чисел не является делителем другого")

# 4.127
a, b, c = map(int, input().split())
max_num = max(a, b, c)
min_num = min(a, b, c)
middle = a + b + c - max_num - min_num
print("Самое большое:", [a, b, c][[a, b, c].index(max_num)])
print("Самое маленькое:", [a, b, c][[a, b, c].index(min_num)])
if middle == a:
    print("Среднее:", a)
elif middle == b:
    print("Среднее:", b)
else:
    print("Среднее:", c)

# 4.128
a, b, c = map(float, input().split())
print("Максимальное:", max(a, b, c))
print("Минимальное:", min(a, b, c))

# 4.129
a, b, c = sorted(map(int, input().split()))
print("Сумма двух наибольших:", sum([a, b, c][1:]))

# 4.130
a, b, c = sorted(map(int, input().split()))
print("Произведение двух наименьших:", a * b)

# 4.131
tr1 = list(map(float, input().split()))
tr2 = list(map(float, input().split()))
def mid_value(t):
    return sorted(t)[1]
avg = (mid_value(tr1) + mid_value(tr2)) / 2
print("Среднее арифметическое средних чисел:", avg)

# 4.132
x, y = map(float, input().split())
if x > 0 and y > 0:
    print("Первая четверть")
elif x < 0 and y > 0:
    print("Вторая четверть")
elif x < 0 and y < 0:
    print("Третья четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
else:
    print("Средняя ось или начало координат")

# 4.133
num = int(input())
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
if 1 <= num <=7:
    print(days[num-1])
else:
    print("Некорректный номер дня")

# 4.134
num = int(input())
months = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
if 1 <= num <= 12:
    print(months[num-1])
else:
    print("Некорректный номер месяца")

# 4.135
num = int(input())
if num in [12, 1, 2]:
    print("Зима")
elif num in [3, 4, 5]:
    print("Весна")
elif num in [6, 7, 8]:
    print("Лето")
elif num in [9, 10, 11]:
    print("Осень")
else:
    print("Некорректный номер месяца")

# 4.136
month = int(input())
leap = int(input())
if month in [1,3,5,7,8,10,12]:
    print("31")
elif month in [4,6,9,11]:
    print("30")
elif month == 2:
    if leap == 1:
        print("29")
    else:
        print("28")
else:
    print("Некорректный месяц")

# 4.137
month = int(input())
days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
print(days.get(month, "Некорректный месяц"))

# 4.138
t = int(input())
if t == 1:
    print("Пики")
elif t == 2:
    print("Трефы")
elif t == 3:
    print("Бубны")
elif t == 4:
    print("Червы")
# 4.139
k = int(input())
if k >= 6 and k <= 10:
    print({6: "Шестерка", 7: "Семерка", 8: "Восьмерка", 9: "Девятка", 10: "Десятка"}[k])
elif k == 11:
    print("Валет")
elif k == 12:
    print("Дама")
elif k == 13:
    print("Король")
elif k == 14:
    print("Туз")
else:
    print("Некорректное значение")

# 4.140
t = int(input())
k = int(input())
dignity_dict = {6: "Шестерка", 7: "Семерка", 8: "Восьмерка", 9: "Девятка", 10: "Десятка",
                11: "Валет", 12: "Дама", 13: "Король", 14: "Туз"}
print(f"{dignity_dict.get(k, 'Некорректное достоинство')} {['пики', 'трефы', 'бубны', 'червы'][t-1]}")

# 4.141
k = int(input())
d = int(input())
weekday_names = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
start_day = 1  # 1 января - понедельник
day_of_week = (start_day + (k - 1)) % 7
if day_of_week == 0:
    day_of_week = 7
print(weekday_names[day_of_week - 1])

# 4.142
p = int(input())
month_index = (p - 1) // 2
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
print(months[month_index])

# 4.143
t = int(input())
n = int(input())
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= t <= 12 and 1 <= n <= month_days[t - 1]:
    if n > 1:
        prev_day = n - 1
        prev_month = t
    else:
        prev_month = t - 1
        prev_day = month_days[prev_month - 1]
    print(f"{prev_day} {prev_month}")
    if n < month_days[t - 1]:
        next_day = n + 1
        next_month = t
    else:
        next_month = t + 1
        next_day = 1
    print(f"{next_day} {next_month}")
else:
    print("Некорректная дата")

# 4.144
g = int(input())
t = int(input())
n = int(input())
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Предыдущий день
if t == 1 and n == 1:
    prev_day = month_days[(g - 1) % 4 != 0]
    prev_month = t - 1 if t > 1 else 12
    prev_year = g - 1
elif n > 1:
    prev_day = n - 1
    prev_month = t
    prev_year = g
else:
    prev_month = t - 1
    prev_day = month_days[prev_month - 1]
    prev_year = g
# Следующий день
if t == 12 and n == 31:
    next_day = 1
    next_month = 1
    next_year = g + 1
elif n < month_days[t - 1]:
    next_day = n + 1
    next_month = t
    next_year = g
else:
    next_day = 1
    next_month = t + 1
    next_year = g
print(f"Предыдущая дата: {prev_day}.{prev_month}.{prev_year}")
print(f"Следующая дата: {next_day}.{next_month}.{next_year}")
4.145
year = int(input())

animals = ["Крыса", "Коза", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца", "Обезьяна", "Петух", "Собака", "Свинья"]
colors = ["Зеленый", "Красный", "Желтый", "Белый", "Черный"]
base_year = 1984
delta = (year - base_year) % 60
animal_index = delta % 12
color_index = (delta // 2) % 5
print(f"{animals[animal_index]}, {colors[color_index]}")
