import hashlib
class PotionBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()



initial_block = PotionBlock("-", ["-", "-"])
with open('transactions.txt', 'r') as input_file, open('block_hashes.txt', 'w') as output_file:
    for line1, line2 in zip(input_file, input_file):
        line1 = line1.strip()
        line2 = line2.strip()
        message = line1 + line2
        potion_block = PotionBlock(initial_block.block_hash, [message])
        output_file.write(potion_block.block_hash + '\n')