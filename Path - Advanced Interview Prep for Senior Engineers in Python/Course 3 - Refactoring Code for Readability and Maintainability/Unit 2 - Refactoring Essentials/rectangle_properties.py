# Combined function with unclear variable names and dual functionality
def calculate_perimeter(length, width):
    return 2 * (length + width)
def calculate_area(length, width):
    return length * width
def calculate_properties(length, width):
    perimeter = calculate_perimeter(length, width)
    area = calculate_area(length, width)
    return perimeter, area

# Function to print the geometry of a "rectangle" with generic terms.
def print_properties(length, width):
    perimeter, area = calculate_properties(length, width)
    print(f"Shape with dimension 1: {length} and dimension 2: {width} has:")
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")

# Constants for the dimensions of the shape.
RECT_LENGTH = 10
RECT_WIDTH = 5

print_properties(RECT_LENGTH, RECT_WIDTH)
