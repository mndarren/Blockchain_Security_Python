import hashlib as hasher
from datetime import datetime
from typing import NamedTuple, List
from transaction import Transaction


class Block(object):
    """
    Represents a block in a blockchain
    """
    def __init__(self, index, timestamp, transactions,  previous_hash):
        self.index: int = index
        self.timestamp: datetime = timestamp
        self.transactions: List[Transaction] = transactions
        self.previous_hash: str = previous_hash
        self.hash: str = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) +
                    str(self.timestamp) +
                    str(self.transactions_to_string()) +
                    str(self.previous_hash)).encode())
        return sha.hexdigest()

    def transactions_to_string(self):
        return ''.join(self.transactions_list_str())

    def transactions_list_str(self):
        return [T.__repr__() for T in self.transactions]


if __name__ == "__main__":
    transaction_0 = Transaction(sender='0', receiver='0', amount=0.0)
    b = Block(index=1, timestamp=datetime.now(), transactions=[transaction_0],
              previous_hash="1")
    print(b.hash)
