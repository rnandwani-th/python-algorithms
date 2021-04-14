# The Vigenère Cipher (named after the 16th century mathematician Blaise de Vigenère) is
# an improvement over simple substitution cipher. The Vigenere Cipher employs a polyalphabetic scheme
# that is much more resistant to frequency analysis. A polyalphabetic encryption system makes use of multiple
# alphabets in a 2-step process: 1) for each symbol in the plaintext, a different encoding
# alphabet is chosen based on a secret encryption-key, known only by the sender and
# receiver; 2) the corresponding symbol (identical offset) in the selected alphabet is then
# substituted for theplaintext character.

# The mechanism behind the vigenere cipher is as follow:

# To encrypt -
# Use the modified alphabet to create a row and column of alphabets.
# The key is then made to be the same length as the message to be encrypted.
# Pick a letter in the message and its corresponding letter in the keyword.
# Use the keyword letter and the message letter as the row and column index.
# The letter that appears at the intersecting point is the cipher letter. Repeat for remaining chars

# To decrypt-
# Pick a letter in the ciphertext and its corresponding character in the keyword.
# Use the keyword letter to find the corresponding row, and the letter heading of the
# column that contains the ciphertext letter is the needed message letter.

# The following code models the Vigenere Cipher using a modified alphabet. It employs a 71 character
# alphabet, including lowercase, uppercase, numbers and symbols. The code also includes a
# mechanism to show the full row and column of the shifted alphabet called the 'sparse'
# mechanism.

# The code also reads arguments from the command line

# Reference:
# http://www.cs.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html



import sys


def sparse(key):
	# Constructs a "sparse" version of the Vigenère table using a Python list that includes
	# only the shifted alphabets corresponding to each character in the encryption key.

	key = str(key)
	alphabetList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
	sparseTable = [] # Initializes the sparse table


	for each in range(len(key)):
		placeholder = ""
		char = key[each] # Sets char to the ith letter of the key
		positionOfKeyChar = alphabetList.index(char) # Gets the position of the char in the alphabet list

		while positionOfKeyChar < 70:
			letter = alphabetList[positionOfKeyChar] # Gets the letter in the position of the character of the key
			placeholder += letter
			positionOfKeyChar += 1		# Increments the positionOfKeyChar to do the same for each of the remaining characters in the list


		x = 0
		positionOfKeyChar = alphabetList.index(char) # Resets the position
		while x < positionOfKeyChar: # Returns the characters preceding the keyChar in the list
			letter = alphabetList[x]
			placeholder += letter
			x += 1
		sparseTable.append(placeholder)

	return sparseTable


def makeKeySameLength(message,key):
	# Makes the key the same length as the message
	times = len(message)//len(key)+1 # Gets how many times to repeat the key
	key = (times*key)[:len(message)] # Removes the excess letters
	return key


def encrypt(message,key):
	alphabetList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
	#print(sparse(key))		# Prints the sparse table for the key
	key = makeKeySameLength(message,key)	# Makes key the same length as the message
	encrypted = ""	# Initializes the encrypted form

	for char in range(len(message)):
		messageChar = message[char]	# Gets the character to be encrypted of the message
		keyChar = key[char]		# Gets the character of the key to be used
		sparseMessageChar = sparse(message[char])		# Forms a sparse version of the character of the message being encrypted
		sparseKeyChar = sparse(key[char])		# Forms a sparse version of the character of the key
		indexOfMessageChar = alphabetList.index(messageChar)	# Gets the index of the char of the message in the alphabet list
		indexOfKeyChar = alphabetList.index(keyChar)	#Gets the index of the char of the key in the alphabet list

		if (indexOfKeyChar > 25) and (indexOfKeyChar< 52):	# Getting the cipher char for lowercase letters
			sparsedMessageChar = ''.join(sparseMessageChar)	# Converts the sparse list to a string
			codedChar = sparsedMessageChar[indexOfKeyChar-1]# Gets the cipher char
			encrypted += codedChar	# Adds the cipher char to the encrypted variable

		else:
			sparsedMessageChar = ''.join(sparseMessageChar)
			codedChar = sparsedMessageChar[indexOfKeyChar]
			encrypted += codedChar

	return encrypted

def decrypt(cipherText,key):
	alphabetList = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?$&;:"
	#print(sparse(key))
	key = makeKeySameLength(cipherText,key) # Makes key the same length as the text
	decrypted = ""

	for each in range(len(cipherText)):	# Iterates through each char in the cipherText
		cipherTextChar = cipherText[each] # Gets the char of the cipherText
		keyChar = key[each]	# Gets the corresponding char of the key
		positionOfKeyChar = alphabetList.index(keyChar)	# Gets the index of the keyChar in the alphabet
		sparseKeyChar = sparse(key[each]) # Forms the sparse form of the keyChar
		sparsedKeyChar = ''.join(sparseKeyChar) # Converts the array into a string
		indexOfCipherTextChar = sparsedKeyChar.index(cipherTextChar) #Gets the position of the cipherText char in the sparsed form of the keyChar

		if (positionOfKeyChar >25) and (positionOfKeyChar<52):
			decoded = alphabetList[indexOfCipherTextChar+1]	# Gets the char in the alphabet list in the position of the cipherTextChar
			decrypted += decoded # Adds the char to the initialized string
		else:
			decoded = alphabetList[indexOfCipherTextChar]
			decrypted += decoded

	return decrypted


print (decrypt("W;D;X4TUxFs6H Mo","FeelsGodly"))

def main():

	while True: 
		try:
			option = int(input("Welcome to the cipher! Enter 1 to encrypt a message or 2 to decrypt a message\n"))
		except ValueError: 
			print("Sorry, I did not understand!\n")
			continue
		else: 
			break


	if (option == 1):
		message = str(input("Please enter the message you wish to encrypt: \n"))
		key = str(input("Please enter the encrypting Key: \n"))
		print("Thank you! Here is your encrypted text with your provided key: \n")
		print(encrypt(message,key))
	elif (option == 2): 
	 	message = str(input("Please enter the encrypted message: \n"))
	 	key = str(input("Please enter the encrypting key: \n"))
	 	print("Here is your decoded message:")
	 	print(decrypt(message,key))
	else: 
		print("Sorry, I do not understand! Please restart the program\n")


main()













