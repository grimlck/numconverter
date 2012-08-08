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

def bin_to_dec(binary):
    decimal = 0
    reversed_binary = str(binary)[::-1]
    for digit in range(len(reversed_binary)):
        decimal = decimal + int(str(reversed_binary)[digit]) * (2 ** digit)

    return decimal

def hex_to_dec(hexa):
    substitution = {
        "a" : "10",
        "b" : "11",
        "c" : "12",
        "d" : "13",
        "e" : "14",
        "f" : "15"
    }
    """
    For further version, following code would inverse a decitionary, even when the values
    are not unique:
    inv_substitution = {}
    for k, v in substitution.iteritems():
        inv_substitution[v] = inv_substitution.get(v, [])
        inv_substitution[v].append(k)
    
    (found here: http://stackoverflow.com/questions/483666/python-reverse-inverse-a-mapping)
    """

    decimal = 0
    rev_hex = str(hexa)[::-1]
    for digit in range(len(rev_hex)):
        if rev_hex[digit].lower() in substitution:
            new_hex = rev_hex[digit].replace(rev_hex[digit],substitution[rev_hex[digit]])
        else:
            new_hex = rev_hex[digit]
        
        decimal = decimal + int(new_hex) * (16 ** digit)

    return decimal

def main():
    number = 15
    binary_input = 1111
    hex_input = "ff"
    binary = dec_to_bin(number)
    print "dec: %s = bin: %s\n" % (number,binary[::-1])
    hexa = dec_to_hex(number)
    print "dec: %s = hex: %s\n" % (number,hexa[::-1])
    print "bin: %s = dec: %s\n" % (binary_input, bin_to_dec(binary_input))
    print "hex: %s = dec: %s\n" % (hex_input, hex_to_dec(hex_input))


if __name__ == "__main__":
    main()

