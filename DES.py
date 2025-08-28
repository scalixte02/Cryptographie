from pyDes import *

def	modification(secret):
	mod = [0] * len(secret)
	mod[9] = 1
#	mod[11] = ord(' ') ^ ord('1')
#	mod[12] = ord(' ') ^ ord('0')
#	mod[13] = ord('1') ^ ord('0')
	return bytes([mod[i] ^ secret[i] for i in range(len(secret))])

#message = b"0123456701234567"
message = b"Vers Bob:    10$ et lui souhaiter bonne chance."
key = b"DESCRYPT"
iv = bytes([1]*8)
k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
secret = k.encrypt(message)
print("Longueur du texte plain : ", len(message))
print("Longueur du texte chiffré : ", len(secret))
print("Message chiffré d'Alice : ", secret)
#print("Premier bloc chiffré : ", secret[0:8])
#print("Deuxième bloc chiffré : ", secret[8:16])
#print("Le reste chiffré : ", secret[16:])
secret = modification(secret)
print("Message chiffré de Bob : ", secret)
message = k.decrypt(secret)
print("Notre message déchiffré : ", message)
