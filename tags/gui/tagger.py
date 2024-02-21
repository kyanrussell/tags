import subprocess
from PIL import Image
from time import sleep
from tags.tag_types.species_code import SpeciesCode
from tags.logic.hamming_distance import get_top_n_closest_species_codes
from tags.logic.tags import add_tag, get_photos, get_tags
from tags.types.photo import Photo
from tags.model.database import con
import argparse
import os


def get_species_codes_input(photo: Photo):
    tag = input("Add 4-letter species code? Press [c] to continue. ").upper()

    # TODO: move to InputGetter class with super method to "continue"
    if tag == "C":
        return True
    # TODO: add [l] to list current tags

    suggested_tags = get_top_n_closest_species_codes(tag, 11)
    input_tag = suggested_tags[0]

    if input_tag.name == tag:
        print(f"{input_tag} accepted.")
        add_tag(tag=input_tag, photo=photo)
        return False

    else:
        nl = '\n'
        print(f"tag {tag} invalid. did you mean:{nl}{nl.join(['  - ' + repr(i) for i in suggested_tags[0:6]])}")
        # TODO: PAGINATE MORE SUGGESTIONS
        cont = input("Press [n] for more suggestions, or enter the correct species code.").upper()
        if cont == "N":
            print(f"{nl.join(['  - ' + repr(i) for i in suggested_tags[6:]])}")

        return False


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fpath", help="Input Folder", required=True)
parser.add_argument("-c", "--continue-from", help="File in Input Folder from which to continue tagging")
args = parser.parse_args()


def main():
    # TODO: start from the first photo without any tags
    found_file_to_continue_from = False

    for file in os.scandir(args.fpath):
        if file.is_file() and file.name[0] != ".":
            if args.continue_from and not found_file_to_continue_from and args.continue_from != file.name:
                continue

            found_file_to_continue_from = True

            photo = Photo(f"{file.path}")

            with Image.open(file.path) as img:
                print(f"Currently tagging {photo.filepath}.")
                img.resize([2048,2048], Image.ANTIALIAS)
                img.show()
                sleep(1)
                subprocess.call(['osascript', '-e', 'tell application "iTerm" to activate'])

                while True:
                    if get_species_codes_input(photo=photo):
                        print(f"Done. Summary of added tags for {photo}:")
                        print(get_tags(photo=photo))
                        subprocess.call(['osascript', '-e', 'tell application "Preview" to quit'])
                        break



if __name__ == "__main__":
    main()
    con.close()