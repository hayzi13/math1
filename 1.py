import math
a = float(input('Введите a: '))
b1 = math.cos(3/8*math.pi-a/4)**2 - math.cos(11/8*math.pi+a/4)**2
b2 = math.sqrt(2)/2*math.sin(a/2)
print(f'b1 = {b1}')
print(f'b2 = {b2}') 
