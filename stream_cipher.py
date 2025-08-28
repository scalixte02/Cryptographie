import random

class KeyStream:
	def __init__(self, key=1):
		self.next = key
	
	def rand(self):
		self.next = (1103515245 * self.next + 12345) % 2**31
		return self.next
	
	def get_key_byte(self):
		return self.rand() % 256 

def encryptDecrypt(key, message):
	return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

def transmit(secret, tauxErreurs):
	b = []
	for c in secret:
		if random.randrange(0, tauxErreurs) == 0:
			c = c ^ 2**random.randrange(0,8)
			b.append(c)
	return bytes(b)

def	modification(secret):
	mod = [0] * len(secret)
	mod[18] = ord(' ') ^ ord('1')
	mod[19] = ord(' ') ^ ord('0')
	mod[20] = ord('1') ^ ord('0')
	return bytes([mod[i] ^ secret[i] for i in range(len(secret))])

def	get_key(message, secret):
	return bytes([message[i] ^ secret[i] for i in range(len(secret))])

def	crack(key_stream, secret):
	length = min(len(key_stream), len(secret))
	return bytes([key_stream[i] ^ secret[i] for i in range(length)])

def	brute_force(plain, secret):
	for key in range(2**31):
		bf_key = KeyStream(key)
		for i in range(len(plain)):
			xor_value = plain[i] ^ secret[i]
			if xor_value != bf_key.get_key_byte():
				break
			else:
			 	return key
	return False

#key = KeyStream()
#for i in range(10):
#	print(key.get_key_byte())

#key = KeyStream(23)
#message = "Hello, World!".encode()
#secret = encryptDecrypt(key, message)
#print("Notre message secret : ", secret)
#key = KeyStream(23)
#message = encryptDecrypt(key, secret)
#print("Notre message en texte : ", message)

#key = KeyStream(23)
#message = "Nous allons attaquer a 12 h, par le cote Est de la prairie".encode()
#secret = encryptDecrypt(key, message)
#print("Notre message est : ", message)
#secret = transmit(secret, 6)
#key = KeyStream(23)
#message = encryptDecrypt(key, secret)
#print("Notre message en texte : ", message)

#key = KeyStream(10)
#message = "Transfert a Bob :   10$".encode()
#print("Alice : ", message)
#secret = encryptDecrypt(key, message)
#print("Le secret : ", secret)
#secret = modification(secret)
#key = KeyStream(10)
#message = encryptDecrypt(key, secret)
#print("La banque : ", message)

#message_Eve = "Ceci est un message super hyper important".encode()
#key = KeyStream(33)
#message = message_Eve
#print("Alice : ", message)
#secret = encryptDecrypt(key, message)
#print("Le secret : ", secret)
#eves_key_stream = get_key(message, secret)
#print("Eve crack : ", crack(eves_key_stream, secret))
#key = KeyStream(33)
#message = encryptDecrypt(key, secret)
#print("Bob : ", message)

cle_secret = random.randrange(0, 2**20) 
print("La clé secrète entre Alice et Bob : ", cle_secret)
key = KeyStream(cle_secret)
header = "MESSAGE: "
message = header + "Un message secret vers Bob"
message = message.encode()
print("Alice : ", message)
secret = encryptDecrypt(key, message)
print("Le secret : ", secret)
key = KeyStream(cle_secret)
message = encryptDecrypt(key, secret)
print("Bob : ", message)
bf_key = brute_force(header.encode(), secret)
print("La clé force brute d'Eve : ", bf_key)
key = KeyStream(bf_key)
message = encryptDecrypt(key, secret)
print("Eve : ", message)
