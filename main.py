from random import randint

array_with_numbers = []
array_with_unique_numbers = []

for i in range(100):
    array_with_numbers.append(randint(1, 5))
print(*array_with_numbers)


def Unique_Values(array, unique_array):
    unique_array.append(array[0])
    for i in range(100):
        for p in range(0, len(unique_array)):
            if array[i] != unique_array[p]:
                unique_array.append(array[i])
            break
    return unique_array


Unique_Values(array_with_numbers, array_with_unique_numbers)
print(*array_with_unique_numbers)
