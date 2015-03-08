# dictionaries do ***NOT*** have an ORDER.

myDict = {"a": "the letter a", "b": "letter b",
  "xyz": "seq. xyz"}

print myDict
print len(myDict)

print myDict["a"]
print myDict["b"]

print "a" in myDict

if "XYZ" in myDict:
    print myDict["XYZ"]
else:
    print "don't have a key 'XYZ'"

myDict["b"] = "this is really the letter b."

print myDict["b"]

#del myDict["a"]

#print myDict

#print myDict.keys()
print
print

for key in myDict:
    print key, ":::", myDict[key]
    