def apply_gene_edit(population, trait, new_value):
    # User can edit specific trait
    edited_count = 0
    old_values = []
    for organism in population:
        if trait in organism["genome"]:
            old_values.append(organism["genome"][trait])
            organism["genome"][trait] = max(0, min(1, new_value)) # New value is normalized between 0 - 1
            edited_count += 1
    old_average = sum(old_values) / len(old_values)
    # Information displayed for user
    print(f"The '{trait}' has been edited in {edited_count} organisms. The previous value was {old_average:.2f} and the new value is {new_value:.2f}.")
    return population

def apply_restricted_gene_edit(population, edits_left):
    trait = input("Enter the trait to edit (speed, camouflage, heat_resistance, metabolism, reproduction_rate, toxin_resistance): ")

    # Calculate the actual trait average
    all_values = [org["genome"][trait] for org in population if trait in org["genome"]]
    
    # In case no organisms are available.
    if len(all_values) == 0:
        print("No organisms available for genetic editing.")
        return edits_left
    
    average_value = sum(all_values)/len(all_values)

    # Define limits
    min_allowed = max(0, average_value - 0.2)
    max_allowed = min(1, average_value + 0.2)
    
    # Displayed information for user
    print(f"Actual average value: {average_value:.2f}")
    print(f"Available range: {min_allowed:.2f} to {max_allowed:.2f}")

    # It tries in case of invalid input
    try:
        new_value = float(input("Enter new value: "))
        # Limit for user edition (fair game condition)
        if min_allowed <= new_value <= max_allowed:
            # Function for gene editing
            apply_gene_edit(population, trait, new_value)
            print("Genetic change applied.")
            return edits_left - 1
        else:
            print(f"Rejected edition. Value must be between {min_allowed:.2f} and {max_allowed:.2f}")
            return edits_left
        
    except ValueError:
        print("Invalid input")
        return edits_left