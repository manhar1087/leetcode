import hashlib

msg= input("Enter a message: ")
hash = hashlib.md5(msg.encode())

print("Md5 hash value is", hash.hexdigest())