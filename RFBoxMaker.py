font = CurrentFont()


MARGIN = 30

for glyph in font:
    if glyph.box:
        glyph.removeOverlap()

        xMin, yMin, xMax, yMax = glyph.box
        print xMin, yMin, xMax, yMax
        
        #yMin = font.info.descender
        #yMax = font.info.ascender
        #xMin = 0
        #xMax = glyph.width
        
        pen = glyph.getPen()
        pen.moveTo((xMin - MARGIN, yMin - MARGIN))
        pen.lineTo((xMin - MARGIN, yMax + MARGIN))
        pen.lineTo((xMax + MARGIN, yMax + MARGIN))
        pen.lineTo((xMax + MARGIN, yMin - MARGIN))
        pen.closePath()
