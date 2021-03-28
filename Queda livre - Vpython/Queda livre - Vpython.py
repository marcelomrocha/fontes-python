#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
from visual import *
from Tkinter import *

scene1 = display(title='Vetores - Gravidade - Velocidade',
     x=0, y=0, width=400, height=600,
     center=(0,0,0), background=(0,0,0))

estado = "desligado"
i = 1 # faz com que a thread seja executada uma so vez
#scene.autoscale = False
floor = box (pos=(0,0,0), length=4, height=0.5, width=4, color=color.blue)
ball = sphere (pos=(0,4,0), radius=1, color=color.red)
ball.velocity = vector(0,-1,0)
dt = 0.01
g = vector(0,-0,0)
label(pos=(-3,6,0), text='g')
label(pos=(-5,6,0), text='v')
vetor_g = arrow(pos=(-3,5,0), axis=g*0.1,shaftwidth=0.2,
		headlength=0.5,headwidth=0.4,fixedwidth = True, 
		color=color.yellow)
vetor_v = arrow(pos=(-4,5,0), axis=(0,0,0),shaftwidth=0.2,
		headlength=0.5,headwidth=0.4,fixedwidth = True, 
		color=color.green)

def vfun():
    while 1:
        while (1 and (estado=="ligado")):
            rate (100)
            ball.pos = ball.pos + ball.velocity*dt
            if ball.y < ball.radius:
                ball.velocity = ball.velocity*-1
            else:
                ball.velocity = ball.velocity + (g*dt)
            vetor_v.axis = (0,ball.velocity.y*0.2,0)

def g_fun(valor): # Funcão que envia o valor do slide Y para a porta serial
   g.y = -int(valor)
   vetor_g.axis = (0,g.y*0.1,0)

def v_fun(valor): # Funcão que envia o valor do slide X para a porta serial
   ball.pos.y = int(valor)
   ball.velocity = vector(0,-1,0)

def raio(valor): # Funcão que envia o valor do slide X para a porta serial
   ball.radius = int(valor) * 0.1
   
def start(): # Função que destrói a Janela principal, antes fecha a porta serial
    global estado,i
    if i==1:
        th.start()
        i=0
    if estado == "desligado":
        b.config(text = 'Pause')
        estado="ligado"
    elif estado == "ligado":
        b.config(text = 'Start')
        estado="desligado"

        
# processo de criação da UI com TKinter

root = Tk() # Cria a janela
root.title('Configuração das variáveis') # Define o títula da janela
root.geometry('280x270') # Define o tamanho

# 

l_g = Label(root, text="Módulo do vetor gravidade (m/s²) 1-30"); # desenha e posiciona os labels
l_g.place(x=20, y=20)
scale = Scale( root, from_=1, to=30, command = g_fun, width=9, length=179, orient=HORIZONTAL )
scale.place(x=20,y=40)

l_p = Label(root, text="Posição inicial (m) 1-20"); # desenha e posiciona os labels
l_p.place(x=20, y=80);
scale = Scale( root, from_=1, to=20, command = v_fun, width=9, length=179, orient=HORIZONTAL )
scale.place(x=20,y=100)

l_r = Label(root, text="Raio da esfera (r) 2-12"); # desenha e posiciona os labels
l_r.place(x=20, y=140)
scale = Scale( root, from_=2, to=12, command = raio, width=9, length=179, orient=HORIZONTAL )
scale.place(x=20,y=160)


# Cria um objeto botão
b = Button(root, text ='Start', command = start)
b.place(x=110,y=220)

th=Thread(target=vfun, args = ()) # roda a janela vpython
root.mainloop() # Coloca o programa em execução
