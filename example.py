def count_occurrences(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count += 1
    return count
print(count_occurrences([5, 2, 5, 7, 5, 9], 5))  # Output: 3