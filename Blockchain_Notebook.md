# Blockchain Notebook
================================================
0. Satoshi Nakamoto published "Bitcoin: A Peer-to-Peer Electronic Cash System" in 2008
1. Blockchain != BitCoin
2. 3 benefits BitCoin than Bank
	```
	1) Don't need 3rd party to finish a transaction (like Bank);
	2) Fast. Don't need 3 days to transfer money;
	3) Free. No transaction fee.
	```
3. Distributed open ledger = chain
4. How to sync the ledger (miner)
	```
	1) validate the new transaction;
	2) key -- proof of work
	```
5. Best directions for me to research Blockchain: Finance and Voting
6. TPS (Transactions Per Second) TPS=175,000 for facebook
7. 3rd generation<br/>
	```
	Web 1.0 -- static web 1990
	Web 2.0 -- dynamic web 2005
	Web 3.0 -- decentralized web
	```
8. Proof-of-Work
	```
	1) implement a distributed timestamp server on p2p basis
	2) essentially one-CPU-one-vote
	3) the longest chain has the greatest proof-of-work effort invested in it;
	4) honest nodes > bad nodes => safety no attack
	```
9. Network
	```
	a) New Transactions are broadcast to all nodes;
	b) Each node collects new transactions into a block;
	c) Each node works on finding a difficult proof-of-work for its block;
	d) When a node finds a proof-of-work, it broadcasts the block to all nodes;
	e) Nodes accept the block only if all transactions in it are valid and not already spent;
	f) Nodes express their acceptance of the block by working on creating the next block 
	   in the chain, using the hash of the accepted block as the previous hash.
	g) Two nodes broadcase different version of the next block simultaneously. when the next
	   proof-of-work is found, the longer one wins.
	```
10. Incentive
	```
	1) the new coin is owned by the creator of the block;
	2) the first transaction of a block is special;
	3) the attacker has to choose to defraud people by stealing back his payment or generate new coin.
	```
11. 