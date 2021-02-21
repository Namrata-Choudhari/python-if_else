water=int(input("Enter the water in Filter-"))
if water<1L:
    print("We have to fill water")
elif water<=10:
    print("We don't have to fill water")
elif water>10:
    print("Water will overflow")