#!/usr/bin/env python3

#saját megoldás
def XOR(input1, input2):
    b1 = bool(input1)
    b2 = bool(input2)

    result = False

    if (1 == False and b2 == True) or (b1 == True and b2 == False):
        result = True

    return result


def main():
    input1 = "Python"
    input2 = None

    if (XOR(input1,input2) == True):
        print("Az XOR muvelet IGAZ")
    else:
        print("Az XOR muvelet HAMIS")

if __name__ == '__main__':
    main()