import math

def screw_area(diameter):
    return math.pi * diameter**2 / 4

def stress(force, area):
    return force / area

def factor_of_safety(material_strength, applied_stress):
    return material_strength / applied_stress


print("LEAD SCREW ANALYSIS")
print("-------------------")

diameter = float(input("Enter screw diameter (mm): "))
force = float(input("Enter applied force (N): "))
material_strength = float(input("Enter material strength (MPa): "))

area = screw_area(diameter)
applied_stress = stress(force, area)
fos = factor_of_safety(material_strength, applied_stress)

print()
print("Cross-sectional area =", area, "mm^2")
print("Stress =", applied_stress, "MPa")
print("Factor of Safety =", fos)

print()
print("Day 45 Manual Calculation:")
print("Area = 239.7 mm^2")
print("Stress = 20.86 MPa")
print("FoS = 11.98")

print()
print("Comparison:")
print("The Python results should closely match the Day 45 manual calculation")
print("when using d = 17.4625 mm, F = 5000 N, and strength = 250 MPa.")
