from tags.types.photo import Photo
from tags.logic.tags import get_photos
from tags.logic.hamming_distance import get_top_n_closest_species_codes
from tags.model.database import con

nl = '\n'

def get_species_codes_input():
    tag = input("Add 4-letter species code? Press [c] to continue. ").upper()

    suggested_tags = get_top_n_closest_species_codes(tag, 11)
    input_tag = suggested_tags[0]

    if input_tag.name == tag:
        print(f"{input_tag} accepted.")
        return input_tag

    else:
        nl = '\n'
        print(f"tag {tag} invalid. did you mean:{nl}{nl.join(['  - ' + repr(i) for i in suggested_tags[0:6]])}")
        # TODO: PAGINATE MORE SUGGESTIONS
        cont = input("Press [n] for more suggestions, or enter the correct species code.").upper()
        if cont == "N":
            print(f"{nl.join(['  - ' + repr(i) for i in suggested_tags[6:]])}")

        return False


def main():

    while True:
        species_code = get_species_codes_input()

        photos = get_photos(tag=species_code)
        print(f"Photos tagged with {species_code}:{nl}{nl.join(['  - ' + repr(i) for i in photos])}")
        


if __name__ == "__main__":
    main()
    con.close()