from tags.tag_types.species_code import SpeciesCode
from tags.logic.tags import add_tag, get_photos, get_tags
from tags.types.photo import Photo
from tags.model.database import con
from tags.logic.hamming_distance import ALL_SPECIES
from tags.logic.hamming_distance import get_top_n_closest_species_codes
from tags.logic.hamming_distance import generate_tricky_codes

def main():
    import pdb;pdb.set_trace()
if __name__ == "__main__":
    main()
    con.close()
