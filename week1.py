#To convert from cartesian to polar coordinates and vice-versa, based on user choice
import numpy as np
import math

def main():
    print("Select from the following:\n1)polar to cartesian\n2)cartesian to polar")
    choice=input()
    coord=input("Enter coordinates as a  comma seperated pair(Either <x,y> or <r,theta>):")
    # print(len(coord))
    coord=coord.split(",")
    print(len(coord))
    print(type(coord))
    if(int(choice)==1):
        # print("entered")
        r,theta=coord
        r=float(r)
        theta=float(theta)
        polar_to_cart(r,theta)
    elif(int(choice)==2):
        # print("entered")
        x,y=coord
        x=float(x)
        y=float(y)
        cart_to_polar(x,y)

def cart_to_polar(x,y):
    r=math.sqrt(x**2+y**2)
    theta=math.atan(y/x)
    print("The values in polar coordinates:")
    print("r:",r)
    print("theta:",theta)


def polar_to_cart(r,theta):
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    print("The values in cartesian coordinates:")
    print("x:",x)
    print("y:",y)
    
if __name__ == "__main__":
    main()