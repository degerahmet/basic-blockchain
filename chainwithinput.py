from main import Block,InputBlock
import datetime
import time


print("""""
Welcome to the Marun Coin Wallet 

1.Send coin (Mining will be start automatically)
2.See all Blocks (You can choose ranges if you want this option)
q.Quit

""")
blocks = []

real_block=[]

cmon = input("Choose your option: ")

sender_id = "0"
receiver_id= "0"
amount= "0"
s = 0

diff = 20
maxNonce = 2**32
target = 2**(256-diff)

say = 0

while True :

    if cmon == "q":
        print("You will be quit in 2 seconds")
        time.sleep(2)

        print("Goodbye")
        break

    elif cmon == "1":

        sender_id = input("Sender: ")
        receiver_id = input("Receiver: ")
        amount = input("Amount: ")

        print("\nYour transaction succesfully")

        cmon = "5"

    elif cmon == "2" :
        for i in real_block:
            time.sleep(0.5)
            print("\n")
            print(i)
            print("\n")
            print("----------------------------------------------------------------")
            if say == len(real_block):
                break
            else :
                say += 1

        say = 0


        cmon = input("\nChoose your option: ")

    elif cmon == "5" :

        if sender_id == "0" or receiver_id == "0" or amount == "0" :
            print("No new precess yet")

            cmon = input("\nChoose your option: ")


        else:

            print("\nMine starting...\n")

            if blocks == []:
                print("if")
                blocks.append(InputBlock("0", "Genesis", datetime.datetime.now(), sender_id, receiver_id, amount))

                for i in range(maxNonce):
                    if int(blocks[s].get_hash(), 16) <= target:
                        real_block.append(blocks[s])
                        print("----------------------------------------\n")
                        print("The Genesis has been created.\n")
                        print(blocks[s])
                        print("\n-------------------------------------")
                        s += 1

                        break

                    else:
                        blocks[s].nonce += 1

                sender_id = "0"
                receiver_id = "0"
                amount = "0"

                cmon = input("\nChoose your option: ")



            else:
                print("else")
                blocks.append(
                    InputBlock(blocks[-1].hash, "Block %d" % s, datetime.datetime.now(), sender_id, receiver_id,
                               amount))

                for i in range(maxNonce):
                    if int(blocks[s].get_hash(), 16) <= target:
                        real_block.append((blocks[s]))
                        print("\n")
                        print(blocks[s].data, " chained with chain.")
                        print("\n")
                        print(blocks[s])
                        s += 1
                        sender_id = "0"
                        receiver_id = "0"
                        amount = "0"
                        break
                    else:
                        blocks[s].nonce += 1

                cmon = input("\nChoose your option: ")

                sender_id = "0"
                receiver_id = "0"
                amount = "0"

    else:

        cmon = input("\nChoose your option: ")












