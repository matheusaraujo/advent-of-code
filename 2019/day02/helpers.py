def g(arr, i):
    return arr[arr[i]]


def s(arr, i, v):
    arr[arr[i]] = v


def simulate(a):
    i = 0
    while a[i] != 99:
        if a[i] == 1:
            s(a, i + 3, g(a, i + 1) + g(a, i + 2))
        elif a[i] == 2:
            s(a, i + 3, g(a, i + 1) * g(a, i + 2))
        i += 4
