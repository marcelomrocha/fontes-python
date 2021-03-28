from visual import *

scene2 = display( title = "www.fisicarduino.com - Lancamento Obliquo", ) 

floor = box (pos=(0,0,0), length=50, height=0.5, width=4, color=color.blue)
ball = sphere (pos=(0,4,0), radius=1, color=color.red)
alvo = sphere (pos=(50,2,0), radius=1, color=color.white)
ball.velocity = vector(10,-24.5,0)
dt = 0.01

vetor_vy = arrow(pos=(-5,2,1), axis=(0,ball.velocity.y,0), shaftwidth=0.5,  color=color.yellow)
vetor_vx = arrow(pos=(-15,2,1), axis=(ball.velocity.x,0,0), shaftwidth=0.5,  color=color.cyan)
while 1:
    rate (100)
    vetor_vy.axis = (0,ball.velocity.y,0)
    vetor_vx.axis = (ball.velocity.x,0,0)
    vetor_vy.pos = (ball.x, ball.y, ball.z)
    vetor_vx.pos = (ball.x, ball.y, ball.z)
    ball.pos = ball.pos + ball.velocity*dt
    if ball.y < ball.radius:
        ball.velocity.y = abs(ball.velocity.y)
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt
        
#>>> def vels(s, vx, g):
#...     return ((s * g) / (2 * vx))
