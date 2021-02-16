"""

watcher module
"""
__strict__ = True

import os
from typing import Dict
from datetime import datetime
import time
import logging

import yaml
import sdnotify

from nitter.nitter import fetch_feed, FetchException
from nitter.notify import send_notify
from nitter.logger import configure_logger


class Watcher:
    """

    Watcher class
    """
    def __init__(self, config_path: str, db_path: str, debug_mode: bool = False):
        """

        Watcher init
        """
        self.config_path = config_path
        self.db_path = db_path
        self._config_data = {}
        self._cached_stamp = 0
        self._cached_time = None
        self._load_db()
        self.logger = configure_logger(logging.DEBUG if debug_mode else logging.INFO)
        self.notifier = sdnotify.SystemdNotifier()
        self.notifier.notify("READY=1")

    @property
    def config_data(self) -> Dict:
        """

        config data getter
        :return:
        """
        return self._config_data

    def run(self):
        """

        run watcher
        :return:
        """
        self.logger.info("Run watcher")
        while True:
            self.notifier.notify("WATCHDOG=1")
            self.execute()
            time.sleep(self.config_data.get("sleep_interval", 5))

    def execute(self):
        """

        execute watcher
        :return:
        """
        stamp = os.stat(self.config_path).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            self.load_config()
        self.fetch()

    def fetch(self):
        """

        fetch feed
        :return:
        """
        new_twitt = False
        followings = self.config_data.get("followings", [])
        self.logger.info("Fetch %s", followings)
        twitts = []
        instance_urls = self.config_data.get("instance_urls", [])
        for instance_url in instance_urls:
            try:
                twitts = fetch_feed(instance_url, followings, self.logger)
                break
            except FetchException as exception:
                self.logger.warning("Failed to fetch followings, %s", exception)
        for item in twitts:
            self.logger.debug("pub_date: %s _cached_time: %s", item.pub_date, self._cached_time)
            if item.pub_date > self._cached_time:
                new_twitt = True
                self.logger.info("Need to notify %s - %s", item.title, item.link)
                send_notify(f"{item.title} - {item.link}")
        if new_twitt:
            self._cached_time = datetime.utcnow()
            self._write_db()

    def load_config(self):
        """

        load config
        :return:
        """
        with open(self.config_path, 'r') as _file:
            self._config_data  = yaml.safe_load(_file)

    def _load_db(self):
        """

        load db
        :return:
        """
        if not os.path.isdir(os.path.dirname(self.db_path)):
            os.makedirs(os.path.dirname(self.db_path))
        if not os.path.isfile(self.db_path):
            self._cached_time = datetime.utcnow()
            return
        with open(self.db_path, 'r') as _file:
            data = float(_file.read())
            self._cached_time = datetime.fromtimestamp(data)

    def _write_db(self):
        """

        write db
        :return:
        """
        with open(self.db_path, 'w') as _file:
            _file.write(str(self._cached_time.timestamp()))
