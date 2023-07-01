import zlib

data = open('demo.txt', 'r').read()
data_bytes = bytes(data, 'utf-8')
zlib.compress(data_bytes)
