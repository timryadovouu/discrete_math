def nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return b


def e(x):
    counter = 0
    for i in range(1, x + 1):
        if nod(i, x) == 1:
            counter += 1

    return counter


print(e(96))
print(410786 % 32)
print((88 ** 96) % 97)
print([i for i in range(1, 410786 + 1) if 410786 % i == 0])
print((61*61)   )
