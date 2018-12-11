import requests

def main():

    translate_it('./DE.txt', './DE-RU.txt', 'de', '')
    translate_it('./ES.txt', './ES-RU.txt', 'es', '')
    translate_it('./FR.txt', './FR-RU.txt', 'fr', '')


def translate_it(source_path, target_path, source_lang, target_lang):

    target_language = 'ru'

    if target_lang:
        target_language = target_lang

    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """

    source_file = open(source_path)
    source_text = source_file.read()
    source_file.close()


    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20181210T212738Z.6ad03b19b495ce7b.0b2e0a50c6c2afafe3595daa192ed65c41f1398f'

    params = {
        'key': key,
        'lang': source_lang + '-' + target_language,
        'text': source_text,
    }

    response = requests.get(url, params=params).json()
    target_text = ' '.join(response.get('text', []))

    target_file = open(target_path, 'w')

    target_file.write(target_text)

    target_file.close()


if __name__ == '__main__':
    main()
