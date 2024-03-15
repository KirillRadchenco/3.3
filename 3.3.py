def find_letter_indices(letter, st):
    first_index = None
    last_index = None

    for i, char in enumerate(st):
        if char == letter:
            if first_index is None:
                first_index = i
            last_index = i

    if first_index is None:
        return (None, None)

    return (first_index, last_index)


# Пример использования
result = find_letter_indices('a', 'banana')
print(result)  # Вывод: (1, 5)

result = find_letter_indices('z', 'banana')
print(result)  # Вывод: (None, None)
