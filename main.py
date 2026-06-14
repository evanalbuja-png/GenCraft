import matplotlib.pyplot as plt
from biology import *
from environment import *
from genetics import *
from visualization import *

def run_simulation(environment):
    # User can only edit the genes 5 times
    gene_edits_remaining = 5
    # It starts with a population of 100
    population = create_population(100, environment)
    # Calculation of stats
    stats = calculate_basical_stats(population)
    traits_avg = calculate_traits_average(population)
    # Figures are updated automatically while program is running
    plt.ion()
    # New figure window
    plt.figure(figsize=(8, 6))

    history = [] # List to storage the stats history

    print(f"An environment of type {environment['type']} has been created")

    # Main loop for simulation
    for generation in range(100):
        print(f"\nGeneratio {generation + 1} - Population: {len(population)}")
        traits_avg = calculate_traits_average(population)

        #Dashboard is updated on every generation
        update_dashboard(
            generation + 1,
            len(population),
            stats["average_fitness"],
            environment["type"],
            traits_avg,
            gene_edits_remaining
        )
        # 1. Evaluate the organisms
        population = evaluate_population(population, environment)
        
        #  Basic stats are storaged
        record_generation_data(generation, population, history)
        print(f"Average fitness: {stats['average_fitness']:.2f}, Max fitness: {stats['max_fitness']:.2f}, Min fitness: {stats['min_fitness']:.2f}")
        
        # 2. Select survivors
        survivors = select_survivors(population)

        # Aging
        survivors = age_and_remove_dead(survivors)
        print(f"Survivors: {len(survivors)}")

        # 3. Reproduction
        offspring = reproduce_next_gen(survivors, environment)
        population = survivors + offspring
        population_size = len(population)
        # Dynamic food to avoid overpopulation
        food_consumed = population_size * 0.00001 # Every organism consumes some food

        environment["food_density"] = max(0, environment["food_density"] - food_consumed) # Food is consumed
        environment["food_density"] = min(1, environment["food_density"] + 0.05) # Food is regenerated

        # 4. Random event
        if generation % 10 == 0:
            trigger_random_event(environment) # Every 10 generations, there is a chance for this to happen

        # 5. Gene editing

        if generation % 10 == 0:
            if gene_edits_remaining > 0:
                print(f"\nRemaining genetic interventions: {gene_edits_remaining}")
                edit = input("Do you want to edit a trait? (y/n):")
                if edit.lower() == 'y':
                    gene_edits_remaining = apply_restricted_gene_edit(population, gene_edits_remaining)
                else:
                    print("\nNo genetic editions applied.")
                
        
        # 6. Verify extinction
        if len(population) == 0:
            print("The population has gone extinct!")
            break

    # Print final results
    print("FINAL RESULTS")
    print(f"Biome: {environment['type'].upper()}")

    # Survived generations are determined
    if len(population) == 0:
        survived_generations = generation + 1
        result = "DEFEAT"
        message = "EXTINCTION"
    else:
        survived_generations = 100
        result = "VICTORY"
        message = "SURVIVING SPECIES"
    
    # Info for user 
    print(f"Survived generations: {survived_generations}")
    print(f"Final population: {len(population)}")

    # Final stats
    if len(population) > 0:
        final_stats = calculate_basical_stats(population)
        print(f"Final average fitness: {final_stats["average_fitness"]:.2f}")
    else:
        print("Final average fitness: N/A (extint population)")
    
    print(f"\nResult: {message}")
    print(f" {result}")

    # Graphics generation
    if len(history) > 0:
        print("Generating graphics...")
        plt.close()
        display_results(history)
    else: 
        print("No data to graphic")


def show_main_menu():
    # Main menu for user
    print("GENCRAFT")
    print("1. New simulation")
    print("2. See instructions")

def show_instructions():
    # General instructions
    print("GENCRAFT INSTRUCTIONS")
    print("You manage a population of organisms in a hostile biome.")
    print("Each generation's fitness is evaluated.")
    print("The fittest survive and reproduce.")
    print("You can edit genes every 10 generations for 5 times.")
    print("Survive 100 generations or avoid extinction.")
    print("\nGood luck evolving your species!")

def select_biome():
    # Biome selection for user
    print("\nSelect biome:")
    print("1. Savanna")
    print("2. Artic")
    print("3. Toxic Swamp")
    print("4. Deep Forest")

    while True:
        # In case user makes an invalid selection
        choice = input("\nEnter the biome number (1–4):")
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("Invalid selection. Please choose a number between 1 and 4.")

def main():
    while True:
        # Main function for program
        show_main_menu()
        option = input("Select an option (1–2):")

        if option == "1":
            biome_choice = select_biome()
            environment = create_environment(biome_choice)
            run_simulation(environment)
        
            input("\nPress Enter to return to the main menu...")
        
        elif option == "2":
            show_instructions()
            input("Press Enter to return to continue...")

        else:
            print("Invalid option. Try again.")
            
if __name__ == "__main__":
    main()