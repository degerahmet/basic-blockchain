import hashlib
import datetime


class Block:
    def __init__(self,prev_blockhash,data,timestamp,nonce = 0):
        self.prev_blockhash = prev_blockhash
        self.data = data
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.get_hash()

    @staticmethod
    def create_genesis():
        return Block("0","0",datetime.datetime.now())

    def get_hash(self):
        header_bin = (str(self.prev_blockhash)+
                      str(self.data)+
                      str(self.nonce)+
                      str(self.timestamp)).encode()

        inner_hash= hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

    def __str__(self):

        return "Previous Block Hash: " +str(self.prev_blockhash) +"\nBlock Data: " + str(self.data) +"\nBlock Timestamp: " +  str(self.timestamp) + "\nBlock Nonce: " + str(self.nonce) +  "\nBlock Hash: " + str(self.hash)
