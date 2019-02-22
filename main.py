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


class InputBlock:

    def __init__(self,prev_hash,data,timestamp,sender,receiver,amount,nonce=0):

        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp
        self.nonce = nonce
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.hash = self.get_hash()


    @staticmethod
    def crate_genesis():
        pass

    def get_hash(self):

        header_bin =(str(self.prev_hash)+
                     str(self.data)+
                     str(self.timestamp)+
                     str(self.nonce)+
                     str(self.timestamp)+
                     str(self.nonce)+
                     str(self.sender)+
                     str(self.receiver)+
                     str(self.amount)

                     ).encode()

        inner_hash = hashlib.sha256(header_bin).hexdigest().encode()
        outer_hash = hashlib.sha256(inner_hash).hexdigest()
        return outer_hash

    def __str__(self):

        return "Previous Block Hash: " + str(self.prev_hash) +"\nBlock Data: " + str(self.data) +"\nSender: " +str(self.sender)+"\nReceiver: " +str(self.receiver)+"\nAmount: "+str(self.amount) +"\nBlock Timestamp: " + str(self.timestamp) +"\nBlock Hash: "+str(self.hash) +"\nNonce: " +str(self.nonce)



