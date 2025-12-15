from itertools import cycle

def xor_bytes(data, key):
    return bytes([b ^ k for b, k in zip(data, cycle(key))])

cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cipher = bytes.fromhex(cipher_hex)
FLAG = "myXORkey"
FLAG = FLAG.encode()

print(xor_bytes(cipher,FLAG))