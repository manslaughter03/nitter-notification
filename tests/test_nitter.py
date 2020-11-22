"""

test nitter
"""
from nitter.watcher import Watcher


def test_load_config(test_config_path):
    """

    test load config
    """
    watcher = Watcher(test_config_path)
    watcher.load_config()
    assert watcher.config_data
    assert watcher.config_data.get("followings")

def test_watcher(test_config_path):
    """

    test Watcher class
    """
    watcher = Watcher(test_config_path)
    watcher.load_config()
