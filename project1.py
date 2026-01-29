import numpy as np


def calculate(data):
    if len(data) != 9:
        raise ValueError("Input data must contain exactly 9 elements.")
    else:
        arr = np.array(data, dtype=int).reshape((3, 3))
        mean = [np.mean(arr, axis=0), np.mean(arr, axis=1), np.mean(arr)]
        variance = [np.var(arr, axis=0), np.var(arr, axis=1), np.var(arr)]
        std_dev = [np.std(arr, axis=0), np.std(arr, axis=1), np.std(arr)]
        max_val = [np.max(arr, axis=0), np.max(arr, axis=1), np.max(arr)]
        min_val = [np.min(arr, axis=0), np.min(arr, axis=1), np.min(arr)]
        sum_val = [np.sum(arr, axis=0), np.sum(arr, axis=1), np.sum(arr)]
        return {
            "mean": mean,
            "variance": variance,
            "standard deviation": std_dev,
            "max": max_val,
            "min": min_val,
            "sum": sum_val,
        }

print("Enter 9 numbers")
numbers = []
for i in range(9):
   numbers.append(int(input(f"Enter number {i + 1}: ")))

results = calculate(numbers)
print(results)