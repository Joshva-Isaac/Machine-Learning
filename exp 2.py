import csv

data = []

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

concepts = [row[:-1] for row in data]
target = [row[-1] for row in data]

S = concepts[0][:]

for i in range(len(concepts)):
    if target[i] == "Yes":
        for j in range(len(S)):
            if S[j] != concepts[i][j]:
                S[j] = "?"

print("Final Specific Hypothesis:")
print(S)
