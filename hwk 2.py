p="Do you wish to continue(Y/N):"
e=""
active=True
while active:
    e=input(p)
    r=e.upper()
    if r=="N":
        active=False
        print("Ending...")
    else:
        varA=input("varA:")
        varB=input("varB:")
        if varA or varB is int:
            if varA>varB:
                print("bigger")
            elif varA<varB:
                print("smaller")
            else:
                print("equal")
        else:
            print("string involved")
        

        

