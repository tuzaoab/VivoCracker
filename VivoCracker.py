import urllib.parse

def xor(texto_codificado):
    return ''.join(chr(ord(caractere) ^ 0x1f) for caractere in texto_codificado)

def decodificar(url_codificada):
    url_decodificada = urllib.parse.unquote(url_codificada)
    print(f"URL decodificada: {url_decodificada}")
    
    senha_original = xor(url_decodificada)
    print(f"Senha original: {senha_original}")
    print("Cracked by: PIROCOTO")
    
    return senha_original


entrada = "COLOQUE O TEXTO AQUI"
print(f"Decodificando: {entrada}")
decodificar(entrada)
