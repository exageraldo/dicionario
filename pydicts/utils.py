from unidecode import unidecode
from lxml import html
import requests


def find_in_url(search, root_url, xpath):
    url = root_url + unidecode(search) + '/'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    xpath_search = tree.xpath(xpath)
    return {'tree': tree, 'result': xpath_search, 'url': url}
