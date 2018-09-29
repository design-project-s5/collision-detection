

import pygame
from pygame.locals import *
from sys import exit
import time
import math

pygame.init()                                      #initialize all imported python modules.
screen = pygame.display.set_mode((640,480))       #to make pygame window.

#fuction to draw a circle.
def drawCircle(screen,color,center,radius):      
    (x,y) = center
    pygame.draw.circle(screen,color,(x,y),radius) #built in fuction in pygame to draw a circle.



#function to check whether 2 circles collide or not.  
def circle(x1,y1,x2,y2,r1,r2): 
   
    distSq = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    radSumSq = (r1 + r2) * (r1 + r2);  
    if (distSq == radSumSq): 
        return 1 
    elif (distSq > radSumSq): 
        return -1 
    else: 
        return 0 
      


#setting colours.(RGB colour value)

red = (255,0,0)
green = (0,255,0)
white=(255,255,255)


screen.fill(white)
x1=300
y1=240
x2=325
y2=240
r1=100
r2=100
    
#function drawcircle is called to draw the circles.

drawCircle(screen,red,(x1,y1),r1)
drawCircle(screen,green,(x2,y2),r2)
pygame.display.update()      #to update a portion of the screen.Pressing no arguments,update the entire display.    

print("This is the 2 circles.")
print("circle 1 with cordinates (300,240) and radius 100")
print("circle 2 with cordinates (325,240) and radius 100")
time.sleep(1)     #pauses python program 


while True:
	 # check for the QUIT event
	for event in pygame.event.get():
		#if the user want to quit.
		 if event.type == QUIT:
			#window get closed.
			pygame.quit()
			sys.exit()


	t=circle(x1,y1,x2,y2,r1,r2)
	if (t == 1): 
   		print("Circle touch to each other.")  
	elif (t < 0): 
   		print("Circle not touch to each other.")  
	else: 
   		print("Circle intersect to each other.")  
   		midx=(x1+x2)/2;
   		midy=(y1+y2)/2;
   		newx1=int(midx+r1*(x1-x2)/math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
   		newy1=int(midy+r1*(y1-y2)/math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
   		newx2=int(midx+r2*(x2-x1)/math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
   		newy2=int(midy+r2*(y2-y1)/math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
		
		screen.fill(white)

		
   		drawCircle(screen,red,(newx1,newy1),100);
   		drawCircle(screen,green,(newx2,newy2),100);
   	pygame.display.update()

	









