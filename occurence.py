# arr = [5,2,5,7,5,9]
# target = 5
# indices = []
# for i in range(len(arr)):
#     if arr[i] == target:
#         indices.append(i)
# print(indices)

#dictionary
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 19},
    {"name": "David", "age": 21},
    {"name": "Eve", "age": 20}
]

indices = []
for i in range(len(students)):
    if students[i]["age"] == 20:
        indices.append(i)
print(indices)