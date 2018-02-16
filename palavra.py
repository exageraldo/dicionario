from unidecode import unidecode
from ftfy import fix_text
from lxml import html
import requests


class Dicionario:
    @staticmethod
    def sinonimos(palavra):
        url = 'https://www.sinonimos.com.br/' + unidecode(palavra) + '/'
        page = requests.get(url)
        tree = html.fromstring(page.content)
        sinonimos = tree.xpath('//*[@id="content"]/div[1]/div[@class="s-wrapper"]/p/a//text()')
        if sinonimos:
            sinonimos = [fix_text(sinonimo) for sinonimo in sinonimos]
            return sinonimos
        return {'status': 'Não encontrado', 'url': url}

    @staticmethod
    def antonimos(palavra):
        url = 'https://www.antonimos.com.br/' + unidecode(palavra) + '/'
        page = requests.get(url)
        tree = html.fromstring(page.content)
        antonimos = tree.xpath('//*[@id="content"]//div[@class="s-wrapper"]/p/a//text()')
        if antonimos:
            antonimos = [fix_text(antonimo) for antonimo in antonimos]
            return antonimos
        return {'status': 'Não encontrado', 'url': url}

    @staticmethod
    def significados(palavra):
        url = 'https://www.dicio.com.br/' + unidecode(palavra) + '/'
        page = requests.get(url)
        tree = html.fromstring(page.content)
        significados = tree.xpath('//*[@id="content"]/div[1]/p[1]/span/text()')
        if significados:
            significados = [fix_text(significado.strip()) for significado in significados[0: -2]]
            return significados
        return {'status': 'Não encontrado', 'url': url}
