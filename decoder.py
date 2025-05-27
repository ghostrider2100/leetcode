
class Decoder:
    def dc_reader(self, key_codes: str) -> dict:
        dc = {}
        f = open(key_codes, "r")
        for line in f:
            line = line.strip('\n')
            new_code = line.split(" ")
            if new_code[0] not in dc.keys():
                dc[new_code[0]] = new_code[1]
        f.close()
        return dc

    def msg_reader(self, msg: str) -> list:
        tmp = []
        nums_list = []
        f = open(msg, "r")
        for line in f:
            line = line.strip('\n')
            tmp = line.split(" ")
            #print (tmp)
            nums_list.append(tmp[-1])
        f.close()
        #print (nums_list)
        return nums_list

    def decode_it(self, words: list, code: dict ):
        for num in words:
            if num in code.keys():
                print (num, code[num] )


dcr = Decoder()
fcodes = "keysdecoder.txt"
kcodes = dcr.dc_reader(fcodes)
#print (kcodes)

fmsg = "encoded_file.txt"
msglist = dcr.msg_reader(fmsg)

dcr.decode_it(msglist, kcodes)




