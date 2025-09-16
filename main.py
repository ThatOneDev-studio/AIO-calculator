import math #all code made by Joel or ThatOneDev-studio
while True:
    cop = int(input("1 for cube, 2 for prism, 3 for circle, 0 to quit, "))
    if cop == 0:
        print("Exiting")
        break
    elif cop == 1:
        cs1 = int(input("Length: "))
        cs2 = int(input("Width: "))
        cs3 = int(input("Height: "))
        print(cs1 * cs2 * cs3, "^3")
    elif cop == 2:
        base = int(input("Base: "))
        height = int(input("Height: "))
        thirdd = int(input("3rd dimension: "))
        x = base * height
        y = x / 2
        vol = y * thirdd
        print(vol, "^3")
    elif cop == 3:
        pi = math.pi
        dia = float(input("What is the diameter? ")) 
        rad = dia / 2
        radtwo = rad * rad
        area = pi * radtwo
        print(area)
    else:
        print("Invalid choice.")
