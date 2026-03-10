// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Zetscoin
 * @dev ERC20 Token implementation for Zetscoin (ZET)
 * @notice This contract implements a standard ERC20 token with minting capabilities
 */
contract Zetscoin is ERC20, Ownable {
    /**
     * @dev Constructor that sets the initial supply
     * @param initialSupply The amount of tokens to mint to the deployer (in whole tokens, no decimals)
     */
    constructor(uint256 initialSupply) ERC20("Zetscoin", "ZET") {
        // Mint initial supply to the deployer
        // ERC20 tokens have 18 decimals by default
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }

    /**
     * @dev Allows the owner to mint new tokens
     * @param to The address to mint tokens to
     * @param amount The amount of tokens to mint (in whole tokens, no decimals)
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount * 10 ** decimals());
    }

    /**
     * @dev Allows the owner to burn tokens from their account
     * @param amount The amount of tokens to burn (in whole tokens, no decimals)
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount * 10 ** decimals());
    }
}