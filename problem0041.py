import math

def is_prime(num):
    for i in range(1, math.ceil(math.sqrt(num)) + 1):
        if i != 1 and num % i == 0:
            return False
    return True


def permutations(elements):
    if len(elements) == 1:
        return [elements]
    
    result = []
    for i, current in enumerate(elements):
        remaining_elements = elements[:i] + elements[i + 1:]

        for p in permutations(remaining_elements):
            result.append([current] + p)

    return result
perm_list = []
for x in permutations([1, 2, 3, 4, 5, 6, 7]):
    curr = ""
    for y in x:
        curr += str(y)
    perm_list.append(curr)

num_list = [str(x) for x in perm_list]

for num in num_list:
    if is_prime(int(num)):
        print(int(num))