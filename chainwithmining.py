from main import Block
import datetime
import time

diff = 20
maxNonce = 2**32
target = 2**(256-diff)

num_blocks_to_add = 10

block_chain = []

genesis=Block.create_genesis()

real_chain = []

for i in range(maxNonce):

    if int(genesis.get_hash(),16) <= target:
        block_chain.append(genesis)

        print("----------------------------------------\n")
        print("The Genesis has been created.")
        print(genesis)
        break

    else:
        genesis.nonce += 1

for i in range(1, num_blocks_to_add + 1):

    block_chain.append(Block(block_chain[i - 1].hash,
                             "Block number %d" % i,
                             datetime.datetime.now()))

#block_chain listesi oluştu fakat genesis dışındakilerin nonce değeri 0 o yüzden mine başlamalı

print("Mine starting...")

f = 1

for i in block_chain:

    for n in range(maxNonce):

        if int(i.get_hash(),16) <= target :

            real_chain.append(i)

            print("---------------------------------------------\n")

            print(i)

            break
        else :
            i.nonce += 1








