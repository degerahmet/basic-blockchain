from main import Block
import datetime
import time

num_blocks_to_add = 10

block_chain = [Block.create_genesis()]
print("------------------------------------------------------------------------\n")
print("The genesis block has been created.")
print( block_chain[0])
time.sleep(2)

for i in range(1, num_blocks_to_add+1):
    block_chain.append(Block(block_chain[i-1].hash,
                             "Block number %d" %i,
                             datetime.datetime.now()))

    print("\n---------------------------------------------------------------------------------\n")
    print("Block #%d created.\n" % i)
    print(block_chain[i])

    time.sleep(2)
