import tinyec.ec as ec
import random
# import tinyec.ecpoint

curve = ec.get_curve('brainpoolP256r1')
priv_key = 123456789
pub_key = priv_key * curve.g

msg = "Hello world"
msg_point = ec.Point.from_bytes(msg.encode(), curve)
encrypt_point = pub_key + msg_point
print(encrypt_point)