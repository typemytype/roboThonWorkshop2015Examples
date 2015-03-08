f = CurrentFont()

master1 = f["b"]
master2 = f["b.bold"]

isCompatible, errorMessage = master1.isCompatible(master2)

if isCompatible:
    factor = (1.22, 1.76)
    #result = master1 * (1 - factor)  + (master2 * factor)
    diff = master2 - master1
    result = master1 + factor * (master2 - master1)

    drawGlyph(result)
    
    f.insertGlyph(result, "b.interpol")
    
else:
    print errorMessage



