from SortAbstract import SortAbstract

class BubbleSort(SortAbstract):
    def __init__(self):
        super().__init__()

    def sort(self):
        arr_copy = super().get_array().copy()
        n = len(arr_copy)
        for i in range(n):
            for j in range(0, n-i-1):
                self.comparisons += 1
                if arr_copy[j] > arr_copy[j+1]:
                    self.swaps += 1
                    arr_copy[j], arr_copy[j+1] = arr_copy[j+1], arr_copy[j]
        return arr_copy
    
class InsertionSort(SortAbstract):
    def __init__(self):
        super().__init__()

    def sort(self):
        arr_copy = super().get_array().copy()
        n = len(arr_copy)
        for i in range(1, n):
            key = arr_copy[i]
            j = i-1
            while j >=0 and key < arr_copy[j]:
                self.comparisons += 1
                arr_copy[j + 1] = arr_copy[j]
                self.swaps += 1
                j -= 1
            arr_copy[j + 1] = key
            if j >= 0:
                self.comparisons += 1
        return arr_copy
    
class SelectionSort(SortAbstract):
    def __init__(self):
        super().__init__()

    def sort(self):
        arr_copy = super().get_array().copy()
        n = len(arr_copy)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                self.comparisons += 1
                if arr_copy[j] < arr_copy[min_idx]:
                    min_idx = j
            if min_idx != i:
                self.swaps += 1
                arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
        return arr_copy
    
class MergeSort(SortAbstract):
    def __init__(self):
        super().__init__()

    def sort(self):
        arr_copy = super().get_array().copy()
        self._merge_sort(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy

    def _merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            self._merge_sort(arr, left, mid)
            self._merge_sort(arr, mid + 1, right)
            self._merge(arr, left, mid, right)

    def _merge(self, arr, left, mid, right):
        L = arr[left:mid + 1]
        R = arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            self.comparisons += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            self.swaps += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            self.swaps += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            self.swaps += 1


class HeapSort(SortAbstract):
    def __init__(self):
        super().__init__()

    def sort(self):
        arr_copy = super().get_array().copy()
        n = len(arr_copy)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr_copy, n, i)

        for i in range(n-1, 0, -1):
            arr_copy[i], arr_copy[0] = arr_copy[0], arr_copy[i]
            self.swaps += 1
            self._heapify(arr_copy, i, 0)

        return arr_copy

    def _heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1
            if arr[left] > arr[largest]:
                largest = left

        if right < n:
            self.comparisons += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.swaps += 1
            self._heapify(arr, n, largest)