import logging
import click
import json
from GarbageCollector import GarbageCollector


@click.command()
@click.argument('cwd')
@click.option('--config-fn', default="config.json", help="provide a custom path to a config file (default is config.jsons)")
@click.option('--verbose', '/ -v', default=False)
def main(cwd, config_fn, verbose):
    logging.basicConfig(level=logging.INFO if not verbose else logging.DEBUG)
    logger = logging.getLogger(__name__)

    config = None
    with open(config_fn) as config_file:
        config = json.load(config_file)

    clean_directory(cwd, config, logger)


def clean_directory(dir: str, config: dict, logger: logging.Logger):
    c = GarbageCollector.Collector(dir, config, logger)

    try:
        c.collect()
    except Exception as e:
        logger.error(f"error while removing black listed files '{e}'")
        raise


if __name__ == "__main__":
    main()
