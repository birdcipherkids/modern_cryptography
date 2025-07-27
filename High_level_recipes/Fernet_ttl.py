from cryptography.fernet import Fernet, InvalidToken
import time

results_mode = ''

def define_mode():

	global results_mode

	mode = input('Do you wish to encrypt or decrypt a message? (Please enter: "e" or "d"): ')

	if mode == 'e':

		print('You have chosen the Encryption Function.')

	elif mode == 'd':

		print('You have chosen the Decryption Function')
	
	while True:

		if mode == 'e':

			try:
				print()
				ttl_assigned = input('Enter the maximum time for your encrypted message: ')
				ttl_assigned = int(ttl_assigned)
				results_mode = [mode, ttl_assigned]
				break

			except ValueError:

				print('You must enter a numerical value')
											
		elif mode == 'd':

			try:
				print()
				ttl_assigned = input('Enter the maximum time for your encrypted message: ')
				ttl_assigned = int(ttl_assigned)
				results_mode = [mode, ttl_assigned]
				break

			except ValueError:

				print('You must enter a numerical value')
				
		else:

			print('You must enter "e" or "d". Try again.')
			print()
			mode = input('Do you wish to encrypt or decrypt a message? (Please enter: "e" or "d"): ')

			if mode == 'e':

				print('You have chosen the Encryption Function.')

			elif mode == 'd':

				print('You have chosen the Decryption Function')			

	
def encrypt_with_ttl(message, key, ttl):

	current_time = int(time.time())
	message_with_time = f'{current_time}:{message}'
	f = Fernet(key)
	token = f.encrypt(message_with_time.encode())

	return token


def decrypt_and_verify_ttl(token, key, ttl):

	f = Fernet(key)

	try:

		decrypted_message = f.decrypt(token).decode()
		creation_time, message = decrypted_message.split(':',1)
		creation_time = int(creation_time)
		current_time = int(time.time())
		difference_time = current_time - creation_time

		if difference_time <= ttl:

			return message.encode()

		else:

			raise Exception('Expired message')

	except Exception as e:

		print()
		print(f'Decryption error or expired ttl:{e}')
		return None


define_mode()

if results_mode[0] == 'e':

	key = Fernet.generate_key()
	print()
	message = input('Enter the message to encrypt: ')
	print()
	ttl = results_mode[1]
	token = encrypt_with_ttl(message, key, ttl)
	print(f'Token cifrado:\n {token.decode()}')
	print()
	print(f'Key for encryption:\n {key.decode()}')

elif results_mode[0] == 'd':

	print()
	key = input('Enter the key for the decryption process:\n ').encode()
	print()
	token = input('Enter the message to decrypt:\n ').encode()
	decrypted_message_ex = decrypt_and_verify_ttl(token, key, results_mode[1])

	if decrypted_message_ex:

		print()
		print(f'Decrypted message:\n{decrypted_message_ex.decode()}')

	else:

		print()
		print(f'The message couldnt be decrypted or the token expired')
