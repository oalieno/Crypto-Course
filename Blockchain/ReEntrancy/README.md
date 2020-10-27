# ReEntrancy Attack

* server
    * `server.py` : watch for GetFlag event on factory contract
    * `flag` : the flag
* solve
    * `solve.js` : solution script
    * `validate.js` : trigger factory to emit GetFlag event
    * `Hack.sol` : the actual hacking contract used to solve this challenge

`ReEntrancyFactory` Address : [0x84fb598a7e8d58715d3c5f2e789570d7b5b0e290](https://ropsten.etherscan.io/address/0x84fb598a7e8d58715d3c5f2e789570d7b5b0e290)

Use `solve.js` and `Hack.sol` to solve the challenge.  
Then use `validate.js` and `server.py` to check whether you successfully solve the challenge
