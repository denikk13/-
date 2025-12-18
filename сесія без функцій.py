n = int(input("Введіть кількість елементів масиву: "))
arr = []
for i in range(n):
    arr.append(float(input(f"Введіть елемент {i+1}: ")))

a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

max_el = arr[0]
for x in arr:
    if x > max_el:
        max_el = x

last_pos_index = -1
for i in range(len(arr)):
    if arr[i] > 0:
        last_pos_index = i

sum_before_last = 0
if last_pos_index != -1:
    for i in range(last_pos_index):
        sum_before_last += arr[i]

new_arr = []
for x in arr:
    if not (a <= abs(x) <= b):
        new_arr.append(x)
while len(new_arr) < len(arr):
    new_arr.append(0)

print("Максимальний елемент:", max_el)
print("Сума до останнього додатного:", sum_before_last)
print("Стиснутий масив:", new_arr)
