from bitarray import bitarray
import sys
import psutil


print(psutil.virtual_memory())

ba = [bitarray(4000000) for _ in range(4000000)]


print(psutil.virtual_memory())

# ba = bitarray(2 ** 20)

print(f'the thing is a {type(ba)} of size {sys.getsizeof(ba)} resulting in {len(ba) / sys.getsizeof(ba)} bits per byte')

print(psutil.virtual_memory())