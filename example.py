#!/usr/bin/env python

from charlist import CharList


s = "test"
print "string:  ", s, repr(s)

cl = CharList(s)
print "CharList:", cl, repr(cl)

assert cl.string == s
assert cl.list == ['t', 'e', 's', 't']


last_letter = cl.pop()
assert last_letter == "t"

assert cl.string == "tes"
assert cl.list == ['t', 'e', 's']


cl[1] = "o"

assert cl.string == "tos"
assert cl.list == ['t', 'o', 's']


cl += "bla"

assert cl.string == "tosbla"
assert cl.list == ['t', 'o', 's', 'b', 'l', 'a']



s = "te_st"
c = CharList(s)

c[1:3] = "oa"
c += "er"

assert c.string == "toaster"
assert c.list == ['t', 'o', 'a', 's', 't', 'e', 'r']


c[1:3:] = "ee"

assert c.string == "teester"
assert c.list == ['t', 'e', 'e', 's', 't', 'e', 'r']



c[1:6:2] = "xxx"

assert c.string == "txextxr"
assert c.list == ['t', 'x', 'e', 'x', 't', 'x', 'r']



## raises regular ValueError about incompatible sizes
#c[1:6:2] = "yyyyy"


## raises custom ValueError
#c[1] = "yy"


## without the customized __setitem__

#s = "test"
#c = CharList(s)

#c[1] = "oa"
#c += "er"

#print c # prints "toaster"
## looks fine until here, but:
#print c.list # print ['t', 'oa', 's', 't', 'e', 'r']



## Should these be CharList, too?

#print c[1:3]
#print c[1:6:2]


