print installedFonts()

size('A4')

fill(1, 0, 0)
stroke(0, 1, 0)

font('AmericanTypewriter-CondensedLight')
fontSize(49)

myText = 'hello world ' * 10

#text(myText, (10, 10))

x, y = 10, 10
w, h = 572, 194

while myText:
    fill(1, 0, 0)
    stroke(0, 1, 0)
    myText = textBox(myText, (x, y, w, h))
    fill(None)
    stroke(0)
    rect(x, y, w, h)
    y += h + 10

