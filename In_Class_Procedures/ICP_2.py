def main():
    # Create an empty dictionary called dog
    dog = {}

    # Add name, color, breed, legs, age to the dog dictionary
    dog["name"] = "Buddy"
    dog["color"] = "Brown"
    dog["breed"] = "Labrador"
    dog["legs"] = 4
    dog["age"] = 3
    print("Dog Dictionary:", dog)

    # Create a student dictionary
    student = {
        "first_name": "John",
        "last_name": "Doe",
        "gender": "Male",
        "age": 20,
        "marital_status": "Single",
        "skills": ["Programming", "Data Analysis"],
        "country": "USA",
        "city": "New York",
        "address": "123 Main St"
    }
    print("Student Dictionary:", student)

    # Get the length of the student dictionary
    student_length = len(student)

    # Get the value of skills and check the data type, it should be a list
    skills_value = student["skills"]
    skills_data_type = type(skills_value)

    # Modify the skills values by adding one or two skills
    student["skills"].extend(["Communication", "Problem Solving"])

    # Get the dictionary keys as a list
    keys_list = list(student.keys())

    # Get the dictionary values as a list
    values_list = list(student.values())

    # Display the results
    print("Length of Student Dictionary:", student_length)
    print("Skills Value:", skills_value)
    print("Skills Data Type:", skills_data_type)
    print("Modified Student Dictionary with Additional Skills:", student)
    print("Dictionary Keys as List:", keys_list)
    print("Dictionary Values as List:", values_list)


main()