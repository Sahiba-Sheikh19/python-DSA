# using a loop
arr = [10, 5, 25, 8, 15]

max_num = arr[0]

for i in arr:
    if i > max_num:
        max_num = i

print(max_num)

# using built-in function
arr = [10, 5, 25, 8, 15]        
max_num = max(arr)
print(max_num)