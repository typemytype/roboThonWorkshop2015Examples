font = CurrentFont()

#print font.selection
#font.selection = ["g", "h"]

print font.info.familyName
print font.info.styleName

font.info.designer = "Me ;)"



print font.keys()

print font.glyphOrder
for glyphName in font.glyphOrder:
    glyph = font[glyphName]
    print glyph
    
    for contour in glyph:
        for point in contour.points:
            if point.y < -100:
                point.y -= 50
    glyph.update() 
