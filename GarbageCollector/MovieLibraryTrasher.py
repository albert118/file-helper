from FileValidation.ValidationRecipes import validatated_movie_content, validated_meda_junk_deletion
import logging
from os import listdir, mkdir
from os.path import isfile, join
from shutil import move

_logger = logging.getLogger(__name__)

LOG_LVL = logging.DEBUG

# GIVEN a director of many potential files
# FIRST determine all potential files
# THEN assert they are valid files
#   valid: non-empty, exists, typed
# AND IF it is "trash"
# THEN it is moved to an archived
#   archive: a temp folder allowing review before final deletion


def setup_logger():
    logging.basicConfig(level=LOG_LVL)
    return logging.getLogger(__name__)


class MovieLibraryTrasher:
    def __init__(self):
        setup_logger()

        self._archive_dir = ".archived_trash"
        self.create_archive_dir()

        self._trash_cover_art = True

        if self._trash_cover_art:
            _logger.warn(
                f"remove custom cover photos flag is enabled, this will attempt to drop any custom cover photos")

    def collect_garbage(self, dir):
        try:
            _logger.info(f"searching '{dir}' for trash...")
            potential_files = self.get_potential_files(dir)

            _logger.info(f"will attempt to trash {len(potential_files)} files")

            self.trash_files(potential_files, dir)
        except Exception as ex:
            _logger.warn(f"a problem occured: '{ex}'")
            return

    def trash_files(self, fns, source_dir):
        for fn in fns:
            self.trash_file(fn, source_dir)

    def trash_file(self, fn, grandparent=None):
        self.archive_trash(join(grandparent, fn))

    def create_archive_dir(self):
        try:
            mkdir(self._archive_dir)
            _logger.debug(f"created archive directory '{self._archive_dir}'")
        except FileExistsError:
            _logger.warn(
                f"cannot create archive directory, as it already exists. Using existing...")

    def archive_trash(self, src_fn):
        try:
            move(src_fn, self._archive_dir)
            _logger.debug(f"archived '{src_fn}'")
        except Exception as e:
            _logger.warn(f"encountered exception during archival: '{e}'")

    def get_potential_files(self, dir):
        return [fn for fn in listdir(dir) if self.should_be_trashed(dir, fn)]

    def should_be_trashed(self, dir, fn):
        return (
            isfile(join(dir, fn))
            and not validatated_movie_content(fn)
            and validated_meda_junk_deletion(fn, remove_custom_cover_photo=self._trash_cover_art)
        )
