# 7.106
numbers = list(map(float, input().split()))
filtered = [x for x in numbers if x > 20]
print(sum(filtered) / len(filtered))

# 7.107
x = int(input())
n = int(input())
numbers = list(map(int, input().split()))
filtered = [a for a in numbers if a > n]
print(sum(filtered) / len(filtered))

# 7.108
m = int(input())
n = int(input())
numbers = list(map(int, input().split()))
filtered = [b for b in numbers if b % n == 0]
print(sum(filtered) / len(filtered))

# 7.109
numbers = list(map(int, input().split()))
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 == 1]
print(sum(even)/len(even) if even else 0, sum(odd)/len(odd) if odd else 0)

# 7.110
masses = list(map(float, input().split()))
heavy = [m for m in masses if m > 100]
light = [m for m in masses if m <= 100]
print(sum(heavy)/len(heavy), sum(light)/len(light))

# 7.111
heights = list(map(float, input().split()))
boys = [abs(h) for h in heights if h < 0]
girls = [h for h in heights if h > 0]
print(sum(boys)/len(boys) if boys else 0, sum(girls)/len(girls) if girls else 0)

# 7.112
numbers = list(map(float, input().split()))
filtered = [x for x in numbers if x > 10]
print(sum(filtered)/len(filtered) if filtered else 0)

# 7.113
x = int(input())
n = int(input())
numbers = list(map(int, input().split()))
filtered = [a for a in numbers if a > n]
print(sum(filtered)/len(filtered) if filtered else 0)

# 7.114
numbers = list(map(int, input().split()))
even = [x for x in numbers if x % 2 == 0]
print(sum(even)/len(even) if even else 0)

# 7.115
m = int(input())
n = int(input())
numbers = list(map(int, input().split()))
filtered = [a for a in numbers if a % n == 0]
print(sum(filtered)/len(filtered) if filtered else 0)

# 7.116
cars = list(map(float, input().split()))
motorcycles = list(map(float, input().split()))
avg_car = sum(cars) / len(cars)
avg_motorcycle = sum(motorcycles) / len(motorcycles)
print(avg_car > 3 * avg_motorcycle)
# 7.117
heights = list(map(float, input().split()))
boys = [abs(h) for h in heights if h < 0]
girls = [h for h in heights if h > 0]
avg_boys = sum(boys) / len(boys)
avg_girls = sum(girls) / len(girls)
print(avg_boys - avg_girls > 10)

# 7.118a
n = int(input())
numbers = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    if numbers[i] == 10:
        print(i+1)
        break

# 7.118b
n = int(input())
numbers = list(map(int, input().split()))
for i in range(n):
    if numbers[i] == 10:
        print(i+1)
        break

# 7.119
n = int(input())
numbers = list(map(int, input().split()))
for i in range(n-1, -1, -1):
    if numbers[i] > 100:
        print(i+1)
        break

# 7.120
n = int(input())
numbers = list(map(int, input().split()))
index = -1
for i in range(n-1, -1, -1):
    if numbers[i] == 25:
        index = i+1
        break
print(index)

# 7.121
k = int(input())
numbers = list(map(int, input().split()))
for i in range(k-1, -1, -1):
    if numbers[i] < 0:
        print(i+1)
        break

# 7.122
m = int(input())
numbers = list(map(int, input().split()))
index = -1
for i in range(m-1, -1, -1):
    if numbers[i] % 100 == 12:
        index = i+1
        break
print(index)

# 7.123
heights = list(map(float, input().split()))
new_height = float(input())
position = 1
for h in heights:
    if new_height < h:
        position += 1
print(position)

# 7.124
points = list(map(int, input().split()))
N = int(input())
position = 1
for p in points:
    if p > N:
        position += 1
print(position)

# 7.125a
numbers = list(map(float, input().split()))
n = float(input())
total = 0
for num in numbers:
    if num < n:
        total += num
print(total)

# 7.125b
numbers = list(map(float, input().split()))
n = float(input())
for i in range(len(numbers)-1):
    if numbers[i] < n < numbers[i+1]:
        print(i+1, numbers[i], i+2, numbers[i+1])
        break

# 7.126
numbers = list(map(float, input().split()))
for i in range(len(numbers)):
    if numbers[i] < 0:
        print(i+1)
        break
else:
    print("No")

# 7.127
numbers = []
num = int(input())
while num != 100:
    numbers.append(num)
    num = int(input())
for i in range(len(numbers)):
    if numbers[i] == 666:
        print(i+1)
        break
else:
    print("No")

# 7.128
numbers = list(map(int, input().split()))
for i in range(len(numbers)):
    if numbers[i] % 10 == 7:
        print(i+1)
        break
else:
    print("No")

# 7.129
numbers = []
num = int(input())
while num != -1:
    numbers.append(num)
    num = int(input())
for i in range(len(numbers)):
    if numbers[i] % 7 == 0:
        print(i+1)
        break
else:
    print("No")

# 7.130
numbers = list(map(int, input().split()))
count = 0
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1]:
        count += 1
print(count)

# 7.131
numbers = list(map(int, input().split()))
max_count = 1
current_count = 1
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1
print(max_count)

# 7.132
numbers = list(map(int, input().split()))
count = 1
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i-1]:
        count += 1
print(count)

# 7.133
numbers = []
num = float(input())
while num != 1000:
    numbers.append(num)
    num = float(input())
max_count = 1
current_count = 1
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1
print(max_count)

# 7.134
numbers = []
num = float(input())
while num != 0:
    numbers.append(num)
    num = float(input())
count = 1
for i in range(1, len(numbers)):
    if numbers[i] != numbers[i-1]:
        count += 1
print(count)

# 7.135a
numbers = list(map(float, input().split()))
print(max(numbers))

# 7.135b
numbers = list(map(float, input().split()))
print(min(numbers))

# 7.135c
numbers = list(map(float, input().split()))
min_val = numbers[0]
max_val = numbers[0]
for num in numbers:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
print(max_val, min_val)

# 7.136
results = []
while True:
    try:
        time = float(input())
        results.append(time)
        print(min(results))
    except:
        break

# 7.137
distances = list(map(float, input().split()))
print(max(distances))

# 7.138
temperatures = list(map(float, input().split()))
print(max(temperatures))

# 7.139
speeds = list(map(float, input().split()))
print(max(speeds))

# 7.140
import math
areas = list(map(float, input().split()))
radii = [math.sqrt(area/math.pi) for area in areas]
print(min(radii))

# 7.141
import math
areas = list(map(float, input().split()))
diagonals = [math.sqrt(2*area) for area in areas]
print(max(diagonals))

# 7.142
materials = []
for _ in range(20):
    mass, volume = map(float, input().split())
    materials.append((mass, volume))
max_density = max(mass/volume for mass, volume in materials)
print(max_density)

# 7.143
countries = []
for _ in range(16):
    population, area = map(float, input().split())
    countries.append((population, area))
min_density = min(population/area for population, area in countries)
print(min_density)

# 7.144a
n = int(input())
max_sum = 0
for _ in range(n):
    a, b = map(float, input().split())
    max_sum = max(max_sum, a + b)
print(max_sum)

# 7.144b
n = int(input())
min_product = float('inf')
for _ in range(n):
    a, b = map(float, input().split())
    min_product = min(min_product, a * b)
print(min_product)

# 7.145
scores = list(map(float, input().split()))
scores.remove(max(scores))
scores.remove(min(scores))
print(sum(scores) / len(scores))

# 7.146
heights = list(map(float, input().split()))
print(max(heights) - min(heights))

# 7.147
students = list(map(int, input().split()))
print(max(students) - min(students))

# 7.148
n = int(input())
numbers = list(map(int, input().split()))
print(max(numbers) - min(numbers) <= 25)

# 7.149
masses = list(map(float, input().split()))
print(max(masses) / min(masses) > 2)

# 7.150
n = int(input())
numbers = list(map(int, input().split()))
max_len = 0
current_len = 0
for num in numbers:
    if num % 2 == 0:
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 0
print(max_len)

# 7.151
sequence = list(map(int, input().split()))
min_len = float('inf')
current_len = 0
for num in sequence:
    if num == 0:
        current_len += 1
    else:
        if current_len > 0:
            min_len = min(min_len, current_len)
        current_len = 0
if current_len > 0:
    min_len = min(min_len, current_len)
print(min_len if min_len != float('inf') else 0)

# 7.152
numbers = list(map(float, input().split()))
n = float(input())
closest_index = 0
min_diff = abs(numbers[0] - n)
for i in range(1, len(numbers)):
    diff = abs(numbers[i] - n)
    if diff < min_diff:
        min_diff = diff
        closest_index = i
print(closest_index+1, numbers[closest_index])

# 7.153
numbers = list(map(int, input().split()))
even_numbers = [x for x in numbers if x % 2 == 0]
print(max(even_numbers) if even_numbers else "No")

# 7.154
numbers = list(map(int, input().split()))
max_count = 1
current_count = 1
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i-1]:
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 1
print(max_count)

# 7.155
numbers = list(map(int, input().split()))
max_len = 1
current_len = 1
for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 1
print(max_len)

# 7.156
numbers = list(map(int, input().split()))
max_len = 1
current_len = 1
for i in range(1, len(numbers)):
    if (numbers[i] > numbers[i-1] and current_len > 0) or (numbers[i] < numbers[i-1] and current_len < 0):
        current_len = abs(current_len) + 1
        if numbers[i] > numbers[i-1]:
            current_len = current_len
        else:
            current_len = -current_len
    else:
        if numbers[i] > numbers[i-1]:
            current_len = 2
        else:
            current_len = -2
    max_len = max(max_len, abs(current_len))
print(max_len)

# 7.157a
n = int(input())
numbers = list(map(int, input().split()))
max_index = 0
for i in range(1, n):
    if numbers[i] >= numbers[max_index]:
        max_index = i
print(max_index+1)

# 7.157b
n = int(input())
numbers = list(map(int, input().split()))
min_index = 0
for i in range(1, n):
    if numbers[i] < numbers[min_index]:
        min_index = i
print(min_index+1)

# 7.158
m = int(input())
numbers = list(map(int, input().split()))
max_index = 0
min_index = 0
for i in range(1, m):
    if numbers[i] >= numbers[max_index]:
        max_index = i
    if numbers[i] < numbers[min_index]:
        min_index = i
print(max_index+1, min_index+1)

# 7.159
residents = list(map(int, input().split()))
max_apartment = 0
for i in range(len(residents)):
    if residents[i] >= residents[max_apartment]:
        max_apartment = i
print(max_apartment+1)

# 7.160
results = list(map(float, input().split()))
best_index = 0
for i in range(1, len(results)):
    if results[i] < results[best_index]:
        best_index = i
print(best_index+1)

# 7.161
points = list(map(int, input().split()))
min_index = 0
for i in range(1, len(points)):
    if points[i] < points[min_index]:
        min_index = i
print(min_index+1)

# 7.162
precipitation = list(map(float, input().split()))
max_day = 0
for i in range(1, len(precipitation)):
    if precipitation[i] >= precipitation[max_day]:
        max_day = i
print(max_day+1)

# 7.163
n = int(input())
times = list(map(float, input().split()))
wait_times = [0] * n
for i in range(1, n):
    wait_times[i] = wait_times[i-1] + times[i-1]
min_time_index = 0
for i in range(1, n):
    if times[i] <= times[min_time_index]:
        min_time_index = i
print(*wait_times)
print(min_time_index+1)

# 7.164a
n = int(input())
max_avg = 0
max_index = 0
for i in range(n):
    a, b = map(float, input().split())
    avg = (a + b) / 2
    if avg >= max_avg:
        max_avg = avg
        max_index = i
print(max_index+1)

# 7.164b
import math
n = int(input())
min_geom = float('inf')
min_index = 0
for i in range(n):
    a, b = map(float, input().split())
    geom = math.sqrt(a * b)
    if geom < min_geom:
        min_geom = geom
        min_index = i
print(min_index+1)

# 7.165
n = 25
max_speed = 0
max_index = 0
for i in range(n):
    distance, time = map(float, input().split())
    speed = distance / time
    if speed > max_speed:
        max_speed = speed
        max_index = i
print(max_index+1)

# 7.166
n = 20
min_current = float('inf')
min_index = 0
for i in range(n):
    voltage, resistance = map(float, input().split())
    current = voltage / resistance
    if current < min_current:
        min_current = current
        min_index = i
print(min_index+1)

# 7.167
n = int(input())
numbers = list(map(int, input().split()))
min_index = 0
max_index = 0
for i in range(1, n):
    if numbers[i] < numbers[min_index]:
        min_index = i
    if numbers[i] > numbers[max_index]:
        max_index = i
if min_index < max_index:
    print("min")
else:
    print("max")

# 7.168
ages = list(map(int, input().split()))
oldest_index = 0
youngest_index = 0
for i in range(1, len(ages)):
    if ages[i] > ages[oldest_index]:
        oldest_index = i
    if ages[i] < ages[youngest_index]:
        youngest_index = i
if oldest_index < youngest_index:
    print("oldest")
else:
    print("youngest")

# 7.169
results = list(map(float, input().split()))
first_place = results.index(min(results))
last_place = results.index(max(results))
print(first_place < last_place)

# 7.170a
numbers = list(map(int, input().split()))
max_sum = numbers[0] + numbers[1]
for i in range(1, len(numbers)-1):
    max_sum = max(max_sum, numbers[i] + numbers[i+1])
print(max_sum)

# 7.170b
numbers = list(map(int, input().split()))
min_sum = numbers[0] + numbers[1]
for i in range(1, len(numbers)-1):
    min_sum = min(min_sum, numbers[i] + numbers[i+1])
print(min_sum)

# 7.170c
numbers = list(map(int, input().split()))
max_sum = numbers[0] + numbers[1]
max_pair = (1, 2)
for i in range(1, len(numbers)-1):
    if numbers[i] + numbers[i+1] > max_sum:
        max_sum = numbers[i] + numbers[i+1]
        max_pair = (i+1, i+2)
print(*max_pair)

# 7.170d
numbers = list(map(int, input().split()))
min_sum = numbers[0] + numbers[1]
min_pair = (1, 2)
for i in range(1, len(numbers)-1):
    if numbers[i] + numbers[i+1] <= min_sum:
        min_sum = numbers[i] + numbers[i+1]
        min_pair = (i+1, i+2)
print(*min_pair)

# 7.171a
numbers = list(map(int, input().split()))
first_max = max(numbers[0], numbers[1])
second_max = min(numbers[0], numbers[1])
for num in numbers[2:]:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max:
        second_max = num
print(first_max, second_max)

# 7.171b
numbers = list(map(int, input().split()))
first_min = min(numbers[0], numbers[1])
second_min = max(numbers[0], numbers[1])
for num in numbers[2:]:
    if num < first_min:
        second_min = first_min
        first_min = num
    elif num < second_min:
        second_min = num
print(first_min, second_min)

# 7.172
results = list(map(float, input().split()))
first = min(results)
results.remove(first)
second = min(results)
print(first, second)

# 7.173
speeds = list(map(float, input().split()))
max_speed = max(speeds)
speeds.remove(max_speed)
second_max = max(speeds)
print(second_max)

# 7.174
points = list(map(int, input().split()))
first = max(points)
points.remove(first)
second = max(points)
points.remove(second)
third = max(points)
print(first, second, third)

# 7.175
n = int(input())
times = list(map(float, input().split()))
sorted_times = sorted(times)
print(sum(sorted_times[:4]))

# 7.176
temperatures = list(map(float, input().split()))
sorted_temps = sorted(temperatures)
print(temperatures.index(sorted_temps[0])+1, temperatures.index(sorted_temps[1])+1)

# 7.177
A = int(input())
if A == 0:
    print(4)
else:
    print(5)

# 7.178a
numbers = list(map(int, input().split()))
max_val = max(numbers)
count = numbers.count(max_val)
print(count)

# 7.178b
numbers = list(map(int, input().split()))
min_val = min(numbers)
count = numbers.count(min_val)
print(count)

# 7.179
residents = list(map(int, input().split()))
max_residents = max(residents)
count = residents.count(max_residents)
print(count)

# 7.180
temperatures = list(map(float, input().split()))
min_temp = min(temperatures)
count = temperatures.count(min_temp)
print(count)

# 7.181a
dominoes = list(map(int, input().split()))
valid = True
for i in range(len(dominoes)-1):
    if dominoes[i] % 10 != dominoes[i+1] // 10:
        valid = False
        break
print(valid)

# 7.181b
dominoes = list(map(int, input().split()))
valid = True
for i in range(len(dominoes)-1):
    current = str(dominoes[i])
    next_dom = str(dominoes[i+1])
    if current[1] != next_dom[0] and current[1] != next_dom[1] and current[0] != next_dom[0] and current[0] != next_dom[1]:
        valid = False
        break
print(valid)
