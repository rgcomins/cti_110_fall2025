import turtle
import math

def project_point(x, y, z, angle_x=30, angle_y=30):
    # Convert angles to radians
    rad_x = math.radians(angle_x)
    rad_y = math.radians(angle_y)

    # Rotate around X axis
    y2 = y * math.cos(rad_x) - z * math.sin(rad_x)
    z2 = y * math.sin(rad_x) + z * math.cos(rad_x)

    # Rotate around Y axis
    x2 = x * math.cos(rad_y) + z2 * math.sin(rad_y)
    z3 = -x * math.sin(rad_y) + z2 * math.cos(rad_y)

    # Ignore z3 for 2D projection
    return x2, y2

def draw_wireframe(points, edges):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Project points
    projected = [project_point(x, y, z) for (x, y, z) in points]

    # Draw edges
    for start, end in edges:
        t.penup()
        t.goto(projected[start])
        t.pendown()
        t.goto(projected[end])

    turtle.done()

# Define cube vertices
cube_points = [
    (0, 0, 0),
    (100, 0, 0),
    (100, 100, 0),
    (0, 100, 0),
    (0, 0, 100),
    (100, 0, 100),
    (100, 100, 100),
    (0, 100, 100),
]

# Define edges by connecting vertices
cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Bottom square
    (4, 5), (5, 6), (6, 7), (7, 4),  # Top square
    (0, 4), (1, 5), (2, 6), (3, 7)   # Vertical edges
]

draw_wireframe(cube_points, cube_edges)
