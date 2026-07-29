
import random
import math
import turtle


# def roll(sides):
#     return random.randint(1, sides)

# # # roll_d = roll(6)

# # # print(roll_d)

# def roll_many(num_dice, sides):
#     results = []
#     for _ in range(num_dice):
#         results.append(roll(sides))
#     return results

# # sides = int(input("Enter the number of sides on the dice: "))
# # num_dice = int(input("Enter the number of dice to roll: "))
# # rolls = roll_many(num_dice, sides)

# # print(rolls)

# print("=== Movement Check (2d6) ===")
# movement = roll_many(2, 6)
# print(f"Rolls: {movement}")
# print(f"Total: {sum(movement)}")
# print()

# print("=== Attack Check (1d20) ===")
# attack = roll(20)
# if attack == 20:
#     print("CRITICAL HIT!")
# elif attack == 1:
#     print("CRITICAL MISS!")
# else:
#     print(f"Result: {attack}")
# print()

# print("=== Damage Roll (3d8) ===")
# damage = roll_many(3, 8)
# total = sum(damage)
# average = round(total / len(damage), 1)
# print(f"Rolls: {damage}")
# print(f"Total: {total}")
# print(f"Average: {average}")
# print()



# Problem 2


# def distance(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# def orbit_circumference(radius):
#     return 2 * math.pi * radius

# def fuel_needed(mass, velocity):
#     return math.floor(0.5 * mass * velocity ** 2) / 100


# ship_pos    = (0, 0)
# station_pos = (143, 892)
# orbit_radius = 6371        # km (Earth's radius)
# ship_mass    = 50000       # kg
# ship_velocity = 7800       # m/s

# print("Distance to station:", distance(*ship_pos, *station_pos))
# print("Orbit circumference:", orbit_circumference(orbit_radius))
# print("Fuel needed:", fuel_needed(ship_mass, ship_velocity))


# Problem 3


# t = turtle.Turtle()

# t.circle(50)


# Problem 4

secret_number = random.randint(1, 100)
count = 0
while True:
       
    guess = int(input("Guess the secret number (1-100): "))
    if math.fabs(guess - secret_number) > 40:
        print("ICE COLD")
    elif math.fabs(guess - secret_number) > 20:
        print("COLD")
    elif math.fabs(guess - secret_number) > 10:
        print("WARM")
    else:
        print("HOT")
    count += 1