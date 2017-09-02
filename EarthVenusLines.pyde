'''The segments connecting Earth and Venus
Peter Farrell September 2, 2017'''

class Planet:
    def __init__(self,r,freq,col):
        self.r = r
        self.freq = freq
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

def setup():
    size(600,600)
    
#time variables
t = 0.0
dt = 0.05

#create planets
venus = Planet(100,1.5,color(255,0,255))
earth = Planet(250,1,color(0,0,255))
    
def draw():
    global t,dt,venus,earth
    background(0)
    translate(width/2,height/2)
    #sun
    fill(255,255,0)#yellow
    ellipse(0,0,50,50)
    #update planets
    venus.update()
    earth.update()
    strokeWeight(1)
    stroke(255)
    line(earth.x,earth.y,venus.x,venus.y)
    t += dt