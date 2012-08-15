#!/usr/bin/env python
import argparse
import string


def dec_to_bin(dec, verbose=False):
    rest = dec % 2
    if int(dec) != 0:
        if verbose == True:
            print "%s \t:\t 2 = %s \t-- Rest: %s" % (dec,int(dec/2),rest)
            verbose = True
        
        binary = str(dec_to_bin(int(dec/2),verbose)) + str(rest)
        return binary
    else:
        return ""

def dec_to_hex(dec, verbose=False):
    substitution = {
        "10" : "A",
        "11" : "B",
        "12" : "C",
        "13" : "D",
        "14" : "E",
        "15" : "F"
    }
    rest = str(dec % 16)
    if rest in substitution:
        rest = rest.replace(rest,substitution[rest])

    if int(dec) != 0:
        if verbose == True:
            print "%s \t:\t 16 = %s \t-- Rest: %s" % (dec,int(dec/16),rest)
            verbose = True

        hexa = str(dec_to_hex(int(dec/16),verbose)) + str(rest)
        return hexa
    else:
        return ""

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

def hex_to_bin(hexa, verbose=False):
    return dec_to_bin(hex_to_dec(hexa), verbose)

def bin_to_hex(bin, verbose=False):
    return dec_to_hex(bin_to_dec(bin), verbose)

def is_binary(s):
    for digit in str(s):
        if digit != "0" and digit != "1":
            result = False
            break
        else:
            result = True
    return result

def main():
    parser = argparse.ArgumentParser(description='Covert hexadecimal, decimal and binary numbers. Use only one argument at a time.')
    parser.add_argument('-H', '--hex', type=str, help='hexadecimal number to convert', required=False, default=None)
    parser.add_argument('-b', '--binary', type=str, help='binary number to convert', required=False, default=None)
    parser.add_argument('-d', '--decimal', type=int, help='positive decimal number to convert', required=False, default=None)
    parser.add_argument('-v', '--verbose', action='store_true', required=False, default=False)

    args = parser.parse_args()
    
    if args.hex and not args.binary and not args.decimal:
        if all(c in string.hexdigits for c in args.hex) == True:
            print "%s(hex) = %s(dec)\n" % (args.hex, hex_to_dec(args.hex))
            print "%s(hex) = %s(bin)\n" % (args.hex,hex_to_bin(args.hex, args.verbose))
        else:
            print "%s is not a hexadecimal." % args.hex

    elif args.binary and not args.hex and not args.decimal:
        if is_binary(args.binary) == True:
            print "%s(bin) = %s(dec)\n" % (args.binary, bin_to_dec(args.binary))
            print "%s(bin) = %s(hex)\n" % (args.binary,bin_to_hex(args.binary,args.verbose))
        else:
            print "%s is not a binary number." % args.binary
            
    elif args.decimal and not args.hex and not args.binary:
        if args.decimal >= 0:
            print "%s(dec) = %s(hex)\n" % (args.decimal,dec_to_hex(args.decimal,args.verbose))
            print "%s(dec) = %s(bin)\n" % (args.decimal,dec_to_bin(args.decimal,args.verbose))
        else:
            print "%s is not a postive decimal number" % args.decimal
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

