def calculate_and_print(points):
    for point in points:
        distance = calculate_distance(point['x'], point['y'])
        print(f"Distance of Point({point['x']}, {point['y']}) from origin is {distance:.2f}")

def calculate_distance(x, y):
    return (((x - 0)**2 + (y - 0)**2)**0.5)

points = [{'x': 3, 'y': 4}, {'x': 5, 'y': 12}, {'x': 8, 'y': 15}]
calculate_and_print(points)
