from Tkinter import *
import os
import pygame, sys
import pygame.camera

from pygame.locals import *


w, h = 400, 400

#pygame.quit()
#sys.exit()	
	
# Add a couple widgets. We're going to put pygame in `embed`.
root = Tk()
embed = Frame(root, width=320, height=240)
embed.pack(side = LEFT,padx=5, pady=5)

frame2 = Frame(root)
frame2.pack()

text = Button(frame2, text='Blah.')
text.pack()
var = DoubleVar()
scale = Scale( frame2, from_=0, to=255, variable = var )
scale.pack(anchor=CENTER)

# Tell pygame's SDL window which window ID to use    
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())

# The wxPython wiki says you might need the following line on Windows
# (http://wiki.wxpython.org/IntegratingPyGame).
#os.environ['SDL_VIDEODRIVER'] = 'windib'

# Show the window so it's assigned an ID.
root.update()

# Usual pygame initialization
pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0",(320,240))
cam.start()

DISPLAYSURF = pygame.display.set_mode((w, h))
#pygame.display.set_caption('Hello World!')


#definindo cores
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

size = (320,240)
display = pygame.display.set_mode(size, 0)
snapshot = pygame.surface.Surface(size, 0, display)

while True: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	#pygame.draw.rect (DISPLAYSURF, (140,240,130), Rect((100,100), (130,170)))
	snapshot = cam.get_image()
	display.blit(snapshot, (0,0))
	pygame.display.update() 
	cam.set_controls(0, 0, scale.get())
	root.update()




