import pygame, sys
import random
from PerceptronClass import Trainer, Perceptron, Points

#Initialize Screen
width=600
height=600
screen=pygame.display.set_mode((height, width))
black=0,0,0
WHITE = (255, 255, 255)
RED   = (255,   0,   0)


ptron = Perceptron(3)

points = []

for i in xrange(100):
    point = Points(width,height)
    points.append(point)

#set Screen 
pygame.display.set_caption("Line", "Line")
screen.fill(black)

#Start screen 
while 1:
    for event in pygame.event.get():       

        if event.type == 12:
            sys.exit()

  

    for i in points: 
        i.display(screen)

    for eachpt in points:
        inputarr = [ eachpt.x , eachpt.y , eachpt.b ]
        ptron.train(inputarr, eachpt.label)
    
        guess = ptron.feedforward(inputarr)
        if(guess == eachpt.label):
            pygame.draw.ellipse(screen, (1,1,1), (eachpt.x, eachpt.y, 8, 8))
            
        else:
             pygame.draw.ellipse(screen, (240,240,240), (eachpt.x, eachpt.y, 8, 8))
             

    pygame.display.flip()
        
                
            

        


    



