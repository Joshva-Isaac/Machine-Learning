import math
def sigmoid(x):
    return 1 / (1 + math.exp(-x))
def sigmoid_derivative(x):
    return x * (1 - x)
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
outputs = [
    [0],
    [1],
    [1],
    [0]
]
w1 = 0.5
w2 = -0.5
w3 = 0.3
w4 = 0.8
w5 = -0.7
w6 = 0.2
learning_rate = 0.5
for epoch in range(10000):
    for i in range(len(inputs)):
        x1 = inputs[i][0]
        x2 = inputs[i][1]
        target = outputs[i][0]

        h1_input = x1 * w1 + x2 * w2
        h2_input = x1 * w3 + x2 * w4

        h1_output = sigmoid(h1_input)
        h2_output = sigmoid(h2_input)

        final_input = h1_output * w5 + h2_output * w6
        final_output = sigmoid(final_input)

        error = target - final_output

        d_output = error * sigmoid_derivative(final_output)

        error_h1 = d_output * w5
        error_h2 = d_output * w6

        d_h1 = error_h1 * sigmoid_derivative(h1_output)
        d_h2 = error_h2 * sigmoid_derivative(h2_output)

        w5 = w5 + learning_rate * d_output * h1_output
        w6 = w6 + learning_rate * d_output * h2_output

        w1 = w1 + learning_rate * d_h1 * x1
        w2 = w2 + learning_rate * d_h1 * x2
        w3 = w3 + learning_rate * d_h2 * x1
        w4 = w4 + learning_rate * d_h2 * x2

print("Artificial Neural Network using Backpropagation")
print("----------------------------------------------")
print("Input1  Input2  Predicted Output")
print("----------------------------------------------")

for i in range(len(inputs)):
    x1 = inputs[i][0]
    x2 = inputs[i][1]

    h1_input = x1 * w1 + x2 * w2
    h2_input = x1 * w3 + x2 * w4

    h1_output = sigmoid(h1_input)
    h2_output = sigmoid(h2_input)

    final_input = h1_output * w5 + h2_output * w6
    final_output = sigmoid(final_input)

    if final_output >= 0.5:
        result = 1
    else:
        result = 0

    print(x1, "      ", x2, "      ", result)

print("----------------------------------------------")
