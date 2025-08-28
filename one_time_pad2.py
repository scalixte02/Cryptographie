import random

def	generate_key_stream(n):
	return bytes([random.randrange(0, 256) for i in range(n)])

def	xor_bytes(key_stream, texte):
	length = min(len(key_stream), len(texte))
	return bytes([key_stream[i] ^ texte[i] for i in range(length)])

message = "UNE ATTAQUE"
message = message.encode()
key_stream = generate_key_stream(len(message))
secret = xor_bytes(key_stream, message)

#Team1
message = "PAS ATTAQUE"
message = message.encode()
guess_key_stream = xor_bytes(message, secret)
print("La clé de chiffrement 1 : ", guess_key_stream)
plain_text = xor_bytes(guess_key_stream, secret)
print("Le texte original de l'équipe 1 : ", plain_text)

#Team2
message = "DES SUPRIS"
message = message.encode()
guess_key_stream = xor_bytes(message, secret)
print("La clé de chifrrement 2: ", guess_key_stream)
plain_text = xor_bytes(guess_key_stream, secret)
print("Le texte original de l'équipe 2 : ", plain_text)
