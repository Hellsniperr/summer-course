### Planet Class

class Planet():
    def __init__(self, name, coordinates, danger, resources, atmosphere):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere
        
    # def planet_name(self, name):
    #     self.name = name
        
    # def planet_loc(self, coordinates):
    #     self.coordinates = coordinates
        
    # def difficulty(self, danger):
    #     if danger == 5:
    #         print(f"This planet will be near impossible")
    #     elif danger >=3:
    #         print(f"This planet will be a challenge")
    #     elif danger >=1:
    #         print(f"The planet shouldn't be too bad")
    #     else:
    #         print(f"This will be a cake walk")
            
    # def 
        
    def __str__(self) -> str: # This is for printing the planet summary
        return f"The planet is called {self.name}. {self.name} is located at {self.coordinates} and contains {self.resources}. The planet is {self.danger} level of difficulty and has a(an) {self.atmosphere} atmosphere."
    
    def __sub__(self, other) -> float:  #calculating distance
        if not isinstance(other, Planet):# input validation
            raise TypeError("Must only subtract planets")
        
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates
        
        return ((x1 - x2) **2 + (y1 -y2) **2 + (z1 -z2) ** 2) ** (1/2)
    
if __name__ == "__main__":
    p1 = Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")
    p2 = Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin")
    print(p1)