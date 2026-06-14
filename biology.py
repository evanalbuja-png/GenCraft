import random

def create_genome():
    # A random number between 0 - 1 generates for every organism characteristic
    speed = random.random()
    camouflage = random.random()
    heat_resistance = random.random()
    metabolism = random.random()
    reproduction_rate = random.random()
    toxin_resistance = random.random()

    # Dictionary with all the characteristics
    return {
        "speed": speed, 
        "camouflage": camouflage, 
        "heat_resistance": heat_resistance,
        "metabolism": metabolism, 
        "reproduction_rate": reproduction_rate, 
        "toxin_resistance": toxin_resistance,
    }

def create_organism():
    # Characteristics of the organism
    age = 0 
    fitness = 0
    alive = True
    genome = create_genome() # Genome of the organism
    # Library with the characteristics of the organism
    return {
        "age": age,
        "fitness": fitness,
        "alive": alive,
        "genome": genome
    }

def compute_fitness(organism, environment):
    # How temperature affects the organism
    heat_score = 1 - abs(organism["genome"]["heat_resistance"] - environment["temperature"])
    # How toxins in the environment affects the organism
    toxin_score = 1 - abs(organism["genome"]["toxin_resistance"] - environment["toxin_level"])
    # How metabolism affects the need for food 
    food_score = 1 - abs(organism["genome"]["metabolism"] - environment["food_density"])
    # How predators can hunt organisms
    predator_score = 1 - abs((organism["genome"]["speed"] + organism["genome"]["camouflage"]) / 2 - environment["predator_pressure"])
    # Average of scores for fitness
    fitness = (heat_score + toxin_score + food_score + predator_score) / 4
    # Reproduction affects fitness
    fitness *= (1 - organism["genome"]["reproduction_rate"] * 0.3)
    # Fitnes is normalized between 0 - 1
    return max(0, min(1, fitness))

def create_population(size, environment):
    # New empty list to storage organisms
    population = []
    # New organism generated for every individual
    for i in range(size):
        organism = create_organism()
        fitness = compute_fitness(organism, environment)
        organism["fitness"] = fitness
        # Organism is added to the list
        population.append(organism)
    # List with all of the organisms
    return population

def evaluate_population(population, environment):
    # Fitness is evaluated for every organism in population
    for organism in population:
        fitness = compute_fitness(organism, environment)
        organism["fitness"] = fitness
    # It returns population with the new fitness value
    return population

def select_survivors(population):
    # Empty list with survivors
    survivors = []
    # It analyzes organisms that will survive depending on fitness
    for organism in population:
        random_number = random.random()
        if random_number < organism["fitness"]:
            survivors.append(organism)
    # List with survivors
    return survivors

def age_and_remove_dead(survivors):
    # It ages survivors an kills the ones that are too old
    alive = []
    for org in survivors:
        org["age"] += 1
        # Max age of 20
        if org["age"] >= 20:
            org["alive"] = False
        else:
            alive.append(org)
    #List with alive organisms
    return alive

def reproduce_next_gen(survivors, environment):
    # Survivors reproduce for next generation
    next_gen = []
    for organism in survivors:
        # Probability is dependent on rate and food
        reproduction_probability = (organism["genome"]["reproduction_rate"] * environment["food_density"])
        if random.random() < reproduction_probability:
            offspring = create_organism()
            offspring["age"] = 0
            # Asexual reproduction
            offspring["genome"] = organism["genome"].copy() # El organismo hijo hereda el genoma del organismo padre
            # Mutation is added
            mutate_genome(offspring["genome"]) # Se muta el genoma del organismo hijo
            #List with next gen
            next_gen.append(offspring)
    return next_gen

def mutate_genome(genome):
    # Probability of 10% for mutation
    mutation_rate = 0.1
    for key in genome:
        if random.random() < mutation_rate:
            genome[key] = random.random()  
    # It returns list with mutated organisms
    return genome