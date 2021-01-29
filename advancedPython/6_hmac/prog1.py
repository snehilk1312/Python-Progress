import hashlib
import hmac

# creating the hashed msg
message_mac = hmac.new(key=b'snehil', msg=b"hello world", digestmod=hashlib.sha256)

# printing the digested hash with upper digestmod
print(message_mac.hexdigest())


digest1 = message_mac.hexdigest()

# creating digest of same message
digest2 = hmac.new(b'snehil', msg=b"hello world", digestmod=hashlib.sha256).hexdigest()

# creating digest of another message
digest3 = hmac.new(b'snehil', msg=b"hell world", digestmod=hashlib.sha256).hexdigest()


# comparing digest of same msg(will give true)
print(hmac.compare_digest(digest1, digest2))

# compare digest of different msg(will give false)
print(hmac.compare_digest(digest1, digest3))
