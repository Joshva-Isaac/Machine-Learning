data = [
    ["Sunny", "Hot", "High", "Weak", "No"],
    ["Sunny", "Hot", "High", "Strong", "No"],
    ["Overcast", "Hot", "High", "Weak", "Yes"],
    ["Rain", "Mild", "High", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Weak", "Yes"],
    ["Rain", "Cool", "Normal", "Strong", "No"]
]
print("Decision Tree")
print("Outlook?")
print("|")
print("|-- Overcast --> Play Tennis = Yes")
print("|")
print("|-- Sunny --> Humidity?")
print("|      |-- High --> No")
print("|      |-- Normal --> Yes")
print("|")
print("|-- Rain --> Wind?")
print("       |-- Weak --> Yes")
print("       |-- Strong --> No")
outlook = "Sunny"
humidity = "Normal"
print("\nNew Sample:")
print("Outlook =", outlook)
print("Humidity =", humidity)
if outlook == "Overcast":
    result = "Yes"
elif outlook == "Sunny":
    if humidity == "High":
        result = "No"
    else:
        result = "Yes"
else:
    result = "Yes"
print("\nPrediction:", result)
