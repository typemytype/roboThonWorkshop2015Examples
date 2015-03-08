#from robofab.world import CurrentGlyph
from random import randint

glyph = CurrentGlyph()

print len(glyph)

for contour in glyph:
    print contour
    for segment in contour:
        print "  ", segment
        for point in segment:
            print "     ", point.x, point.y, point.type
            if point.type != "offCurve":
                point.x += randint(-10, 10)
            
glyph.update()
            