

from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0"*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yeah! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct hash after trying {MAX_NONCE}")


if __name__ == '__main__':
    transactions = '''
        Sachin->Aashiq->40,
        Aman->Yadav->35
    '''
    # if we try changing the difficulty to higher number and we will see it will take more time for mining
    # mining time increases as difficulty increases
    difficulty = 5

    import time
    start = time.time()
    print("mining started !")
    new_hash = mine(5, transactions, "0000000x036944e29568d0cff17edbe038f81208fecf9a66be9a66be9a2b8321c6ec7", difficulty)
    total_time = str((time.time() - start))
    print(f"mining ended ! Mining took: {total_time} seconds")
    print(new_hash)

