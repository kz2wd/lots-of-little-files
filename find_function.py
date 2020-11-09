import math


def digit_sum(number):
    to_add = 0
    for i, (a, b) in enumerate(zip(number_separation[:-1], number_separation[1:])):
        if a <= number < b:
            return (i + 1) * (number - a + 1) + to_add
        else:
            to_add += (b - a) * (i + 1)


conversion_table = [(1, 1), (11, 10), (192, 100), (2893, 1000), (38894, 10000),
                    (488895, 100000), (5888896, 1000000), (68888897, 10000000)]

number_separation = [10 ** i for i in range(0, 9)]
print(number_separation)


conversion_table = [(digit_sum(i), i) for i in number_separation][:-1]


def number_from_digit(digit_count, st_offset=0):
    count = 0
    len_dc = len(str(digit_count))
    digit_count -= conversion_table[len_dc - 1][0]
    count += conversion_table[len_dc - 1][1]
    count += digit_count / len_dc
    return count


st = 8
ed = 10
ds = digit_sum(ed) - digit_sum(st)
print("ds :", ds)

ds = int(ds / 2)
dstx = number_from_digit(ds)
print(dstx + st - 1)



