from .MovieContent import MovieContent
from .Deletion import Deletion


def validatated_movie_content(data):
    return (
        MovieContent(data)
        .is_typed()
        .is_non_empty()
        .is_movie_or_related_content()
        .is_valid()
    )


def validated_meda_junk_deletion(data, remove_custom_cover_photo=False):
    return (
        Deletion(data)
        .is_typed()
        .is_non_empty()
        .is_garbage_type()
        .is_known_garbage()
        .is_known_garbage_media()
        .is_custom_cover_photo(remove_custom_cover_photo)
        .is_valid()
    )


def validated_deletion(data, garbage_ftypes: list):
    return (
        Deletion(data)
        .is_typed()
        .is_non_empty()
        .is_valid()
        .is_given_garabage_type(garbage_ftypes)
    )
