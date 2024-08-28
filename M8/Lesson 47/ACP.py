# // polygon area calculator

import math

def polygon_area_calculator():
    print("Welcome to the Polygon Area Calculator!")
    num_sides = int(input("Enter the number of sides of the polygon: "))

    if num_sides < 3:
        print("A polygon must have at least 3 sides.")
        return

    side_length = float(input("Enter the length of each side: "))

    # Formula to calculate the area of a regular polygon
    area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

    print(f"The area of the polygon with {num_sides} sides, each of length {side_length}, is: {area:.2f}")

if __name__ == "__main__":
    polygon_area_calculator()
