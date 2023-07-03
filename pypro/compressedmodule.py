import base64
import zlib


def compress(inputfile, outputfile):
    data = open(inputfile, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
    decoded_data = compressed_data.decode('utf-8')
    compressed_file = open(outputfile, 'w')
    compressed_file.write(decoded_data)


def decompress(inputfile, outputfile):
    file_content = open(inputfile, 'r').read()
