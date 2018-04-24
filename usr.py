## Python 3

import hashlib

def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


## Example
a = computeMD5hash("some")
b = computeMD5hash("some")
c = computeMD5hash("some1")

print (a == b)
print (a == c)


