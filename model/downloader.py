import urllib
from urlparse import urljoin

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
        urllib.urlretrieve(download_url,full_path)