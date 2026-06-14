import matplotlib.pyplot as plt

def calculate_basical_stats(population):
    # Average fitness is calculated for population
    average_fitness = sum([organism["fitness"] for organism in population]) / len(population)
    # Max fitness value is calculated
    max_fitness = max([organism["fitness"] for organism in population])
    # Min fitness value is calculated
    min_fitness = min([organism["fitness"] for organism in population])
    # Dictionary with stats
    return {
        "average_fitness": average_fitness,
        "max_fitness": max_fitness,
        "min_fitness": min_fitness
    }

def calculate_traits_average(population):
    # Average value for traits
    speed_avg = sum([organism["genome"]["speed"] for organism in population]) / len(population)
    camouflage_avg = sum([organism["genome"]["camouflage"] for organism in population]) / len(population)
    heat_resistance_avg = sum([organism["genome"]["heat_resistance"] for organism in population]) / len(population)
    metabolism_avg = sum([organism["genome"]["metabolism"] for organism in population]) / len(population)
    reproduction_rate_avg = sum([organism["genome"]["reproduction_rate"] for organism in population]) / len(population)
    toxin_resistance_avg = sum([organism["genome"]["toxin_resistance"] for organism in population]) / len(population)
    # Dictionary with traits
    return {
        "speed": speed_avg,
        "camouflage": camouflage_avg,
        "heat_resistance": heat_resistance_avg,
        "metabolism": metabolism_avg,
        "reproduction_rate": reproduction_rate_avg,
        "toxin_resistance": toxin_resistance_avg
    }

def record_generation_data(generation, population, history):
    # Stats are registered for graphics
    stats = calculate_basical_stats(population)
    traits_avg = calculate_traits_average(population)

    # Dictionary with all of the population info
    
    generation_data = {
        "generation": generation + 1,
        "population_size": len(population),
        "stats": stats,
        "traits_average": traits_avg,
    }

    # Information stored
    history.append(generation_data)

def display_results(history):
    # Information extracted for graphics
    generations = [h["generation"] for h in history]
    fitness_history = [h["stats"]["average_fitness"] for h in history]
    population_history = [h["population_size"] for h in history]

    # Fitness graphic
    plt.subplot(1, 2, 1)
    plt.plot(generations, fitness_history, color = "blue")
    plt.title("Evolution of average fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")

    # Population graphic
    plt.subplot(1, 2, 2)
    plt.plot(generations, population_history, color = "green")
    plt.title("Population size")
    plt.xlabel("Generation")
    plt.ylabel("Population")

    # Space is adjusted
    plt.tight_layout()
    # Program is paused till the window is closed 
    plt.show(block=True)

    input("Press Enter to close the graphic and go back to main menu")

def update_dashboard(
    generation,
    population_size,
    average_fitness,
    biome,
    traits_avg,
    edits_remaining
):
    # It cleans the actual figure
    plt.clf()

    plt.suptitle("GENCRAFT STATUS")
    
    # Text displayed on right for user 
    plt.text(
        0.65,
        0.95,
        f"Generation: {generation}",
        transform=plt.gca().transAxes
    )

    plt.text(
        0.65,
        0.90,
        f"Population: {population_size}",
        transform=plt.gca().transAxes
    )

    plt.text(
        0.65,
        0.85,
        f"Average Fitness: {average_fitness:.2f}",
        transform=plt.gca().transAxes
    )

    plt.text(
        0.65,
        0.80,
        f"Biome: {biome}",
        transform=plt.gca().transAxes
    )

    plt.text(
        0.65,
        0.75,
        f"Genetic Interventions Left: {edits_remaining}",
        transform=plt.gca().transAxes
    )

    # List created for graphic to be created
    traits = [
        "Speed",
        "Camouflage",
        "Heat",
        "Metabolism",
        "Reproduction",
        "Toxin"
    ]

    # List created for graphic to be created
    values = [
        traits_avg["speed"],
        traits_avg["camouflage"],
        traits_avg["heat_resistance"],
        traits_avg["metabolism"],
        traits_avg["reproduction_rate"],
        traits_avg["toxin_resistance"]
    ]

    # Bar plot 
    plt.barh(traits, values)

    # Value normalized between 0 - 1
    plt.xlim(0, 1)

    # Space adjusted
    plt.tight_layout()
    
    # Refresh for user to see the changes
    plt.pause(0.01)
