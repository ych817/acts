import numpy as np

# 创建前 10 个正整数的 NumPy array
arr = np.arange(1, 11)

# 打印数组
print("Array:", arr)

# 打印形状和数据类型
print("Shape:", arr.shape)
print("Data type:", arr.dtype)

# 每个元素乘以 2
arr_times_two = arr * 2
print("Multiplied by 2:", arr_times_two)
