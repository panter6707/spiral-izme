import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("Turtle Python")


turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
hız = input("0 ile 10 arası rakam girin: ")
hız1 = int(hız)
turtle.speed(hız1) # 0 en hızlı, 10 hızlı, 6 normal, 3 yavaş, 1 en yavaş

turtle_colors =["red", "purple", "blue","green","orange","yellow"]
sayı = input("sayı giriniz: ")
reel = int(sayı)
for i in range(reel):
    turtle_instance.color(turtle_colors[i % 6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)







turtle.done()