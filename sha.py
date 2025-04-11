import hashlib

msg= input("Enter a message: ")
hash = hashlib.sha1(msg.encode())

print("SHA1 hash value is", hash.hexdigest())