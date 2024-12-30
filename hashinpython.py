import hashlib

result = hashlib.sha256(bytes('hai'))
result2 = hashlib.md5(b'')
print(result.hexdigest())
print(result2.hexdigest())