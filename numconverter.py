#!/usr/bin/env python
def dec_to_bin(dec):
    result = dec / 2
    rest = dec % 2
    print "%s : 2 = %s -- Rest: %s" % (dec,int(result),rest)
    return (int(result),str(rest))
def main():
    number = 12345
    binary=""
    while True:
        number,rest = dec_to_bin(number)
        if rest != 0:
            binary = binary+rest
        else:
            break
    print binary

if __name__ == "__main__":
    main()

