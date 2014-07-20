import urllib
from urlparse import urljoin
import os

class Downloader(object):

    def __init__(self, base_url):
        self.base_url = base_url


    def set_base_url(self, base_url):
        self.base_url = base_url

    def join_url(self, fragment):
        return urljoin(self.base_url, fragment)

    def set_url(self, url):
        self.set_base_url(url)
        self.url = url


    def download(self, word):
        filename = word + '.mp3'
        download_url = self.join_url(filename)
        full_path = './download/'+filename
        file_out, headers = urllib.urlretrieve(download_url,full_path)
        if not "audio/mpeg" in headers["content-type"]:
            os.remove(file_out)
            raise Exception("Downloaded File is not an audio file!")
