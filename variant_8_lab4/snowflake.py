import turtle

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    for _ in range(iters):
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string
    return start_string

def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

axiom = "F++F++F"
rules = {"F": "F-F++F-F"}
iterations = 4
angle = 60
length = 3
size = 2
y_offset = -100
x_offset = -25
offset_angle = 30
width = 450
height = 450


inst = create_l_system(iterations, axiom, rules)

t = turtle.Turtle()
wn = turtle.Screen()
wn.setup(width, height)

t.up()
t.setpos(x_offset, y_offset)
t.left(offset_angle)
t.down()
t.speed(0)
t.pensize(size)

draw_l_system(t, inst, angle, length)

t.hideturtle()
wn.exitonclick()
