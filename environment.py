import random

def create_environment(biome_choice):
    # It lets the user choose the environment
    choice = str(biome_choice)
    # Numbers chosen to be a fair game
    if choice == 1:
        return {
            "type": "savanna",
            "temperature": 0.8,
            "food_density": 0.90,
            "predator_pressure": 0.80,
            "toxin_level": 0
        }
        
    elif choice == 2:
        return {
            "type": "artic",
            "temperature": 0.85,
            "food_density": 0.30,
            "predator_pressure": 0.30,
            "toxin_level": 0
        }
    elif choice == 3:
        return {
            "type": "toxic swamp",
            "temperature": 0.40,
            "food_density": 0.70,
            "predator_pressure": 0.20,
            "toxin_level": 0.85
        }
    
    elif choice == 4:
        return {
            "type": "deep forest",
            "temperature": 0.30,
            "food_density": 0.80,
            "predator_pressure": 0.85,
            "toxin_level": 0.20
        }
    
    else:
        print("Invalid biome, using Savanna by default.")
        return {
            "type": "savanna",
            "temperature": 0.9,
            "food_density": 0.8,
            "predator_pressure": 0.9,
            "toxin_level": 0.1
        }

def trigger_random_event(environment):
    if random.random() < 0.5: # 50% chance of a random event happening
        # Random event is simulated
        event_type = random.choice(["heat_wave", "toxin_spill", "predator_invasion", "food_boom"])
        if event_type == "heat_wave":
            environment["temperature"] = min(1, environment["temperature"] + 0.2) # Environment temperature is increased
            print("Heat wave! The environment temperature has increased.")
        elif event_type == "toxin_spill":
            environment["toxin_level"] = min(1, environment["toxin_level"] + 0.2) # Environment toxins are increased 
            print("Toxin spill! The toxin level in the environment has increased.")
        elif event_type == "predator_invasion":
            environment["predator_pressure"] = min(1, environment["predator_pressure"] + 0.2) # Predator pressure is increased
            print("Predator invasion! Predator pressure in the environment has increased.")
        elif event_type == "food_boom":
            environment["food_density"] = min(1, environment["food_density"] + 0.2) # Food density is increased
            print("Food boom! Food density in the environment has increased.")
