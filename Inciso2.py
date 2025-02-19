from stack import Stack
import time

def respuesta2():
    t1 = time.time()

    n = 55500000
    s1 = Stack(n)
    for i in range(n):
        s1.push('f')

    t2 = time.time()
    tiempo = t2 - t1
    return tiempo

print(respuesta2())
