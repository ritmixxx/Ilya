# 7.57
feb_precipitation = list(map(float, input().split()))
even_sum = 0
odd_sum = 0
for i in range(len(feb_precipitation)):
    if (i+1) % 2 == 0:
        even_sum += feb_precipitation[i]
    else:
        odd_sum += feb_precipitation[i]
print(even_sum > odd_sum)

# 7.58
residents = list(map(int, input().split()))
odd_side = 0
even_side = 0
for i in range(len(residents)):
    if (i+1) % 2 == 1:
        odd_side += residents[i]
    else:
        even_side += residents[i]
print("odd" if odd_side > even_side else "even")

# 7.59
grades = list(map(int, input().split()))
print(grades.count(5))

# 7.60
temperatures = list(map(float, input().split()))
count = 0
for temp in temperatures:
    if temp < 0:
        count += 1
print(count)

# 7.61
heights = list(map(float, input().split()))
count = 0
for height in heights:
    if height < 165:
        count += 1
print(count)

# 7.62a
n = int(input())
p = float(input())
numbers = list(map(int, input().split()))
count = 0
for num in numbers:
    if num > p:
        count += 1
print(count)

# 7.62b
n = int(input())
numbers = list(map(int, input().split()))
count = 0
for num in numbers:
    if num % 10 == 5:
        count += 1
print(count)

# 7.62c
n = int(input())
k = int(input())
numbers = list(map(int, input().split()))
count = 0
for num in numbers:
    if num % k == 0:
        count += 1
print(count)

# 7.63
grades = list(map(int, input().split()))
count_5 = grades.count(5)
count_2 = grades.count(2)
print(count_5, count_2)

# 7.64
birth_years = list(map(int, input().split()))
before_1990 = 0
after_2000 = 0
for year in birth_years:
    if year < 1990:
        before_1990 += 1
    elif year > 2000:
        after_2000 += 1
print(before_1990, after_2000)

# 7.65
n = int(input())
count = 0
for _ in range(n):
    wins, losses = map(int, input().split())
    if wins > losses:
        count += 1
print(count)

# 7.66
n = int(input())
numbers = list(map(float, input().split()))
count = 0
for num in numbers:
    if num >= 0:
        break
    count += 1
print(count)

# 7.67
numbers = []
num = float(input())
while num != 0:
    numbers.append(num)
    num = float(input())
print(len(numbers))

# 7.68
n = int(input())
numbers = list(map(int, input().split()))
first_num = numbers[0]
count = 0
for num in numbers:
    if num != first_num:
        break
    count += 1
print(count)
# 7.69
grades = list(map(int, input().split()))
count = 0
for grade in grades:
    if grade != 5:
        break
    count += 1
print(count)

# 7.70
precipitation = list(map(float, input().split()))
count = 0
for precip in precipitation:
    if precip > 0:
        break
    count += 1
print(count)

# 7.71
n = int(input())
count = 0
for _ in range(n):
    exam1, exam2 = map(int, input().split())
    if exam1 == 2 or exam2 == 2:
        count += 1
print(count)

# 7.72
n = int(input())
numbers = list(map(float, input().split()))
positive = 0
negative = 0
for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
print(negative, positive)

# 7.73
m = int(input())
numbers = list(map(int, input().split()))
count_3 = 0
count_7 = 0
for num in numbers:
    if num % 3 == 0:
        count_3 += 1
    if num % 7 == 0:
        count_7 += 1
print(count_3, count_7)

# 7.74
n = int(input())
count = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a + b > c:
        count += 1
print(count)

# 7.75
import math
n = int(input())
R = float(input())
H = float(input())
P = float(input())
g = 9.8
hits = 0
for _ in range(n):
    alpha, v0 = map(float, input().split())
    alpha_rad = math.radians(alpha)
    t = R / (v0 * math.cos(alpha_rad))
    y = v0 * t * math.sin(alpha_rad) - g * t * t / 2
    if H <= y <= H + P:
        hits += 1
print(hits / n * 100)

# 7.76
team1_penalties = 0
team1_time = 0
team2_penalties = 0
team2_time = 0
for _ in range(24):
    team, time = map(int, input().split())
    if team == 1:
        team1_penalties += 1
        team1_time += time
    else:
        team2_penalties += 1
        team2_time += time
print(team1_penalties, team1_time, team2_penalties, team2_time)

# 7.77
team1_penalties = 0
team1_time = 0
team2_penalties = 0
team2_time = 0
while True:
    team = int(input())
    if team == 0:
        break
    time = int(input())
    if team == 1:
        team1_penalties += 1
        team1_time += time
    else:
        team2_penalties += 1
        team2_time += time
print(team1_penalties, team1_time, team2_penalties, team2_time)

# 7.78
grades = list(map(int, input().split()))
count_5 = grades.count(5)
count_4 = grades.count(4)
count_3 = grades.count(3)
count_2 = grades.count(2)
print(count_5, count_4, count_3, count_2)

# 7.79
points = list(map(int, input().split()))
wins = points.count(3)
draws = points.count(1)
losses = points.count(0)
print(wins, losses, draws)

# 7.80a
for _ in range(20):
    scored, conceded = map(int, input().split())
    if scored > conceded:
        print("выигрыш")
    elif scored == conceded:
        print("ничья")
    else:
        print("проигрыш")

# 7.80b
wins = 0
for _ in range(20):
    scored, conceded = map(int, input().split())
    if scored > conceded:
        wins += 1
print(wins)

# 7.80c
wins = 0
losses = 0
for _ in range(20):
    scored, conceded = map(int, input().split())
    if scored > conceded:
        wins += 1
    elif scored < conceded:
        losses += 1
print(wins, losses)

# 7.80d
wins = 0
draws = 0
losses = 0
for _ in range(20):
    scored, conceded = map(int, input().split())
    if scored > conceded:
        wins += 1
    elif scored == conceded:
        draws += 1
    else:
        losses += 1
print(wins, draws, losses)

# 7.80e
high_scoring = 0
for _ in range(20):
    scored, conceded = map(int, input().split())
    if scored >= 3:
        high_scoring += 1
print(high_scoring)

# 7.80f
total_points = 0
for _ in range(20):
    scored, conceded = map(int, input().split())
    if scored > conceded:
        total_points += 3
    elif scored == conceded:
        total_points += 1
print(total_points)

# 7.81
for _ in range(20):
    result = input().strip()
    if len(result) == 1:
        scored = 0
        conceded = 0
    else:
        scored = int(result[0])
        conceded = int(result[1])
    if scored > conceded:
        print("выигрыш")
    elif scored == conceded:
        print("ничья")
    else:
        print("проигрыш")

# 7.82a
n = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in range(n-1):
    if numbers[i] == numbers[i+1]:
        count += 1
print(count)

# 7.82b
n = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in range(n-1):
    if numbers[i] == 0 and numbers[i+1] == 0:
        count += 1
print(count)

# 7.82c
n = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in range(n-1):
    if numbers[i] % 2 == 0 and numbers[i+1] % 2 == 0:
        count += 1
print(count)

# 7.82d
n = int(input())
numbers = list(map(int, input().split()))
count = 0
for i in range(n-1):
    if numbers[i] % 10 == 5 and numbers[i+1] % 10 == 5:
        count += 1
print(count)
# 7.83
numbers = list(map(int, input().split()))
has_even = any(x % 2 == 0 for x in numbers)
print(has_even)

# 7.84
numbers = list(map(int, input().split()))
positive_count = sum(1 for x in numbers if x > 0)
print(positive_count <= 5)

# 7.85
numbers = list(map(float, input().split()))
count = sum(1 for x in numbers if x <= 33.2)
print(count % 4 == 0)

# 7.86
n = int(input())
numbers = list(map(int, input().split()))
count = sum(1 for x in numbers if x < 20)
print(count == 5)

# 7.87
m = int(input())
numbers = list(map(int, input().split()))
count = sum(1 for x in numbers if x > 0)
print(count % 3 == 0)

# 7.88
n = int(input())
x = int(input())
numbers = list(map(int, input().split()))
count = sum(1 for x in numbers if x < 0)
print(count > x)

# 7.89
m = int(input())
p = int(input())
numbers = list(map(int, input().split()))
count = sum(1 for x in numbers if x > m)
print(count % p == 0)

# 7.90
grades = list(map(int, input().split()))
has_3 = any(grade == 3 for grade in grades)
print(not has_3)

# 7.91
precipitation = list(map(float, input().split()))
dry_days = sum(1 for precip in precipitation if precip == 0)
print(dry_days == 10)

# 7.92
grades = list(map(int, input().split()))
has_2 = any(grade == 2 for grade in grades)
print(has_2)

# 7.93
powers = list(map(int, input().split()))
has_powerful = any(power > 200 for power in powers)
print(has_powerful)

# 7.94
numbers = list(map(float, input().split()))
count = 0
for i in range(1, len(numbers)-1):
    if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
        count += 1
print(count)

# 7.95
numbers = list(map(int, input().split()))
count = 0
for i in range(1, len(numbers)):
    if numbers[i] * numbers[i-1] < 0:
        count += 1
print(count)

# 7.96
numbers = list(map(int, input().split()))
for i in range(len(numbers)-1):
    if numbers[i] == numbers[i+1]:
        print(i+1, i+2)
        break
else:
    print("No")

# 7.97
numbers = []
num = int(input())
while num != -1:
    numbers.append(num)
    num = int(input())
for i in range(len(numbers)-1):
    if numbers[i] == numbers[i+1]:
        print(i+1, i+2)
        break
else:
    print("No")

# 7.98
numbers = list(map(int, input().split()))
for i in range(len(numbers)-1):
    if numbers[i] % 2 == 1 and numbers[i+1] % 2 == 1:
        print(i+1, i+2)
        break
else:
    print("No")

# 7.99
numbers = []
num = int(input())
while num != 9999:
    numbers.append(num)
    num = int(input())
for i in range(len(numbers)-1):
    if numbers[i] % 2 == 0 and numbers[i+1] % 2 == 0:
        print(i+1, i+2)
        break
else:
    print("No")

# 7.100
numbers = list(map(float, input().split()))
for i in range(len(numbers)-1):
    if numbers[i] >= numbers[i+1]:
        print(i+2)
        break
else:
    print("Yes")

# 7.101
numbers = []
num = float(input())
while num != 10000:
    numbers.append(num)
    num = float(input())
for i in range(len(numbers)-1):
    if numbers[i] >= numbers[i+1]:
        print(i+2)
        break
else:
    print("Yes")

# 7.102
heights = list(map(float, input().split()))
for i in range(len(heights)-1):
    if heights[i] < heights[i+1]:
        print("No")
        break
else:
    print("Yes")

# 7.103
points = list(map(int, input().split()))
for i in range(len(points)-1):
    if points[i] < points[i+1]:
        print("No")
        break
else:
    print("Yes")

# 7.104
numbers = list(map(int, input().split()))
all_equal = all(x == numbers[0] for x in numbers)
print(all_equal)

# 7.105
numbers = []
num = int(input())
while num >= 0:
    numbers.append(num)
    num = int(input())
all_equal = all(x == numbers[0] for x in numbers)
print(all_equal)
