import zlib

data = open('demo.txt', 'r').read()
data = bytes(data, 'utf-8')
zlib.compress(data)