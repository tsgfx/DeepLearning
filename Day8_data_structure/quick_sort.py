# 作者: 郭瑞超
# 2025年01月04日14时33分24秒
# grcsxb269@163.com
def partition(arr, low, high):
    pivotkey = arr[low]
    while low < high:
        while low < high and arr[high] >= pivotkey:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivotkey:
            low += 1
        arr[high] = arr[low]
    arr[low] = pivotkey
    return low

def quick_sort(arr, low, high):
    if low >= high: return
    pivotpos = partition(arr, low, high)
    quick_sort(arr, low, pivotpos-1)
    quick_sort(arr, pivotpos+1, high)

if __name__ == '__main__':
    arr = [5, 2, 8, 3, 9, 1, 7, 4, 6]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)


