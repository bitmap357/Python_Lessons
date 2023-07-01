import zlib

data = open('demo.txt', 'r').read()
zlib.compress(data)