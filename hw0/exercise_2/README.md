# Bài Tập 2: Nhân Ma Trận và Duyệt Hình Xoắn Ốc

## Nội Dung

Thực hiện hai nhiệm vụ sau:

### 1. Nhân Ma Trận
- Nhân hai ma trận vuông cùng kích thước
- Sử dụng thuật toán nhân ma trận cơ bản
- Đo lường thời gian thực thi cho các ma trận có kích thước khác nhau

### 2. Duyệt Ma Trận Theo Hình Xoắn Ốc
- Duyệt tất cả phần tử của ma trận theo hình xoắn ốc theo chiều kim đồng hồ

## Cấu Trúc Dự Án

```
exercise_2/
└── main.py                 # File chính - chứa các hàm và chạy test
```

## Yêu Cầu

- Python


## Cách Chạy

### Chạy chương trình

Để chạy chương trình chính:

```bash
python main.py
```

## Quá trình kiểm thử

Chương trình kiểm thử nhân ma trận với các kích thước:
- 10 × 10
- 20 × 20
- 30 × 30
- 40 × 40
- 50 × 50

Thời gian thực thi sẽ tăng lên đáng kể khi kích thước ma trận tăng do độ phức tạp O(n³).

## Ghi Chú

- Các phần tử ma trận được khởi tạo ngẫu nhiên từ 1 đến $n^2$
- Thời gian nhân ma trận được tính bằng mili giây (ms)
- Duyệt hình xoắn ốc theo chiều kim đồng hồ
