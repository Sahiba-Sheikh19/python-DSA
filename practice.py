name = ["Alice", "Bob", "Charlie", "David", "Eve"]
target = "charlie"

def search(name,target):
    for i in range(len(name)):
        if name[i].lower() == target.lower():
            return i
    return -1

result = search(name, target)
print(result)