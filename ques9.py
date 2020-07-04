def binary_search(items, value):
    flag = 0
    position = None 
    for i in range(len(items)):
        if value == items[i]:
            flag = 1
            position = i
        
    if flag == 1:
        return position
    else:
        return -1
result = binary_search(sorted([4,6,3,1,2,5,7,8,3,1]), 6)
print(result)