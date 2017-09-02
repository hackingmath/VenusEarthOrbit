'''The segments connecting Earth and Venus
Peter Farrell September 2, 2017'''

from random import randint

scl = 1.5
erase = False
pause = False

class Star:
  def __init__(self):
    self.x = randint(0,600)
    self.y = randint(0,600)
    
  def update(self):
    fill(255)
    ellipse(self.x,
            self.y,
            5,5)

class Planet:
    def __init__(self,r,period,col):
        self.r = r
        #convert the period into the frequency
        self.freq = TWO_PI/period
        self.col = col #color
        
    def update(self):
        #orbit
        noFill()
        stroke(255)
        strokeWeight(4)
        ellipse(0,0,2*self.r,2*self.r)
        #planet
        noStroke()
        fill(self.col)
        self.x = self.r*cos(self.freq*t)
        self.y = self.r*sin(self.freq*t)
        ellipse(self.x,self.y,20,20)
        
class Line:
    def __init__(self,beginning,ending):
        self.ax = beginning.x
        self.ay = beginning.y
        self.bx = ending.x
        self.by = ending.y
        
    def update(self):
        line(self.ax,self.ay,self.bx,self.by)

def setup():
    size(600,600)
    
#time variables
t = 0.0
dt = 0.01

#create planets
#yes, these are their real average radii and orbital periods!
venus = Planet(108.2*scl,0.6152,color(255,0,255))
earth = Planet(149.6*scl,1,color(0,0,255))

#create stars
starList = []
for i in range(10):
  starList.append(Star())

#line list
lineList = []
    
def draw():
    global starList,venus, t,dt,lineList
    background(0)
    for star in starList:
        star.update()
    translate(width/2,height/2)
    #sun
    fill(255,255,0)#yellow
    ellipse(0,0,50,50)
    #update planets
    venus.update()
    earth.update()
    lineList.append(Line(venus,earth))
    strokeWeight(1)
    stroke(255)
    if erase:
        lineList = [] #empty the line list
    #draw all the lines (if there are any)
    for n in lineList:
        n.update()
    else:
        line(venus.x,venus.y,earth.x,earth.y)
    if not pause:
        t += dt
    
def keyPressed():
    global erase,pause
    if key == 'e':
        erase = not erase
    if key == 'p':
        pause = not pause
        
