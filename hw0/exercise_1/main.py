from SortStrategy import BubbleSort, InsertionSort, SelectionSort, MergeSort, HeapSort
from Sorter import Sorter
import random
import time
import pandas as pd

def main():
    # Nhập n số lượng phần tử

    name_strategy = ['BubbleSort', 'InsertionSort', 'SelectionSort', 'MergeSort', 'HeapSort']
    num_items = [10, 100, 1000, 10000, 100000]
    
    
    comparisons_matrix = []
    swaps_matrix = []
    time_matrix = []
    for n in num_items:
        comparisons_arr, swaps_arr, time_arr = sort_test(n)
        comparisons_matrix.append(comparisons_arr)
        swaps_matrix.append(swaps_arr)
        time_matrix.append(time_arr)

    print('Ma trận So sánh')
    print(comparisons_matrix)
    print('Ma trận hoán vị')
    print(swaps_matrix)
    print('Ma trận thời gian')
    print(time_matrix)

    df_comparisons = pd.DataFrame(comparisons_matrix, columns = name_strategy, index = num_items)
    df_swaps = pd.DataFrame(swaps_matrix, columns = name_strategy, index = num_items)
    df_time = pd.DataFrame(time_matrix, columns = name_strategy, index = num_items)


    df_comparisons.to_csv('data/comparisons.csv')
    df_swaps.to_csv('data/swaps.csv')
    df_time.to_csv('data/time.csv')


def sort_test(n):
    comparisons_arr = [0] * 5
    swaps_arr = [0] * 5
    time_arr = [0.0] * 5

    arr = [0] * n
    # Random từ phần tử của mảng
    for i in range(n):
        arr[i] = random.randint(1, 105)
    
    print(f'Mảng khởi tạo với {n} phần tử')

    print('Thuật toán BubbleSort')
    sorter = Sorter(BubbleSort())
    sorter.fit(arr)
    time_s = time.time()
    sorted_arr = sorter.sort()
    time_e = time.time()
    comparisons, swaps = sorter.num_comparisons_and_swaps()
    delta = round((time_e - time_s) * 1000, 5)

    comparisons_arr[0] = comparisons
    swaps_arr[0] = swaps
    time_arr[0] = delta

    print("Mảng đã sắp xếp:", sorted_arr)
    print("Số phép so sánh:", comparisons)
    print("Số phép hoán vị:", swaps)
    print("Thời gian chạy:", delta)

    print('Thuật toán InsertionSort')
    sorter = Sorter(InsertionSort())
    sorter.fit(arr)
    time_s = time.time()
    sorted_arr = sorter.sort()
    time_e = time.time()
    comparisons, swaps = sorter.num_comparisons_and_swaps()
    delta = round((time_e - time_s) * 1000, 5)

    comparisons_arr[1] = comparisons
    swaps_arr[1] = swaps
    time_arr[1] = delta

    print("Mảng đã sắp xếp:", sorted_arr)
    print("Số phép so sánh:", comparisons)
    print("Số phép hoán vị:", swaps)
    print("Thời gian chạy:", delta)

    print('Thuật toán SelectionSort')
    sorter = Sorter(SelectionSort())
    sorter.fit(arr)
    time_s = time.time()
    sorted_arr = sorter.sort()
    time_e = time.time()
    comparisons, swaps = sorter.num_comparisons_and_swaps()
    delta = round((time_e - time_s) * 1000, 5)

    comparisons_arr[2] = comparisons
    swaps_arr[2] = swaps
    time_arr[2] = delta

    print("Mảng đã sắp xếp:", sorted_arr)
    print("Số phép so sánh:", comparisons)
    print("Số phép hoán vị:", swaps)
    print("Thời gian chạy:", delta)

    print('Thuật toán MergeSort')
    sorter = Sorter(MergeSort())
    sorter.fit(arr)
    time_s = time.time()
    sorted_arr = sorter.sort()
    time_e = time.time()
    comparisons, swaps = sorter.num_comparisons_and_swaps()
    delta = round((time_e - time_s) * 1000, 5)

    comparisons_arr[3] = comparisons
    swaps_arr[3] = swaps
    time_arr[3] = delta

    print("Mảng đã sắp xếp:", sorted_arr)
    print("Số phép so sánh:", comparisons)
    print("Số phép hoán vị:", swaps)
    print("Thời gian chạy:", delta)

    print('Thuật toán HeapSort')
    sorter = Sorter(HeapSort())
    sorter.fit(arr)
    time_s = time.time()
    sorted_arr = sorter.sort()
    time_e = time.time()
    comparisons, swaps = sorter.num_comparisons_and_swaps()
    delta = round((time_e - time_s) * 1000, 5)

    comparisons_arr[4] = comparisons
    swaps_arr[4] = swaps
    time_arr[4] = delta

    print("Mảng đã sắp xếp:", sorted_arr)
    print("Số phép so sánh:", comparisons)
    print("Số phép hoán vị:", swaps)
    print("Thời gian chạy:", delta)

    return (comparisons_arr, swaps_arr, time_arr)
if __name__ == "__main__":
    main()