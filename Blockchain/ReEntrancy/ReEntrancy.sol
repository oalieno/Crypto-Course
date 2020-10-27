// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;

contract Challenge {
    address player;

    constructor (address _player) {
        player = _player;
    }

    modifier onlyPlayer () {
        require(msg.sender == player);
        _;
    }
}

contract ReEntrancyFactory {
    event GetFlag(uint token);
    mapping(address => address) public instances;

    function create () public payable {
        require(msg.value >= 0.5 ether);
        instances[msg.sender] = address(new ReEntrancy(msg.sender));
        instances[msg.sender].call{value: 0.5 ether}("");
    }

    function validate (uint token) public {
        require(address(instances[msg.sender]).balance == 0);
        emit GetFlag(token);
    }
}

contract ReEntrancy is Challenge {
    mapping(address => uint) public balances;

    constructor (address _player) Challenge(_player) {}

    function deposite() public payable onlyPlayer {
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint _amount) public payable onlyPlayer {
        require(balances[msg.sender] >= _amount);
        msg.sender.call{value: _amount}("");
        balances[msg.sender] -= _amount;
    }
    
    receive () external payable {}
}

