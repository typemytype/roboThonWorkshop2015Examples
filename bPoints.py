from random import randint

glyph = CurrentGlyph()

for contour in glyph:
    for bPoint in contour.bPoints:
        print "anchor:", bPoint.anchor
        print "bcp in:",  bPoint.bcpIn
        print "bcp out:",  bPoint.bcpOut
        print 
        x, y = bPoint.anchor
        bcpIn = bPoint.bcpIn
        bcpOut = bPoint.bcpOut
        
        bPoint.anchor = (x + randint(-10, 10), y)
        bPoint.bcpIn = bcpIn
        bPoint.bcpOut = bcpOut

glyph.update()