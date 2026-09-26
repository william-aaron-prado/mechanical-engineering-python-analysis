import math

def screw_area(diameter):
    return math.pi * (diameter**2)/ 4

def stress(force, area):
    return force / area

def factor_of_safety(material_strength, applied_stress):
    return material_strength / applied_stress



print("LEAD SCREW ANALYSIS")
print("-------------------")

diameter = 10, 15, 20, 25, 30, 35, 40
force = 5000
material_strength = 250

for i in diameter:
    area = screw_area(i)
    applied_stress = stress(force, area)
    fos = factor_of_safety(material_strength, applied_stress)

    print()
    print("Cross-sectional area =", area, "mm^2")
    print("Stress =", applied_stress, "MPa")
    print("Factor of Safety =", fos)

    print()
    print("Comparison:")
    print("The Python results should closely match the Day 45 manual calculation")
    print("when using d = 17.4625 mm, F = 5000 N, and strength = 250 MPa.")
