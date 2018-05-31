#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  # Created by Darren Zhao Xie on 05/28/2018
  # Blockchain example by python
"""

import datetime as date
from block import Block
from transaction import Transaction
from typing import List


class Blockchain(object):
    def __init__(self, blockchain):
        self.blockchain: List[Block] = blockchain

    def create_genesis_block(self):
        transaction_0 = Transaction(sender='0', receiver='0', amount=0.0)
        return Block(index=0, timestamp=date.datetime.now(),
                     transactions=[transaction_0], previous_hash="0")

    def next_block(self, last_block: Block):
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = "Hey! I'm block " + str(this_index)
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)

    def run(self):
        block_chain = [self.create_genesis_block()]
        previous_block = block_chain[0]
        num_blocks = 20

        for i in range(0, num_blocks):
            block_to_add = self.next_block(previous_block)
            block_chain.append(block_to_add)
            previous_block = block_to_add
            print(f'Block {block_to_add.index} has been added to the blockchain')
            print(f'Hash: {block_to_add.hash}')


if __name__ == "__main__":
    Blockchain().run()
