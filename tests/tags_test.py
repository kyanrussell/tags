import pytest
from datetime import date
from enum import Enum
from tags.tag_types.location import Location
from tags.tag_types.species_code import SpeciesCode
from tags.types.tag import Tag
from tags.types.photo import Photo
from tags.logic.tags import add_tag, get_photos


def test_basic():
	foo = Photo("foo")
	bar = Photo("bar")
	add_tag(foo, date(2022,1,1))
	add_tag(foo, SpeciesCode.WEGU)
	add_tag(bar, SpeciesCode.WEGU)
	add_tag(bar, Location.MONTEREY_BAY)


	assert get_photos(SpeciesCode.WEGU) == [foo, bar]