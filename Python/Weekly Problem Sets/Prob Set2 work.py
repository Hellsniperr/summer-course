# def pizzas_needed(people, slices_per_person, slices_per_pizza):

#     total_slices_needed = people * slices_per_person
#     pizzas = total_slices_needed // slices_per_pizza
#     if total_slices_needed % slices_per_pizza != 0:
#         pizzas += 1
#     return pizzas

# def leftover_slices(people, slices_per_person, slices_per_pizza):
#     total_slices_needed = people * slices_per_person
#     pizzas = total_slices_needed // slices_per_pizza
#     if total_slices_needed % slices_per_pizza != 0:
#         pizzas += 1
#     total_slices = pizzas * slices_per_pizza
#     return total_slices - total_slices_needed

# people = int(input("Enter the number of people: "))
# slices_per_person = int(input("Enter the number of slices per person: "))
# slices_per_pizza = int(input("Enter the number of slices per pizza: "))

# # print("Pizzas needed:", pizzas_needed(people, slices_per_person, slices_per_pizza))
# total_pizzas = pizzas_needed(people, slices_per_person, slices_per_pizza)
# total_slices = total_pizzas * slices_per_pizza
# leftover = leftover_slices(people, slices_per_person, slices_per_pizza)



# row1 = f"=== PARTY SUMMARY ==="
# row2 = f"Guests:            {people}"
# row3 = f"Pizzas to order:   {total_pizzas}"
# row4 = f"Total slices:      {total_slices}"
# row5 = f"Leftover slices:   {leftover}"


# print(row1)
# print(row2)
# print(row3)
# print(row4)
# print(row5)



# Problem 2

# def o2_status(level):
#     if level >= 23:
#         return "HIGH"
#     elif level >= 19 and level <= 23:
#         return "NORMAL"
#     elif level >= 15 and level <= 18:
#         return "LOW"
#     else:
#         return "CRITICAL"

# readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]

# counts = {"HIGH": 0, "NORMAL": 0, "LOW": 0, "CRITICAL": 0}

# for hour, level in enumerate(readings, start=1):
#     status = o2_status(level)
#     counts[status] += 1
#     if status == "CRITICAL":
#         print("*** ALERT: TAKE ACTION IMMEDIATELY ***")
#     print(f"Hour: {hour} - Level: {level}% - Status: {status}")


# print()
# print("=== SUMMARY ===")
# print(f"HIGH: {counts['HIGH']} hours")
# print(f"NORMAL: {counts['NORMAL']} hours")
# print(f"LOW: {counts['LOW']} hours")
# print(f"CRITICAL: {counts['CRITICAL']} hours")

#problem 3

# def attack(defender_hp: int, damage: int) -> int:
#     new_hp = defender_hp - damage
#     if new_hp < 0:
#         return 0
#     return new_hp

# def is_alive(hp: int) -> bool:
#     return hp > 0

# defender_hp = 100
# monster_hp = 90 
# damage_hero = 18
# damage_mon = 12
# round = 0


# while is_alive(defender_hp) and is_alive(monster_hp):
#     round += 1

#     monster_hp = attack(monster_hp, damage_hero)

#     if is_alive(monster_hp):
#         defender_hp = attack(defender_hp, damage_mon)
#     print(f"Round {round}: Hero HP = {defender_hp}, Monster HP = {monster_hp}")

# if is_alive(defender_hp):
#     print("Hero wins!")
# else:
#     print("Monster wins!")


# # Problem 4


# def check_fitness(score):
#     """Cleared if score >= 70."""
#     return score >= 70

# def check_rank(rank):
#     """Cleared if rank is 'Corporal', 'Sergeant', or 'Lieutenant'."""
#     return rank in ['Corporal', 'Sergeant', 'Lieutenant']

# def check_service_years(years):
#     """Cleared if years >= 2."""
#     return years >= 2


# def mission_clear(status: bool) -> str:
#     if status:
#         return "MISSION CLEAR"
#     else:
#         return "MISSION FAILED"

# name = input("Enter your name: ")
# score = int(input("Enter your fitness score: "))
# rank = input("Enter your rank: ")
# years = int(input("Enter your years of service: "))

# status = check_fitness(score) and check_rank(rank) and check_service_years(years)
# print(f"{name}: {mission_clear(status)}")



# Problem 5

athletes = [
    ("Jordan",  82, 15),   # (name, games_played, goals_scored)
    ("Patel",   78, 22),
    ("Okonkwo", 90, 18),
    ("Li",      65, 9),
    ("Reyes",   88, 31),
    ("Fischer", 72, 14),
]

def goals_per_game(goals, games):
    if games == 0:
        return 0.0
    return round((goals / games), 2)

def mvp_candidate(gpg):
    if gpg >= 0.25:
        return True
    return False

top_name = None
top_goals = -1

for name, games, goals in athletes:
    gpg = goals_per_game(goals, games)
    marker = "*" if mvp_candidate(gpg) else ""
    if mvp_candidate(gpg):
        print(f"{name} is an MVP candidate with {gpg} goals per game.")
    if goals > top_goals:
        top_goals = goals
        top_name = name

print(f"Top scorer: {top_name} with {top_goals} goals.")