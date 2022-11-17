from tags.tag_types.species_code import SpeciesCode
from collections import defaultdict

ALL_SPECIES = [species for species in SpeciesCode]

def generate_tricky_codes():
    """
    Generate special-case codes.
    e.g. Heermann's Gull and Herring Gull have a collision (HEGU), so they have
    special-cased codes (HEEG and HERG respectively).
    """
    tricky_codes = defaultdict(lambda: [])
    for species_code in ALL_SPECIES:
        words = species_code.value.replace('-',' ').split(' ')
        if len(words) == 1:
            code = words[0][:4]
        if len(words) == 2:
            code = words[0][:2] + words[1][:2]
        if len(words) == 3:
            # TODO: support Western Screech-Owl (currently WSOw, not WeSO)
            code = words[0][:1] + words[1][:1] + words[2][:2]
        if len(words) == 4:
            code = words[0][:1] + words[1][:1] + words[2][:1] + words[3][:1]
        code = code.upper()
        if species_code.name != code:
            tricky_codes[code].append(species_code)

    return tricky_codes

TRICKY_CODES = generate_tricky_codes()


def hamming_distance(string1, string2): 
    """
    http://claresloggett.github.io/python_workshops/improved_hammingdist.html#:~:text=Hamming%20distance%20is%20the%20simplest,strings%20are%20the%20same%20lengths.
    Return the Hamming distance between string1 and string2.
    string1 and string2 should be the same length.
    """
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

    trick = TRICKY_CODES[input_code]
    rest = [species for species, distance in sorted_species_distances]
    # input_code should always be first
    return (trick + [code for code in rest if code not in trick])[:n]