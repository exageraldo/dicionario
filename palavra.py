from lxml import html
import unidecode
import requests


class Dicionario:
    @staticmethod
    def sinonimos(palavra):
        palavra = unidecode.unidecode(palavra)
        page = requests.get('https://www.sinonimos.com.br/' + palavra + '/')
        tree = html.fromstring(page.content)
        sinonimos = tree.xpath('//*[@id="content"]/div[1]/div[@class="s-wrapper"]/p/a//text()')
        return sinonimos

    @staticmethod
    def antonimos(palavra):
        palavra = unidecode.unidecode(palavra)
        page = requests.get('https://www.antonimos.com.br/' + palavra + '/')
        tree = html.fromstring(page.content)
        antonimos = tree.xpath(
            '//*[@id="content"]//div[@class="s-wrapper"]/p/a//text()')
        return antonimos

    @staticmethod
    def significados(palavra):
        palavra = unidecode.unidecode(palavra)
        page = requests.get('https://www.dicio.com.br/' + palavra + '/')
        tree = html.fromstring(page.content)
        significados = tree.xpath('//*[@id="content"]/div[1]/p[1]/span/text()')
        significados = [significado.strip() for significado in significados[0: -2]]
        return significados
