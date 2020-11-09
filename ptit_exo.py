def tri(a, b, c):
    return (a, b, c) if (a < b < c) else (a, c, b) if (a < c < b) else (b, a, c) if (b < a < c) else (b, c, a) if (b < c < a) else (c, a, b) if (c < a < b) else (c, b ,a)


def sec_to_hours(n):
    hours = n // 3600
    reste = n % 3600
    mins = reste // 60
    reste %= 60
    secs = reste
    return hours, mins, secs


print(sec_to_hours(86523))
print(tri(1, 2,  3))
