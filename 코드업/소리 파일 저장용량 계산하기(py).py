h, b, c, s = map(int, input().split())
print('{:0.1f} MB'.format((h * b * c * s)/(8 * 1024 * 1024)))