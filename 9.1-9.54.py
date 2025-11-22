# 9.1
print("9.1:")
# a)
for i in range(5):
    print("8 " * 3)
print()

# б)
for i in range(1, 8):
    print(f"{i} " * i)
print()

# в)
for i in range(1, 9):
    print(f"{i*10} " * 4)
print()

# г)
for i in range(1, 9):
    print(f"{i*10+2} " * 4)
print()

# д)
for i in range(5):
    for j in range(2, 21):
        print(j, end=" ")
    print()
print()

# е)
for i in range(5):
    for j in range(15, 2, -1):
        print(j, end=" ")
    print()
print()

# ж)
for i in range(5, 0, -1):
    print("0 " * i)
print()

# з)
for i in range(8, 0, -1):
    for j in range(8, 8-i, -1):
        print(j, end=" ")
    print()
print()

# и)
for i in range(9):
    for j in range(2+i, 11):
        print(j, end=" ")
    print()
print()

# й)
for i in range(1, 10):
    print("2 3 " * i)
print()

# к)
for i in range(3, 7):
    print(f"{i} " * i)
print()

# л)
for i in range(1, 6):
    print(f"{20+i} " * i)
print()

# м)
for i in range(1, 6):
    print(f"{i} " * (8-i))
print()

# н)
for i in range(1, 6):
    print(f"{i*10} " * i)
print()

# 9.2
print("9.2:")
# a)
for j in range(1, 10):
    for i in range(1, 10):
        print(f"{i} + {j} = {i+j}")
print()

# б)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} + {j} = {i+j}")
print()

# 9.3
print("9.3:")
# a)
for j in range(1, 10):
    for i in range(1, 10):
        print(f"{i} * {j} = {i*j}")
print()

# б)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")
print()

# 9.4
print("9.4:")
import random
students = 12
subjects = 3
grades = [[random.randint(2, 5) for _ in range(subjects)] for _ in range(students)]

# 1) по строкам
total_sum1 = 0
for i in range(students):
    for j in range(subjects):
        total_sum1 += grades[i][j]
print(f"Сумма по строкам: {total_sum1}")

# 2) по столбцам
total_sum2 = 0
for j in range(subjects):
    for i in range(students):
        total_sum2 += grades[i][j]
print(f"Сумма по столбцам: {total_sum2}")
print()

# 9.5
print("9.5:")
workers = 12
months = 3
salaries = [[random.randint(20000, 50000) for _ in range(months)] for _ in range(workers)]

# а) общая сумма за квартал
total_quarter = 0
for i in range(workers):
    for j in range(months):
        total_quarter += salaries[i][j]
print(f"Общая сумма за квартал: {total_quarter}")

# б) зарплата каждого работника за квартал
worker_totals = []
for i in range(workers):
    worker_total = sum(salaries[i])
    worker_totals.append(worker_total)
    print(f"Работник {i+1}: {worker_total}")

# в) общая зарплата за каждый месяц
month_totals = []
for j in range(months):
    month_total = sum(salaries[i][j] for i in range(workers))
    month_totals.append(month_total)
    print(f"Месяц {j+1}: {month_total}")
print()

# 9.6
print("9.6:")
sportsmen = 15
programs = 3
scores = [[random.randint(1, 10) for _ in range(programs)] for _ in range(sportsmen)]

# а) среднее каждого спортсмена
for i in range(sportsmen):
    avg = sum(scores[i]) / programs
    print(f"Спортсмен {i+1}: {avg:.2f}")

# б) среднее по каждому виду программы
for j in range(programs):
    avg = sum(scores[i][j] for i in range(sportsmen)) / sportsmen
    print(f"Программа {j+1}: {avg:.2f}")
print()

# 9.7
print("9.7:")
students = 15
subjects = 3
grades = [[random.randint(2, 5) for _ in range(subjects)] for _ in range(students)]

# а) общее количество пятерок
fives = 0
for i in range(students):
    for j in range(subjects):
        if grades[i][j] == 5:
            fives += 1
print(f"Пятерок: {fives}")

# б) количество троек у каждого ученика
for i in range(students):
    threes = grades[i].count(3)
    print(f"Ученик {i+1}: троек - {threes}")

# в) количество двоек по каждому предмету
for j in range(subjects):
    twos = sum(1 for i in range(students) if grades[i][j] == 2)
    print(f"Предмет {j+1}: двоек - {twos}")
print()

# 9.8
print("9.8:")
students = 14
subjects = 3
grades = [[random.randint(2, 5) for _ in range(subjects)] for _ in range(students)]

# а) студенты без двоек
no_twos = 0
for i in range(students):
    if 2 not in grades[i]:
        no_twos += 1
print(f"Студентов без двоек: {no_twos}")
# б) предметы только с 4 и 5
good_subjects = 0
for j in range(subjects):
    if all(grades[i][j] in [4, 5] for i in range(students)):
        good_subjects += 1
print(f"Предметов только с 4 и 5: {good_subjects}")

# в) количество двоек по каждому предмету
for j in range(subjects):
    twos = sum(1 for i in range(students) if grades[i][j] == 2)
    print(f"Предмет {j+1}: двоек - {twos}")
print()

# 9.9
print("9.9:")
sportsmen = 8
sports = 5
scores = [[random.randint(1, 10) for _ in range(sports)] for _ in range(sportsmen)]

# а) максимальная оценка
max_score = max(max(row) for row in scores)
print(f"Максимальная оценка: {max_score}")

# б) баллы победителя
winner_score = max(sum(row) for row in scores)
print(f"Баллы победителя: {winner_score}")
print()

# 9.10
print("9.10:")
workers = 12
months = 3
salaries = [[random.randint(20000, 50000) for _ in range(months)] for _ in range(workers)]

# а) максимальная зарплата
max_salary = max(max(row) for row in salaries)
print(f"Максимальная зарплата: {max_salary}")

# б) работник с наибольшей суммой
max_worker = max(range(workers), key=lambda i: sum(salaries[i]))
print(f"Работник с наибольшей суммой: {max_worker + 1}")

# в) месяц с максимальной общей зарплатой
month_totals = [sum(salaries[i][j] for i in range(workers)) for j in range(months)]
max_month = month_totals.index(max(month_totals)) + 1
print(f"Месяц с максимальной общей зарплатой: {max_month}")
print()

# 9.11
print("9.11:")
workers = 12
months = 3
salaries = [[random.randint(20000, 50000) for _ in range(months)] for _ in range(workers)]

# а) для каждого работника - месяц с наибольшей зарплатой
for i in range(workers):
    max_month = salaries[i].index(max(salaries[i])) + 1
    print(f"Работник {i+1}: месяц {max_month}")

# б) для каждого месяца - работник с наибольшей зарплатой
for j in range(months):
    max_worker = max(range(workers), key=lambda i: salaries[i][j])
    print(f"Месяц {j+1}: работник {max_worker + 1}")
print()

# 9.12
print("9.12:")
parallels = 11
classes = 4
students = [[random.randint(20, 30) for _ in range(classes)] for _ in range(parallels)]

# а) самый малочисленный класс
min_class = min(min(row) for row in students)
print(f"Самый малочисленный класс: {min_class} учеников")

# б) минимальное количество в параллели
min_parallel = min(sum(row) for row in students)
print(f"Минимальное количество в параллели: {min_parallel}")

# в) минимальное общее количество по классам А, Б, В, Г
class_totals = [sum(students[i][j] for i in range(parallels)) for j in range(classes)]
min_class_total = min(class_totals)
print(f"Минимальное общее количество по классам: {min_class_total}")
print()

# 9.13
print("9.13:")
parallels = 11
classes = 4
students = [[random.randint(20, 30) for _ in range(classes)] for _ in range(parallels)]

min_students = min(min(row) for row in students)
print(f"Самый малочисленный класс: {min_students} учеников")
print()

# 9.14
print("9.14:")
shops = 3
days = 10
income = [[random.randint(10000, 50000) for _ in range(days)] for _ in range(shops)]

# а) магазин с максимальным общим доходом
shop_totals = [sum(income[i]) for i in range(shops)]
max_shop = shop_totals.index(max(shop_totals)) + 1
print(f"Магазин с максимальным доходом: {max_shop}")

# б) день с максимальным общим доходом
day_totals = [sum(income[i][j] for i in range(shops)) for j in range(days)]
max_day = day_totals.index(max(day_totals)) + 1
print(f"День с максимальным доходом: {max_day}")

# в) магазин и день с максимальным доходом за день
max_income = 0
max_shop_day = (0, 0)
for i in range(shops):
    for j in range(days):
        if income[i][j] > max_income:
            max_income = income[i][j]
            max_shop_day = (i+1, j+1)
print(f"Максимальный доход за день: магазин {max_shop_day[0]}, день {max_shop_day[1]}")
print()

# 9.15
print("9.15:")
shops = 3
days = 10
income = [[random.randint(10000, 50000) for _ in range(days)] for _ in range(shops)]

# а) для каждого магазина - день с максимальным доходом
for i in range(shops):
    max_day = income[i].index(max(income[i])) + 1
    print(f"Магазин {i+1}: день {max_day}")
# б) для каждого дня - магазин с максимальным доходом
for j in range(days):
    max_shop = max(range(shops), key=lambda i: income[i][j])
    print(f"День {j+1}: магазин {max_shop + 1}")
print()

# 9.16
print("9.16:")
courses = 5
groups = 6
students = [[random.randint(15, 30) for _ in range(groups)] for _ in range(courses)]

# а) курс с наименьшим количеством студентов
course_totals = [sum(students[i]) for i in range(courses)]
min_course = course_totals.index(min(course_totals)) + 1
print(f"Курс с наименьшим количеством студентов: {min_course}")

# б) самая малочисленная группа
min_students = float('inf')
min_group = (0, 0)
for i in range(courses):
    for j in range(groups):
        if students[i][j] < min_students:
            min_students = students[i][j]
            min_group = (i+1, j+1)
print(f"Самая малочисленная группа: курс {min_group[0]}, группа {min_group[1]}")

# в) самая малочисленная группа на каждом курсе
for i in range(courses):
    min_group = students[i].index(min(students[i])) + 1
    print(f"Курс {i+1}: самая малочисленная группа {min_group}")
print()

# 9.17
print("9.17:")
products = 5
days = 6
prices = [random.randint(100, 1000) for _ in range(products)]
quantities = [[random.randint(1, 20) for _ in range(days)] for _ in range(products)]

# а) общий доход по каждому виду товара
product_income = []
for i in range(products):
    income = sum(quantities[i][j] * prices[i] for j in range(days))
    product_income.append(income)
    print(f"Товар {i+1}: доход {income}")

# б) общий доход за каждый день
day_income = []
for j in range(days):
    income = sum(quantities[i][j] * prices[i] for i in range(products))
    day_income.append(income)
    print(f"День {j+1}: доход {income}")

# в) общий доход за 6 дней
total_income = sum(day_income)
print(f"Общий доход за 6 дней: {total_income}")

# г) товар с максимальным доходом
max_product = product_income.index(max(product_income)) + 1
print(f"Товар с максимальным доходом: {max_product}")

# д) день с максимальным доходом
max_day = day_income.index(max(day_income)) + 1
print(f"День с максимальным доходом: {max_day}")
# 9.18
import random
groups = 3
students_per_group = 20
exams = 3
scores = [[[random.randint(3, 5) for _ in range(exams)] for _ in range(students_per_group)] for _ in range(groups)]
group_averages = []
for group in scores:
    total = 0
    count = 0
    for student in group:
        total += sum(student)
        count += len(student)
    group_averages.append(total / count)
best_group = group_averages.index(max(group_averages)) + 1
print(f"9.18: Лучшая группа - {best_group}")

# 9.19
print("9.19:")
for num in range(120, 141):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    print(f"Число {num}: {divisors} делителей")

# 9.20
n = int(input("9.20. Введите n: "))
for num in range(1, n + 1):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    print(f"{num}{'+' * divisors}")

# 9.21
print("9.21:")
result = []
for num in range(1, 301):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    if divisors == 5:
        result.append(num)
print(result)

# 9.22
print("9.22:")
result = []
for num in range(200, 501):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    if divisors == 6:
        result.append(num)
print(result)

# 9.23
a, b, k = 100, 200, 8
print("9.23:")
result = []
for num in range(a, b + 1):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    if divisors == k:
        result.append(num)
print(result)

# 9.24
a, b = 100, 200
print("9.24:")
max_divisors = 0
numbers = []
for num in range(a, b + 1):
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += 1
    if divisors > max_divisors:
        max_divisors = divisors
        numbers = [num]
    elif divisors == max_divisors:
        numbers.append(num)
print(f"a) {max(numbers)}")
print(f"b) {min(numbers)}")

# 9.25
print("9.25:")
primes = []
for num in range(100, 1000):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print(primes)

# 9.26
print("9.26:")
primes = []
num = 2
while len(primes) < 100:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    num += 1
print(primes)

# 9.27
print("9.27:")
for num in range(50, 71):
    divisors_sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors_sum += i
    print(f"Число {num}: сумма делителей = {divisors_sum}")

# 9.28
print("9.28:")
result = []
for num in range(100, 301):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    if divisors_sum == 50:
        result.append(num)
print(result)

# 9.29
print("9.29:")
result = []
for num in range(300, 601):
    divisors_sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors_sum += i
    if divisors_sum % 10 == 0:
        result.append(num)
print(result)

# 9.30
print("9.30:")
for num in range(100, 1000):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    if divisors_sum == num:
        print(num)

# 9.31
print("9.31:")
perfect_numbers = []
num = 1
while num < 100000:
    divisors_sum = 0
    i = 1
    while i < num:
        if num % i == 0:
            divisors_sum += i
        i += 1
    if divisors_sum == num:
        perfect_numbers.append(num)
    num += 1
print(perfect_numbers)

# 9.32
a, b = 100, 200
print("9.32:")
max_sum = 0
result_num = a
for num in range(a, b + 1):
    divisors_sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors_sum += i
    if divisors_sum > max_sum:
        max_sum = divisors_sum
        result_num = num
print(result_num)

9.33
def sum_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def find_amicable_numbers(limit):
    amicable_pairs = []
    for a in range(2, limit):
        b = sum_divisors(a)
        if b > a and b < limit:
            if sum_divisors(b) == a:
                amicable_pairs.append((a, b))
    return amicable_pairs

pairs = find_amicable_numbers(50000)
for pair in pairs:
    print(pair)
# 9.34
n = 15
print("9.34:")
count = 0
for ten in range(n // 10 + 1):
    for five in range((n - ten * 10) // 5 + 1):
        for two in range((n - ten * 10 - five * 5) // 2 + 1):
            one = n - ten * 10 - five * 5 - two * 2
            if one >= 0:
                count += 1
print(f"a) {count} способов")

print("b) Все способы:")
for ten in range(n // 10 + 1):
    for five in range((n - ten * 10) // 5 + 1):
        for two in range((n - ten * 10 - five * 5) // 2 + 1):
            one = n - ten * 10 - five * 5 - two * 2
            if one >= 0:
                print(f"10р: {ten}, 5р: {five}, 2р: {two}, 1р: {one}")

# 9.35
n = 50
denominations = [64, 32, 16, 8, 4, 2, 1]
print("9.35:")
for amount in range(n, n + 11):
    temp = amount
    result = []
    for denom in denominations:
        count = temp // denom
        if count > 0:
            result.append(f"{denom}:{count}")
        temp %= denom
    print(f"{amount}: {', '.join(result)}")

# 9.36
s = 24
print("9.36 a):")
for a in range(1, s + 1):
    if s % a == 0:
        b = s // a
        print(f"{a}x{b}")

print("9.36 b):")
for a in range(1, int(s**0.5) + 1):
    if s % a == 0:
        b = s // a
        if a <= b:
            print(f"{a}x{b}")

# 9.37
v = 24
print("9.37 a):")
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if v % (a * b) == 0:
            c = v // (a * b)
            if a * b * c == v:
                print(f"{a}x{b}x{c}")

print("9.37 b):")
found = set()
for a in range(1, v + 1):
    for b in range(a, v + 1):
        if v % (a * b) == 0:
            c = v // (a * b)
            if c >= b and a * b * c == v:
                triple = tuple(sorted([a, b, c]))
                if triple not in found:
                    found.add(triple)
                    print(f"{a}x{b}x{c}")

# 9.38
print("9.38:")
solutions = set()
for x in range(1, 31):
    for y in range(x, 31):
        k2 = x*x + y*y
        k = int(k2**0.5)
        if k <= 30 and k*k == k2:
            solutions.add((x, y, k))
for sol in sorted(solutions):
    print(f"{sol[0]}^2 + {sol[1]}^2 = {sol[2]}^2")

# 9.39
m, n = 5, 2
result = 0
for i in range(1, m + 1):
    result += i ** n
print(f"9.39: {result}")

# 9.40
n = 5
result = 0
for i in range(1, n + 1):
    result += i ** i
print(f"9.40: {result}")

# 9.41
n = 15
print("9.41:")
for i in range(100, 1000):
    digits = [i // 100, (i // 10) % 10, i % 10]
    if sum(digits) == n:
        print(i)

# 9.42
print("9.42:")
for i in range(100, 1000):
    digits = [i // 100, (i // 10) % 10, i % 10]
    if len(set(digits)) == 3:
        print(i)

# 9.43
numbers = [12, 18, 24]
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

result = numbers[0]
for num in numbers[1:]:
    result = gcd(result, num)
print(f"9.43: {result}")

# 9.44
weights = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
v = 2500
count = 0
for i in range(2**10):
    total = 0
    for j in range(10):
        if i & (1 << j):
            total += weights[j]
    if total == v:
        count += 1
print(f"9.44: {count} способов")

# 9.45
m, n = 25, 100
print("9.45:")
for num in range(1, n):
    digits = [int(d) for d in str(num)]
    if sum(digits) ** 2 == m:
        print(num)

# 9.46
def digital_root(num):
    while num >= 10:
        num = sum(int(d) for d in str(num))
    return num

print(f"9.46: Цифровой корень 12345 = {digital_root(12345)}")

# 9.47
print("9.47:")
for bulls in range(11):
    for cows in range(21):
        calves = 100 - bulls - cows
        if calves >= 0 and bulls * 10 + cows * 5 + calves * 0.5 == 100:
            print(f"Быков: {bulls}, Коров: {cows}, Телят: {calves}")

9.48
def prime_factors_unique(n):
    factors = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1:
        factors.add(n)
    return sorted(factors)

def prime_factors_multiple(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

n = int(input())

print("Вариант 1 (уникальные множители):")
unique_factors = prime_factors_unique(n)
print(" × ".join(map(str, unique_factors)))

print("Вариант 2 (все множители):")
multiple_factors = prime_factors_multiple(n)
print(" × ".join(map(str, multiple_factors)))
# 9.49
n = 84
print("9.49:")
prime_factors = set()
temp = n
divisor = 2
while temp > 1:
    while temp % divisor == 0:
        prime_factors.add(divisor)
        temp //= divisor
    divisor += 1
print(prime_factors)

# 9.50
n = 30
print("9.50:")
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

result = []
for i in range(1, n):
    if gcd(i, n) == 1:
        result.append(i)
print(result)

# 9.51
n, p = 30, 12
print("9.51:")
result = []
for i in range(1, n):
    if gcd(i, p) == 1:
        result.append(i)
print(result)

# 9.52
p, q = 12, 30
print("9.52:")
result = []
for i in range(1, q + 1):
    if q % i == 0 and gcd(i, p) == 1:
        result.append(i)
print(result)

# 9.53
print("9.53:")
cubes = {}
found = None
n = 1
while found is None:
    for a in range(1, int(n**(1/3)) + 1):
        for b in range(a, int(n**(1/3)) + 1):
            if a**3 + b**3 == n:
                if n in cubes:
                    found = n
                    break
                else:
                    cubes[n] = (a, b)
    n += 1
print(f"Наименьшее число: {found}")

# 9.54
print("9.54:")
fractions = set()
for denominator in range(2, 8):
    for numerator in range(1, denominator):
        if gcd(numerator, denominator) == 1:
            fractions.add((numerator, denominator))
for frac in sorted(fractions, key=lambda x: x[0]/x[1]):
    print(f"{frac[0]}/{frac[1]}")
