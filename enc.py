from Crypto.Cipher import AES
import os
import base64

encoded=''

secret=''

def enc(prv):

	block=16
	padding='{'
	pad=lambda s:s+(block-len(s)%block)*padding
	EncodeAES=lambda c,s:base64.b64encode(c.encrypt(pad(s)))
	
	global secret
	secret=os.urandom(block)
	
	print 'encryption key',secret
	
	cipher=AES.new(secret)
	
	global encoded
	encoded = EncodeAES(cipher,prv)
	print 'encrypt string: ',encoded


def dec(encryptedString):

	PADDING = '{'
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	

	encryption = encryptedString

	key=secret	

	cipher = AES.new(key)
	decoded = DecodeAES(cipher, encryption)
	print decoded


ven=raw_input('>>')
enc(ven)

global encoded

dec(encoded)
