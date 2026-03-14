import urllib.parse

def mess_userpass_decode(encoded):
    """Decodifica uma string aplicando XOR com 0x1f (reverte mess_userpass)."""
    return ''.join(chr(ord(c) ^ 0x1f) for c in encoded)

def decode_url_and_mess_userpass(url_encoded):
    """Decodifica URL-encoded e depois aplica XOR 0x1f."""
    # 1
    decoded_url = urllib.parse.unquote(url_encoded)
    print(f"URL-decoded: {decoded_url}")
    
    # 2
    decoded_password = mess_userpass_decode(decoded_url)
    print(f"senha original: {decoded_password}")
    print("cracked by: PIROCOTO")
    
    return decoded_password

# 3
url_encoded = "~{rvq"
print(f"decodificando: {url_encoded}")
decode_url_and_mess_userpass(url_encoded)
