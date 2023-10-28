import sys

from phone.model import Mobile, Phone


def main()->None:
    if len(sys.argv)<=1:
        raise ValueError("Nincs argumentum")
    n=int(sys.argv[1])

    result=[]
    for i in range(n):
        line=input()
        tokens=line.split(";")

        if len(tokens)==3:
            phone=Mobile(tokens[0], tokens[1], int(tokens[2]))

            result.append(phone)

        else:
            result.append(Phone(tokens[0], tokens[1], int(tokens[2]), int(tokens[3])))

    result.sort()
    for phone in result:
        print(phone)

    print(Mobile.before(result))

if __name__ == '__main__':
    main()
    print("end")
    print("*", Mobile.count)



