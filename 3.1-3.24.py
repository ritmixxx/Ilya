3.1
def cm_m(cm):
    return f'В {cm} см {cm // 100} полных метров'
3.2
def kg_cent(kg):
    return f'В {kg} кг {kg // 100} центнеров'
3.3
print(f'За этот период прошло {234 // 7} недель')
3.4
def apples(N, k):
    return f'Каждому школьнику достанется {k // N} яблок, а в корзинке останется {k % N}'
3.5
def otrezh_kvadrat(a=543, b=130, c=130):
    a1 = a // c
    a2 = b // c
    if a < c or b < c:
        return f"Хер ты получишь квадрат со стороной {c}"
    elif a1 >= 1 and a2 >= 1:
        return f'Ты можешь получить {min(a1, a2)} квадратов'
3.6
def kupe(mesto):
    if 0 <= mesto <= 36:
        return f'Ваше место находится в {mesto // 4} купе'
    else:
        return 'Твоё место в другом поезде, идиот'
3.7
import math
def etazh(kvartira):
    if 0 <= kvartira <= 15:
        return f'Ваш этаж - {math.ceil(kvartira / 3)}'
    else:
        return 'Вали с нашей территории'
3.8
n = 20
m = 15
a = [[0] * m for i in range(n)]
k = 1643
for i in range(n):
    for j in range(m):
        a[i][j] = k
        k += 1
def row(bilet):
    if 1643 <= bilet < 1943:
        for i in range(n):
            for j in range(m):
                if a[i][j] == bilet:
                    return f'Ваш ряд: {i + 1}'
    else:
        return f'Вы не в том кинотеатре'
3.9
def time(secunds):
    print(f'С начала суток прошло {secunds // 3600} часов')
    print(f'С начала очередного часа прошло {secunds % 3600} минут')
    print(f'С начала очередной минуты прошло {secunds % 3600 % 60} секунд')
3.10
nedela = {1: 'понедельник',
          2: 'вторник',
          3: 'среда',
          4: 'четверг',
          5: 'пятница',
          6: 'суббота',
          7: 'воскресенье'}

def den_nedely(k=1, d=1):
    if k not in range(1, 366):
        return 'В году 365 дней, дебил!'
    elif d not in range(1, 8):
        return "В неделе всего 7 дней, придурок!"

    if d == 1:
        if k % 7 == 0:
            return f'Этот день недели - {nedela.get(k % 7 + 7)}'
        else:
            return f'Этот день недели - {nedela.get(k % 7)}'
    elif d != 1:
        if (k + d - 1) % 7 == 0:
            return f'Этот день недели - {nedela.get((k + d - 1) % 7 + 7)}'
        else:
            return f'Этот день недели - {nedela.get((k + d - 1) % 7)}'
3.11
def mesyac(n):
    return n % 12 + 1
3.12 
import math
"""
c = []
m, n, k, r = 4, 5, 1, 1  # Объявление переменных

for i in range(m):
    c.append([])
    r += 1
    for j in range(n):
        c[i].append(k)  # Создание массива квартира - порядковый номер
        k += 4  # Типа c[0] - это 1 порядковый номер, т.о. 1,5,9,13,17 кв - первые на своих этажах
    k = r


def kvartira(nomer):
    print(f'Квартира находится на {math.ceil(nomer / 4)} этаже')  # Находим этаж квартиры
    check = 0
    for i in range(m):
        while nomer not in c[i]:  # Находим, какому массиву принадлежит число, возвращаем его
            i += 1
            check = i
    print(f'Эта квартира по счёту {check + 1} на этаже')
"""
def kvartira(nomer):
    print(f'Квартира находится на {math.ceil(nomer / 4)} этаже')
    print(f'Квартира по счёту {abs(nomer - (math.ceil(nomer / 4) - 1) * 4)} на этаже')

3.13 
import math
c = []
m, n, k = 10, 5, 1

for i in range(m):
    c.append([])
    for j in range(n):
        c[i].append(k)
        k += 1

def koord(chislo):
    print(f'Данное число находится в {math.ceil(chislo / 5)} строке')
    print(f'Данное число находится в {(abs(chislo - (math.ceil(chislo / 5) - 1) * 5))} столбце')
3.14
def kv_pod(nomer):
    podezd = math.ceil(nomer / 54)
    etazh = nomer - (podezd - 1) * 54
    print(f'Данная квартира находится в {podezd} подъезде')
    print(f'Данная квартира находится на {math.ceil(etazh / 6)} этаже')
    print(f'Данная квартира по счёту {abs(nomer - (math.ceil(nomer / 6) - 1) * 6)} на этаже')
3.15
import math

def tovar1(nomer):
    yarus = math.ceil(nomer / 120)
    sekcia = math.ceil((nomer - 120 * (yarus - 1)) / 15)

    print(f'Данный товар находится в секции {sekcia} на ярусе {yarus}')

def tovar2(nomer):
    yarus = nomer - 10 * (math.ceil(nomer / 10) - 1)
    sekcia = math.ceil(nomer / 150)

    print(f'Данный товар находится в секции {sekcia} на ярусе {yarus}')
3.16
def des_ed(chislo):
    if chislo > 99 or chislo < 10:
        print("Двузначное число!!!!")
    else:
        print(f'Число десятков в числе - {chislo // 10}')
        print(f'Число единиц в числе - {chislo % 10}')
3.17
def digit_sum(chislo):
    if chislo > 99 or chislo < 10:
        print("Двузначное число!!!!")
    else:
        print(f'Сумма цифр в числе - {chislo // 10 + chislo % 10}')
3.18
def digit_naoborot(chislo):
    if chislo > 99 or chislo < 10:
        print("Двузначное число!!!!")
    else:
        print(f'Число наоборот - {10 * (chislo % 10) + 1 * (chislo // 10)}')
3.19
def digits(chislo):
    if chislo < 100 or chislo > 999:
        print("Трёхзначное число!!!")
    else:
        print(chislo // 100, ', ', chislo // 10 % 10, ', ', chislo % 10, sep='')
3.20
def digit_3_ops(chislo):
    if chislo < 100 or chislo > 999:
        print("Трёхзначное число!!!")
    else:
        print(f'Число единиц в числе - {chislo % 10}')
        print(f'Число десятков в числе - {chislo // 10}')
        print(f'Сумма цифр числа - {(chislo // 100) + (chislo // 10 % 10) + (chislo % 10)}')
        print(f'Произведение цифр числа - {(chislo // 100) * (chislo // 10 % 10) * (chislo % 10)}')
3.21
def digits_3_naoborot(chislo):
    if chislo < 100 or chislo > 999:
        print("Трёхзначное число!!!")
    else:
        print(f'Число наоборот - {1 * (chislo // 100) + 10 * (chislo // 10 % 10) + 100 * (chislo % 10)}')
3.22
def digit_1to3(chislo):
    if chislo < 100 or chislo > 999:
        print("Трёхзначное число!!!")
    else:
        print(
            f'Первое слева цифру перенесли в конец - {1 * (chislo // 100) + 100 * (chislo // 10 % 10) + 10 * (chislo % 10)}')
3.23
def digit_3to1(chislo):
    if chislo < 100 or chislo > 999:
        print("Трёхзначное число!!!")
    else:
        print(
            f'Первую справа цифру перенесли в начало - {10 * (chislo // 100) + 1 * (chislo // 10 % 10) + 100 * (chislo % 10)}')
3.24
def digit_2to1(chislo):
    if chislo < 100 or chislo > 999:
        print("Трёхзначное число!!!")
    else:
        print(
            f'Первую и вторую цифры поменяли - {10 * (chislo // 100) + 100 * (chislo // 10 % 10) + 1 * (chislo % 10)}')
