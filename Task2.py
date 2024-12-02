import numpy as np

array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

mean_value = array.mean()

min_diff = np.abs(array - mean_value).min()
closest_coords = np.argwhere(np.abs(array - mean_value) == min_diff)

print("Координаты элемента, наиболее близкого к среднему значению:", closest_coords[0])
