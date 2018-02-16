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

    @staticmethod
    def conjugacao(verbo):
        url = 'https://www.conjugacao.com.br/verbo-' + unidecode(verbo) + '/'
        page = requests.get(url)
        tree = html.fromstring(page.content)
        verbo = tree.xpath('/html/body/div/div[2]/div/h1//text()')
        if 'Página Não Encontrada' not in verbo:
            conjugar = tree.xpath('/html/body/div/div[2]/div/div[2]/div[1]/div/div//text()')
            tempos_verbais = ['Presente', 'Pretérito Imperfeito', 'Pretérito Perfeito', 'Pretérito Mais-que-perfeito', 'Futuro do Presente', 'Futuro do Pretérito']
            pessoas = ['eu', 'tu', 'ele', 'nós', 'vós', 'eles']
            conjugar = [c for c in conjugar if c not in pessoas]
            lista_indices = [conjugar.index(tempo) for tempo in tempos_verbais]
            lista_indices.append(len(conjugar))
            conjugacao = {}
            for item in range(len(lista_indices)-1):
                lista = conjugar[lista_indices[item]+1:lista_indices[item+1]]
                conjugacao[conjugar[lista_indices[item]]] = lista
            return conjugacao
        return {'status': 'Não encontrado', 'url': url}
