#!/bin/python
encoding = {}
decoding = {}
debug = False

no_dict = """Warning there was no dictionary
Please run A3.createDictionary before attempting to encode or decode.
"""

def createDictionaries(path):
	res = 0 # set res as 0 if anything hapends change the value
	if debug == True: print(path,'\n')
	try:
		f=open(path,'r') # read file specified in path
		for line in f:
			line = line.strip('\n') # strip the newline fron the end
			key,value = line.split(' ') # seperate key and value from each line
			if len(line) != 3: res = 2 # Check for length of each line (3 including white space)
			# Check for repeated keys and values
			elif key in encoding.keys(): res = 3
			elif value in encoding.values(): res = 4
			else:
				encoding[key] = value
				decoding[value] = key
		if debug == True: print(encoding,'\n\n',decoding)
	except: res = 1
	if debug == True: print(res)
	return res

def encode(string):
	result = ''
	string = string.lower() # make the string lower case
	for s in string: # for every charater in the string:
		result += str(encoding.get(s, '#')) # search dictionary for key if it isn't there then set result as #
	if debug == True: print(result,'\n')
	if len(decoding) == 0: print(no_dict)
	return result

def decode(string):
	result = ''
	string = string.lower()
	for s in string: # for every charater in the string:
		result += str(decoding.get(s, '#')) # search dictionary for key if it isn't there then set result as #
	if debug == True: print(result,'\n')
	if len(decoding) == 0: print(no_dict)
	else: return result
