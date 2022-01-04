// SPDX-License-Identifier: MIT
pragma solidity ^0.4.21;


contract Greeter{ 
    string public greeting;


    function Greeter() public{ 
        greeting = "hello";

    }

    function setgreeting(string message) public{ 
        greeting = message;
    }
    
    function greet() view public returns(string)
    { 
        return greeting;
    }
}