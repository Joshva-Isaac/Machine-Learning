# FIND-S Algorithm Implementation

# Training data
# Format: [Sky, AirTemp, Humidity, Wind, Water, Forecast, EnjoySport]

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Initialize the most specific hypothesis
hypothesis = ['0'] * (len(data[0]) - 1)

print("Initial Hypothesis:")
print(hypothesis)

# Applying FIND-S Algorithm
for sample in data:
    
    # Consider only positive examples
    if sample[-1] == 'Yes':
        
        for i in range(len(hypothesis)):
            
            # If hypothesis is empty
            if hypothesis[i] == '0':
                hypothesis[i] = sample[i]
            
            # If values do not match
            elif hypothesis[i] != sample[i]:
                hypothesis[i] = '?'

# Final Hypothesis
print("\nFinal Hypothesis:")
print(hypothesis)
