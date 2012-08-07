#!/usr/bin/env python
def dec_to_bin(dec):
    result = dec / 2
    rest = dec % 2
    print "%s : 2 = %s -- Rest: %s" % (dec,int(result),rest)
    if int(result) != 0:
        binary = str(rest) + str(dec_to_bin(int(result)))
        return binary
    else:
        return str(rest)
def main():
    number = 12345
    binary = dec_to_bin(number)
    print binary[::-1]
    

if __name__ == "__main__":
    main()

