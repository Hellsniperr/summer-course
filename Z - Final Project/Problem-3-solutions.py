import math

def area_circle(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

def equal_tri_pizza(side):
    return (math.sqrt(3) / 4) * side ** 2

def area_square(side):
    return side ** 2

# Automatron 1

a1_area = 2 * area_circle(15)
a1_dough = 20
a1_eff = a1_area / a1_dough

#Automatron 2

a2_area = equal_tri_pizza(20)
a2_dough = 20
a2_eff = a2_area /a2_dough

#Automatron 3

a3_area = area_square(18)
a3_dough = 18
a3_eff = a3_area / a3_dough

print(f"Automatron 1: {a1_area:.2f} sq in, {a1_eff:.2f} sq in per unit dough")
print(f"Automatron 2: {a2_area:.2f} sq in, {a2_eff:.2f} sq in per unit dough")
print(f"Automatron 3: {a3_area:.2f} sq in, {a3_eff:.2f} sq in per unit dough")


results = {
    "Automatron 1": a1_eff,
    "Automatron 2": a2_eff,
    "Automatron 3": a3_eff,
}

winner = max(results, key=results.get)

print(f"\nMost efficient: {winner} ({results[winner]:.2f} sq in per unit dough)")