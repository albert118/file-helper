from os.path import splitext

from .BaseValidator import BaseValidator

RELATE_MEDIA_FTYPES = [
    "srt",
    "ssa",
    "ttml",
    "sbv",
    "dfxp",
    "vtt",
    "sub"
]

MOVIE_FTYPES = [
    "mp4",
    "avi",
    "mkv",
    "mov",
    "flv",
    "qt",
    "amv",
    "m4v",
    "svi"
]

def get_ftype(fn: str):
    _, fType = splitext(fn)
    return fType.replace('.', '')

class MovieContent(BaseValidator):
    def is_movie_or_related_content(self):
        ftype = get_ftype(self._data)
        self._is_valid &= ftype in MOVIE_FTYPES or ftype in RELATE_MEDIA_FTYPES
        return self
