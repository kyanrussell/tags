from __future__ import annotations
from typing import Any
from datetime import date
from enum import Enum
from tags.tag_types.location import Location
from tags.tag_types.species_code import SpeciesCode
from tags.types.tag import Tag
from tags.types.photo import Photo
from tags.model.database import con
from sqlite3 import IntegrityError

TAG_TYPES = {
    "SpeciesCode": lambda tag: SpeciesCode[tag],
    "Location": lambda tag: Location[tag],
    "date": lambda tag: date(int(tag[:4]), int(tag[5:7]), int(tag[8:])),
}

def add_tag(photo: Photo, tag: Tag):

    # new_con = sqlite3.connect("tags.db")
    # new_cur = new_con.cursor()
    try:
        res = con.execute(
            f"INSERT INTO tags VALUES ('{type(tag).__name__}', '{tag.name}', '{photo.filepath}')"
        )
        con.commit()
    except IntegrityError:
        pass


def get_photos(tag: Tag):

    # new_con = sqlite3.connect("tags.db")
    # new_cur = new_con.cursor()
    res = con.execute(f"SELECT photo FROM tags WHERE tag = '{tag.name}'")
    return res.fetchall()


def get_tags(photo: Photo):
    res = con.execute(f"SELECT tag_type, tag FROM tags WHERE photo = '{photo.filepath}'")
    return [TAG_TYPES[tag_type](tag) for tag_type, tag in res.fetchall()]

