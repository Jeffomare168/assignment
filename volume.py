from math import pi

radius = float(input("Enter the radius of the sphere: "))

def volume(r):
    vol = (4.00/3.00)*pi*r**3
    return float(vol)

print(volume(radius))