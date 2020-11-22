"""

Twitt class
"""
from datetime import datetime


class Twitt:
    """

    Twitt class
    """
    def __init__(self, **kwargs):
        """

        Twitt init
        """
        self._data = kwargs

    @property
    def title(self) -> str:
        """

        title getter
        :return:
        """
        return self._data.get("title")

    @property
    def description(self) -> str:
        """

        description getter
        :return:
        """
        return self._data.get("description")

    @property
    def pub_date(self) -> datetime:
        """

        pub_date getter
        example: Sat, 21 Nov 2020 20:36:51 GMT
        :return:
        """
        return self._data.get("pub_date")

    @property
    def guid(self) -> str:
        """

        guid getter
        :return:
        """
        return self._data.get("guid")

    @property
    def link(self) -> str:
        """

        link getter
        :return:
        """
        return self._data.get("link")

    def __repr__(self) -> str:
        """

        print format
        :return:
        """
        return f"{self.guid} - {self.title} - {self.pub_date}: {self.description} - {self.link}"
