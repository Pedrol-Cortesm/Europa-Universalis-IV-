from googletrans import Translator

def traduzir_texto(texto, idioma_destino='pt'):
    translator = Translator()
    traducao = translator.translate(texto, dest=idioma_destino)
    return traducao.text
