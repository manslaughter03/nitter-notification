"""

nitter module
"""
from datetime import datetime
import logging
from typing import List

import requests
from lxml import etree

from nitter.types import Twitt


def fetch_feed(followings: List[str], logger: logging.Logger) -> List[Twitt]:
    """

    fetch nitter rss
    :param username:
    :return:
    """
    url = f"https://nitter.net/{','.join(followings)}/rss"
    logger.info("Request on %s", url)
    resp = requests.get(url)
    root = etree.fromstring(resp.text.encode()) # pylint: disable=c-extension-no-member
    return [Twitt(**{"title": item.find("title").text,
                     "description": item.find("description").text,
                     "guid": item.find("guid").text,
                     "link": item.find("link").text,
                     "pub_date": datetime.strptime(item.find("pubDate").text,
                                                   "%a, %d %b %Y %H:%M:%S %Z")})
            for item in root.xpath("/rss/channel/item")]
