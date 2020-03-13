def find_uniq(arr):
    if arr.count(arr[0]) == 1: return arr[0]
    for num in arr:
        if num != arr[0]: return num
