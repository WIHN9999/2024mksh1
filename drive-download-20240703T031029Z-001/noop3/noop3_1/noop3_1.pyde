def setup():
    size(500,500)
    background(255,255,235)
def draw():
    if mousePressed:
        line(mouseX, mouseY,pmouseX, pmouseY)  
