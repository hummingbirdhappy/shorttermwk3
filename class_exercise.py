#x = 3
#print "Value of x is", x
#y=x
#print "Id of x is ", id(x)
#print "Id of y is ", id(y)
#print "Value of y is", y
#x=x+1
#print "new value of x is", x
#print "new value of y is", y
#print "New id of x is ", id(x)
#print "New id of y is ", id(y)

#a = [1,2]
#b = a
#print "list a is", a
#print "list b is", b
#print "id of a is ", id(a)
#print "id of b is ", id(b)

#a.append(3)
#print "new list a is", a
#print "new list b is", b
#print "new id of a is", id(a)
#print "new id of b is", id(b)

#b = b.append(4)
#print "new list b is", b
#print "new list a is", a
#print "new id of b is", id(b)

s = 'banana'
t = s
print "string s is", s
print "string t is", t
print "new id of s is", id(s)
print "new id of t is", id(t)

s=s+'s'
print "new string s is", s
print "new string t is", t
print "new id of s is", id(s)
print "new id of t is", id(t)

s = s.replace('s','') 
print "new string s is", s
print "new string t is", t
print "new is of s is", id(s)
print "new id of t is", id(t)
