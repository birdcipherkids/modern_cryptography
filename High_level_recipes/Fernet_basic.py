from cryptography.fernet import Fernet, InvalidToken

def define_mode():

	while True:

		mode = input('Do you wish to encrypt or decrypt a message? (Please enter: "encrypt" or "decrypt"): ')
		
		if mode == 'encrypt':

			mode = mode[0]
			return mode

		elif mode == 'decrypt':

			mode = mode[0]
			return mode

		else:

			print('You must enter "encrypt" or "decrypt". Try again.')
			print()


mode = define_mode()
print()


if mode == 'e':

	key = Fernet.generate_key()
	f = Fernet(key)
	message = input('Enter the message to encrypt: ')
	print()
	message = message.encode()
	token = f.encrypt(message)
	print('The key for the encryption process is: \n', key.decode())
	print()
	print('Your encrypted message is: \n', token.decode())

elif mode == 'd':

	try:

		key = input('Enter the key to decrypt the message: ').encode()
		f = Fernet(key)
		print()
		token = input('Enter the encrypted message to decrypt: \n').encode()
		decrypted_message = f.decrypt(token)
		print()
		print('Your plaintext is: \n', decrypted_message.decode())

	except ValueError:

		print()
		print('Error: Incorrect key')


	except InvalidToken:

		print()
		print('Error: Your token or key is not valid')


