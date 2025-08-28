from pyDes import *
import random

message = b"01234567"
key_11 = random.randrange(0, 256)
key_1 = bytes([key_11, 0, 0, 0, 0, 0, 0, 0])
key_21 = random.randrange(0, 256)
key_2 = bytes([key_21, 0, 0, 0, 0, 0, 0, 0])
iv = bytes([0] * 8)
k1 = des(key_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
k2 = des(key_2, ECB, iv, pad=None, padmode=PAD_PKCS5)

secret = k2.encrypt(k1.encrypt(message))
print("La clé 11: ", key_11)
print("La clé 21: ", key_21)
print("Le message chiffré d'Alice : ", secret)
message = k1.decrypt(k2.decrypt(secret))
print("Le message que Bob reçoit: ", message)

lookup = {}
for i in range(256):
	k = bytes([i, 0, 0, 0, 0, 0, 0, 0])
	k = des(k, ECB, iv, pad=None, padmode=PAD_PKCS5)
	lookup[k.encrypt(message)] = i

for i in range(256):
	k = bytes([i, 0, 0, 0, 0, 0, 0, 0])
	k = des(k, ECB, iv, pad=None, padmode=PAD_PKCS5)
	if k.decrypt(secret) in lookup:
		k_11 = lookup[k.decrypt(secret)]
		k_21 = i
		k_1 = bytes([k_11, 0, 0, 0, 0, 0, 0, 0])
		k_2 = bytes([k_21, 0, 0, 0, 0, 0, 0, 0])
		k_1 = des(k_1, ECB, iv, pad=None, padmode=PAD_PKCS5)
		k_2 = des(k_2, ECB, iv, pad=None, padmode=PAD_PKCS5)
		print("Clé k_11 : ", k_11)
		print("Clé k_21 : ", k_21)
		message = k_1.decrypt(k_2.decrypt(secret))
		print("Le message qu'Eve déchiffre: ", message)
		break
