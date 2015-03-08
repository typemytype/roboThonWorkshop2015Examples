a = 0xFFFF
b = 010
c = 0b110
print c
# print a != b
# print a == b
# print a < b
# print a <= b
# print a > b
# print a >= b

# print True
# print False

result = a > b
print result

if a > b:
    print 'a greater than b'
    print 'this is nice' 
    if a == c:
        print 'bladibla'
        print 'bladibla'
        
elif a < b: # else if
    print 'b greater than a'
else:
    print 'it is equal'
    
print 'the script is done'