import csv
from collections import Counter

with open('height-weight.csv', newline='') as file:
    reader = csv.reader(file)
    file_data = list(reader)

file_data.pop(0)

# mean
data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    data.append(float(n_num))

data_length = len(data)
total = 0
for x in data:
    total += x

mean = total / data_length

# median
data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    data.append(n_num)

data_length = len(data)
data.sort()


if data_length % 2 == 0:
    median1 = float(data[data_length//2])
    median2 = float(data[data_length//2 - 1])
    median = (median1 + median2)/2
else:
    median = data[data_length//2]

# mode
data = []

for i in range(len(file_data)):
    n_num = file_data[i][1]
    data.append(n_num)

counter = Counter(data)
mode_data_for_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

for height, occurrence in counter.items():
    if 50 < float(height) < 60:
        mode_data_for_range["50-60"] += occurrence
    elif 60 < float(height) < 70:
        mode_data_for_range["60-70"] += occurrence
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurrence

mode_range, mode_occurrence = 0, 0
for range, occurrence in mode_data_for_range.items():
    if occurrence > mode_occurrence:
        mode_range, mode_occurrence = [
            int(range.split("-")[0]), int(range.split("-")[1])], occurrence
mode = float((mode_range[0] + mode_range[1]) / 2)


print("Mean (Average) is -> " + str(mean))
print("Median is -> " + str(median))
print(f"Mode is -> {mode:2f}")
