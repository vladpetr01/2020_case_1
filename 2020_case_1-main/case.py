import turtle as tl
import math
# Petrov V.A. 70%
# Udachev N.V. 40%
# Kuleshov R.A. 30%

drawing_area = tl.Screen()
drawing_area.setup(width=1280, height=720)
tl.speed(1000)


def triangle(x, y, z, color):
    tl.up()
    tl.goto(x, y)
    tl.down()
    tl.color(color)
    tl.begin_fill()
    tl.left(45)
    tl.fd(z * math.sqrt(2) / 2)
    tl.left(135)
    tl.fd(z)
    tl.left(135)
    tl.fd(z * math.sqrt(2) / 2)
    tl.end_fill()


def square(x, y, z, color):
    tl.up()
    tl.goto(x, y)
    tl.down()
    tl.color(color)
    tl.begin_fill()
    tl.fd(z)
    tl.right(90)
    tl.fd(z)
    tl.right(90)
    tl.fd(z)
    tl.right(90)
    tl.fd(z)
    tl.right(90)
    tl.end_fill()


def parallelogram(x, y, z, color):
    tl.up()
    tl.goto(x, y)
    tl.down()
    tl.color(color)
    tl.begin_fill()
    tl.left(45)
    tl.fd(z * math.sqrt(2) / 2)
    tl.right(45)
    tl.fd(z)
    tl.right(135)
    tl.fd(z * math.sqrt(2) / 2)
    tl.right(45)
    tl.fd(z)
    tl.end_fill()


def fish():
    tl.left(45)
    square(-300, 250, 50, 'orange')
    tl.right(270)
    triangle(50 * math.sqrt(2) - 300, 350, 2*50*math.sqrt(2), 'red')
    tl.right(45)
    triangle(50 * math.sqrt(2) - 300, 150, 2*50*math.sqrt(2), 'yellow' )
    tl.left(90)
    triangle(1.75*50 * math.sqrt(2) - 300, 250, 100, 'blue' )
    tl.left(180)
    triangle(-350, 250, 50*math.sqrt(2), 'pink' )
    tl.right(135)
    triangle(-350, 200, 50*math.sqrt(2), 'purple')
    tl.left(135)
    parallelogram(-300, 250, 50*math.sqrt(2) , 'green')


def bunny():
    tl.left(45)
    triangle(-500, 100, 200, 'red')
    tl.right(135)
    triangle(-200 * math.sqrt(2)/2 - 500, 100, 200, 'yellow')
    tl.right(135)
    triangle(-50 * math.sqrt(2)/2 - 500, -200 * math.sqrt(2) / 2 + 100, 150, 'skyblue')
    tl.right(45)
    triangle(-50*math.sqrt(2)/2 - 500, -200 * math.sqrt(2) / 2 + 100, 100, 'purple')
    tl.right(180)
    triangle(-460, 100, 75, 'pink')
    tl.left(45)
    square(-500, 150 * math.sqrt(2) / 2 + 100, 50, 'orange')
    tl.left(45)
    parallelogram(-475, (150 * math.sqrt(2) / 2) + 50 + 100, 50 * math.sqrt(2), 'green')


def cock():
    tl.left(225)
    triangle(-50, 0, 200, 'yellow')
    square(200 * math.sqrt(2) / 2 - 50, 0, 100 / math.sqrt(2), 'orange')
    tl.right(45)
    triangle(-50, 100, 200, 'red')
    tl.right(270)
    triangle(-120, 172, 200 * math.sqrt(2) / 2, 'skyblue')
    tl.right(45)
    parallelogram(-150, -27, 85, 'green')
    tl.right(90)
    triangle((200 * math.sqrt(2) / 2) - 71, (200*math.sqrt(2) / 2) - 20, 100, 'pink')
    tl.right(225)
    triangle(-60 + 200 * math.sqrt(2) / 4, (-200 * math.sqrt(2) / 2) + 60, 100, 'purple')


def big_square():
    tl.right(45)
    square(-450, -150, 100 / math.sqrt(2), 'orange')
    tl.right(45)
    triangle(-450, -150, 100, 'purple')
    tl.left(135)
    triangle(-500, -200, 200, 'red')
    tl.left(135)
    triangle(-500, -200, 200, 'yellow')
    tl.left(135)
    triangle(-500, -200, 100, 'pink')
    tl.right(90)
    triangle(-400, -300, 140, 'skyblue')
    parallelogram(-600, -300, 100, 'green')


def men():
    tl.right(45)
    square(500, 272, 50, 'orange')
    tl.right(90)
    triangle(500, 200, 200, 'yellow')
    tl.right(45)
    triangle(500, 200, 200, 'red')
    tl.right(135)
    triangle(500, 30 - 200 * math.sqrt(2) / 2 + 100, 100, 'skyblue')
    tl.right(45)
    parallelogram(500, 100 - 200 * math.sqrt(2) / 2 + 100, 50 * math.sqrt(2), 'green')
    triangle(470, - 30 - 200 * math.sqrt(2) / 2 + 100, 70, 'pink')
    tl.left(135)
    triangle(600, 27 - 200 * math.sqrt(2) / 2 + 100, 70, 'purple')


def ship():
    tl.left(45)
    square(300, -200, 100 / math.sqrt(2), 'orange')
    tl.left(45)
    triangle(350, -150, 200, 'red')
    tl.left(135)
    triangle(300, -200, 100, 'pink')
    tl.right(135)
    triangle(275, -325, 140, 'skyblue')
    tl.left(180)
    parallelogram(275, -325, 100, 'green')
    tl.left(90)
    triangle(250, -230, 200, 'yellow')
    tl.right(45)
    triangle(250, -50, 100, 'purple')


def helicopter():
    tl.left(45)
    square(0, 175, 100 / math.sqrt(2), 'orange')
    tl.right(45)
    triangle(125, 100, 100, 'pink')
    tl.right(135)
    triangle(175, 150, 100, 'purple')
    tl.left(135)
    triangle(175, 150, 200, 'yellow')
    tl.right(135)
    triangle(375, 150, 200, 'red')
    tl.right(45)
    parallelogram(275, 250, 100, 'green')
    triangle(200, 330, 140, 'skyblue')


def rocket():
    tl.left(45)
    square(-370, -170, 100 / math.sqrt(2), 'orange')
    tl.left(45)
    triangle(-320, -220, 100, 'purple')
    tl.right(135)
    triangle(-320, -120, 200, 'red')
    tl.left(45)
    parallelogram(-220, -120, 100, 'green')
    triangle(-220, -20, 200, 'yellow')
    tl.left(90)
    triangle(-220, 80, 140, 'skyblue')
    tl.left(90)
    triangle(-270, 130, 100, 'pink')


def main():
    fish()
    tl.left(45)
    bunny()
    tl.left(45)
    cock()
    tl.left(135)
    big_square()
    tl.left(180)
    men()
    tl.right(90)
    rocket()
    tl.right(135)
    ship()
    tl.left(90)
    helicopter()

    tl.done()


if __name__ == '__main__':
    main()
    
