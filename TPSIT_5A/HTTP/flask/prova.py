import hashlib

password ="ciaociao"

h = hashlib.md5()
h.update(password.encode('utf-8'))
print(h)
print(h.hexdigest())