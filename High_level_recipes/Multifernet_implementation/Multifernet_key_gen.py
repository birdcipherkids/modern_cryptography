from cryptography.fernet import Fernet, MultiFernet

print()
print()
print(' ====================================================================================================================== ')
print()
print('                                     Welcome to the MultiFernet Key Generator Program                                   ')
print()
print(' =======================================================================================================================')
print()
print()

def key_generator():

	message = input('    Please enter the message to encrypt:\n    ')
	message = message.encode()
	print()
	print()

	key1 = Fernet.generate_key()
	key2 = Fernet.generate_key()
	key3 = Fernet.generate_key()
	key1_prep = Fernet(key1)
	key2_prep = Fernet(key2)
	key3_prep = Fernet(key3)

	f = MultiFernet([key1_prep, key2_prep, key3_prep])
	token = f.encrypt(message)

	message_decrypted = f.decrypt(token)

	results = [token, key1, key2, key3, message_decrypted]

	return results


gen = key_generator()


print('    Your encrypted message is:\n    ', gen[0].decode())
print()
print()
print('    The administrative first key (used for encrypting the messages) in the decryption process will be:\n    ', gen[1].decode())
print()
print()
print('    The second key for the decryption process will be:\n    ', gen[2].decode())
print()
print()
print('    The third key for the decryption process will be:\n    ', gen[3].decode())
print()
print()
print(' ······································· proof of decryption of the supplied message ···································')
print()
print('    Your decrypted message is:\n    ', gen[4].decode())
print()
print(' ·······················································································································')
print()
print()
print('========================================================================================================================')