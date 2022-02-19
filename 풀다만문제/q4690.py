# 졸라 틀리는 구만
for a in range(5, 101):
    cube = a**3
    for d in range(2, a) :
        for c in range(2, d):
            for b in range(2, c):
                triple = b**3 + c**3 + d**3
                if(cube == triple):
                    print('Cube = %d, Triple = (%d,%d,%d)' %(a, b, c, d))