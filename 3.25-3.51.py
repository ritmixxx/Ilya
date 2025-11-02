3.25 
def digit_2to3(chislo):
    if chislo < 100 or chislo > 999:
        print("Трёхзначное число!!!")
    else:
        print(
            f'Вторую и третью цифры поменяли - {100 * (chislo // 100) + 1 * (chislo // 10 % 10) + 10 * (chislo % 10)}')
3.26 
def perestanovka(chislo):
    if (chislo < 100 or chislo > 999) or \
            (chislo // 100 == chislo // 10 % 10 or chislo // 100 == chislo % 10 or chislo // 10 % 10 == chislo % 10):
        print("Трёхзначное число с разными цифрами!!!!")
    else:
       print(1 * (chislo // 100) + 10 * (chislo // 10 % 10) + 100 * (chislo % 10))
       print(1 * (chislo // 100) + 100 * (chislo // 10 % 10) + 10 * (chislo % 10))
       print(10 * (chislo // 100) + 1 * (chislo // 10 % 10) + 100 * (chislo % 10))
       print(10 * (chislo // 100) + 100 * (chislo // 10 % 10) + 1 * (chislo % 10))
       print(100 * (chislo // 100) + 1 * (chislo // 10 % 10) + 10 * (chislo % 10))
       print(f'А шестая комбинация - это само число {chislo}')
3.27
def sum_digit(chislo):
    if len(str(chislo)) == 4:
        return \
            f'Сумма цифр числа - {chislo % 10 + chislo // 1000 + chislo // 100 % 10 + chislo // 10 % 10}'
    elif len(str(chislo)) == 5:
        return \
            f'Сумма цифр числа - {chislo // 10000 + chislo // 1000 % 10 + chislo // 100 % 10 + chislo // 10 % 10 + chislo % 10}'
3.28
num = int(input())
reversed_num = int(str(num)[::-1])
print(reversed_num)
digits = list(str(num))
new_num_str = digits[1] + digits[0] + digits[3] + digits[2]
print(int(new_num_str))
digits = list(str(num))
digits[1], digits[2] = digits[2], digits[1]
print(int(''.join(digits)))
a, b, c, d = str(num)
print(int(c + d + a + b))
print(int(c + d + a + b))
3.29
def ed_des(chislo):
    if chislo < 10:
        return "Введите число больше 9!!!"

    print(f'Единиц в числе - {chislo % 10}')
    print(f'Десятков в числе - {chislo // 10}')
3.30  
def des_sot(chislo):
    if chislo < 100:
        return f'Число должно быть больше 99!!!'

    print(f'Десятков в числе - {chislo % 100 // 10}')
    print(f'Сотен в числе - {chislo // 100}')
3.31
def sot_tis(chislo):
    if chislo < 1000:
        return f'Нужно число больше 999!!!'

    print(f'Сотен в числе - {chislo // 100 % 10}')
    print(f'Тысяч в числе - {chislo // 1000}')
3.32 
def nashel_x(chislo=237):
    if chislo < 100 or chislo > 999:
        return "Трёхзначное число!!!"

    a = chislo % 100
    b = a * 10
    c = b + chislo // 100

    return f'Изначальное число - {c}'
3.33
def nashel_n(chislo):
    if chislo > 999 or chislo < 100:
        return "Трёхзначное число!!!"

    a = chislo - (chislo % 10)
    b = a // 10
    c = 100 * (chislo % 10) + b

    return f'Полученное число - {c}'
3.34
def nashel_x_1(chislo):
    if chislo > 999 or chislo < 1:
        return "Попробуй другое число!"

    a = chislo // 10
    b = 100 * (chislo % 10) + a

    return f'Первоначальное число - {b}'
3.35
p = int(input())
for x in range(100, 1000):
    s = str(x)
    first_digit = int(s[0])
    remaining_number = int(s[1:])
    if remaining_number * 10 + first_digit == p:
        print("Ответ:", x)
        break

3.36  
def nashel_x_2(chislo):
    if chislo < 10 or chislo > 999 or chislo // 10 % 10 == 0:
        return "Попробуй другое число"

    a = 100 * (chislo // 10 % 10) + 10 * (chislo // 100) + 1 * (chislo % 10)

    return f'Первоначальное число - {a}'
3.37
p = int(input())
p_str = str(p)
if len(p_str) == 2:
    p_str = '0' + p_str
second_digit = p_str[0]
for x in range(100, 1000):
    s = str(x)
    if s[1] == second_digit:
        new_number = int(second_digit + s[0] + s[2])
        if new_number == p:
            print("Ответ:", x)
            break
3.38
def nashel_x_3(chsilo):
    if chsilo > 999 or chsilo < 100:
        return "Попробуй другое число"

    a = 100 * (chsilo // 100) + 10 * (chsilo % 10) + 1 * (chsilo // 10 % 10)

    return f'Первоначальное число - {a}'
3.39
p = int(input())
p_str = str(p)
if len(p_str) == 2:
    p_str = '0' + p_str
for x in range(100, 1000):
    s = str(x)
    second_digit = s[1]
    remaining_number = s[0] + s[2]
    candidate = int(remaining_number + second_digit)
    if candidate == p:
        print("Ответ:", x)
        break
3.40
def nashel_x_4(chislo):
    if chislo < 1 or chislo > 999:
        return 'Попробуй другое число'
    a = 100 * (chislo % 10) + 10 * (chislo // 10 % 10) + 1 * (chislo // 100)
    return f'Первоначальное число - {a}'
3.41
p = int(input())
p_str = str(p)
if len(p_str) == 2:
    p_str = '0' + p_str
last_digit = p_str[0]
rest = p_str[1:]
for x in range(100, 1000):
    s = str(x)
    last_digit_x = s[2]
    remaining_two = s[:2]
    permuted = remaining_two[::-1]
    candidate = int(last_digit_x + permuted)
    if candidate == p:
        print("Ответ:", x)
        break
3.42
a = int(input())
b = int(input())
num_a = a * 10 + a
result = num_a + b
result_tens = result // 10
result_units = result % 10
print(result_tens, result_units)
3.43
a = int(input())
b = int(input())
suma = (a * 10 + a) + (b * 10 + b)
digit_1 = suma // 10
digit_0 = suma % 10
print(digit_1, digit_0)
3.44
a = int(input())
b = int(input())
suma = (a * 100 + a * 10 + a) + (b * 10 + b)
digit_100 = suma // 100
digit_10 = (suma // 10) % 10
digit_1 = suma % 10
print(digit_100, digit_10, digit_1)
3.45
k = int(input())
text = ''
for num in range(10, 100):
    text += str(num)
pos = k - 1
pair_index = pos // 2 + 1
pair_digits = text[pos:pos+2]
if k % 2 == 0:
    digit = int(text[pos])
else:
    digit = int(text[pos])
print(pair_index)
print(int(pair_digits))
print(digit)
3.46
k = int(input())
text = ''
for num in range(101, 151):
    text += str(num)
digit_k = text[k - 1]
if k % 3 == 0:
    print(digit_k)
elif k in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100, 103, 106, 109, 112, 115, 118, 121, 124, 127, 130, 133, 136, 139, 142, 145, 148]:
    print(digit_k)
elif k in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 137, 140, 143, 146, 149]:
    print(digit_k)
3.47
h = int(input())
m = int(input())
s = int(input())
total_hours = h + (m + s / 60) / 60
angle = total_hours * 30
print(angle)
3.48
u = float(input())
full_hours = int(u // 30)
full_minutes = int((u % 30) * 2)
print(full_hours, full_minutes)
