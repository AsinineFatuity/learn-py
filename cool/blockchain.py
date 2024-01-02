"""
my coins are called KeFoCoins (KFC)
transaction_1 = Anne sends John 2 KFC
transaction_2 = John sends Daniel 4.3 KFC
transaction_3 = Mark sends Daniel 3.2 KFC

All these transactions are stored in one block say B1. B1 is also our initial block hence it has basis as AAA as part of its hash
B1("AAA",transaction_1,transaction_2,transaction_3), this block results in a given hash output, usually implemented in SHA256 (e.g 76fd89)
B2("76fd89",transaction_4,transaction_5,transaction_6)->8923ff
"""