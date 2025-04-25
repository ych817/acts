import numpy as np

temp_celsius_lst = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
temp_celsius_avg = np.mean(temp_celsius_lst)
temp_celsius_max = np.max(temp_celsius_lst)
temp_celsius_min = np.min(temp_celsius_lst)
temp_celsius_to_fahrenheit = lambda temp_celsius: (9 / 5) * temp_celsius + 32
temp_fahrenheit  = map(temp_celsius_to_fahrenheit, temp_celsius_lst)
temp_celsius_above_20 = lambda temp_celsius: temp_celsius - 20 > 0
temp_celsius_above_20_idx = np.where(temp_celsius_above_20(temp_celsius_lst))[0]

# 1. Print the average temperature for this week
print(f"1: Average temperature for this week: {temp_celsius_avg:.2f} °C;")
# 2. Print the highest and lowest temerature for this week
print(f"2: Highest temperature for this week: {temp_celsius_max:.2f} °C,")
print(f"   Lowest  temperature for this week: {temp_celsius_max:.2f} °C;")
# 3. Convert all temperature to Fahrenheit and print the result.
print(f"3. All temperatures in Fahrenheit:")
for temp in temp_fahrenheit:
    print(f"   {temp:.2f} °F")
# 4. Print the days where temperature was above 20 degrees Celsius
print(f"4. Days where temperature was above 20 degrees Celsius:\n")
for idx in temp_celsius_above_20_idx:
    print(f"   day: {idx}: {temp_celsius_lst[idx]:.2f} °C")