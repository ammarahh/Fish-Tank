def setup():
#1
    size(500,500)
    background(random(255),random(255),random(255))
    numFish=0
    makeFish(250,250,239,14,25)
    while numFish<100:
        makeFish(random(500),random (500),random(255),random(255),random(255))
        numFish=numFish+1
    
    

    
def makeFish(x,y,red,green, blue):
    fill(red,green,blue)
    #head
#2
    ellipse(x,y,40,20)
    #tail
#3
    triangle(x+20,y,x+30,y-10,x+30,y+10)
    
