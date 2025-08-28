import random

def	generate_key_stream(n):
	return bytes([random.randrange(0, 256) for i in range(n)])

def	xor_bytes(key_stream, texte):
	length = min(len(key_stream), len(texte))
	return bytes([key_stream[i] ^ texte[i] for i in range(length)])

message = input("Message: ")
message = message.encode()
print("Encoded:", message)
key_stream = generate_key_stream(len(message))
secret = xor_bytes(key_stream, message)
print("Secret:", secret)
plain_text = xor_bytes(key_stream, secret)
print("Plain:", plain_text.decode())
