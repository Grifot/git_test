# (100°F − 32) × 5/9 = 37.778°C

fahrenheit = float(input('화씨 온도 : '))
celsius    = (fahrenheit - 32.) * 5./9.
print(f'화씨 온도 {fahrenheit}도는 섭씨 온도 {celsius:.4f}도입니다.')
