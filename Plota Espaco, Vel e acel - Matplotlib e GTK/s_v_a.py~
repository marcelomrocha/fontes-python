# matplotlib Figure object
from matplotlib.figure import Figure

# import the GtkAgg FigureCanvas object, that binds Figure to
# GTKAgg backend. In this case, this is a gtk.DrawingArea
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas


import numpy as np

# gtk module
import gtk
import gobject

import serial; # importa o modulo para a comunicacao serial
import time # importa a biblioteca para trabalhar com temporizacao

ser = ""

tamanho = 100
i = 0

x = np.arange(tamanho)
s = np.arange(tamanho)
v = np.arange(tamanho)
a = np.arange(tamanho)
	

def conecta():
	global ser
	print "abrindo a porta serial..."
	ser = serial.Serial("/dev/ttyUSB0", 9600);  # abre a portal serial
	print "conexao feita com sucesso!"
	
def fecha():
	global ser
	print "...fechando a porta serial"
	ser.close()
	
	
def le_dados():
	global x, s, v, a, ser	
	s = np.delete(s, 0)
	s = np.append(s, int(ser.readline()))
	v = np.delete(v, 0)
	v = np.append(v, (s[tamanho-1]-s[tamanho-5])/.5)
	a = np.delete(a, 0)
	a = np.append(a, (v[tamanho-1]-v[tamanho-5])/.5)
	
def update_draw(*args):
	global x, s, v, a, i
	i = i + 1
	le_dados()
	
	ls.set_data(x, s)
	lv.set_data(x, v)
	la.set_data(x, a)
	
	fig.canvas.draw()
	#if i > 30:
	#	return False
	#else:
	#	time.sleep(0.1)
	#time.sleep(0.05)
	return True


# instantiate the GTK+ window object
win = gtk.Window()
# connect the 'destroy' signal to gtk.main_quit function
win.connect("destroy",gtk.main_quit)
# define the size of the GTK+ window
win.set_default_size(600, 8750)
# set the window title
win.set_title("Monitor de Luminosidade - Usando MatPlotLib e Gtk")

# matplotlib code to generate the plot
fig = Figure(figsize=(6, 6), dpi=70)
#grafico do espaco x tempo
axs = fig.add_subplot(311)
axs.set_ylim(-230, 230)
axs.set_xlabel("Tempo")
axs.set_ylabel("Espaco (cm)")
axs.grid()

#grafico da velocidade x tempo
axv = fig.add_subplot(312)
axv.set_ylim(-230, 230)
axv.set_xlabel("Tempo")
axv.set_ylabel("Velocidade (cm/s)")
axv.grid()

#grafico da aceleracao x tempo
axa = fig.add_subplot(313)
axa.set_ylim(-230, 230)
axa.set_xlabel("Tempo")
axa.set_ylabel("Aceleracao ((cm/s)*(1/s))")
axa.grid()


ls, = axs.plot(x, s, color='blue')
lv, = axv.plot(x, v, color='green')
la, = axa.plot(x, a, color='red')


# we bind the figure to the FigureCanvas, so that it will be
# drawn using the specific backend graphic functions
canvas = FigureCanvas(fig)
# add that widget to the GTK+ main window
win.add(canvas)

conecta()
# explicit update the graph (speedup graph visualization)
update_draw()

# exec our "updated" funcion when GTK+ main loop is idle
gobject.idle_add(update_draw)

# show all the widget attached to the main window
win.show_all()
# start the GTK+ main loop
gtk.main()

#fecha()
	


