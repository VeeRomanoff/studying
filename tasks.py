def numbers_generating(a, b):
    odd_numbers = []
    for x in range(a, b):
        if x % 2 != 0:
            odd_numbers.append(x)
    return odd_numbers
print(numbers_generating(0, 15))        