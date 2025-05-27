class myfilereader:
    def test(self):
        print("\n This is a test")
        f = open ("bidenloans.txt", "r")
        lines = f.readlines()
        #print (lines)
        f.close()
        words = []
        dd = {}

        for ln in lines:
            w = ln.split()
            for ww in w:
                words.append(ww)

        for w in words:
            if w in dd.keys():
                dd[w] += 1
            else:
                dd[w] = 1

        print (dd)

        mx = max(dd.values())
        print (mx)

        res = [ wd for wd, w in dd.items() if w == mx ]
        print ( res )

        #test = [x for x, w in dd.items() if w == mx]
        #print (test)

        for k in dd.keys():
            if dd[k] == mx :
                print (k, mx)



#        result = [lastname for lastname, firstname in names.items() if firstname == "Jane"]






        print ("\n")
        print (words)





myr = myfilereader()
myr.test()

