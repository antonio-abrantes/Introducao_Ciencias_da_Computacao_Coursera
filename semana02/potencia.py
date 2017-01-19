def pot(base, exp):
    mult = 1
    for i in range(0, exp):
        mult *= base

    return mult


print(pot(3, 3))