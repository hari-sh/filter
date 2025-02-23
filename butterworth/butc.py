import cmath

a = 1
b = 1
c = 1

dis = (b**2) - (4 * a*c)

ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)

print('The roots are')
print(ans1)
print(ans2)
