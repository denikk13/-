def max_element(arr):
    return max(arr)

def sum_before_last_positive(arr):
    index = -1
    for i in range(len(arr)):
        if arr[i] > 0:
            index = i
    if index == -1:
        return 0
    return sum(arr[:index])

def compress_array(arr, a, b):
    new_arr = []
    for x in arr:
        if not (a <= abs(x) <= b):
            new_arr.append(x)
    while len(new_arr) < len(arr):
        new_arr.append(0)
    return new_arr

arr = [3.5, -2.1, 0, 4.2, -5.5, 6.0]
a = 2
b = 5

print("Масив:", arr)
print("Максимальний елемент:", max_element(arr))
print("Сума до останнього додатного:", sum_before_last_positive(arr))
print("Стиснутий масив:", compress_array(arr, a, b))
