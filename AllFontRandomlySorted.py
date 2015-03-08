allFonts = installedFonts()

allFonts = allFonts[400:500]

while allFonts:
    newPage(500, 1000)
    fill(1)
    rect(0, 0, width(), height())
    for i in range(9):
        if not allFonts:
            break
        fontName = choice(allFonts)
        allFonts.remove(fontName)
    
        fill(0)
        font(fontName)
        fontSize(100)
        text("Hello", (50, 100+100*i))
        fontSize(14)
        font("Arial")
        text(fontName, (50, 80+100*i))


saveImage(["myTypeSpeciment.gif", "myTypeSpeciment.pdf", "myTypeSpeciment.png"])
