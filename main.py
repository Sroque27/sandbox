from vpython import * #import vpython library

class beaver:
    #constructor method for teddybear
    def __init__(self):
        f = sphere() #sphere for face
        f.radius = 3 #sizes face
        f.color = vector(188/255, 143/255, 108/255) #colors face
        self.face = F
        #list of spheres for ears
        self.eyes = []
        for i in range(2):
            eye = sphere()
            eye.radius = 0.5
            eye.pos.y += 1
            if i == 0:
                eye.pos.x = i-1
            else:
                eye.pos.x = i
            eye.pos.z = 3
            self.eyes.append(eye)

t = beaver()

while True:
    rate(10)