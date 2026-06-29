def permutations(elements):
    if len(elements) == 1:
        return [elements]
    
    result = []
    for i, current in enumerate(elements):
        remaining_elements = elements[:i] + elements[i + 1:]

        for p in permutations(remaining_elements):
            result.append([current] + p)

    return result

print(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])[999_999])