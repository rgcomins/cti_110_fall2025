import turtle

def draw_cube(size):
    t = turtle.Turtle()
    t.speed(3)

    # Draw front square
    for _ in range(4):
        t.forward(size)
        t.left(90)

    # Draw top face
    t.left(45)
    t.forward(size / 1.414)  # size / sqrt(2)
    t.right(45)
    for _ in range(4):
        t.forward(size)
        t.right(90)

    # Draw side face
    t.left(135)
    t.forward(size / 1.414)
    t.left(45)
    for _ in range(4):
        t.forward(size)
        t.left(90)

    turtle.done()

draw_cube(100)