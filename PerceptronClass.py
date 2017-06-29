import random
import pygame

class Perceptron(object):
    weights = []
    learningconstant = 0.01
    
    def __init__(self, n):
        for i in range(0,n):
            val=random.uniform(-1,1)
            self.weights.append(val)
    
    def activate(self, n):
        if(n>0):
            return 1
        else:
            return -1

    def feedforward(self, inputs):
        sum=0
        temparr=inputs
        for i in range(0, len(self.weights)):
            sum+=temparr[i]+self.weights[i]

        return self.activate(sum)

    def train(self, input, desired):
        guess=self.feedforward(input)
        error=desired-guess
        #adjust the weight
        for i in range(0,len(self.weights)):
            self.weights[i]+=self.learningconstant*error*input[i]


class Trainer(object):
    input=[]
    def __init__(self,x,y,a):
        self.answer=a
        bias=1

        self.input.append(x)
        self.input.append(y)
        self.input.append(bias)

    def display(self, screen, color):
            print self.input                
            pygame.draw.ellipse(screen, color , (self.input[0], self.input[1], 6,6))
            pygame.display.flip()

class Points(object):
    x = 0
    y = 0
    b = 1
    label = 0

    def __init__(self, width, height):
        self.x = random.randint(0, width-1)
        self.y = random.randint(0, height-1)        
        if(self.x>self.y):
            self.label = 1
        else:
            self.label = -1
        self.width = width
        self.height = height

    def display(self, screen):
        color = 0        
        if(self.label > 0):
            color = (255,255,255)
        else:
            color = (255, 0 ,0)
        pygame.draw.line(screen, (255,230,9), (0,0),(self.width, self.height) )
        pygame.draw.ellipse(screen, color, (self.x, self.y, 18, 18))
        # pygame.display.flip()

    

    


        
