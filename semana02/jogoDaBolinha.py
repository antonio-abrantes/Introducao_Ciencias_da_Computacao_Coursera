#http://www.codeskulptor.org/#user42_QkudAngbNS_0.py
#import simplegui
import random
import math

raio = 10
largura = 600
altura = 400
pos_x = 200
pos_y = 200
score = 10


def timer_handler():
    global pos_x, pos_y
    pos_x = random.randint(0, largura)
    pos_y = random.randint(0, altura)


def mouse_handler(position):
    global score
    dist = math.sqrt((pos_x - position[0]) ** 2 + (pos_y - position[1]) ** 2)

    if dist <= raio:
        score += 1
    else:
        if score > 0:
            score -= 1


def draw_handler(canvas):
    label_score.set_text('Pontos: ' + str(score))
    canvas.draw_circle([pos_x, pos_y], raio, 20, 'Yellow')


frame = simplegui.create_frame("Jogo", largura, altura)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(mouse_handler)
label_score = frame.add_label('Pontos: ' + str(score), 200)
frame.start()

timer = simplegui.create_timer(1000, timer_handler)
timer.start()

frame.start()