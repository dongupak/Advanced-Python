import time

# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

start_t = time.time()
for x in fibon(1000000):
    pass

end_t = time.time()
print('total time = ',end_t - start_t)

