# Vacuum Cleaner Problem

def vacuum_cleaner(env, start):
    location = start
    cost = 0
    
    print("Initial Environment:", env)
    
    while "Dirty" in env.values():
        print("\nVacuum at:", location)
        
        if env[location] == "Dirty":
            print("Cleaning", location)
            env[location] = "Clean"
            cost += 1
        else:
            print(location, "is already clean")
        
        # Move to the other location
        if location == "A":
            location = "B"
        else:
            location = "A"
        cost += 1
    
    print("\nFinal Environment:", env)
    print("Performance Cost:", cost)

# Example Environment
environment = {"A": "Dirty", "B": "Dirty"}

# Start at location A
vacuum_cleaner(environment, "A")
