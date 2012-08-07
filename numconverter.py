#!/usr/bin/env python
def dec_to_bin(dec):
    result = dec / 2
    rest = dec % 2
    print "%s \t:\t 2 = %s \t-- Rest: %s" % (dec,int(result),rest)
    if int(result) != 0:
        binary = str(rest) + str(dec_to_bin(int(result)))
        return binary
    else:
        return str(rest)

def dec_to_hex(dec):
    substitution = {
        "10" : "A",
        "11" : "B",
        "12" : "C",
        "13" : "D",
        "14" : "E",
        "15" : "F"
    }
    result = dec / 16
    rest = str(dec % 16)
    print "%s \t:\t 16 = %s \t-- Rest: %s" % (dec,int(result),rest)
    if rest in substitution:
        rest = rest.replace(rest,substitution[rest])

    if int(result) != 0:
           hexa = str(rest) + str(dec_to_hex(int(result)))
           return hexa
    else:
        return str(rest)

def main():
    number = 123455
    binary = dec_to_bin(number)
    print "dec: %s = bin: %s\n" % (number,binary[::-1])
    hexa = dec_to_hex(number)
    print "dec: %s = hex: %s\n" % (number,hexa[::-1])
    

if __name__ == "__main__":
    main()

