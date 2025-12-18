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

n = int(input("Введіть кількість елементів масиву: "))
arr = []
for i in range(n):
    arr.append(float(input(f"Введіть елемент {i+1}: ")))

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

print("Максимальний елемент:", max_element(arr))
print("Сума до останнього додатного:", sum_before_last_positive(arr))
print("Стиснутий масив:", compress_array(arr, a, b))

