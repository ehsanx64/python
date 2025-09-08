import turtle
t = turtle.Turtle()

for i in range(4 * 50):
    # Forward 50 steps
    t.fd(50)

    # Turn left
    t.lt(42 + (i / 2))
     
# Keep repeating
turtle.mainloop()
