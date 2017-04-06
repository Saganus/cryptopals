import binascii
import sys


def xor_hex(input1, input2):
	buf1 = binascii.unhexlify(input1)
	buf2 = binascii.unhexlify(input2)

	int_buf1 = int.from_bytes(buf1, sys.byteorder)
	int_buf2 = int.from_bytes(buf2, sys.byteorder)

	xor = int_buf1 ^ int_buf2
	xor_bytes = xor.to_bytes(len(buf1), sys.byteorder)

	return binascii.hexlify(xor_bytes)


input1 = '1c0111001f010100061a024b53535009181c'
input2 = '686974207468652062756c6c277320657965'

print('XOR result: ', xor_hex(input1, input2))



