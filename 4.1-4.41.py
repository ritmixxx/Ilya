4.1
def compare(a, b):
    if a > b:
        return f'Число {a} больше, чем {b}'
    else:
        return f'Число {b} больше, чем {a}'
4.2
import math
def y_func(x):
    if x > 0:
        y = (math.sin(x)) ** 2
    else:
        y = 1 - 2 * math.sin(x ** 2)
    return y
4.3 
import math
def y_func(x):
    if x > 0:
        y = (math.sin(x)) ** 2
    else:
        y = 1 + 2 * math.sin(x ** 2)
    return y
4.4 
def find_oblast(x=0, y=0):
    if x > 4:
        return f'Это область II'
    elif x < 4:
        return 'Это область I'
    elif x == 4:
        return 'Вы попали чётко на линию'
4.5
def find_oblast(x=0, y=0):
    if y < 3:
        return f'Это область II'
    elif y > 3:
        return 'Это область I'
    elif y == 3:
        return 'Вы попали чётко на линию'
4.6
# Вариант А
def find_y(x):
    if x < 2:
        return f'y = {x}'
    else:
        return f'y = 2'
# Вариант B
def find_y(x):
    if x < 3:
        return f'y = {-x}'
    else:
        return f'y = -3'
4.7
import math
def func(x):
    if math.sin(x) < 0:
        k = x ** 2
    else:
        k = abs(x)

    if k < x:
        return k * x
    else:
        return k + x
4.8 
import math
def func(x):
    if math.sin(x) < 0:
        k = abs(x)
    else:
        k = x ** 2

    if k < x:
        return abs(x)
    else:
        return k * x
4.9
def find_min_max(a, b):
    if a > b:
        return f'{a} - максимальное, {b} - минимальное'
    return f'{b} - максимальное, {a} - минимальное'
4.10
def kmetr_or_foot(kmetr, foot):
    foot_to_kmet = foot * 0.3048 / 1000
    if kmetr > foot_to_kmet:
        return f'Расстояние в километрах больше'
    elif kmetr < foot_to_kmet:
        return 'Расстояние в футах больше'
    elif kmetr == foot_to_kmet:
        return 'Расстояния равны'
4.11
def which_V_is_bigger(kmph, mps):
    kmph_to_mps = kmph / 3.6

    if kmph_to_mps > mps:
        return f'Скорость км/ч больше, чем м/с'
    elif kmph_to_mps < mps:
        return f'Скорость м/с больше, чем км/ч'
    elif kmph_to_mps == mps:
        return f'Скорости равны'
4.12
import math
def Ssquare_or_Scirle(square_a, circle_r):
    Ssquare = square_a ** 2
    Scircle = math.pi * (circle_r ** 2)

    if Ssquare > Scircle:
        return f'Площадь квадрата больше, чем круга'
    elif Ssquare < Scircle:
        return f'Площадь круга больше, чем квадрата'
    elif Ssquare == Scircle:
        return f'Площади равны'
4.13
def density(m1, v1, m2, v2):
    den1 = m1 / v1
    den2 = m2 / v2

    if den1 > den2:
        return f'Плотность первого тела больше, чем второго'
    elif den1 < den2:
        return f'Плотность второго тела больше, чем первого'
    elif den1 == den2:
        return f'Плотности равны'
4.14
def current(r1, r2, u1, u2):
    i1 = u1 / r1
    i2 = u2 / r2

    if i1 > i2:
        return f'Ток первого участка больше, чем второго'
    elif i1 < i2:
        return f'Ток второго участка больше, чем первого'
    elif i2 == i2:
        return f'Токи равны'
4.15
def discriminant(a, b, c):
    if a == 0:
        return f'Коэффициент не подходит под условие задачи'

    discrim = b ** 2 - 4 * a * c

    if discrim > 0:
        return f'Уравнение имеет 2 корня'
    elif discrim < 0:
        return f'Уравнение не имеет корней'
    elif discrim == 0:
        return f'Уравнение имеет 1 корень'
4.16
import math
def find_roots(a, b, c):
    if a == 0:
        return f'Коэффициент не подходит под условие задачи'

    discrim = b ** 2 - 4 * a * c

    if discrim >= 0:
        x1 = (-b + math.sqrt(discrim)) / (2 * a)
        x2 = (-b - math.sqrt(discrim)) / (2 * a)

        return f'Корень №1: {x1}, ' \
               f'Корень №2: {x2}'

    elif discrim < 0:
        return f'Корней нет'
4.17
def find_age(year, month, year_today, month_today):
    if 0 > month > 13 or 0 > month_today > 13 or not isinstance(month, int) or not isinstance(month_today, int) \
            or not isinstance(year, int) or not isinstance(year_today, int):
        return 'Некорректно ведены данные'

    if month > month_today:
        full_year = year_today - year - 1
    elif month <= month_today:
        full_year = year_today - year

    return f'Человеку {full_year} полных лет'
4.18
import math

def fit_in(Ssquare, Scircle):
    ans = []

    a = math.sqrt(Ssquare)
    r = math.sqrt(Scircle / math.pi)
    diam = 2 * r
    diag = math.sqrt(a**2 + a ** 2)

    if diam <= a:
        ans.append('Круг вместится в квадрат')
    else:
        ans.append('Круг НЕ вместится в квадрат')

    if diag <= diam:
        ans.append('Квадрат вместится в круг')
    else:
        ans.append('Квадрат НЕ вместится в круг')

    return ans
