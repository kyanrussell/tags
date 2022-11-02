from tags.tag_types.species_code import SpeciesCode

ALL_SPECIES = [species for species in SpeciesCode]


# Return the Hamming distance between string1 and string2.
# string1 and string2 should be the same length.
def hamming_distance(string1, string2): 
    # Start with a distance of zero, and count up
    distance = 0
    # Loop over the indices of the string
    L = len(string1)
    for i in range(L):
        # Add 1 to the distance if these two characters are not equal
        if string1[i] != string2[i]:
            distance += 1
    # Return the final count of differences
    return distance

def get_top_n_closest_species_codes(input_code: str, n: int):
    """
    Returns the top n SpeciesCodes with the smallest Hamming distance from the input_code
    that also start with same letter.
    """
    assert len(input_code) == 4
    species_distances = [
        (species_code, hamming_distance(input_code, species_code.name))
        for species_code in ALL_SPECIES
        # first letter must be the same
        if species_code.name[0] == input_code[0]
    ]

    sorted_species_distances = sorted(species_distances, key=lambda x: x[1])

    # input_code should always be first
    return [species for species, distance in sorted_species_distances[:n]]
