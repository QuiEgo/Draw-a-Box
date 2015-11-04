import turtle

wn = turtle.Screen()
wn.bgcolor("violet")
tim = turtle.Turtle()
tim.color("red")
tim.shape("circle")
terry = turtle.Turtle()
terry.color("orange")
terry.shape("circle")
tanya = turtle.Turtle()
tanya.color("yellow")
tanya.shape("circle")
taylor = turtle.Turtle()
taylor.color("green")
taylor.shape("circle")
tony = turtle.Turtle()
tony.color("blue")
tony.shape("circle")

for a in range(4):
    tim.stamp()
    tim.forward(12.5)
    tim.left(90)

    terry.stamp()
    terry.forward(25)
    terry.left(90)
    
    tanya.stamp()
    tanya.forward(50)
    tanya.left(90)
    
    taylor.stamp()
    taylor.forward(100)
    taylor.left(90)
    
    tony.stamp()
    tony.forward(200)
    tony.left(90)

wn.mainloop()
