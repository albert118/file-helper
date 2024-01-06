from logging import Logger
from FileValidation.ValidationRecipes import validated_deletion
from os import listdir, mkdir
from shutil import move


class Collector:
    def __init__(self, dir: str, config: dict, logger: Logger):
        self._cwd = dir
        self._logger = logger
        self._config = config

        self._setup_archive_dir()
        self._determine_garbage_extensions()

    def _determine_garbage_extensions(self):
        w = self._config["whitelist"]
        b = self._config["blacklist"]
        self._garbage_extensions = [ext for ext in b if ext not in w]

    def _setup_archive_dir(self):
        self._archive_dir = self._config["archive_dir"]

        try:
            mkdir(self._archive_dir)
            self._logger.debug(
                f"created archive directory '{self._archive_dir}'")
        except FileExistsError:
            self._logger.warn(
                f"cannot create archive directory, as it already exists. Will use the existing...")

    def _get_potential_files(self):
        return [fn for fn in listdir(self._cwd) if validated_deletion(fn, self._garbage_extensions)]

    def _pickup_garabage(self, garbage_fn):
        try:
            move(garbage_fn, self._archive_dir)
            self._logger.debug(f"archived '{garbage_fn}'")
        except Exception as e:
            self._logger.warn(f"encountered exception during archival: '{e}'")

    def collect(self):
        try:
            self._logger.info(f"searching '{self._cwd}' for garbage...")
            potential_files = self._get_potential_files()
            self._logger.info(f"{len(potential_files)} garbage files found")

            for fn in potential_files:
                self._pickup_garabage(fn, self._cwd)
        except Exception as ex:
            self._logger.warn(f"a problem occured: '{ex}'")
            return
