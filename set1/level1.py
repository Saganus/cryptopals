import base64
import binascii

expected = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

input_string = input('Input string: ')

input_hex = binascii.unhexlify(input_string)

input_b64 = base64.b64encode(input_hex)

print('Base64: ', input_b64)

if(expected == input_b64):
	print('SUCCESS!')