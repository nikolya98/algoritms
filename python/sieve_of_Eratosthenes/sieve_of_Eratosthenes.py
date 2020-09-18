def eratosthenes(n):
    simple_numbers = list(range(2, n + 1))
    start_index = 0
    while True:
        if len(simple_numbers) == start_index:
            break
        st = simple_numbers[start_index]
        for i in simple_numbers[start_index + 1:]:
            if i % st == 0:
                del simple_numbers[simple_numbers.index(i)]
        start_index += 1
    return simple_numbers