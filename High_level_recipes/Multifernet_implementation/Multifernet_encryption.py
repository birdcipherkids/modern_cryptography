from cryptography.fernet import Fernet, MultiFernet
from Multifernet_key_gen import gen1

print()
print()
print(' ====================================================================================================================== ')
print()
print('                                     Welcome to the MultiFernet Encryption Program                                      ')
print()
print(' =======================================================================================================================')
print()
print()

def Cipher_Machine():

	message = input('    Please enter the message to encrypt:\n    ')
	message = message.encode()
	print()
	print()

	key1 = gen1[0]
	key2 = gen1[1]
	key3 = gen1[2]
	key1_prep = Fernet(key1)
	key2_prep = Fernet(key2)
	key3_prep = Fernet(key3)

	f = MultiFernet([key1_prep, key2_prep, key3_prep])
	token = f.encrypt(message)

	message_decrypted = f.decrypt(token)

	results = [token, key1, key2, key3, message_decrypted]

	return results


results = Cipher_Machine()


print('    Your encrypted message is:\n    ', results[0].decode())
print()
print()
print('    The key for the decryption process will be:\n    ', results[3])
print()
print()
print(' ······································· proof of decryption of the supplied message ···································')
print()
print('    Your decrypted message is:\n    ', results[4].decode())
print()
print(' ·······················································································································')
print()
print()
print('========================================================================================================================')