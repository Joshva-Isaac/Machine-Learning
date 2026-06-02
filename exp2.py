# Candidate Elimination Algorithm

# Training Data
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Number of attributes
num_attributes = len(data[0]) - 1

# Initialize Specific Hypothesis
S = data[0][:-1]

# Initialize General Hypothesis
G = [['?' for i in range(num_attributes)] for i in range(num_attributes)]

print("Initial Specific Hypothesis:")
print(S)

print("\nInitial General Hypothesis:")
for g in G:
    print(g)

# Candidate Elimination Algorithm
for example in data:

    # Positive Example
    if example[-1] == 'Yes':

        for i in range(num_attributes):

            if S[i] != example[i]:
                S[i] = '?'
                G[i][i] = '?'

    # Negative Example
    else:

        for i in range(num_attributes):

            if S[i] != example[i]:
                G[i][i] = S[i]

            else:
                G[i][i] = '?'

# Final Output
print("\nFinal Specific Hypothesis:")
print(S)

print("\nFinal General Hypothesis:")
for g in G:
    print(g)
