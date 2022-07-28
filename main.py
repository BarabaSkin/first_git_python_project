# creating of 2 empty arrays
class MyClass(object):
    def __init__(self, number):
        self.number = number


array_with_numbers = []
for i in range(100):
    u = int(input())
    array_with_numbers.append(MyClass(u).number)
array_with_unique_numbers = []
print(*array_with_numbers)


def Unique_Values(array, unique_array):
    for number in array:
        if number in unique_array:
            continue
        else:
            unique_array.append(number)
    return unique_array


Unique_Values(array_with_numbers, array_with_unique_numbers)
print(*array_with_unique_numbers)
