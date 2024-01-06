from logging import Logger
from FileValidation.ValidationRecipes import validated_deletion
from os import listdir, mkdir, path
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
            self._logger.debug("created archive directory")
        except FileExistsError:
            self._logger.warn("pre-existing archive directory found")
        finally:
            self._logger.info(f"will archive files to '{self._archive_dir}'")

    def _get_potential_files(self):
        return [fn for fn in listdir(self._cwd) if validated_deletion(fn, self._garbage_extensions)]

    def _pickup_garabage(self, garbage_fn):
        move(garbage_fn, self._archive_dir)
        self._logger.debug(f"archived '{garbage_fn}'")

    def collect(self):
        try:
            self._logger.info(f"searching '{self._cwd}' for garbage...")
            potential_files = self._get_potential_files()
            count_potential_files = len(potential_files)

            if count_potential_files > 0:
                self._logger.info(
                    f"{count_potential_files} garbage files found")
                self._logger.debug(
                    f"found potential files: [ {', '.join(potential_files)} ]")

                for fn in potential_files:
                    self._pickup_garabage(path.join(self._cwd, fn))

                self._logger.info(f"{count_potential_files} files archived")
            else:
                self._logger.info("no garbage files found, finishing early")
        except Exception as ex:
            self._logger.error(f"a problem occured, {ex}")
            return
