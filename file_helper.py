import logging
import click
import json
from GarbageCollector import GarbageCollector


@click.command()
@click.argument('cwd')
@click.option('--config-fn', default="config.json", help="provide a custom path to a config file (default is config.jsons)")
@click.option('--verbose', is_flag=True)
def cli(cwd, config_fn, verbose):
    logging.basicConfig(level=logging.INFO if not verbose else logging.DEBUG)
    logger = logging.getLogger(__name__)

    config = None
    with open(config_fn) as config_file:
        config = json.load(config_file)

    GarbageCollector.Collector(cwd, config, logger).collect()
