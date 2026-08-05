# Problem 1

from os import name


reports = [
    "SANTOS | Private | Fitness:91 | Status:available",
    "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
    "OKAFOR | Sergeant | Fitness:88 | Status:available",
    "BRIGGS | Private | Fitness:55 | Status:available",
    "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
    "REYES | Sergeant | Fitness:79 | Status:available",
]

class Soldier():
    def __init__(self, name, rank, fitness, deployed):
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    def dispatch(self) -> None:
        self.deployed = True

    def __str__(self):
        return f"{self.name}, {self.rank}, Fitness: {self.fitness}, Deployed: {self.deployed}"

def process_reports(reports):
    roster = {}
    ranks = set()

    for report in reports:
        name, rank, fitness_str, status_str = report.split(" | ")
        fitness = int(fitness_str.split(":")[1]) #split the fitness string to get the number. split outputs a list, so we take the second element of the list (index 1)
        deployed = status_str.split(":")[1].strip().lower() == "deployed" #split the status string to get the status. split outputs a list, so we take the second element of the list (index 1). Then we check if it is equal to "deployed"
        name = name.title()
        rank = rank.upper()
            
        soldier = Soldier(name, rank, fitness, deployed)
        roster[name] = soldier
        ranks.add(rank)
    return roster, ranks


def show_available(roster):
    available = []

    for soldier in roster.values():
        if not soldier.deployed:
            available.append(soldier.name)

    available.sort()
    print(f"Available soldiers: {available}")

def dispatch(roster, name):
    name = name.title()

    if name in roster:
        soldier = roster[name]
        if soldier.deployed:
            print(f"{name} is already deployed.")
        else:
            soldier.dispatch()
            print(f"{name} has been dispatched.")
    else:
        print(f"{name} not found or unavailable.")


# Problem 2

recipe_data = {
    "omelette":        ["eggs", "butter", "salt", "pepper", "cheese"],
    "pancakes":        ["flour", "eggs", "milk", "butter", "sugar", "salt"],
    "tomato pasta":    ["pasta", "tomatoes", "garlic", "olive oil", "salt", "pepper"],
    "grilled cheese":  ["bread", "cheese", "butter"],
}

pantry_items = ["eggs", "butter", "salt", "pepper", "cheese", "milk", "bread", "garlic"]

class Recipe():
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def can_make(self,pantry_set):
        if set(self.ingredients).issubset(pantry_set):
            return True
        else:
            return False

    def missing_ingredients(self,pantry_set):
        missing = set(self.ingredients) - pantry_set
        return sorted(list(missing))

class Pantry():
    def __init__(self, items):
        self.items = set(items)

    def add_ingredients(self, extra_ingredients):
        for ingredient in extra_ingredients:
            self.items.add(ingredient)

    def has(self, ingredient):
        return ingredient in self.items

    def get_items(self) -> set[str]:
        return self.items

def create_recipes(recipe_data):
    recipes = []
    for name, ingredients in recipe_data.items():
        recipes.append(Recipe(name, ingredients))
    return recipes

def check_recipes(recipes, pantry):
    pantry_set = pantry.get_items()
    for recipe in recipes:
        if recipe.can_make(pantry_set):
            print(f"You can make {recipe.name}.")
        else:
            missing = recipe.missing_ingredients(pantry_set)
            print(f"You cannot make {recipe.name}. Missing ingredients: {missing}")
    all_ingredients = set()
    for recipe in recipes:
        all_ingredients.update(recipe.ingredients)

    sorted_ingredients = sorted(all_ingredients)
    print(f"All unique ingredients ({len(sorted_ingredients)}): {sorted_ingredients}")


# Problem 3

class LyricAnalyzer():
    def __init__(self, lyrics):
        self.lyrics = lyrics

        parsed_lyrics = lyrics.lower()
        parsed_lyrics = parsed_lyrics.replace("\n", " ")

        self.words = parsed_lyrics.split()

    def count_words(self):
        word_count = {}
        for word in self.words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        return word_count

    def unique_word_count(self):
        return len(set(self.words))

    def most_common_word(self):
        counts = self.count_words()

        best_word = None
        best_count = 0

        for word, count in counts.items():
            if count > best_count:
                best_word = word
                best_count = count

        return best_word, best_count




if __name__ == "__main__":

    pass