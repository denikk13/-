arr = [3.5, -2.1, 0, 4.2, -5.5, 6.0]
a = 2
b = 5

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

print("Масив:", arr)
print("Максимальний елемент:", max_el)
print("Сума до останнього додатного:", sum_before_last)
print("Стиснутий масив:", new_arr)
