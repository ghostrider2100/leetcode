
#For the given string, add a <b> and </b> inline before and after the target substrings.
#Note there are no delimeters or space in the string

#case1
s = "thisisatest"
keywords = ["this", "test"]

#case2
#keywords = ["this", "test"]
#case3
#s = "aaabcdaaa"
#keywords = ["aaa", "bc"]
#case4

#s=[]
#keywords = []

stack = []
idx = 0
if len(keywords) == 0:
    print (s)
    pass

for k in keywords:
    if k in s:
        #print (s)
        idx = s.index(k)
        if idx != 0:
            stack.append(s[0:idx])
            s = s.replace(s[0:idx], '')
        #print(idx)
        stack.append("<b>")
        stack.append(k)
        stack.append("</b>")
        s= s.replace(k,'')

#print (s)
if len(s) != 0:
    stack.append(s)

print ("".join(stack) )
