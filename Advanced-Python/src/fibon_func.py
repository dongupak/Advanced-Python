import time

# function version
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result

start_t = time.time()
for x in fibon(1000000):
    pass

end_t = time.time()
print('total time = ', end_t - start_t)
