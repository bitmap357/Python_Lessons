import zlib

data = open('demo.txt', 'r').read()
bytes(data, 'utf-8')
zlib.compress(data)