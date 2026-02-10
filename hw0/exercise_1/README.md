# Bài Tập 1: So Sánh Hiệu Năng Các Thuật Toán Sắp Xếp

## Nội Dung

So sánh hiệu năng của 5 thuật toán sắp xếp khác nhau:

1. **BubbleSort** - Thuật toán sắp xếp nổi bọt
2. **InsertionSort** - Thuật toán sắp xếp chèn
3. **SelectionSort** - Thuật toán sắp xếp chọn
4. **MergeSort** - Thuật toán sắp xếp trộn
5. **HeapSort** - Thuật toán sắp xếp vun đống

### Các Yếu Tố Đo Lường

Mỗi thuật toán được đánh giá dựa trên:
- **Số lần so sánh (Comparisons)**: Tổng số phép so sánh giữa các phần tử
- **Số lần hoán vị (Swaps)**: Tổng số lần hoán vị các phần tử
- **Thời gian chạy (Time)**: Thời gian thực thi tính bằng mili giây

### Nội dung kiểm thử

Các thuật toán được kiểm thử với các mảng có kích thước khác nhau:
- 10 phần tử
- 100 phần tử
- 1.000 phần tử
- 10.000 phần tử
- 100.000 phần tử

## Cấu Trúc Dự Án

Cấu trúc folder thực hiện dựa trên Design Pattern Strategy được học trong môn OOP
```
exercise_1/
├── main.py                 # File chính - chạy các test
├── SortStrategy.py         # Định nghĩa các lớp sắp xếp
├── SortAbstract.py         # Lớp trừu tượng cho các thuật toán
├── Sorter.py               # Lớp wrapper để gọi các thuật toán
├── visualization.ipynb     # Jupyter notebook để trực quan hóa kết quả
└── data/                   # Thư mục lưu kết quả
    ├── comparisons.csv     
    ├── swaps.csv           
    └── time.csv            
```

## Yêu Cầu

- Python
- Thư viện: `pandas`


## Cách Chạy

### 1. Chạy chương trình chính

Để chạy các test so sánh các thuật toán sắp xếp:

```bash
python main.py
```

**Kết quả**:
- In ra console các thông tin: số phép so sánh, số phép hoán vị, thời gian chạy
- Tạo ba file CSV trong thư mục `data/`:
  - `comparisons.csv` - Bảng số lần so sánh
  - `swaps.csv` - Bảng số lần hoán vị
  - `time.csv` - Bảng thời gian chạy

### 2. Xem Trực Quan Hóa Kết Quả

Để xem biểu đồ so sánh hiệu năng, mở file `visualization.ipynb`

## Ghi Chú

- Các mảng được khởi tạo với các số ngẫu nhiên từ 1 đến 105
- Thời gian chạy được tính bằng mili giây (ms)
- Kết quả được lưu dưới dạng CSV để dễ dàng phân tích và vẽ biểu đồ
