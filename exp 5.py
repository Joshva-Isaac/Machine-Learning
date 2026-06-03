import math

data = [
    [150, 50, "Short"],
    [155, 52, "Short"],
    [160, 55, "Short"],
    [170, 65, "Tall"],
    [175, 70, "Tall"],
    [180, 75, "Tall"]
]

new_sample = [165, 60]
k = 3

distances = []

for row in data:
    height = row[0]
    weight = row[1]
    label = row[2]

    distance = math.sqrt((new_sample[0] - height) ** 2 + 
                         (new_sample[1] - weight) ** 2)

    distances.append([distance, label])

distances.sort()

nearest = distances[:k]

short_count = 0
tall_count = 0

for item in nearest:
    if item[1] == "Short":
        short_count += 1
    else:
        tall_count += 1

if short_count > tall_count:
    result = "Short"
else:
    result = "Tall"

print("K-Nearest Neighbours Algorithm")
print("--------------------------------")
print("Training Dataset:")
print("Height  Weight  Class")

for row in data:
    print(row[0], "   ", row[1], "   ", row[2])

print("\nNew Sample:")
print("Height =", new_sample[0])
print("Weight =", new_sample[1])

print("\nNearest Neighbours:")
print("Distance   Class")

for item in nearest:
    print(round(item[0], 2), "     ", item[1])

print("\nPredicted Class:", result)
