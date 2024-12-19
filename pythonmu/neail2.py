import math
import turtle

#nesil bebisime o cok begendigi kalpli kod ama yavaş calısandan

# Kalbin X ve Y koordinatlarını hesaplayan fonksiyonlar
def xt(t, scale):
    return scale * (16 * math.sin(t)**3)

def yt(t, scale):
    return scale * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))

# Turtle ayarları
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor('black')
t.pensize(2)
t.pencolor('purple')
t.hideturtle()

# Kalp çizimi
for scale in range(1, 16):  # 1'den 15'e kadar büyüyen kalpler
    t.penup()
    t.goto(xt(0, scale), yt(0, scale))  # İlk noktaya git
    t.pendown()
    for i in range(16, 324):  # 0'dan 2*pi'ye kadar (360 derece = 2*pi)
        t.goto(xt(i / 100, scale), yt(i / 100, scale))

turtle.done()

