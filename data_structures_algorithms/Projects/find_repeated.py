def find_all(arr):
    result = []
    counter = {}
    for num in arr:
        if num in counter.keys():
            counter[num] += 1
            if num not in result:
                result.append(num)
        else:
            counter[num] = 1
    return result

print(find_all([0,0,1,1,2,3,4,5,5]))
print(find_all([]))
print(find_all([0,1,2,3,4,5,5]))
print(find_all([0,1, 1,2,3,4,5,1,1]))

def find_all_second(arr):
    result = []
    counter = {}
    for num in arr:
        if num in counter.keys():
            counter[num] += 1
            if num not in result:
                result.append(num)
        else:
            counter[num] = 1
    return result