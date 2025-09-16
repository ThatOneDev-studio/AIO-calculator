import math #all code made by Joel or ThatOneDev-studio
while True:
    cop = int(input("1 for cube, 2 for prism, 3 for circle, 0 to quit, "))
    if cop == 0:
        print("Exiting")
        break
    elif cop == 1:
        cs1 = float(input("Length: "))
        cs2 = float(input("Width: "))
        cs3 = float(input("Height: "))
        print(cs1 * cs2 * cs3, "^3")
    elif cop == 2:
        base = float(input("Base: "))
        height = float(input("Height: "))
        thirdd = float(input("3rd dimension: "))
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
