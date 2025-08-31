
def selection_sort():
    arr = list(map(int, input().split()))
    newArr = []
    for i in range(len(arr)):
        tempArr = arr[0:len(arr)]
        tempMin = min(tempArr)
        newArr.append(tempMin)
        arr.remove(tempMin)
    print(newArr)

selection_sort()
