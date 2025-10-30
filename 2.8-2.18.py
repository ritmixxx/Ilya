2.8
import math
r = float(input("Введите радиус окружности: "))
circumference = 2 * math.pi * r
area = math.pi * r ** 2
print(f"Длина окружности: {circumference}")
print(f"Площадь круга: {area}")
2.9
import math
x = float(input("x: "))
y = float(input("y: "))
z = 2*x**3 - 3.44*x*y + 2.3*x**2 - 7.1*y + 2
print(z)
2.9
a = float(input("Введите a: "))
b = float(input("Введите b: "))
x = 3.14 * (a + b)**3 + 2.75 * b**2 - 12.7 * a - 4.1
print(x)
2.10
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
average = (a + b) / 2
print("Среднее арифметическое:", average)
2.10
import math
a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
geometric_mean = math.sqrt(a * b)
print("Среднее геометрическое:", geometric_mean)
2.11
mass = float(input("Введите массу тела (в килограммах): "))
volume = float(input("Введите объем тела (в кубических метрах): "))
if volume != 0:
    density = mass / volume
    print("Плотность материала:", density)
else:
    print("Объем не может быть нулевым.")
2.12
population = int(input("Введите количество жителей: "))
area = float(input("Введите площадь территории (в км²): "))
if area != 0:
    density = population / area
    print("Плотность населения:", density, "человек на км²")
else:
    print("Площадь не может быть равна нулю.")
2.13
def linearEq(a, b):
  if a == 0:
      return "Нет решения"
  else:
      return -b / a
2.14
import math
a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))
hypotenuse = math.sqrt(a**2 + b**2)
print("Гипотенуза:", hypotenuse)
2.15
import math
R = float(input("Введите внешний радиус (R): "))
r = float(input("Введите внутренний радиус (r): "))
if R > r >= 0:
    area = math.pi * (R**2 - r**2)
    print("Площадь кольца:", area)
else:
    print("Ошибка: внешний радиус должен быть больше внутреннего, а внутренний неотрицателен.")
2.16
import math

a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

c = math.sqrt(a**2 + b**2)
perimeter = a + b + c

print("Периметр треугольника:", perimeter)
2.17
import math

a = float(input("Введите длину верхнего основания (a): "))
b = float(input("Введите длину нижнего основания (b): "))
h = float(input("Введите высоту трапеции (h): "))

if b >= a >= 0 and h > 0:
    c = math.sqrt(h**2 + ((b - a)/2)**2)
    perimeter = a + b + 2 * c
    print("Периметр равнобедренной трапеции:", perimeter)
else:
    print("Ошибка: проверьте, что основания неотрицательны, a ≤ b, и высота положительна.")
2.18
def z(x, y):
    return (x + (2 + y) / (x ** 2)) / (y + 1 / (x ** 2 + 10) ** (1 / 2))
def q(x, y):
    return 7.25 * math.sin(x) - abs(y)
