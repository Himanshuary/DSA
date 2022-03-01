def calculatingpower(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * calculatingpower(base, exp-1)

print(calculatingpower(5,3))