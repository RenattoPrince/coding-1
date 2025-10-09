def binarySearch(arr, target, low, high):
    if low > high:
        return -1
    mid =(low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return mid
    elif target < arr[mid]:
        return binarySearch(arr, target, low, mid - 1)
    else:
        return binarySearch(arr, target, mid + 1, high)
    
def binary_search(arr, target):
    return binarySearch(arr, target, 0, len(arr) - 1)

if __name__ =="__main__":
    arr = [2 ,4, 7, 10,13, 18, 21, 25, 30]
    target = 13
    result = binary_search(arr, target)

    if result != -1:
        print(f"Target {target} found at index {result}")
    else:
        print(f"target {target} not found in the array")