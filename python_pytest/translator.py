from googletrans import Translator

class GoogleTranslator():
    def __init__(self):
        self.translator = Translator()

    def get_language_id(self, language_name):
        languages = {
            '日本語': 'ja',
            '英語': 'en',
            '中国語': 'zh-cn',
            'フランス語': 'fr',
            'ドイツ語': 'de',
            'ヒンディー語': 'hi',
            'イタリア語': 'it',
            '韓国語': 'ko',
            'ロシア語': 'ru',
            'スペイン語': 'es'
        }
        return languages[language_name]

    def convert(self, text_original, language_original_name, language_translated_name):
        language_original_id = self.get_language_id(language_original_name)
        language_translated_id = self.get_language_id(language_translated_name)
        text_translated = self.translator.translate(text_original, src=language_original_id, dest=language_translated_id)
        return text_translated.text


# trans = GoogleTranslator()
# text_translated = trans.convert('私の名前は佐藤です。', '日本語', '英語')
# print(text_translated)