#Jose Ricardo Vasquez Vega
import math

def sumacplx(a,b):
    real = a[0] + b[0]
    imag = a [1] + b[1]
    return (real,imag)

def restcplx(a,b):
    realr = a[0] - b[0]
    imagr = a [1] - b[1]
    return (realr,imagr)

def mutcplx(a,b):
    realx = a[0]* b[0] - a[1]*b[1]
    imagx = a[1]* b[0] + a[0]* b[1]
    return (realx, imagx)

def divcplx(a,b):
    divisor = (b[0]**2 + b[1]**2)
    if divisor != 0:
        reald = (a[0] * b[0] + a[1]*b[1])/divisor
        imagd = (b[0] * a[1] - a[0]*b[1])/divisor
        return reald, imagd
    return print('La divisor es 0')

def modulcplx(a):
    a = (a[0]*a[0]+a[1]*a[1])**(0.5)
    return a

def conjucplx(a):
    return a[0],-a[1]

def ConverPolarCart(a):
    realCPC = a[0] * math.cos(a[1])
    imagCPC = a[0] * math.sin(a[1])
    return (realCPC, imagCPC)

def ConverCartPolar(a):
    r = abs((a[0]*a[0]) + (a[1]*a[1]))
    grados = math.atan2(a[1], a[0])
    return r, grados

def retornarFase(a):
    Fase = math.atan2(a[1], a[0])
    return Fase

if __name__ == '__main__':
    print(sumacplx((3, 2), (-5, 5.2)))
    print(restcplx((3, 2), (-5, 5.2)))
    print(mutcplx((3, 5), (-2.6, 6.8)))
    print(divcplx((3, 5), (-2.6, 6.8)))
    print(modulcplx((-2.6, 6.8)))
    print(conjucplx((3, 2)))
    print(ConverPolarCart((4.24, math.pi/6)))
    print(ConverCartPolar((-2.6, 6.8)))
    print(retornarFase((-2.6, 6.8)))
