import math

a, b, c = map(int, input().split())

def ans(a, b, c):
    D = (b**2) - 4*a*c  
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(x1, x2)
    elif D == 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        print(x1)
        print("중근을 갖습니다.")
    else:
        print("근이 존재하지 않습니다.")

ans(a, b, c)
