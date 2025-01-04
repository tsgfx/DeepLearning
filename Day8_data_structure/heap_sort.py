class HeapSort:
    def __init__(self, arr):
        self.arr = arr
        self.len = len(arr)

    # 调整某一棵子树为大根堆
    def adjust_max_heap(self, adjust_pos, arr_length):
        arr = self.arr
        dad = adjust_pos
        son = 2 * dad + 1  # 左孩子和父亲的下标位置关系

        while son < arr_length:  # 下标要小于列表的长度
            if son + 1 < arr_length and arr[son] < arr[son + 1]:
                son += 1  # 选择较大的子节点

            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]  # 交换父节点和较大的子节点
                dad = son  # 更新父节点位置
                son = 2 * dad + 1  # 继续检查下一个子节点
            else:
                break

    def heap_sort(self):
        arr = self.arr
        # 调整为大根堆
        for i in range(self.len // 2 - 1, -1, -1):  # 从最后一个非叶子节点开始向上调整
            self.adjust_max_heap(i, self.len)

        # 对堆进行排序
        for i in range(self.len - 1, 0, -1):  # 逐步将最大值移到堆的末尾
            arr[0], arr[i] = arr[i], arr[0]  # 交换顶部元素和末尾元素
            self.adjust_max_heap(0, i)  # 重新调整堆


if __name__ == '__main__':
    arr = [5, 3, 8, 6, 2, 7, 1, 4]
    heap_sorter = HeapSort(arr)
    heap_sorter.heap_sort()
    print(arr)  # 输出排序后的数组l
