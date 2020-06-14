# Assignment3
A3 – Simple encoder / decoder program

The A3 module uses a simple Caesar cipher to encrypt and decrypt strings.

       Constants
The A3 module exports the following constants:

A3.createDictionaries(file_path)
	createDictionaries() takes a file path as argument and creates encoding and decoding dictionaries from the information provided in the file.  Each line of the file contains two letters.  The first letter denotes the letter to be encoded.  The second letter is the encoding of that letter.  The letters are separated by whitespace.  For example:

Valid file_path: C:\\Users\\(username)\\Desktop\\(filename).txt

    • There are no problems return the value 0.
    • The file path provided as argument to createDictionaries() is not valid. The value returned by createDictionaries(). Return the value 1.
    • There is a line in the file that does not contain exactly two letters (not including whitespace or newline). Return the value 2.
    • A key (i.e. the first letter of a line) appears more than once in the file. Return the value 3.
    • A value (i.e. the second letter of a line) appears more than once in the file. Return the value 4.

A3.encode(string)
	encode() takes the string as an argument and changes all the charaters to lowercase. Encodes then using the encoding dictionary from createDictionaries(). If the charater doesn’t have a matching key it will use ‘#’

	Dependency: createDictionaries()

A3.encode(string)
	decode() takes the string as an argument and changes all the charaters to lowercase. Decodes then using the decoding dictionary from createDictionaries(). If the charater doesn’t have a matching key it will use ‘#’

	Dependency: createDictionaries()
