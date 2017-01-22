from math import sqrt
import locale

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = b * b - 4 * a * c

if(delta <= 0 or a <= 0 ):
		print("Impossivel calcular")
else:
    r1 = (-b + sqrt(delta)) / (2 * a)
    r2 = (-b - sqrt(delta)) / (2 * a)
    print("R1 =", locale.format("%1.5f", r1));
    print("R2 =", locale.format("%1.5f", r2));