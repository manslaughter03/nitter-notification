"""

nitter entrypoint
"""
import argparse
import os
from pathlib import Path

from nitter.watcher import Watcher

def main():
    """

    main nitter entrypoint
    """
    default_config_path = os.path.join(Path.home(),
                                       ".config",
                                       "nitter",
                                       "config.yaml")
    default_db_path = os.path.join(Path.home(),
                                   ".config",
                                   "nitter",
                                   "db")
    parser = argparse.ArgumentParser(description="Nitter notification tools")
    parser.add_argument("--cfg",
                        default=default_config_path,
                        help="Nitter notification config file")
    parser.add_argument("--db",
                        default=default_db_path,
                        help="Nitter notification db")
    parser.add_argument("--debug",
                        action="store_true",
                        help="Activate debug mode")
    args = parser.parse_args()

    watcher = Watcher(args.cfg, args.db, args.debug)
    watcher.run()


if __name__ == "__main__":
    main()
