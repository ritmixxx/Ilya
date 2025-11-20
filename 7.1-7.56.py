# 7.1
numbers = list(map(float, input().split()))
print(sum(numbers))

# 7.2
n = int(input())
numbers = list(map(float, input().split()))
print(sum(numbers))

# 7.3
sides = list(map(float, input().split()))
print(sum(sides))

# 7.4
masses = list(map(float, input().split()))
print(sum(masses))

# 7.5
salaries = list(map(float, input().split()))
print(sum(salaries))

# 7.6
resistances = list(map(float, input().split()))
print(sum(resistances))

# 7.7
resistances = list(map(float, input().split()))
total = sum(1/r for r in resistances)
print(1/total)

# 7.8a
num = int(input())
total = 0
while num != 0:
    total += num
    num = int(input())
print(total)

# 7.8b
num = int(input())
count = 0
while num != 0:
    count += 1
    num = int(input())
print(count)

# 7.9
student1 = list(map(int, input().split()))
student2 = list(map(int, input().split()))
print(sum(student1), sum(student2))

# 7.10
athlete1 = list(map(int, input().split()))
athlete2 = list(map(int, input().split()))
print(sum(athlete1), sum(athlete2))

# 7.11
numbers = list(map(float, input().split()))
product = 1
for num in numbers:
    product *= num
print(product)

# 7.12
numbers = []
num = int(input())
while num != 0:
    numbers.append(num)
    num = int(input())
for i in range(len(numbers)):
    print(*numbers[:i+1])

# 7.13
numbers = list(map(float, input().split()))
print(sum(x*x for x in numbers))

# 7.14
n = int(input())
numbers = list(map(float, input().split()))
print(sum(x*x for x in numbers))

# 7.15
numbers = list(map(float, input().split()))
print(sum(numbers) > 100.78)

# 7.16
n = int(input())
p = int(input())
numbers = list(map(int, input().split()))
print(sum(numbers) < p)

# 7.17
numbers = list(map(int, input().split()))
print(sum(numbers) % 2 == 0)

# 7.18
n = int(input())
b = int(input())
numbers = list(map(int, input().split()))
print(sum(numbers) % b == 0)

# 7.19
feb_this_year = list(map(float, input().split()))
feb_last_year = list(map(float, input().split()))
print(sum(feb_this_year) > sum(feb_last_year))

# 7.20
capacity = float(input())
masses = list(map(float, input().split()))
print(sum(masses) <= capacity)

# 7.21
athlete1 = list(map(int, input().split()))
athlete2 = list(map(int, input().split()))
print(1 if sum(athlete1) > sum(athlete2) else 2)

# 7.22
set1 = list(map(float, input().split()))
set2 = list(map(float, input().split()))
print(1 if sum(set1) < sum(set2) else 2)

# 7.23
numbers = list(map(float, input().split()))
product = 1
for num in numbers:
    product *= num
print(product < 10000)

# 7.24
n = int(input())
numbers = list(map(float, input().split()))
product = 1
for num in numbers:
    product *= num
print(product > n)

# 7.25
numbers = list(map(float, input().split()))
print(sum(numbers)/len(numbers))

# 7.26
n = int(input())
numbers = list(map(float, input().split()))
print(sum(numbers)/n)

# 7.27
grades = list(map(int, input().split()))
print(sum(grades)/len(grades))

# 7.28
grades = list(map(int, input().split()))
print(sum(grades)/len(grades))

# 7.29
grades = list(map(int, input().split()))
print(sum(grades)/len(grades))

# 7.30
masses = list(map(float, input().split()))
print(sum(masses)/len(masses))

# 7.31
total = 0
count = 0
num = int(input())
while num >= 0:
    total += num
    count += 1
    num = int(input())
print(total/count if count > 0 else 0)

# 7.32
class1 = list(map(float, input().split()))
class2 = list(map(float, input().split()))
print(sum(class1)/len(class1), sum(class2)/len(class2))

# 7.33
january = list(map(float, input().split()))
march = list(map(float, input().split()))
print(sum(january)/len(january), sum(march)/len(march))

# 7.34
class1 = list(map(float, input().split()))
class2 = list(map(float, input().split()))
print(sum(class1)/len(class1), sum(class2)/len(class2))
# 7.35
class1 = list(map(int, input().split()))
class2 = list(map(int, input().split()))
print(sum(class1)/len(class1), sum(class2)/len(class2))

# 7.36
areas = []
for _ in range(10):
    s, y = map(float, input().split())
    areas.append((s, y))
total_wheat = sum(s * y for s, y in areas)
avg_yield = total_wheat / sum(s for s, y in areas)
print(total_wheat, avg_yield)

# 7.37
districts = []
for _ in range(12):
    people, area = map(float, input().split())
    districts.append((people, area))
total_people = sum(people for people, area in districts)
total_area = sum(area for people, area in districts)
print(total_people / total_area)

# 7.38
districts = []
for _ in range(12):
    people, density = map(float, input().split())
    districts.append((people, density))
total_area = sum(people / density for people, density in districts)
print(total_area)

# 7.39a
n = int(input())
numbers = list(map(float, input().split()))
print(sum(abs(x) for x in numbers))

# 7.39b
n = int(input())
numbers = list(map(float, input().split()))
product = 1
for x in numbers:
    product *= abs(x)
print(product)

# 7.39c
n = int(input())
numbers = list(map(float, input().split()))
result = []
for i in range(0, n-1, 2):
    result.append(numbers[i] + numbers[i+1])
print(*result)

# 7.39d
n = int(input())
numbers = list(map(float, input().split()))
total = 0
sign = 1
for x in numbers:
    total += sign * abs(x)
    sign = -sign
print(total)

# 7.40
numbers = list(map(float, input().split()))
print(sum(x for x in numbers if x > 10.75))

# 7.41
n = int(input())
p = float(input())
numbers = list(map(float, input().split()))
print(sum(x for x in numbers if x > p))

# 7.42
numbers = list(map(int, input().split()))
print(sum(x for x in numbers if x % 2 == 0))

# 7.43
numbers = list(map(int, input().split()))
print(sum(x for x in numbers if x % 10 == 0))

# 7.44
numbers = list(map(int, input().split()))
total = 0
for i in range(1, 20, 2):
    total += numbers[i]
print(total)

# 7.45
numbers = list(map(float, input().split()))
total = 0
for i in range(0, 15, 2):
    total -= numbers[i]
print(total)

# 7.46a
n = int(input())
numbers = list(map(int, input().split()))
print(numbers[0] + numbers[-1])

# 7.46b
n = int(input())
numbers = list(map(int, input().split()))
print(numbers[1] - numbers[-2])

# 7.47
prices = list(map(float, input().split()))
print(sum(x for x in prices if x > 1000))

# 7.48
pages = list(map(int, input().split()))
newspaper_max = 16
print(sum(x for x in pages if x > newspaper_max))

# 7.49
days = list(map(float, input().split()))
total = 0
for i in range(1, len(days), 2):
    total += days[i]
print(total)

# 7.50
classes = list(map(int, input().split()))
total = 0
for i in range(0, len(classes), 2):
    total += classes[i]
print(total)

# 7.51
numbers = list(map(int, input().split()))
total = 0
for num in numbers:
    if num % 2 == 0:
        break
    total += num
print(total)

# 7.52a
numbers = list(map(int, input().split()))
print(sum(x for x in numbers if x > 20) > 100)

# 7.52b
numbers = list(map(int, input().split()))
print(sum(x for x in numbers if x < 50) % 2 == 0)

# 7.53a
n = int(input())
numbers = list(map(float, input().split()))
print(sum(x for x in numbers if x < 25.5) <= 50)

# 7.53b
n = int(input())
numbers = list(map(float, input().split()))
print(sum(x for x in numbers if x <= 20) % 3 == 0)

# 7.54
n = int(input())
p = float(input())
numbers = list(map(float, input().split()))
print(sum(x for x in numbers if x > 20.5) < p)

# 7.55
n = int(input())
m = float(input())
q = float(input())
numbers = list(map(float, input().split()))
print(sum(x for x in numbers if x <= m) > q)

# 7.56
n = int(input())
m = float(input())
p = int(input())
numbers = list(map(float, input().split()))
print(sum(x for x in numbers if x <= m) % p == 0)
