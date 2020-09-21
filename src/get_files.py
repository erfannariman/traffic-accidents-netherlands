from urllib import request
import os
import json
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://data.overheid.nl/dataset/verkeersongevallen"


class GetFiles:
    def __init__(self):
        self.url = BASE_URL
        self.data_dir = os.path.join("..", "data")

    def get_links(self):
        """
        Returns
        -------
        retrieved download links for the csv's.
        """
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")
        script = soup.find("script", {"type": "application/ld+json"})
        json_string = json.loads(script.string)
        links = [link["contentUrl"] for link in json_string["distribution"]]

        return links

    def download_csvs(self):
        """
        Returns
        -------
        None, saves files to the data dir.
        """
        links = self.get_links()
        for link in links:
            file_name = link.split("/")[-1]
            request.urlretrieve(link, os.path.join(self.data_dir, file_name))

