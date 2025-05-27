


x = [ 'asdfd', '343','mnb']

print ( x.sort() )   # this has will print none, but if you then print x it works
print (x)           # ok; sorted in place; permanent
print (sorted(x) )  # ok, not permanent
print (x[::-1])     # reversed but not permanent
print (x[::1])      # not permanent
