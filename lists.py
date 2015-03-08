print range(10, 5, -1)


myList = [10, 10, 30, 50]



for index in range(len(myList)):
    print index, myList[index]

print "index now equals:", index

counter = 0
for item in myList:
    print counter, item
    counter += 1
    # counter = counter + 1

print "counter now equals:", counter