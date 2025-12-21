from Crypto.Util.number import long_to_bytes

p = 61
q = 53
e = 17
c = 2790

n = p * q
phi = (p - 1) * (q - 1)     
d = pow(e, -1, phi)                                 # d : private-key
                                                    # c : encryption  pow(m,e,n)
m = pow(c, d, n)                                    # m : message/decryption
print(long_to_bytes(m))
