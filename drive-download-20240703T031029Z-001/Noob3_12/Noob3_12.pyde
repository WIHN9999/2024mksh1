def setup():
    global img, img1
    size(750,501)  
    img = loadImage('Noob1.jpg')
    img1 = loadImage('Noob2.jpg')
def draw():
    global img, ing1
    image(img, 0, 0)
    for i in range(10):
        image(img1, x[i], y[i], 200, 230)
    image(img1, mouseX, mouseY, 300,230)
x = [0]*10
y = [0]*10
N = 0    
def mousePressed():
    global N
    x[N], y[N] = mouseX, mouseY
    N += 1
