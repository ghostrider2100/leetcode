
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    fh = open ("/Users/slx/Documents/mytext.txt", 'r')
    #rw = fh.readline()

    dw = {};


    for ln in fh:
        print (ln)
        words = ln.split()
        for w in words:
            w = w.lower()
            if w in dw.keys():
                dw[w] = dw[w] +1
            else:
                dw[w] = 1

    #print (dw)
    key_list = list (dw.keys() )
    val_list = list (dw.values() )
    ind = val_list.index( max ( dw.values() )  )

    print ( ind )
    print ( key_list.index(ind) ) 
