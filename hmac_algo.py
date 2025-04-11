import hashlib
import hmac

key = "secret"

msg = input("Enter a msg: ")

hash = hmac.new(key.encode(), msg.encode(), hashlib.sha512)

print("HMAC hash Value is ", hash.hexdigest())