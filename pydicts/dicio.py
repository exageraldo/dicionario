import ftfy
from pydicts import utils


class Dicio:
    @staticmethod
    def synonyms(word):
        url = 'https://www.sinonimos.com.br/'
        xpath = '//*[@id="content"]/div[1]/div[@class="s-wrapper"]/p/a//text()'
        synonyms = utils.find_in_url(word, url, xpath)
        if synonyms['result']:
            synonyms_list = [ftfy.fix_text(s) for s in synonyms['result']]
            for synonyms in synonyms_list:
                yield synonyms
        return {'status': 'Word not found', 'url': synonyms['url']}

    @staticmethod
    def antonyms(word):
        url = 'https://www.antonimos.com.br/'
        xpath = '//*[@id="content"]//div[@class="s-wrapper"]/p/a//text()'
        antonyms = utils.find_in_url(word, url, xpath)
        if antonyms['result']:
            antonyms_list = [ftfy.fix_text(a) for a in antonyms['result']]
            for antonyms in antonyms_list:
                yield antonyms
        return {'status': 'Word not found', 'url': antonyms['url']}

    @staticmethod
    def meanings(word):
        url = 'https://www.dicio.com.br/'
        xpath = '//*[@id="content"]/div[1]/p[1]/span/text()'
        meanings = utils.find_in_url(word, url, xpath)
        if meanings['result']:
            meanings_list = [ftfy.fix_text(significado.strip())
                             for significado in meanings['result'][0: -2]]
            for meaning in meanings_list:
                yield meaning
        return {'status': 'Word not found', 'url': meanings['url']}
