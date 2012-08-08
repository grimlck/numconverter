#!/usr/bin/env python
import argparse
import string


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
    rev_hex = str(hexa)[::-1].lower()
    for digit in range(len(rev_hex)):
        if rev_hex[digit] in substitution:
            new_hex = rev_hex[digit].replace(rev_hex[digit],substitution[rev_hex[digit]])
        else:
            new_hex = rev_hex[digit]
        
        decimal = decimal + int(new_hex) * (16 ** digit)

    return decimal

def hex_to_bin(hexa):
    return dec_to_bin(hex_to_dec(hexa))

def bin_to_hex(bin):
    return dec_to_hex(bin_to_dec(bin))

def is_binary(s):
    for digit in str(s):
        if digit != "0" and digit != "1":
            result = False
            break
        else:
            result = True
    return result

def main():
    parser = argparse.ArgumentParser(description='Covert hexadecimal, decimal and binary numbers.')
    parser.add_argument('-H', '--hex', type=str, help='hexadecimal number to convert', required=False, default=None)
    parser.add_argument('-b', '--binary', type=str, help='binary number to convert', required=False, default=None)
    parser.add_argument('-d', '--decimal', type=int, help='decimal number to convert', required=False, default=None)


    args = parser.parse_args()
    
    if args.hex:
        if all(c in string.hexdigits for c in args.hex) == True:
            print "%s(hex) = %s(dec)\n" % (args.hex, hex_to_dec(args.hex))
            binary = hex_to_bin(args.hex)
            print "%s(hex) = %s(bin)\n" % (args.hex,binary[::-1])
        else:
            print "%s is not a hexadecimal." % args.hex

    if args.binary:
        if is_binary(args.binary) == True:
            print "%s(bin) = %s(dec)\n" % (args.binary, bin_to_dec(args.binary))
            hexa = bin_to_hex(args.binary)
            print "%s(bin) = %s(hex)\n" % (args.binary,hexa[::-1])
        else:
            print "%s is not a binary number." % args.binary
    if args.decimal:
        print "%s(dec) = %s(hex)\n" % (args.decimal,dec_to_hex(args.decimal))
        print "%s(dec) = %s(bin)\n" % (args.decimal,dec_to_bin(args.decimal))
    if not args.decimal and not args.hex and not args.binary:
        parser.print_help()


if __name__ == "__main__":
    main()

