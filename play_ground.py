def float_list(start, stop, step):
    count = int((stop - start) / step)
    values = []
    for a in range(count):
        values.append(round(a * step, 2))
    return values

start = 0
stop = 2
step = 0.1
values = float_list(start, stop, step)
values.append(round(stop, 2))

print(values)