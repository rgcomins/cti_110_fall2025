import turtle
import math

def project_point(x, y, z, angle_x=30, angle_y=30):
    rad_x = math.radians(angle_x)
    rad_y = math.radians(angle_y)

    y2 = y * math.cos(rad_x) - z * math.sin(rad_x)
    z2 = y * math.sin(rad_x) + z * math.cos(rad_x)

    x2 = x * math.cos(rad_y) + z2 * sin(rad_y)
    z3 = -x * math.sin(rad_y) + z2 * math.cos(rad_y)

    return x2, y2

def draw_wireframe(points, edges):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    projected = [project_point(x, y, z) for (x, y, z) in points]

    for start, end in edges:
        t.penup()
        t.goto(projected[start])
        t.pendown()
        t.goto(projected[end])

# Cube vertices
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

cube_edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

# Triangle vertices (pyramid tip above cube)
triangle_tip = (50, 50, 150)  # Centered above top face
triangle_points = cube_points + [triangle_tip]

# Triangle edges connecting tip to top face corners
triangle_edges = cube_edges + [
    (8, 4), (8, 5), (8, 6), (8, 7)
]

draw_wireframe(triangle_points, triangle_edges)
turtle.done()
