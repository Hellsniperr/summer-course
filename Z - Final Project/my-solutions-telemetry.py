def user_input()-> None: 
    get_telemetry = input("Miles above Mars or Kilometers above Mars: ")

    if get_telemetry == "Miles above Mars":
        user_input_miles = float(input("Enter your current miles above Mars: "))
        output_yds = f"There are {user_input_miles * 1760} yards in {user_input_miles} miles"
        output_feet = f"There are {user_input_miles * 5280} feet in {user_input_miles} miles"
        output_inches = f"There are {user_input_miles * 63360} inches in {user_input_miles} miles"
        
        print(output_yds)
        print(output_feet)
        print(output_inches)
    
    else:
        user_input_km = float(input("Enter your current KM above Mars: "))
        output_m = f"There are {user_input_km * 1000} meters in {user_input_km} KMs"
        output_cm = f"There are {user_input_km * 100000} centimeters in {user_input_km} KMs"
        output_mm = f"There are {user_input_km * 1000000} millimeters in {user_input_km} KMs"
        
        print(output_m)
        print(output_cm)
        print(output_mm)
    
user_input()