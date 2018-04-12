#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 1:
        print("{} {}.".format(length - 1, "arguments"))
    else:
        for i in range(length):
            if i == 0:
                print("{} {}:".format(length - 1, "arguments"))
            else:
                print("{}: {}".format(i, argv[i]))
