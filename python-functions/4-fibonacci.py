def fibonacci_sequence(n):
    list = []

    a, b = 0, 1
    count = 0

    if n == 1:
        return [a]
    elif n <= 0:
        return []
    else:
        while count < n:
            list.append(a)
            nth = a + b
            a = b
            b = nth
            count += 1
    return list
