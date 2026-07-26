from urllib.parse import urlparse


def validate_url(url: str):

    parsed = urlparse(url)

    if parsed.scheme not in ["http", "https"]:
        return False

    if not parsed.netloc:
        return False

    return True