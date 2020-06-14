#!/bin/python

import A3
import os

path = os.getcwd()
filename = 'keys.txt'
path = path+'/'+filename

#A3.debug = True

print(A3.createDictionaries(path))
tmp = A3.encode('Hello World')
print(tmp)
print(A3.decode(tmp))
