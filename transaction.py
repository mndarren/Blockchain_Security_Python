#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  # Created by Darren Zhao Xie on 05/28/2018
  # Blockchain example by python
"""
from typing import NamedTuple


class Transaction(NamedTuple):
    """Represents an transaction"""
    sender: str
    receiver: str
    amount: float

    def __repr__(self) -> str:
        return f'Sender={self.sender}, receiver={self.receiver}, amount={self.amount}'
