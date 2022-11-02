from __future__ import annotations
from typing import Any
from datetime import date
from enum import Enum
from tags.tag_types.location import Location
from tags.tag_types.species_code import SpeciesCode
from tags.types.tag import Tag
from tags.types.photo import Photo

PHOTOS: dict[Photo, [Tag]] = {}
LOCATIONS: dict[Location: [Photo]] = {}
DATES: dict[date: [Photo]] = {}
SPECIES_CODES: dict[SpeciesCode: [Photo]] = {}

TAG_TYPE_TO_TAGS: dict[Any, dict[Tag, [Photo]]] = {
	Location: LOCATIONS,
	date: DATES,
	SpeciesCode: SPECIES_CODES,
}


def add_tag(photo: Photo, tag: Tag):
	tags: dict[Tag, [Photo]] = TAG_TYPE_TO_TAGS[type(tag)]
	tagged_photos: [Photo] = tags.get(tag)
	if tagged_photos:
		tagged_photos.append(photo)
	else:
		tags[tag] = [photo]

	photo_tags: [Tag] = PHOTOS.get(photo)
	if photo_tags:
		photo_tags.append(tag)
	else:
		PHOTOS[photo] = [tag]
	# TODO: write to log
	# print(f"added {tag}: {photo}")


def get_photos(tag: Tag):
	tags: dict[Tag, [Photo]] = TAG_TYPE_TO_TAGS[type(tag)]
	tagged_photos: [Photo] = tags.get(tag)
	return tagged_photos


def get_tags(photo: Photo):
	return PHOTOS.get(photo)

