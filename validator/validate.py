from urllib.parse import urlparse

class Validate:
    def url(self, url: str):
        result = urlparse(url)
        return all([result.scheme, result.netloc])
