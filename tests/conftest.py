"""

conftest
"""
import os

import pytest


@pytest.fixture
def test_config_path():
    """

    :return:
    """
    yield os.path.join(os.path.dirname(__file__), "confs", "nba.yaml")


@pytest.fixture
def test_db_path():
    """

    :return:
    """
    yield os.path.join(os.path.dirname(__file__), "db", "nba.yaml")
