# Initialize an empty list to store weights in pounds
weights_lbs = []

# Take weights in pounds from the user until a non-numeric input is given
while True:
    try:
        weight_lbs = float(input("Enter weight in pounds (or any non-numeric input to stop): "))
        weights_lbs.append(weight_lbs)
    except ValueError:
        break

# Determine N by taking the length of the list
num_students = len(weights_lbs)

# Convert weights to kilograms and store in a separate list
weights_kgs = [round(weight_lbs * 0.45359237, 2) for weight_lbs in weights_lbs]

# Display the results
print(f"Weights in pounds: {weights_lbs}")
print(f"Weights in kilograms: {weights_kgs}")
