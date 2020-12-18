n=5
def fac(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    print("res = n! =", factorial)
    return factorial

fac(n)
