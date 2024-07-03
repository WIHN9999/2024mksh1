names = ['senna', 'make', 'cala'] # list 陣列
for name in names:
    print(name)
background(255,0,0)
size(400,400)
for i in range(len(names)):
    text(names[i], i*100, 100)
