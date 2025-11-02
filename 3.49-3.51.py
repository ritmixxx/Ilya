3.49
import math

u = float(input())
y = (u / math.pi) * 2
full_hours = int(u)
full_minutes = int(round((y - int(y)) * 60))
print(y, full_hours, full_minutes)
3.50
h, t = map(int, input().split())
def time_to_overlap(h, t):
    hours_in_deg = 30 * h + 0.5 * t
    minutes_in_deg = 6 * t
    diff = abs(hours_in_deg - minutes_in_deg)
    if diff > 180:
        diff = 360 - diff
    return int((diff / 5.5) + 0.5)
def time_to_perpendicular(h, t):
    hours_in_deg = 30 * h + 0.5 * t
    minutes_in_deg = 6 * t
    diff = abs(hours_in_deg - minutes_in_deg)
    if diff > 180:
        diff = 360 - diff
    for i in range(0, 720): 
        new_t = (t + i) % 60
        new_h = (h + (t + i)//60) % 12
        hours_deg = 30 * new_h + 0.5 * new_t
        minutes_deg = 6 * new_t
        diff_deg = abs(hours_deg - minutes_deg)
        if diff_deg > 180:
            diff_deg = 360 - diff_deg
        if abs(diff_deg - 90) < 1e-6:
            return i
    return None

print(time_to_overlap(h, t))
print(time_to_perpendicular(h, t))
3.51
a = int(input())
b = int(input())
print(int((a % b == 0) or (b % a == 0)))
