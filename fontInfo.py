glyph = CurrentGlyph()

print "name", glyph.name
print "unicode", glyph.unicode
print "width", glyph.width
print "leftMargin", glyph.leftMargin
print "rightMargin", glyph.rightMargin


for contour in glyph:
    for point in contour.points:
        
        if point.y < -100:
            point.y -= 50

glyph.update()