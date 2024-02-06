import math


def main():
    # Given radius
    radius = 30

    # Calculate the area of a circle
    area_of_circle = math.pi * (radius ** 2)

    # Calculate the circumference of circle
    circum_of_circle = 2 * math.pi * radius

    # Display the results
    print("Area of the circle:", area_of_circle)
    print("Circumference of the circle:", circum_of_circle)

    # Take radius as user input and calculate the area
    user_radius = float(input("Enter the radius of the circle: "))
    user_area_of_circle = math.pi * (user_radius ** 2)

    # Display the result based on user input
    print(f"Area of the circle with user-input radius ({user_radius}): {user_area_of_circle}")


main()
