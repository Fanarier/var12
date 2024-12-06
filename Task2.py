matrix = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 16)
)

rows, cols = len(matrix), len(matrix[0])
min_sum = float('inf')
min_columns = None

for c in range(cols - 1):
    col_sum = sum(matrix[r][c] + matrix[r][c + 1] for r in range(rows))
    if col_sum < min_sum:
        min_sum = col_sum
        min_columns = (c, c + 1)

print(f"Номера столбцов с минимальной суммой: {min_columns}, сумма: {min_sum}")
