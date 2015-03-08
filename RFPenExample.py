glyph = CurrentGlyph()

glyph.clear()

pen = glyph.getPen()

pen.moveTo((30, 50))
pen.lineTo((30, 700))
pen.lineTo((500, 700))
pen.curveTo((590, 524), (550, 200), (500, 50))
pen.closePath()

pen.moveTo((200, 200))
pen.lineTo((300, 200))
pen.lineTo((300, 400))
pen.lineTo((200, 400))
pen.closePath()


# glyph.update()