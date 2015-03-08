print 100 + random() * 100
#print randint(1, 6)


diameter = 50


for j in range(17):
    y = j * 50
    for i in range(13):
        x = i * 50
        #print x, y
        fill(i / 12, 0, 0.3 *random())
        if random() > 0.5:
            oval(x, y, diameter, diameter)
        else:
            rect(x, y, diameter, diameter)
