import jwt

class Criptografia():

    def encode(self, msg):
        encoded_jwt = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
        return encoded_jwt

    def decode(self, encoded_jwt):
        msg = jwt.decode(encoded_jwt, 'secret', algorithms=['HS256'])
        return msg
