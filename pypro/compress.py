import zlib

data = open('demo.txt', 'r').read()
data_bytes = bytes(data, 'utf-8')
compressed_data = zlib.compress(data_bytes)
print(compressed_data)
