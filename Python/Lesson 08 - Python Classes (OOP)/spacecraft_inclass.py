




# class Spacecraft:
#     # current_fuel = 0
#     # fuel_capacity = 100
#     # distance = int(input(f"Enter the distance you wish to travel: "))
    
    
#     def __init__(self, name: str, fuel_level: float, fuel_efficiency: float, distance: float):
#         self.name = name
#         self.fuel_level = fuel_level
#         self.fuel_efficiency = fuel_efficiency
#         self.max_fuel = 200000
        
    
#     # def fuel_efficiency(self):
#     #     distance = float(input(f"Enter the distance you wish to travel: "))
#     #     km_per_unit = 1
#     #     fuel_needed = distance / km_per_unit
#     #     fuel_capacity = 100.0
#     #     if distance > fuel_capacity:
#     #         return f"You don't have enough fuel!"
        
#     #     return f"Fuel needed: {fuel_needed}, units (efficiency: {km_per_unit})"
        
        
       
#     def add_fuel(self, amount: float):
#         self.fuel_level = min(self.max_fuel, self.fuel_level + amount)
#         self.fuel_level = max(self.fuel_level, 0)
        
    
#     def fuel_req(self, distance):
#         amount = distance / self.fuel_efficiency
        
#         return amount
    
#     def fuel_available(self, distance):
#         return self.fuel_level >= self.fuel_req(distance)
    
    
#     def launch(self, distance):
        
#         if self.fuel_available(distance):
#             self.fuel_level -= self.fuel_req(distance)
#             print(f"launched {self.name} {distance} kilometers")
#         else:
#             print(f"Not enough fuel")
        
    
#     # def fuel_deduct():
#     #     pass
    
# sp1 = Spacecraft("Vostok 1", 250, 1.5)
# sp2 = Spacecraft("Voyager 1", 400, 2.0)

