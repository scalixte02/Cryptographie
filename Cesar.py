
def	generate_key(n):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	key = {}
	cnt = 0

	for c in letters:
		key[c] = letters[(cnt + n) % len(letters)]
		cnt += 1

	return key

def	generate_dkey(key):
	switched_key = {}

	for index, value in key.items():
		switched_key[value] = index

	return switched_key

def	encrypt_decrypt(key, message):
	processed = ""

	for letter in message.upper():
		if letter in key:
			processed += key[letter]
		else:
			processed += letter

	return processed

def	brute_force(secret):

	for i in range(26):
		dkey = generate_key(i)
		message = encrypt_decrypt(dkey, secret)
		print(message)

key = generate_key(3)
message = input("Enter the message to encrypt: ")
secret = encrypt_decrypt(key, message)
print("Encrypted:", secret)

dkey = generate_dkey(key)
message = encrypt_decrypt(dkey, secret)
print("Decrypted:", message)