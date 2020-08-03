def readn(fin, n):
    s = 0
    for ti in fin.read(n):
        s = s * 256 + ord(ti)
    return s
     
# def fletcher(fin, k):
#     if  k not in (16, 32, 64):
#         raise ValueError("Valid choices of k are 16, 32 and 64")
#     nbytes = k // 16
#     mod = 2 ** (8 * nbytes) - 1
#     s = s2 = 0
#     t = readn(fin, nbytes)
#     while t:
#         s += t
#         s2 += s 
#         t = readn(fin, nbytes)
#     return s % mod + (mod + 1) * (s2 % mod)


# def create_checksums(message):

# asumiendo que el mensaje entra como bitarray
def fletcher16(message):
    # hacer mensaje len % 8 = 0
    residue = len(message) % 8 
    # se le agregan 0s para que sea divisible en 8 bits
    xtra_0s = bitarray('0' * (8-residue))
    msg = xtra_0s + message
    block_len = len(msg) // 8
    # get the mod of checksum 
    mod = 2 ** (8) - 1
    # break message in k blocks of 8 bits
    blocks = []
    for k in range(block_len, 0, -1):
        blocks.append(bitarray(msg[k*8-8:k*8]))
    suma = bin(0)
    for block in blocks:
        block_str = (str(block).split('\'')[1])
        suma = bin(int((block_str), 2) + int(suma,2))
    # residuo de suma se agrega 
    residue = len(str(suma).split("b")[1]) % 8
    while residue != 0:
        extra = str(suma).split("b")[1][0:residue]
        suma = bin(int(extra, 2) + int(suma,2))



    
    
